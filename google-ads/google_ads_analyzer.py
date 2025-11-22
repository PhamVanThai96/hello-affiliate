#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Ads Keyword Analyzer
Tích hợp Google Ads API để lấy:
- Search Volume chính xác (monthly searches)
- CPC (Cost Per Click) thực tế
- Competition level (LOW/MEDIUM/HIGH)
- Keyword ideas từ Google Ads Keyword Planner
- Geographic targeting (Vietnam)
"""

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
import json
from datetime import datetime
import os
import time


class GoogleAdsKeywordAnalyzer:
    """
    Phân tích từ khóa sử dụng Google Ads API
    Lấy dữ liệu chính xác từ Google Ads Keyword Planner
    """
    
    def __init__(self, config_file='google-ads.yaml'):
        """
        Khởi tạo Google Ads Client
        
        Args:
            config_file: Đường dẫn file config YAML (absolute hoặc relative)
        """
        self.client = None
        self.customer_id = None
        
        # Resolve the config file path
        if not os.path.isabs(config_file):
            # If relative path, resolve from script directory
            config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), config_file)
        
        self.config_file = config_file
        
        try:
            print(f"📋 Đang load configuration từ: {config_file}")
            
            # Check if file exists
            if not os.path.exists(config_file):
                raise FileNotFoundError(f"File không tồn tại: {config_file}")
            
            self.client = GoogleAdsClient.load_from_storage(config_file)
            self.customer_id = self.client.login_customer_id
            
            if not self.customer_id or self.customer_id == 'YOUR_CUSTOMER_ID':
                raise ValueError("Customer ID chưa được cấu hình trong google-ads.yaml")
            
            print(f"✅ Kết nối Google Ads API thành công!")
            print(f"   Customer ID: {self.customer_id}")
            
        except FileNotFoundError:
            print(f"❌ Không tìm thấy file config: {config_file}")
            print("   Vui lòng tạo file google-ads.yaml với thông tin API")
            print("   Hoặc chạy: python3 get_new_token.py")
        except ValueError as e:
            print(f"❌ {e}")
            print("   Vui lòng cập nhật Customer ID trong google-ads.yaml")
        except Exception as e:
            print(f"❌ Lỗi kết nối Google Ads API: {e}")
            print(f"   Chi tiết: {type(e).__name__}")
            
            if 'invalid_grant' in str(e) or 'RefreshError' in str(type(e).__name__):
                print("\n💡 Refresh token không hợp lệ!")
                print("   Chạy: python3 get_new_token.py để lấy token mới")
    
    
    def is_connected(self):
        """
        Kiểm tra kết nối
        """
        return self.client is not None and self.customer_id is not None
    
    
    def get_keyword_ideas(self, keywords, location_id=2704, language_id=1010, page_size=50):
        """
        Lấy keyword ideas với CPC và search volume
        
        Args:
            keywords: List hoặc string từ khóa cần phân tích
            location_id: 2704 = Vietnam, 2840 = US
            language_id: 1010 = Vietnamese, 1000 = English
            page_size: Số lượng kết quả tối đa
        
        Returns:
            List keyword ideas với CPC và volume
        """
        if not self.is_connected():
            print("❌ Chưa kết nối Google Ads API")
            return []
        
        keyword_plan_idea_service = self.client.get_service("KeywordPlanIdeaService")
        
        request = self.client.get_type("GenerateKeywordIdeasRequest")
        request.customer_id = self.customer_id
        
        # Cấu hình location và language
        request.geo_target_constants.append(
            f"geoTargetConstants/{location_id}"
        )
        request.language = f"languageConstants/{language_id}"
        
        # Thêm seed keywords
        if isinstance(keywords, str):
            keywords = [keywords]
        
        request.keyword_seed.keywords.extend(keywords)
        
        # Số lượng kết quả
        request.page_size = page_size
        
        try:
            print(f"\n🔍 Đang tìm keyword ideas cho: {', '.join(keywords)}")
            response = keyword_plan_idea_service.generate_keyword_ideas(request=request)
            
            results = []
            for idea in response:
                metrics = idea.keyword_idea_metrics
                
                keyword_data = {
                    'keyword': idea.text,
                    'avg_monthly_searches': metrics.avg_monthly_searches,
                    'competition': metrics.competition.name,
                    'competition_index': metrics.competition_index,
                    'low_top_of_page_bid_micros': metrics.low_top_of_page_bid_micros / 1_000_000 if metrics.low_top_of_page_bid_micros else 0,
                    'high_top_of_page_bid_micros': metrics.high_top_of_page_bid_micros / 1_000_000 if metrics.high_top_of_page_bid_micros else 0,
                }
                
                # Tính CPC trung bình
                if keyword_data['low_top_of_page_bid_micros'] and keyword_data['high_top_of_page_bid_micros']:
                    keyword_data['avg_cpc_usd'] = (
                        keyword_data['low_top_of_page_bid_micros'] + 
                        keyword_data['high_top_of_page_bid_micros']
                    ) / 2
                    keyword_data['avg_cpc_vnd'] = keyword_data['avg_cpc_usd'] * 24000  # Tỷ giá USD-VND
                else:
                    keyword_data['avg_cpc_usd'] = 0
                    keyword_data['avg_cpc_vnd'] = 0
                
                results.append(keyword_data)
            
            print(f"✅ Tìm thấy {len(results)} keyword ideas")
            return results
            
        except GoogleAdsException as ex:
            print(f"\n❌ Lỗi Google Ads API:")
            for error in ex.failure.errors:
                print(f"   • {error.message}")
            return []
        except Exception as e:
            print(f"❌ Lỗi: {e}")
            return []
    
    
    def analyze_keyword(self, keyword, location='VN'):
        """
        Phân tích chi tiết một từ khóa
        
        Args:
            keyword: Từ khóa cần phân tích
            location: VN, US, etc.
        
        Returns:
            Dict với thông tin chi tiết
        """
        location_map = {
            'VN': (2704, 1010),  # Vietnam, Vietnamese
            'US': (2840, 1000),  # United States, English
            'UK': (2826, 1000),  # United Kingdom, English
            'JP': (2392, 1005),  # Japan, Japanese
        }
        
        location_id, language_id = location_map.get(location, (2704, 1010))
        
        ideas = self.get_keyword_ideas([keyword], location_id, language_id, page_size=20)
        
        if not ideas:
            return None
        
        # Lấy keyword chính
        main_keyword = next((k for k in ideas if k['keyword'].lower() == keyword.lower()), ideas[0])
        
        # Lấy related keywords
        related_keywords = [k for k in ideas if k['keyword'].lower() != keyword.lower()][:10]
        
        # Tính opportunity score
        opportunity_score = self._calculate_opportunity_score(main_keyword)
        
        result = {
            'keyword': keyword,
            'timestamp': datetime.now().isoformat(),
            'location': location,
            'source': 'Google Ads API',
            'main_keyword_data': main_keyword,
            'related_keywords': related_keywords,
            'summary': {
                'avg_monthly_searches': main_keyword['avg_monthly_searches'],
                'avg_cpc_usd': round(main_keyword['avg_cpc_usd'], 2),
                'avg_cpc_vnd': round(main_keyword['avg_cpc_vnd'], 0),
                'competition': main_keyword['competition'],
                'competition_index': main_keyword['competition_index'],
                'opportunity_score': opportunity_score
            }
        }
        
        return result
    
    
    def _calculate_opportunity_score(self, keyword_data):
        """
        Tính điểm cơ hội (0-100)
        Dựa trên: Volume cao, CPC thấp-trung bình, Competition thấp
        """
        # Volume score (40 điểm)
        volume = keyword_data['avg_monthly_searches']
        if volume >= 10000:
            volume_score = 40
        elif volume >= 5000:
            volume_score = 35
        elif volume >= 1000:
            volume_score = 25
        elif volume >= 100:
            volume_score = 15
        else:
            volume_score = 5
        
        # Competition score (30 điểm)
        comp_index = keyword_data['competition_index']
        competition_score = (100 - comp_index) * 0.3
        
        # CPC score (30 điểm) - CPC vừa phải là tốt nhất
        cpc = keyword_data['avg_cpc_usd']
        if 0.1 <= cpc <= 2:  # Sweet spot
            cpc_score = 30
        elif 2 < cpc <= 5:
            cpc_score = 20
        elif cpc < 0.1:
            cpc_score = 10  # Quá rẻ có thể không có giá trị
        else:
            cpc_score = 5   # Quá đắt
        
        total_score = volume_score + competition_score + cpc_score
        return round(total_score, 2)
    
    
    def export_report(self, keyword, location='VN', output_dir='report'):
        """
        Xuất báo cáo phân tích ra file
        """
        os.makedirs(output_dir, exist_ok=True)
        
        result = self.analyze_keyword(keyword, location)
        
        if not result:
            print(f"❌ Không thể phân tích từ khóa: {keyword}")
            return None
        
        # Tạo filename
        safe_keyword = keyword.replace(' ', '_').replace('/', '_')
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"google_ads_analysis_{safe_keyword}_{timestamp}.json"
        filepath = os.path.join(output_dir, filename)
        
        # Lưu file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Đã lưu báo cáo: {filepath}")
        
        # In tóm tắt
        self._print_summary(result)
        
        return filepath
    
    
    def _print_summary(self, result):
        """
        In tóm tắt kết quả
        """
        print("\n" + "="*80)
        print(f"📊 PHÂN TÍCH TỪ KHÓA: {result['keyword']}")
        print("="*80)
        
        main = result['main_keyword_data']
        summary = result['summary']
        
        print(f"\n🔍 Thông tin chính:")
        print(f"   • Search Volume: {main['avg_monthly_searches']:,} searches/month")
        print(f"   • CPC trung bình: ${main['avg_cpc_usd']:.2f} USD ({summary['avg_cpc_vnd']:,.0f} VNĐ)")
        print(f"   • Competition: {main['competition']} ({main['competition_index']}/100)")
        print(f"   • CPC Range: ${main['low_top_of_page_bid_micros']:.2f} - ${main['high_top_of_page_bid_micros']:.2f} USD")
        print(f"   • Opportunity Score: {summary['opportunity_score']}/100")
        
        # Đánh giá
        if summary['opportunity_score'] >= 70:
            rating = "🌟 XUẤT SẮC - Từ khóa rất tiềm năng!"
        elif summary['opportunity_score'] >= 50:
            rating = "✅ TỐT - Đáng đầu tư"
        elif summary['opportunity_score'] >= 30:
            rating = "⚠️  TRUNG BÌNH - Cân nhắc kỹ"
        else:
            rating = "❌ YẾU - Không khuyến nghị"
        
        print(f"\n💡 Đánh giá: {rating}")
        
        print(f"\n📈 Top 5 từ khóa liên quan:")
        for i, kw in enumerate(result['related_keywords'][:5], 1):
            print(f"   {i}. {kw['keyword']}")
            print(f"      Volume: {kw['avg_monthly_searches']:,} | CPC: ${kw['avg_cpc_usd']:.2f} | Competition: {kw['competition']}")
        
        print("\n" + "="*80)


def main():
    """
    Main function - Interactive keyword analysis với Google Ads API
    """
    print("="*80)
    print("GOOGLE ADS API - KEYWORD ANALYZER")
    print("Phân tích từ khóa với dữ liệu CHÍNH XÁC từ Google Ads")
    print("="*80)
    
    # Khởi tạo analyzer
    analyzer = GoogleAdsKeywordAnalyzer('config/google-ads.yaml')
    
    if not analyzer.is_connected():
        print("\n" + "="*80)
        print("⚠️  CHƯA CẤU HÌNH GOOGLE ADS API")
        print("="*80)
        print("\n📝 Các bước setup:")
        print("\n1️⃣  Cập nhật file google-ads.yaml với thông tin:")
        print("   • developer_token: g8hYH85l_QlKKQ6RamWwgw (đã có)")
        print("   • client_id: Lấy từ Google Cloud Console")
        print("   • client_secret: Lấy từ Google Cloud Console")
        print("   • refresh_token: Chạy get_refresh_token.py để lấy")
        print("   • login_customer_id: Customer ID từ Google Ads")
        print("\n2️⃣  Hướng dẫn chi tiết:")
        print("   a. Tạo OAuth credentials:")
        print("      - Truy cập: https://console.cloud.google.com/")
        print("      - APIs & Services > Credentials")
        print("      - Create OAuth 2.0 Client ID (Desktop app)")
        print("      - Download client_secret.json")
        print("\n   b. Lấy refresh token:")
        print("      - Chạy: python3 get_refresh_token.py")
        print("      - Đăng nhập và cho phép quyền")
        print("      - Copy refresh_token vào google-ads.yaml")
        print("\n   c. Customer ID:")
        print("      - Vào Google Ads account")
        print("      - Xem Customer ID ở góc trên (123-456-7890)")
        print("      - Bỏ dấu gạch ngang: 1234567890")
        print("\n3️⃣  Sau khi setup xong, chạy lại script này")
        print("\n" + "="*80)
        return
    
    # Loop phân tích
    while True:
        print("\n" + "="*80)
        keyword = input("\n🔍 Nhập từ khóa cần phân tích (hoặc 'quit' để thoát): ").strip()
        
        if keyword.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Cảm ơn bạn đã sử dụng Google Ads Keyword Analyzer!")
            break
        
        if not keyword:
            print("⚠️  Vui lòng nhập từ khóa!")
            continue
        
        # Chọn location
        print("\n🌍 Chọn khu vực:")
        print("   1. Vietnam (VN)")
        print("   2. United States (US)")
        print("   3. United Kingdom (UK)")
        print("   4. Japan (JP)")
        
        location_choice = input("\nNhập số (mặc định: 1): ").strip() or "1"
        location_map = {"1": "VN", "2": "US", "3": "UK", "4": "JP"}
        location = location_map.get(location_choice, "VN")
        
        # Phân tích và xuất báo cáo
        print(f"\n⏳ Đang phân tích từ khóa '{keyword}' cho khu vực {location}...")
        
        try:
            analyzer.export_report(keyword, location)
        except Exception as e:
            print(f"\n❌ Lỗi khi phân tích: {e}")
        
        # Tiếp tục?
        continue_analysis = input("\n🔄 Phân tích từ khóa khác? (y/n) [mặc định: y]: ").strip().lower() or 'y'
        
        if continue_analysis != 'y':
            print("\n👋 Cảm ơn bạn đã sử dụng Google Ads Keyword Analyzer!")
            break


if __name__ == "__main__":
    main()
