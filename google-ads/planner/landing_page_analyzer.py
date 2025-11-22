#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Landing Page Analyzer - Phân tích landing page để đề xuất từ khóa, CPC, CVR
"""

import requests
from bs4 import BeautifulSoup
import json
import re
from urllib.parse import urlparse
from collections import Counter
import time


class LandingPageAnalyzer:
    """
    Phân tích landing page và đề xuất chiến lược keywords, CPC, CVR
    """
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Industry benchmarks (dựa trên data thực tế từ Google Ads)
        self.industry_benchmarks = {
            'e-commerce': {
                'avg_cvr': 2.5,  # 2.5% conversion rate
                'avg_cpc_range': (5000, 15000),  # VNĐ
                'keywords': ['mua', 'giá', 'sale', 'khuyến mãi', 'giảm giá']
            },
            'fashion': {
                'avg_cvr': 2.0,
                'avg_cpc_range': (8000, 25000),
                'keywords': ['thời trang', 'đẹp', 'sang trọng', 'cao cấp', 'xu hướng']
            },
            'electronics': {
                'avg_cvr': 1.8,
                'avg_cpc_range': (10000, 30000),
                'keywords': ['chính hãng', 'bảo hành', 'mới nhất', 'giá tốt']
            },
            'services': {
                'avg_cvr': 3.5,
                'avg_cpc_range': (15000, 50000),
                'keywords': ['dịch vụ', 'uy tín', 'chuyên nghiệp', 'nhanh chóng']
            }
        }
    
    def fetch_page_content(self, url):
        """
        Lấy nội dung trang web
        """
        try:
            print(f"\n🌐 Đang truy cập: {url}")
            response = requests.get(url, headers=self.headers, timeout=30)
            response.raise_for_status()
            
            print(f"✅ Đã tải trang thành công (Status: {response.status_code})")
            return response.text
        
        except requests.exceptions.RequestException as e:
            print(f"❌ Lỗi khi truy cập trang: {e}")
            return None
    
    def extract_page_info(self, html_content, url):
        """
        Trích xuất thông tin từ HTML
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        
        info = {
            'url': url,
            'title': '',
            'meta_description': '',
            'h1_tags': [],
            'h2_tags': [],
            'product_names': [],
            'prices': [],
            'all_text': '',
            'links': [],
            'avg_price': 0
        }
        
        # Title
        title_tag = soup.find('title')
        if title_tag:
            info['title'] = title_tag.get_text().strip()
        
        # Meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            info['meta_description'] = meta_desc.get('content', '').strip()
        
        # H1, H2 tags
        info['h1_tags'] = [h1.get_text().strip() for h1 in soup.find_all('h1')]
        info['h2_tags'] = [h2.get_text().strip() for h2 in soup.find_all('h2')]
        
        # Product names (tìm trong các thẻ thường dùng cho tên sản phẩm)
        product_selectors = [
            '.product-name', '.product-title', '.item-name',
            '[class*="product"]', '[class*="item-title"]'
        ]
        
        for selector in product_selectors:
            products = soup.select(selector)
            for product in products[:20]:  # Giới hạn 20 sản phẩm
                text = product.get_text().strip()
                # Clean up whitespace and remove prices
                text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with single space
                text = re.sub(r'\d{1,3}(?:[.,]\d{3})*\s*(?:đ|vnd|₫)', '', text)  # Remove prices
                text = text.strip()
                if len(text) > 5 and len(text) < 100:
                    info['product_names'].append(text)
        
        # Prices
        price_patterns = [
            r'(\d{1,3}(?:[.,]\d{3})*)\s*(?:đ|vnd|₫)',
            r'(\d{1,3}(?:[.,]\d{3})*)\s*đồng'
        ]
        
        text_content = soup.get_text()
        for pattern in price_patterns:
            matches = re.findall(pattern, text_content, re.IGNORECASE)
            info['prices'].extend(matches[:30])
        
        # Calculate average price
        if info['prices']:
            try:
                prices_int = [int(p.replace(',', '').replace('.', '')) for p in info['prices']]
                # Filter out unrealistic prices
                prices_filtered = [p for p in prices_int if 10000 <= p <= 50000000]
                if prices_filtered:
                    info['avg_price'] = int(sum(prices_filtered) / len(prices_filtered))
            except:
                pass
        
        # All text (để phân tích keywords)
        info['all_text'] = soup.get_text(separator=' ', strip=True)
        
        # Internal links
        for link in soup.find_all('a', href=True)[:50]:
            href = link.get('href', '')
            if href and not href.startswith(('http://', 'https://', '#', 'javascript:')):
                info['links'].append(href)
        
        return info
    
    def detect_industry(self, page_info):
        """
        Phát hiện ngành hàng dựa trên nội dung trang
        """
        text_lower = (page_info['title'] + ' ' + 
                     page_info['meta_description'] + ' ' + 
                     ' '.join(page_info['h1_tags'])).lower()
        
        industry_keywords = {
            'fashion': ['giày', 'dép', 'túi', 'thời trang', 'quần', 'áo', 'váy', 'đầm', 'phụ kiện'],
            'electronics': ['điện thoại', 'laptop', 'máy tính', 'tai nghe', 'camera', 'tivi'],
            'e-commerce': ['mua', 'bán', 'shop', 'store', 'cửa hàng'],
            'services': ['dịch vụ', 'tư vấn', 'hỗ trợ', 'chăm sóc']
        }
        
        scores = {}
        for industry, keywords in industry_keywords.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            scores[industry] = score
        
        # Trả về ngành có điểm cao nhất
        detected = max(scores, key=scores.get) if scores else 'e-commerce'
        
        # Nếu điểm quá thấp, mặc định là e-commerce
        if scores[detected] < 2:
            detected = 'e-commerce'
        
        print(f"\n🏷️  Ngành hàng phát hiện: {detected}")
        print(f"   Điểm số: {scores}")
        
        return detected
    
    def detect_target_age(self, page_info, industry):
        """
        Phát hiện độ tuổi mục tiêu dựa trên nội dung và ngành hàng
        """
        text_lower = (page_info['title'] + ' ' + 
                     page_info['meta_description'] + ' ' + 
                     page_info['all_text'][:2000]).lower()
        
        # Age-related keywords
        age_indicators = {
            '18-24': ['teen', 'sinh viên', 'học sinh', 'trẻ trung', 'năng động', 'gen z'],
            '25-34': ['văn phòng', 'công sở', 'trẻ', 'hiện đại', 'millennial', 'startup'],
            '35-44': ['gia đình', 'bố mẹ', 'trung niên', 'lịch lãm', 'sang trọng', 'chín chắn'],
            '45-60': ['trưởng thành', 'cao cấp', 'đẳng cấp', 'lịch thiệp', 'phong cách']
        }
        
        scores = {}
        for age_range, keywords in age_indicators.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            scores[age_range] = score
        
        # Industry-based defaults if no clear indicators
        industry_defaults = {
            'fashion': '25-40',
            'electronics': '20-45',
            'e-commerce': '25-45',
            'services': '30-50'
        }
        
        # Get highest score
        if scores and max(scores.values()) > 0:
            detected = max(scores, key=scores.get)
            print(f"\n👥 Độ tuổi mục tiêu phát hiện: {detected}")
            print(f"   Điểm số: {scores}")
            return detected
        else:
            # Use industry default
            default = industry_defaults.get(industry, '25-45')
            print(f"\n👥 Độ tuổi mục tiêu (default theo ngành): {default}")
            return default
    
    def extract_keywords_from_content(self, page_info):
        """
        Trích xuất từ khóa từ nội dung trang
        """
        # Combine all important text
        important_text = (
            page_info['title'] + ' ' +
            page_info['meta_description'] + ' ' +
            ' '.join(page_info['h1_tags']) + ' ' +
            ' '.join(page_info['h2_tags']) + ' ' +
            ' '.join(page_info['product_names'])
        )
        
        # Clean text
        text = re.sub(r'[^\w\s]', ' ', important_text.lower())
        
        # Tokenize (tách từ tiếng Việt đơn giản)
        words = text.split()
        
        # Remove stopwords (từ dừng tiếng Việt)
        stopwords = {
            'của', 'và', 'có', 'cho', 'với', 'từ', 'tại', 'là', 'được', 'các',
            'trong', 'để', 'một', 'những', 'này', 'đó', 'về', 'như', 'khi',
            'hoặc', 'đã', 'bởi', 'the', 'and', 'or', 'in', 'on', 'at', 'to'
        }
        
        words = [w for w in words if len(w) > 2 and w not in stopwords]
        
        # Count frequency
        word_freq = Counter(words)
        
        # Get top keywords (single words)
        top_keywords = [word for word, count in word_freq.most_common(50) if count >= 2]
        
        # Extract 2-word and 3-word phrases
        phrases = []
        words_list = important_text.lower().split()
        
        # 2-word phrases
        for i in range(len(words_list) - 1):
            phrase = ' '.join(words_list[i:i+2])
            if len(phrase) > 5:
                phrases.append(phrase)
        
        # 3-word phrases
        for i in range(len(words_list) - 2):
            phrase = ' '.join(words_list[i:i+3])
            if len(phrase) > 8:
                phrases.append(phrase)
        
        phrase_freq = Counter(phrases)
        top_phrases = [phrase for phrase, count in phrase_freq.most_common(30) if count >= 2]
        
        return {
            'single_keywords': top_keywords[:30],
            'phrases': top_phrases[:20]
        }
    
    def generate_keyword_suggestions(self, page_info, industry, extracted_keywords, 
                                     commission_rate=8.0, avg_product_price=None):
        """
        Tạo danh sách từ khóa đề xuất với CPC và CVR
        CPC được tính dựa trên commission rate và giá sản phẩm
        """
        suggestions = []
        
        # Get industry benchmark
        benchmark = self.industry_benchmarks.get(industry, self.industry_benchmarks['e-commerce'])
        
        # Calculate max acceptable CPC based on commission
        # Formula: Max CPC = (Avg Product Price * Commission Rate * Target Profit Margin) / (1 / CVR)
        # Với target profit margin = 0.5 (50% of commission goes to ads)
        
        if avg_product_price is None:
            avg_product_price = page_info.get('avg_price', 500000)
        
        commission_per_sale = avg_product_price * (commission_rate / 100)
        target_cvr = benchmark['avg_cvr'] / 100  # Convert to decimal
        
        # Max CPC = 50% of commission / expected conversions needed
        # If CVR = 2%, we need 50 clicks for 1 conversion
        # So max CPC = (commission * 0.5) / 50
        max_cpc_base = (commission_per_sale * 0.5) * target_cvr
        
        print(f"\n💰 TÍNH TOÁN CPC DỰA TRÊN HOA HỒNG:")
        print(f"   - Giá trung bình sản phẩm: {avg_product_price:,} VNĐ")
        print(f"   - Commission rate: {commission_rate}%")
        print(f"   - Hoa hồng/đơn hàng: {commission_per_sale:,} VNĐ")
        print(f"   - Target CVR: {benchmark['avg_cvr']}%")
        print(f"   - Max CPC khuyến nghị (50% commission): {int(max_cpc_base):,} VNĐ")
        
        # Base từ khóa từ tên sản phẩm
        for product in page_info['product_names'][:15]:
            keyword = product.strip().lower()
            
            # Ước tính CPC dựa trên độ dài và chất lượng từ khóa
            word_count = len(keyword.split())
            
            # Estimate clicks needed per conversion based on keyword quality
            if word_count == 1:
                # Single word - expensive, high competition, need more clicks
                clicks_per_conversion = 100  # Very generic
                competition = 'HIGH'
                cvr = benchmark['avg_cvr'] * 0.8  # Lower CVR for generic terms
            elif word_count == 2:
                # Two words - moderate
                clicks_per_conversion = 50
                competition = 'MEDIUM'
                cvr = benchmark['avg_cvr']
            else:
                # Long-tail - cheaper, lower competition, better qualified traffic
                clicks_per_conversion = 30
                competition = 'LOW'
                cvr = benchmark['avg_cvr'] * 1.3  # Higher CVR for specific terms
            
            # Calculate max CPC based on commission economics
            # max_cpc = (commission_per_sale * profit_margin) / clicks_per_conversion
            # Use 50% profit margin (other 50% for commission)
            max_cpc = (commission_per_sale * 0.5) / clicks_per_conversion
            min_cpc = max_cpc * 0.6  # Min CPC is 60% of max
            
            suggestions.append({
                'keyword': keyword,
                'source': 'product_name',
                'estimated_cpc_range': {
                    'min': int(min_cpc),
                    'max': int(max_cpc),
                    'currency': 'VND'
                },
                'estimated_avg_cpc': int((min_cpc + max_cpc) / 2),
                'estimated_cvr': round(cvr, 2),
                'competition': competition,
                'monthly_budget_recommendation': {
                    'min': int((min_cpc + max_cpc) / 2 * 100),  # 100 clicks/month
                    'max': int((min_cpc + max_cpc) / 2 * 500),  # 500 clicks/month
                },
                'match_types': ['Exact', 'Phrase', 'Broad'] if word_count <= 2 else ['Exact', 'Phrase'],
                'commission_based': True,
                'estimated_clicks_per_conversion': clicks_per_conversion
            })
        
        # Từ khóa từ phrases được extract
        for phrase in extracted_keywords['phrases'][:20]:
            keyword = phrase.strip().lower()
            word_count = len(keyword.split())
            
            # Phrase keywords - usually long-tail, better qualified
            clicks_per_conversion = 30 if word_count >= 3 else 40
            competition = 'LOW' if word_count >= 3 else 'MEDIUM'
            cvr = benchmark['avg_cvr'] * 1.2
            
            # Calculate CPC based on commission
            max_cpc = (commission_per_sale * 0.5) / clicks_per_conversion
            min_cpc = max_cpc * 0.6
            
            suggestions.append({
                'keyword': keyword,
                'source': 'content_analysis',
                'estimated_cpc_range': {
                    'min': int(min_cpc),
                    'max': int(max_cpc),
                    'currency': 'VND'
                },
                'estimated_avg_cpc': int((min_cpc + max_cpc) / 2),
                'estimated_cvr': round(cvr, 2),
                'competition': competition,
                'monthly_budget_recommendation': {
                    'min': int((min_cpc + max_cpc) / 2 * 100),
                    'max': int((min_cpc + max_cpc) / 2 * 500),
                },
                'match_types': ['Exact', 'Phrase'],
                'commission_based': True,
                'estimated_clicks_per_conversion': clicks_per_conversion
            })
        
        # Thêm từ khóa brand + modifier
        brand_name = urlparse(page_info['url']).netloc.split('.')[0]
        modifiers = ['mua', 'giá', 'khuyến mãi', 'sale', 'ưu đãi', 'chính hãng']
        
        for modifier in modifiers:
            keyword = f"{brand_name} {modifier}"
            
            # Brand keywords - high intent, need fewer clicks per conversion
            clicks_per_conversion = 20  # Brand traffic converts better
            cvr = benchmark['avg_cvr'] * 1.8  # Very high CVR for brand + intent
            
            # Calculate CPC - brand keywords can afford higher CPC due to better conversion
            max_cpc = (commission_per_sale * 0.5) / clicks_per_conversion
            min_cpc = max_cpc * 0.7  # Brand keywords stay closer to max
            
            suggestions.append({
                'keyword': keyword,
                'source': 'brand_modifier',
                'estimated_cpc_range': {
                    'min': int(min_cpc),
                    'max': int(max_cpc),
                    'currency': 'VND'
                },
                'estimated_avg_cpc': int((min_cpc + max_cpc) / 2),
                'estimated_cvr': round(cvr, 2),
                'competition': 'MEDIUM',
                'monthly_budget_recommendation': {
                    'min': int((min_cpc + max_cpc) / 2 * 150),
                    'max': int((min_cpc + max_cpc) / 2 * 600),
                },
                'match_types': ['Exact', 'Phrase'],
                'commission_based': True,
                'estimated_clicks_per_conversion': clicks_per_conversion
            })
        
        return suggestions
    
    def calculate_campaign_projections(self, keyword_suggestions, monthly_budget):
        """
        Tính toán dự báo campaign dựa trên keywords và budget
        """
        if not keyword_suggestions:
            return {
                'monthly_budget': monthly_budget,
                'estimated_metrics': {
                    'avg_cpc': 0,
                    'avg_cvr': 0,
                    'estimated_clicks_per_month': 0,
                    'estimated_conversions_per_month': 0,
                    'estimated_cpa': 0,
                    'estimated_impressions': 0
                },
                'keyword_distribution': {
                    'total_keywords': 0,
                    'by_competition': {},
                    'by_source': {}
                },
                'recommendations': [{
                    'type': 'warning',
                    'category': 'Keywords',
                    'message': 'Không có từ khóa được tạo. Vui lòng kiểm tra landing page.'
                }]
            }
        
        # Calculate weighted averages
        total_keywords = len(keyword_suggestions)
        
        # Filter out zero CPCs to calculate average
        valid_cpcs = [k['estimated_avg_cpc'] for k in keyword_suggestions if k['estimated_avg_cpc'] > 0]
        
        if not valid_cpcs:
            # Fallback: use a default CPC if all are zero
            avg_cpc = 10000  # Default 10k VND
            print(f"⚠️  Không tính được CPC. Sử dụng giá trị mặc định: {avg_cpc:,} VNĐ")
        else:
            avg_cpc = sum(valid_cpcs) / len(valid_cpcs)
        
        avg_cvr = sum(k['estimated_cvr'] for k in keyword_suggestions) / total_keywords
        
        # Ensure avg_cpc is not zero to prevent division error
        if avg_cpc <= 0:
            avg_cpc = 10000
        
        # Calculate projections
        estimated_clicks = int(monthly_budget / avg_cpc)
        estimated_conversions = int(estimated_clicks * (avg_cvr / 100))
        estimated_cpa = int(monthly_budget / estimated_conversions) if estimated_conversions > 0 else 0
        
        # Competition distribution
        competition_counts = Counter(k['competition'] for k in keyword_suggestions)
        
        return {
            'monthly_budget': monthly_budget,
            'estimated_metrics': {
                'avg_cpc': int(avg_cpc),
                'avg_cvr': round(avg_cvr, 2),
                'estimated_clicks_per_month': estimated_clicks,
                'estimated_conversions_per_month': estimated_conversions,
                'estimated_cpa': estimated_cpa,
                'estimated_impressions': estimated_clicks * 20  # CTR ~5%
            },
            'keyword_distribution': {
                'total_keywords': total_keywords,
                'by_competition': dict(competition_counts),
                'by_source': dict(Counter(k['source'] for k in keyword_suggestions))
            },
            'recommendations': self._generate_recommendations(
                estimated_cpa, avg_cvr, competition_counts
            )
        }
    
    def _generate_recommendations(self, cpa, cvr, competition_counts):
        """
        Tạo khuyến nghị dựa trên dữ liệu
        """
        recommendations = []
        
        # CPA recommendations
        if cpa > 200000:
            recommendations.append({
                'type': 'warning',
                'category': 'CPA',
                'message': 'CPA cao (>200k VNĐ). Nên tối ưu landing page và targeting.'
            })
        elif cpa < 50000:
            recommendations.append({
                'type': 'success',
                'category': 'CPA',
                'message': 'CPA tốt (<50k VNĐ). Có thể scale budget.'
            })
        
        # CVR recommendations
        if cvr < 1.5:
            recommendations.append({
                'type': 'warning',
                'category': 'CVR',
                'message': 'CVR thấp (<1.5%). Cần cải thiện landing page và offer.'
            })
        elif cvr > 3.0:
            recommendations.append({
                'type': 'success',
                'category': 'CVR',
                'message': 'CVR cao (>3%). Landing page tối ưu tốt.'
            })
        
        # Competition recommendations
        high_comp = competition_counts.get('HIGH', 0)
        total = sum(competition_counts.values())
        
        if high_comp / total > 0.5:
            recommendations.append({
                'type': 'info',
                'category': 'Competition',
                'message': 'Nhiều từ khóa cạnh tranh cao. Nên thêm long-tail keywords.'
            })
        
        return recommendations
    
    def analyze_landing_page(self, url, monthly_budget=10000000, commission_rate=8.0, avg_product_price=None):
        """
        Phân tích landing page và tạo đề xuất từ khóa với CPC dựa trên commission
        
        Args:
            url: Landing page URL
            monthly_budget: Ngân sách tháng (VNĐ)
            commission_rate: Tỷ lệ hoa hồng (%)
            avg_product_price: Giá trung bình sản phẩm (nếu không có sẽ tự extract từ page)
        """
        print("="*80)
        print("LANDING PAGE ANALYZER")
        print("="*80)
        
        # Fetch page
        html_content = self.fetch_page_content(url)
        if not html_content:
            return None
        
        # Extract info
        print("\n📄 Đang trích xuất thông tin trang...")
        page_info = self.extract_page_info(html_content, url)
        
        print(f"\n✅ Đã trích xuất:")
        print(f"   - Title: {page_info['title'][:100]}...")
        print(f"   - H1 tags: {len(page_info['h1_tags'])}")
        print(f"   - H2 tags: {len(page_info['h2_tags'])}")
        print(f"   - Product names: {len(page_info['product_names'])}")
        print(f"   - Prices found: {len(page_info['prices'])}")
        if page_info['avg_price'] > 0:
            print(f"   - Giá trung bình: {page_info['avg_price']:,} VNĐ")
        
        # Detect industry
        industry = self.detect_industry(page_info)
        
        # Detect target age
        target_age = self.detect_target_age(page_info, industry)
        
        # Extract keywords
        print("\n🔍 Đang phân tích từ khóa từ nội dung...")
        extracted_keywords = self.extract_keywords_from_content(page_info)
        
        print(f"\n✅ Đã tìm thấy:")
        print(f"   - Single keywords: {len(extracted_keywords['single_keywords'])}")
        print(f"   - Phrases: {len(extracted_keywords['phrases'])}")
        
        # Generate suggestions với commission-based CPC
        print("\n💡 Đang tạo đề xuất từ khóa với CPC dựa trên hoa hồng...")
        keyword_suggestions = self.generate_keyword_suggestions(
            page_info, industry, extracted_keywords,
            commission_rate=commission_rate,
            avg_product_price=avg_product_price
        )
        
        print(f"\n✅ Đã tạo {len(keyword_suggestions)} đề xuất từ khóa")
        
        # Calculate projections
        print("\n📊 Đang tính toán dự báo campaign...")
        projections = self.calculate_campaign_projections(
            keyword_suggestions, monthly_budget
        )
        
        # Compile report
        report = {
            'analysis_date': time.strftime('%Y-%m-%d %H:%M:%S'),
            'landing_page': {
                'url': url,
                'title': page_info['title'],
                'meta_description': page_info['meta_description'],
                'h1_tags': page_info['h1_tags'][:5],
                'product_count': len(page_info['product_names']),
                'sample_products': page_info['product_names'][:10],
                'avg_product_price': page_info.get('avg_price', avg_product_price or 0),
                'target_age_range': target_age
            },
            'commission_settings': {
                'commission_rate': commission_rate,
                'avg_product_price': avg_product_price or page_info.get('avg_price', 0),
                'commission_per_sale': int((avg_product_price or page_info.get('avg_price', 0)) * (commission_rate / 100))
            },
            'industry_detected': industry,
            'industry_benchmark': self.industry_benchmarks[industry],
            'keyword_suggestions': keyword_suggestions,
            'campaign_projections': projections,
            'top_keywords_by_cpc': sorted(
                keyword_suggestions,
                key=lambda x: x['estimated_avg_cpc'],
                reverse=True
            )[:10],
            'top_keywords_by_cvr': sorted(
                keyword_suggestions,
                key=lambda x: x['estimated_cvr'],
                reverse=True
            )[:10]
        }
        
        return report
    
    def save_report(self, report, output_path):
        """
        Lưu báo cáo
        """
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Đã lưu báo cáo: {output_path}")
        
        return output_path
    
    def print_summary(self, report):
        """
        In tóm tắt báo cáo
        """
        print("\n" + "="*80)
        print("📊 TÓM TẮT PHÂN TÍCH")
        print("="*80)
        
        print(f"\n🌐 Landing Page: {report['landing_page']['url']}")
        print(f"📝 Title: {report['landing_page']['title']}")
        print(f"🏷️  Ngành hàng: {report['industry_detected']}")
        
        print(f"\n📈 Benchmark ngành:")
        benchmark = report['industry_benchmark']
        print(f"   - Average CVR: {benchmark['avg_cvr']}%")
        print(f"   - CPC Range: {benchmark['avg_cpc_range'][0]:,} - {benchmark['avg_cpc_range'][1]:,} VNĐ")
        
        proj = report['campaign_projections']
        print(f"\n💰 Dự báo với budget {proj['monthly_budget']:,} VNĐ/tháng:")
        metrics = proj['estimated_metrics']
        print(f"   - Avg CPC: {metrics['avg_cpc']:,} VNĐ")
        print(f"   - Avg CVR: {metrics['avg_cvr']}%")
        print(f"   - Clicks/tháng: {metrics['estimated_clicks_per_month']:,}")
        print(f"   - Conversions/tháng: {metrics['estimated_conversions_per_month']:,}")
        print(f"   - CPA: {metrics['estimated_cpa']:,} VNĐ")
        print(f"   - Impressions: {metrics['estimated_impressions']:,}")
        
        print(f"\n🔑 Từ khóa đề xuất:")
        print(f"   - Tổng: {proj['keyword_distribution']['total_keywords']}")
        print(f"   - By competition: {proj['keyword_distribution']['by_competition']}")
        
        print(f"\n🎯 Top 5 từ khóa CPC cao nhất:")
        for i, kw in enumerate(report['top_keywords_by_cpc'][:5], 1):
            print(f"   {i}. '{kw['keyword']}' - CPC: {kw['estimated_avg_cpc']:,} VNĐ, CVR: {kw['estimated_cvr']}%")
        
        print(f"\n🏆 Top 5 từ khóa CVR cao nhất:")
        for i, kw in enumerate(report['top_keywords_by_cvr'][:5], 1):
            print(f"   {i}. '{kw['keyword']}' - CVR: {kw['estimated_cvr']}%, CPC: {kw['estimated_avg_cpc']:,} VNĐ")
        
        if proj['recommendations']:
            print(f"\n💡 Khuyến nghị:")
            for rec in proj['recommendations']:
                emoji = '⚠️' if rec['type'] == 'warning' else '✅' if rec['type'] == 'success' else 'ℹ️'
                print(f"   {emoji} [{rec['category']}] {rec['message']}")
        
        print("="*80)


def main():
    """
    Test function
    """
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 landing_page_analyzer.py <URL> [monthly_budget]")
        print("Example: python3 landing_page_analyzer.py https://www.vascara.com 10000000")
        sys.exit(1)
    
    url = sys.argv[1]
    budget = int(sys.argv[2]) if len(sys.argv) > 2 else 10000000
    
    analyzer = LandingPageAnalyzer()
    report = analyzer.analyze_landing_page(url, budget)
    
    if report:
        # Save report
        import os
        output_dir = '../report/landing_page_analysis'
        os.makedirs(output_dir, exist_ok=True)
        
        domain = urlparse(url).netloc.replace('.', '_')
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        output_file = f"{output_dir}/{domain}_analysis_{timestamp}.json"
        
        analyzer.save_report(report, output_file)
        analyzer.print_summary(report)


if __name__ == "__main__":
    main()
