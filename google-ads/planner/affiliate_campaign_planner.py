#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Ads Affiliate Campaign Planner
Thu thập thông tin và lập kế hoạch chiến dịch affiliate marketing
"""

import json
import os
import sys
from datetime import datetime

# Add parent directory to path to import keyword_analyzer
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from keyword_analyzer import KeywordAnalyzer
except ImportError:
    print("⚠️  Warning: keyword_analyzer not found. Keyword analysis will be skipped.")
    KeywordAnalyzer = None

try:
    from landing_page_analyzer import LandingPageAnalyzer
except ImportError:
    print("⚠️  Warning: landing_page_analyzer not found. Landing page analysis will be skipped.")
    LandingPageAnalyzer = None


class AffiliateCampaignPlanner:
    """
    Tool lập kế hoạch chiến dịch Google Ads cho Affiliate Marketing
    """
    
    def __init__(self):
        self.campaign_data = {}
        self.keyword_analyzer = KeywordAnalyzer() if KeywordAnalyzer else None
        self.landing_page_analyzer = LandingPageAnalyzer() if LandingPageAnalyzer else None
        self.landing_page_report = None
    
    def parse_number(self, input_str, default_value, as_int=False):
        """
        Parse number input, handling Vietnamese format (comma as decimal separator)
        
        Args:
            input_str: Input string to parse
            default_value: Default value if parsing fails or input is empty
            as_int: If True, return int; otherwise return float
        
        Returns:
            Parsed number (int or float) or default_value
        """
        if not input_str or not input_str.strip():
            return default_value
        
        # Replace comma with dot for decimal
        cleaned = input_str.strip().replace(',', '.')
        
        try:
            # Try as float first
            if '.' in cleaned:
                result = float(cleaned)
                return int(result) if as_int else result
            else:
                return int(cleaned)
        except ValueError:
            return default_value
    
    def collect_basic_info(self):
        """
        Bước 1: Thu thập thông tin cơ bản
        """
        print("\n" + "="*80)
        print("BƯỚC 1: THÔNG TIN CƠ BẢN VỀ CHIẾN DỊCH")
        print("="*80)
        
        # Brand & Domain
        print("\n📌 Thông tin Brand:")
        self.campaign_data['brand_name'] = input("   Tên thương hiệu (VD: varcasa): ").strip()
        self.campaign_data['domain'] = input("   Domain website (VD: varcasa.com): ").strip()
        self.campaign_data['landing_page'] = input("   Landing page URL (hoặc Enter để dùng homepage): ").strip()
        
        if not self.campaign_data['landing_page']:
            self.campaign_data['landing_page'] = f"https://{self.campaign_data['domain']}"
        
        # Loại hình kinh doanh
        print("\n📌 Loại hình kinh doanh:")
        business_types = [
            "E-commerce (Bán hàng online)",
            "Dịch vụ (Service)",
            "B2B (Business to Business)",
            "Lead Generation",
            "Content/Blog",
            "App Download",
            "Khác"
        ]
        
        for i, btype in enumerate(business_types, 1):
            print(f"   {i}. {btype}")
        
        business_choice = input("\n   Chọn loại hình (1-7): ").strip()
        self.campaign_data['business_type'] = business_types[int(business_choice)-1] if business_choice.isdigit() else "Khác"
        
        # Sản phẩm/Dịch vụ
        print("\n📌 Sản phẩm/Dịch vụ chính:")
        self.campaign_data['main_products'] = input("   Liệt kê các sản phẩm/dịch vụ (cách nhau bởi dấu phẩy):\n   ").strip().split(',')
        self.campaign_data['main_products'] = [p.strip() for p in self.campaign_data['main_products']]
        
        # Affiliate commission
        print("\n📌 Thông tin Affiliate:")
        commission_input = input("   Commission rate (%, VD: 8): ").strip()
        self.campaign_data['affiliate_commission'] = self.parse_number(commission_input, 8.0, as_int=False)
        
        print("\n   💡 Gợi ý: Giá trung bình sản phẩm sẽ được tự động phát hiện từ landing page")
        avg_price_input = input("   Giá trung bình sản phẩm (VNĐ) [Enter để auto-detect]: ").strip()
        if avg_price_input:
            self.campaign_data['avg_product_price'] = self.parse_number(avg_price_input, 500000, as_int=True)
        else:
            self.campaign_data['avg_product_price'] = None  # Will be detected from landing page
        
        if self.campaign_data['avg_product_price']:
            print(f"   → Hoa hồng trung bình/đơn hàng: {int(self.campaign_data['avg_product_price'] * self.campaign_data['affiliate_commission'] / 100):,} VNĐ")
        else:
            print(f"   → Giá sẽ được tự động phát hiện khi phân tích landing page")
        
        # Target audience
        print("\n📌 Đối tượng khách hàng mục tiêu:")
        print("   💡 Gợi ý: Độ tuổi sẽ được tự động phát hiện từ landing page")
        age_input = input("   Độ tuổi [Enter để auto-detect]: ").strip()
        self.campaign_data['target_audience'] = {
            'age_range': age_input if age_input else None,  # Will be detected from landing page
            'gender': input("   Giới tính (Nam/Nữ/Tất cả): ").strip(),
            'location': input("   Khu vực (VD: Hà Nội, TP.HCM, Toàn quốc): ").strip(),
            'interests': input("   Sở thích/Quan tâm (cách nhau bởi dấu phẩy): ").strip().split(',')
        }
        
        # Brand keywords policy
        print("\n📌 Affiliate Policy - Brand Keywords:")
        print("   Một số chương trình affiliate không cho phép SEM brand name")
        brand_allowed = input("   Cho phép từ khóa chứa brand name? (y/n) [default: n]: ").strip().lower()
        self.campaign_data['allow_brand_keywords'] = brand_allowed in ['y', 'yes']
        
        if not self.campaign_data['allow_brand_keywords']:
            print("   ✅ Sẽ loại bỏ tất cả từ khóa chứa brand name")
        else:
            print("   ✅ Sẽ bao gồm cả từ khóa brand")
        
        print("\n✅ Đã thu thập thông tin cơ bản!")
    
    def analyze_landing_page_content(self):
        """
        Bước 1.5: Phân tích landing page để đề xuất từ khóa, CPC, CVR
        """
        if not self.landing_page_analyzer:
            print("\n⚠️  Landing page analyzer không khả dụng. Bỏ qua bước này.")
            return
        
        print("\n" + "="*80)
        print("BƯỚC 1.5: PHÂN TÍCH LANDING PAGE")
        print("="*80)
        
        landing_url = self.campaign_data.get('landing_page')
        if not landing_url:
            print("⚠️  Không có landing page URL. Bỏ qua phân tích.")
            return
        
        print(f"\n🔍 Đang phân tích landing page: {landing_url}")
        print("   (Quá trình này có thể mất 10-30 giây...)")
        
        try:
            # Get monthly budget for projections
            monthly_budget = 10000000  # Default
            if 'budget' in self.campaign_data:
                monthly_budget = int(self.campaign_data['budget'].get('monthly_budget', '10000000').replace(',', ''))
            
            # Get affiliate commission info
            commission_rate = self.campaign_data.get('affiliate_commission', 8.0)
            avg_price = self.campaign_data.get('avg_product_price', 500000)
            
            # Analyze landing page
            self.landing_page_report = self.landing_page_analyzer.analyze_landing_page(
                landing_url,
                monthly_budget,
                commission_rate=commission_rate,
                avg_product_price=avg_price
            )
            
            if self.landing_page_report:
                # Update campaign data with insights
                self.campaign_data['landing_page_analysis'] = {
                    'analyzed': True,
                    'title': self.landing_page_report['landing_page']['title'],
                    'industry': self.landing_page_report['industry_detected'],
                    'products_found': self.landing_page_report['landing_page']['product_count']
                }
                
                # Auto-populate avg_product_price if not set
                if not self.campaign_data.get('avg_product_price'):
                    detected_price = self.landing_page_report['landing_page'].get('avg_product_price', 0)
                    if detected_price > 0:
                        self.campaign_data['avg_product_price'] = detected_price
                        print(f"\n✅ Đã tự động phát hiện giá trung bình: {detected_price:,} VNĐ")
                        commission = self.campaign_data.get('affiliate_commission', 8.0)
                        print(f"   → Hoa hồng trung bình/đơn hàng: {int(detected_price * commission / 100):,} VNĐ")
                
                # Auto-populate age_range if not set
                if not self.campaign_data['target_audience'].get('age_range'):
                    detected_age = self.landing_page_report['landing_page'].get('target_age_range')
                    if detected_age:
                        self.campaign_data['target_audience']['age_range'] = detected_age
                        print(f"\n✅ Đã tự động phát hiện độ tuổi mục tiêu: {detected_age}")
                
                # Merge keywords from landing page analysis
                lp_keywords = [kw['keyword'] for kw in self.landing_page_report['keyword_suggestions']]
                
                print(f"\n✅ Phân tích hoàn tất!")
                print(f"   - Tìm thấy {len(lp_keywords)} từ khóa từ landing page")
                print(f"   - Ngành hàng: {self.landing_page_report['industry_detected']}")
                
                # Show top 5 keywords
                top_5 = self.landing_page_report['keyword_suggestions'][:5]
                print(f"\n   📊 Top 5 từ khóa đề xuất:")
                for i, kw in enumerate(top_5, 1):
                    print(f"      {i}. {kw['keyword']}")
                    print(f"         CPC: {kw['estimated_avg_cpc']:,} VNĐ | CVR: {kw['estimated_cvr']}%")
            
        except Exception as e:
            print(f"\n❌ Lỗi khi phân tích landing page: {e}")
            import traceback
            traceback.print_exc()
        
        print("\n✅ Hoàn thành phân tích landing page!")
    
    def collect_campaign_goals(self):
        """
        Bước 2: Thu thập mục tiêu chiến dịch
        """
        print("\n" + "="*80)
        print("BƯỚC 2: MỤC TIÊU CHIẾN DỊCH")
        print("="*80)
        
        # Mục tiêu chính
        print("\n📌 Mục tiêu chính của chiến dịch:")
        goals = [
            "Tăng traffic website",
            "Tăng conversions (mua hàng, đăng ký)",
            "Brand awareness (nhận diện thương hiệu)",
            "Lead generation (thu thập thông tin khách hàng)",
            "App installs",
            "Phone calls",
            "Store visits"
        ]
        
        for i, goal in enumerate(goals, 1):
            print(f"   {i}. {goal}")
        
        goal_choice = input("\n   Chọn mục tiêu chính (1-7): ").strip()
        self.campaign_data['primary_goal'] = goals[int(goal_choice)-1] if goal_choice.isdigit() else goals[0]
        
        # KPIs
        print("\n📌 Chỉ số đo lường (KPIs):")
        self.campaign_data['kpis'] = {
            'target_clicks': input("   Số lượt click mục tiêu/tháng (VD: 5000): ").strip(),
            'target_conversions': input("   Số conversions mục tiêu/tháng (VD: 100): ").strip(),
            'target_cpa': input("   CPA (Cost Per Acquisition) mong muốn (VD: 50000 VNĐ): ").strip(),
            'target_roas': input("   ROAS (Return on Ad Spend) mong muốn (VD: 300%): ").strip()
        }
        
        print("\n✅ Đã thiết lập mục tiêu chiến dịch!")
    
    def collect_budget_info(self):
        """
        Bước 3: Ngân sách và lịch trình
        """
        print("\n" + "="*80)
        print("BƯỚC 3: NGÂN SÁCH & LỊCH TRÌNH")
        print("="*80)
        
        print("\n📌 Ngân sách quảng cáo:")
        self.campaign_data['budget'] = {
            'monthly_budget': input("   Ngân sách tháng (VNĐ, VD: 10000000): ").strip(),
            'daily_budget': input("   Ngân sách ngày (VNĐ, VD: 350000): ").strip(),
            'max_cpc': input("   Max CPC mong muốn (VNĐ, VD: 5000): ").strip()
        }
        
        print("\n📌 Lịch trình chạy:")
        self.campaign_data['schedule'] = {
            'start_date': input("   Ngày bắt đầu (YYYY-MM-DD hoặc Enter để bắt đầu ngay): ").strip() or datetime.now().strftime('%Y-%m-%d'),
            'end_date': input("   Ngày kết thúc (YYYY-MM-DD hoặc Enter nếu không giới hạn): ").strip(),
            'day_parting': input("   Khung giờ chạy (VD: 8:00-22:00 hoặc Enter nếu chạy 24/7): ").strip() or "24/7",
            'days_of_week': input("   Ngày trong tuần (VD: Thứ 2-6 hoặc Enter nếu chạy cả tuần): ").strip() or "Tất cả"
        }
        
        print("\n✅ Đã thiết lập ngân sách và lịch trình!")
    
    def analyze_keywords(self):
        """
        Bước 4: Nghiên cứu và phân tích từ khóa
        """
        print("\n" + "="*80)
        print("BƯỚC 4: NGHIÊN CỨU TỪ KHÓA")
        print("="*80)
        
        print("\n📌 Phân tích từ khóa cho sản phẩm/dịch vụ...")
        
        all_keywords = []
        keyword_analysis = {}
        
        # Kiểm tra xem có keyword_analyzer không
        if not self.keyword_analyzer:
            print("\n⚠️  Google Trends API không khả dụng.")
            print("   Bạn cần nhập từ khóa thủ công.\n")
        else:
            # Phân tích từ khóa chính từ sản phẩm
            for product in self.campaign_data['main_products'][:3]:  # Giới hạn 3 sản phẩm để tránh rate limit
                print(f"\n🔍 Đang phân tích: {product}")
                
                try:
                    # Sử dụng Google Trends API
                    result = self.keyword_analyzer.analyze_keyword(product, timeframe='today 3-m')
                    
                    if result and result.get('related_queries'):
                        # Lấy top related keywords
                        if result['related_queries']['top']:
                            top_keywords = [q['query'] for q in result['related_queries']['top'][:10]]
                            all_keywords.extend(top_keywords)
                            print(f"   ✅ Tìm thấy {len(top_keywords)} từ khóa liên quan")
                        
                        # Lấy rising keywords
                        if result['related_queries']['rising']:
                            rising_keywords = [q['query'] for q in result['related_queries']['rising'][:5]]
                            all_keywords.extend(rising_keywords)
                            print(f"   📈 Tìm thấy {len(rising_keywords)} từ khóa đang tăng")
                        
                        keyword_analysis[product] = result
                    
                except Exception as e:
                    print(f"   ⚠️  Lỗi khi phân tích '{product}': {e}")
        
        # Thu thập thêm từ khóa thủ công
        print("\n📌 Bạn có muốn thêm từ khóa thủ công không?")
        manual_keywords = input("   Nhập từ khóa (cách nhau bởi dấu phẩy, hoặc Enter để bỏ qua): ").strip()
        
        if manual_keywords:
            manual_list = [k.strip() for k in manual_keywords.split(',')]
            all_keywords.extend(manual_list)
        
        # Phân loại từ khóa
        print("\n📌 Phân loại từ khóa:")
        self.campaign_data['keywords'] = {
            'brand_keywords': [],
            'generic_keywords': [],
            'competitor_keywords': [],
            'long_tail_keywords': []
        }
        
        brand_name_lower = self.campaign_data['brand_name'].lower()
        
        for kw in set(all_keywords):  # Remove duplicates
            kw_lower = kw.lower()
            
            if brand_name_lower in kw_lower:
                self.campaign_data['keywords']['brand_keywords'].append(kw)
            elif len(kw.split()) >= 4:
                self.campaign_data['keywords']['long_tail_keywords'].append(kw)
            else:
                self.campaign_data['keywords']['generic_keywords'].append(kw)
        
        # In tóm tắt
        print("\n📊 TÓM TẮT TỪ KHÓA:")
        for kw_type, kw_list in self.campaign_data['keywords'].items():
            if kw_list:
                print(f"   {kw_type}: {len(kw_list)} từ khóa")
        
        self.campaign_data['keyword_analysis'] = keyword_analysis
        
        print("\n✅ Hoàn thành nghiên cứu từ khóa!")
    
    def create_ad_copy(self):
        """
        Bước 5: Tạo mẫu quảng cáo
        """
        print("\n" + "="*80)
        print("BƯỚC 5: TẠO MẪU QUẢNG CÁO")
        print("="*80)
        
        print("\n📌 Thông điệp chính:")
        self.campaign_data['ad_copy'] = {
            'unique_selling_points': [],
            'call_to_action': '',
            'headlines': [],
            'descriptions': []
        }
        
        # USPs
        print("\n   Nhập 3-5 điểm nổi bật của sản phẩm/dịch vụ:")
        for i in range(1, 6):
            usp = input(f"   USP {i} (hoặc Enter để bỏ qua): ").strip()
            if usp:
                self.campaign_data['ad_copy']['unique_selling_points'].append(usp)
            else:
                break
        
        # Call to Action
        print("\n📌 Call-to-Action (CTA):")
        cta_options = [
            "Mua ngay",
            "Đăng ký ngay",
            "Tìm hiểu thêm",
            "Nhận ưu đãi",
            "Liên hệ ngay",
            "Dùng thử miễn phí",
            "Đặt hàng ngay"
        ]
        
        for i, cta in enumerate(cta_options, 1):
            print(f"   {i}. {cta}")
        
        cta_choice = input("\n   Chọn CTA (1-7 hoặc nhập custom): ").strip()
        if cta_choice.isdigit() and 1 <= int(cta_choice) <= 7:
            self.campaign_data['ad_copy']['call_to_action'] = cta_options[int(cta_choice)-1]
        else:
            self.campaign_data['ad_copy']['call_to_action'] = cta_choice
        
        # Generate sample headlines
        print("\n📝 Tự động tạo mẫu Headlines...")
        brand = self.campaign_data['brand_name']
        usps = self.campaign_data['ad_copy']['unique_selling_points']
        
        sample_headlines = [
            f"{brand} - {usps[0] if usps else 'Giải pháp hàng đầu'}",
            f"{usps[1] if len(usps) > 1 else 'Chất lượng cao'} | {brand}",
            f"Mua {self.campaign_data['main_products'][0]} tại {brand}",
            f"{brand} - Uy tín, Chất lượng",
            f"Giảm giá {self.campaign_data['main_products'][0]} | {brand}"
        ]
        
        self.campaign_data['ad_copy']['headlines'] = sample_headlines
        
        # Generate sample descriptions
        print("📝 Tự động tạo mẫu Descriptions...")
        sample_descriptions = [
            f"{' | '.join(usps[:2])}. {self.campaign_data['ad_copy']['call_to_action']} hôm nay!",
            f"Mua sắm {self.campaign_data['main_products'][0]} tại {brand}. Giao hàng nhanh, đảm bảo chất lượng.",
            f"Ưu đãi đặc biệt cho khách hàng mới. {self.campaign_data['ad_copy']['call_to_action']} ngay!"
        ]
        
        self.campaign_data['ad_copy']['descriptions'] = sample_descriptions
        
        # Hiển thị preview
        print("\n" + "="*60)
        print("PREVIEW QUẢNG CÁO")
        print("="*60)
        
        for i, headline in enumerate(self.campaign_data['ad_copy']['headlines'], 1):
            print(f"\nHeadline {i}: {headline}")
        
        print("\n---")
        
        for i, desc in enumerate(self.campaign_data['ad_copy']['descriptions'], 1):
            print(f"\nDescription {i}: {desc}")
        
        print(f"\nDisplay URL: {self.campaign_data['domain']}")
        print(f"Final URL: {self.campaign_data['landing_page']}")
        print("="*60)
        
        print("\n✅ Đã tạo mẫu quảng cáo!")
    
    def setup_tracking(self):
        """
        Bước 6: Thiết lập tracking và conversion
        """
        print("\n" + "="*80)
        print("BƯỚC 6: THIẾT LẬP TRACKING & CONVERSION")
        print("="*80)
        
        self.campaign_data['tracking'] = {}
        
        # Google Analytics
        print("\n📌 Google Analytics:")
        ga_id = input("   Google Analytics ID (VD: G-XXXXXXXXXX hoặc Enter để bỏ qua): ").strip()
        self.campaign_data['tracking']['ga_id'] = ga_id
        
        # Conversion tracking
        print("\n📌 Conversion Actions:")
        print("   Các hành động được tính là conversion:")
        
        conversion_actions = []
        default_conversions = [
            "Mua hàng",
            "Đăng ký",
            "Gửi form liên hệ",
            "Gọi điện thoại",
            "Thêm vào giỏ hàng",
            "Download app"
        ]
        
        print("\n   Chọn conversion actions (cách nhau bởi dấu phẩy, VD: 1,2,4):")
        for i, action in enumerate(default_conversions, 1):
            print(f"   {i}. {action}")
        
        choices = input("\n   Nhập lựa chọn: ").strip()
        
        if choices:
            for choice in choices.split(','):
                if choice.strip().isdigit():
                    idx = int(choice.strip()) - 1
                    if 0 <= idx < len(default_conversions):
                        conversion_actions.append(default_conversions[idx])
        
        self.campaign_data['tracking']['conversion_actions'] = conversion_actions
        
        # UTM parameters
        print("\n📌 UTM Parameters cho tracking:")
        self.campaign_data['tracking']['utm_parameters'] = {
            'utm_source': 'google',
            'utm_medium': 'cpc',
            'utm_campaign': input("   UTM Campaign name (VD: summer_sale_2024): ").strip(),
            'utm_content': input("   UTM Content (VD: text_ad_v1 hoặc Enter để bỏ qua): ").strip(),
            'utm_term': '{keyword}'  # Dynamic keyword insertion
        }
        
        print("\n✅ Đã thiết lập tracking!")
    
    def create_campaign_structure(self):
        """
        Bước 7: Cấu trúc chiến dịch
        """
        print("\n" + "="*80)
        print("BƯỚC 7: CẤU TRÚC CHIẾN DỊCH")
        print("="*80)
        
        # Campaign type
        print("\n📌 Loại chiến dịch:")
        campaign_types = [
            "Search Campaign (Hiển thị trên kết quả tìm kiếm)",
            "Display Campaign (Banner trên websites)",
            "Shopping Campaign (Cho e-commerce)",
            "Video Campaign (YouTube)",
            "Performance Max (Tự động tối ưu đa kênh)"
        ]
        
        for i, ctype in enumerate(campaign_types, 1):
            print(f"   {i}. {ctype}")
        
        type_choice = input("\n   Chọn loại chiến dịch (1-5): ").strip()
        self.campaign_data['campaign_structure'] = {
            'campaign_type': campaign_types[int(type_choice)-1] if type_choice.isdigit() else campaign_types[0]
        }
        
        # Ad groups
        print("\n📌 Cấu trúc Ad Groups:")
        print("   Gợi ý: Mỗi ad group nên tập trung vào 1 nhóm từ khóa liên quan")
        
        ad_groups = []
        
        # Auto-suggest ad groups based on products
        for product in self.campaign_data['main_products']:
            ad_group = {
                'name': f"AG_{product.replace(' ', '_')}",
                'keywords': [],
                'match_types': ['Exact', 'Phrase', 'Broad']
            }
            ad_groups.append(ad_group)
        
        self.campaign_data['campaign_structure']['ad_groups'] = ad_groups
        
        print(f"\n   ✅ Đã tạo {len(ad_groups)} ad groups dựa trên sản phẩm")
        
        # Bidding strategy
        print("\n📌 Chiến lược đặt giá (Bidding):")
        bidding_strategies = [
            "Manual CPC (Kiểm soát hoàn toàn)",
            "Enhanced CPC (Tự động điều chỉnh)",
            "Maximize Clicks (Tối đa hóa clicks)",
            "Target CPA (Mục tiêu CPA cố định)",
            "Target ROAS (Mục tiêu ROAS cố định)",
            "Maximize Conversions (Tối đa hóa conversions)"
        ]
        
        for i, strategy in enumerate(bidding_strategies, 1):
            print(f"   {i}. {strategy}")
        
        bid_choice = input("\n   Chọn chiến lược (1-6): ").strip()
        self.campaign_data['campaign_structure']['bidding_strategy'] = (
            bidding_strategies[int(bid_choice)-1] if bid_choice.isdigit() else bidding_strategies[0]
        )
        
        print("\n✅ Đã thiết lập cấu trúc chiến dịch!")
    
    def generate_action_plan(self):
        """
        Bước 8: Tạo kế hoạch hành động
        """
        print("\n" + "="*80)
        print("BƯỚC 8: KẾ HOẠCH HÀNH ĐỘNG")
        print("="*80)
        
        action_plan = {
            'phase_1_setup': [
                "✅ Tạo Google Ads account (nếu chưa có)",
                "✅ Cài đặt Google Ads conversion tracking tag",
                "✅ Liên kết Google Analytics với Google Ads",
                "✅ Thiết lập billing và payment method",
                "✅ Tạo campaign với cấu trúc đã định"
            ],
            'phase_2_launch': [
                "✅ Upload keywords vào các ad groups",
                "✅ Tạo ads với headlines và descriptions",
                "✅ Thiết lập ad extensions (sitelinks, callouts, etc.)",
                "✅ Cấu hình audience targeting",
                "✅ Thiết lập negative keywords",
                "✅ Review và launch campaign"
            ],
            'phase_3_optimization': [
                "📊 Monitor performance hàng ngày (tuần đầu)",
                "📊 Phân tích search terms report",
                "📊 Thêm negative keywords",
                "📊 Điều chỉnh bids dựa trên performance",
                "📊 A/B test ad copy",
                "📊 Tối ưu landing pages",
                "📊 Scale budget cho ads có ROI tốt"
            ],
            'phase_4_scaling': [
                "📈 Mở rộng keyword list",
                "📈 Thử nghiệm campaign types mới",
                "📈 Remarketing cho visitors cũ",
                "📈 Lookalike audiences",
                "📈 Tăng budget dần dần"
            ]
        }
        
        self.campaign_data['action_plan'] = action_plan
        
        print("\n📋 KẾ HOẠCH TRIỂN KHAI:")
        
        for phase, tasks in action_plan.items():
            phase_name = phase.replace('_', ' ').title()
            print(f"\n🎯 {phase_name}:")
            for task in tasks:
                print(f"   {task}")
        
        print("\n✅ Đã tạo kế hoạch hành động!")
    
    def generate_checklist(self):
        """
        Tạo checklist để đảm bảo không bỏ sót gì
        """
        print("\n" + "="*80)
        print("CHECKLIST TRƯỚC KHI LAUNCH")
        print("="*80)
        
        checklist = {
            'Account Setup': [
                "☐ Google Ads account đã được tạo và verified",
                "☐ Payment method đã được thêm",
                "☐ Billing address đã chính xác",
                "☐ Account permissions đã được setup (nếu có team)"
            ],
            'Tracking & Analytics': [
                "☐ Google Analytics đã được cài đặt",
                "☐ Conversion tracking đã được setup",
                "☐ Goals đã được định nghĩa trong GA",
                "☐ UTM parameters đã được chuẩn bị",
                "☐ Test tracking đã hoạt động"
            ],
            'Campaign Setup': [
                "☐ Campaign settings đã được configure",
                "☐ Budget và bidding strategy đã phù hợp",
                "☐ Location targeting đã chính xác",
                "☐ Schedule đã được thiết lập",
                "☐ Ad groups đã được tạo với cấu trúc rõ ràng"
            ],
            'Keywords': [
                "☐ Keywords đã được nghiên cứu kỹ",
                "☐ Match types đã phù hợp",
                "☐ Negative keywords đã được thêm",
                "☐ Keyword bids đã hợp lý"
            ],
            'Ads': [
                "☐ Ads đã có đầy đủ headlines (tối thiểu 3)",
                "☐ Ads đã có descriptions (tối thiểu 2)",
                "☐ URLs đã chính xác và working",
                "☐ Ad extensions đã được thêm",
                "☐ Ads đã follow Google Ads policies"
            ],
            'Landing Pages': [
                "☐ Landing pages đã được tối ưu cho conversion",
                "☐ Page load speed < 3 seconds",
                "☐ Mobile-friendly",
                "☐ Clear CTA",
                "☐ Trust signals (reviews, testimonials)"
            ],
            'Final Checks': [
                "☐ Preview ads trên tất cả devices",
                "☐ Test all links",
                "☐ Review targeting settings",
                "☐ Double-check budget",
                "☐ Set up alerts và reports"
            ]
        }
        
        for category, items in checklist.items():
            print(f"\n📋 {category}:")
            for item in items:
                print(f"   {item}")
        
        self.campaign_data['checklist'] = checklist
    
    def save_campaign_plan(self):
        """
        Lưu toàn bộ campaign plan
        """
        # Get absolute path to parent directory
        parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        output_dir = os.path.join(parent_dir, 'report', 'campaign_plans')
        os.makedirs(output_dir, exist_ok=True)
        
        brand_name = self.campaign_data.get('brand_name', 'campaign').replace(' ', '_')
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{brand_name}_campaign_plan_{timestamp}.json"
        filepath = os.path.join(output_dir, filename)
        
        # Save JSON
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.campaign_data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Đã lưu campaign plan: {filepath}")
        
        # Generate markdown report
        md_filename = filename.replace('.json', '.md')
        md_filepath = os.path.join(output_dir, md_filename)
        
        self._generate_markdown_report(md_filepath)
        
        print(f"✅ Đã tạo báo cáo Markdown: {md_filepath}")
        
        # Save landing page analysis report if available
        lp_report_path = None
        if self.landing_page_report:
            lp_filename = f"{brand_name}_landing_page_analysis_{timestamp}.json"
            lp_filepath = os.path.join(output_dir, lp_filename)
            
            with open(lp_filepath, 'w', encoding='utf-8') as f:
                json.dump(self.landing_page_report, f, ensure_ascii=False, indent=2)
            
            lp_report_path = lp_filepath
            print(f"✅ Đã lưu Landing Page Analysis: {lp_filepath}")
        
        return filepath, md_filepath, lp_report_path
    
    def _generate_markdown_report(self, filepath):
        """
        Tạo báo cáo dạng Markdown
        """
        with open(filepath, 'w', encoding='utf-8') as f:
            # Header
            f.write(f"# CAMPAIGN PLAN: {self.campaign_data.get('brand_name', 'N/A').upper()}\n\n")
            f.write(f"**Domain:** {self.campaign_data.get('domain', 'N/A')}\n\n")
            f.write(f"**Ngày tạo:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("---\n\n")
            
            # Basic Info
            f.write("## 1. THÔNG TIN CƠ BẢN\n\n")
            f.write(f"- **Thương hiệu:** {self.campaign_data.get('brand_name', 'N/A')}\n")
            f.write(f"- **Website:** {self.campaign_data.get('domain', 'N/A')}\n")
            f.write(f"- **Landing Page:** {self.campaign_data.get('landing_page', 'N/A')}\n")
            f.write(f"- **Loại hình:** {self.campaign_data.get('business_type', 'N/A')}\n")
            f.write(f"- **Sản phẩm/Dịch vụ:**\n")
            for product in self.campaign_data.get('main_products', []):
                f.write(f"  - {product}\n")
            f.write("\n")
            
            # Target Audience
            if 'target_audience' in self.campaign_data:
                f.write("### Đối tượng mục tiêu\n\n")
                audience = self.campaign_data['target_audience']
                f.write(f"- **Độ tuổi:** {audience.get('age_range', 'N/A')}\n")
                f.write(f"- **Giới tính:** {audience.get('gender', 'N/A')}\n")
                f.write(f"- **Khu vực:** {audience.get('location', 'N/A')}\n")
                f.write(f"- **Sở thích:** {', '.join(audience.get('interests', []))}\n\n")
            
            # Goals
            f.write("## 2. MỤC TIÊU CHIẾN DỊCH\n\n")
            f.write(f"**Mục tiêu chính:** {self.campaign_data.get('primary_goal', 'N/A')}\n\n")
            
            if 'kpis' in self.campaign_data:
                f.write("### KPIs\n\n")
                kpis = self.campaign_data['kpis']
                f.write(f"- **Target Clicks:** {kpis.get('target_clicks', 'N/A')}/tháng\n")
                f.write(f"- **Target Conversions:** {kpis.get('target_conversions', 'N/A')}/tháng\n")
                f.write(f"- **Target CPA:** {kpis.get('target_cpa', 'N/A')} VNĐ\n")
                f.write(f"- **Target ROAS:** {kpis.get('target_roas', 'N/A')}\n\n")
            
            # Budget
            f.write("## 3. NGÂN SÁCH\n\n")
            if 'budget' in self.campaign_data:
                budget = self.campaign_data['budget']
                f.write(f"- **Ngân sách tháng:** {budget.get('monthly_budget', 'N/A')} VNĐ\n")
                f.write(f"- **Ngân sách ngày:** {budget.get('daily_budget', 'N/A')} VNĐ\n")
                f.write(f"- **Max CPC:** {budget.get('max_cpc', 'N/A')} VNĐ\n\n")
            
            # Schedule
            if 'schedule' in self.campaign_data:
                f.write("### Lịch trình\n\n")
                schedule = self.campaign_data['schedule']
                f.write(f"- **Bắt đầu:** {schedule.get('start_date', 'N/A')}\n")
                f.write(f"- **Kết thúc:** {schedule.get('end_date', 'Không giới hạn')}\n")
                f.write(f"- **Khung giờ:** {schedule.get('day_parting', '24/7')}\n")
                f.write(f"- **Ngày trong tuần:** {schedule.get('days_of_week', 'Tất cả')}\n\n")
            
            # Keywords
            f.write("## 4. TỪ KHÓA\n\n")
            if 'keywords' in self.campaign_data:
                keywords = self.campaign_data['keywords']
                
                if keywords.get('brand_keywords'):
                    f.write("### Brand Keywords\n\n")
                    for kw in keywords['brand_keywords'][:10]:
                        f.write(f"- {kw}\n")
                    f.write("\n")
                
                if keywords.get('generic_keywords'):
                    f.write("### Generic Keywords\n\n")
                    for kw in keywords['generic_keywords'][:20]:
                        f.write(f"- {kw}\n")
                    f.write("\n")
                
                if keywords.get('long_tail_keywords'):
                    f.write("### Long-tail Keywords\n\n")
                    for kw in keywords['long_tail_keywords'][:15]:
                        f.write(f"- {kw}\n")
                    f.write("\n")
            
            # Ad Copy
            f.write("## 5. MẪU QUẢNG CÁO\n\n")
            if 'ad_copy' in self.campaign_data:
                ad_copy = self.campaign_data['ad_copy']
                
                f.write("### USPs\n\n")
                for usp in ad_copy.get('unique_selling_points', []):
                    f.write(f"- {usp}\n")
                f.write("\n")
                
                f.write(f"**CTA:** {ad_copy.get('call_to_action', 'N/A')}\n\n")
                
                f.write("### Headlines\n\n")
                for i, headline in enumerate(ad_copy.get('headlines', []), 1):
                    f.write(f"{i}. {headline}\n")
                f.write("\n")
                
                f.write("### Descriptions\n\n")
                for i, desc in enumerate(ad_copy.get('descriptions', []), 1):
                    f.write(f"{i}. {desc}\n")
                f.write("\n")
            
            # Campaign Structure
            f.write("## 6. CẤU TRÚC CHIẾN DỊCH\n\n")
            if 'campaign_structure' in self.campaign_data:
                structure = self.campaign_data['campaign_structure']
                f.write(f"**Loại chiến dịch:** {structure.get('campaign_type', 'N/A')}\n\n")
                f.write(f"**Bidding Strategy:** {structure.get('bidding_strategy', 'N/A')}\n\n")
                
                if structure.get('ad_groups'):
                    f.write("### Ad Groups\n\n")
                    for ag in structure['ad_groups']:
                        f.write(f"- **{ag['name']}**\n")
                        f.write(f"  - Match Types: {', '.join(ag.get('match_types', []))}\n")
                    f.write("\n")
            
            # Tracking
            f.write("## 7. TRACKING & CONVERSION\n\n")
            if 'tracking' in self.campaign_data:
                tracking = self.campaign_data['tracking']
                f.write(f"**Google Analytics ID:** {tracking.get('ga_id', 'N/A')}\n\n")
                
                if tracking.get('conversion_actions'):
                    f.write("### Conversion Actions\n\n")
                    for action in tracking['conversion_actions']:
                        f.write(f"- {action}\n")
                    f.write("\n")
                
                if tracking.get('utm_parameters'):
                    f.write("### UTM Parameters\n\n")
                    utm = tracking['utm_parameters']
                    f.write(f"```\n")
                    for key, value in utm.items():
                        f.write(f"{key}={value}\n")
                    f.write(f"```\n\n")
            
            # Action Plan
            f.write("## 8. KẾ HOẠCH HÀNH ĐỘNG\n\n")
            if 'action_plan' in self.campaign_data:
                for phase, tasks in self.campaign_data['action_plan'].items():
                    phase_name = phase.replace('_', ' ').title()
                    f.write(f"### {phase_name}\n\n")
                    for task in tasks:
                        f.write(f"{task}\n")
                    f.write("\n")
            
            # Checklist
            f.write("## 9. CHECKLIST\n\n")
            if 'checklist' in self.campaign_data:
                for category, items in self.campaign_data['checklist'].items():
                    f.write(f"### {category}\n\n")
                    for item in items:
                        f.write(f"{item}\n")
                    f.write("\n")
            
            # Footer
            f.write("---\n\n")
            f.write("**Lưu ý:** Đây là campaign plan template. Cần điều chỉnh dựa trên:\n")
            f.write("- Phân tích đối thủ cạnh tranh chi tiết\n")
            f.write("- A/B testing kết quả\n")
            f.write("- Phản hồi từ thị trường\n")
            f.write("- Budget thực tế và ROI\n\n")
            f.write(f"*Generated by Affiliate Campaign Planner - {datetime.now().strftime('%Y-%m-%d')}*\n")
    
    def run(self):
        """
        Chạy toàn bộ quy trình
        """
        print("="*80)
        print("GOOGLE ADS AFFILIATE CAMPAIGN PLANNER")
        print("Công cụ lập kế hoạch chiến dịch affiliate marketing")
        print("="*80)
        
        print("\n📋 Quy trình gồm 8 bước:")
        print("   1. Thu thập thông tin cơ bản")
        print("   1.5. Phân tích landing page (CPC, CVR, keywords)")
        print("   2. Xác định mục tiêu")
        print("   3. Thiết lập ngân sách")
        print("   4. Nghiên cứu từ khóa")
        print("   5. Tạo mẫu quảng cáo")
        print("   6. Thiết lập tracking")
        print("   7. Cấu trúc chiến dịch")
        print("   8. Tạo kế hoạch hành động")
        
        input("\n👉 Nhấn Enter để bắt đầu...")
        
        try:
            # Run all steps
            self.collect_basic_info()
            self.analyze_landing_page_content()  # New step
            self.collect_campaign_goals()
            self.collect_budget_info()
            self.analyze_keywords()
            self.create_ad_copy()
            self.setup_tracking()
            self.create_campaign_structure()
            self.generate_action_plan()
            self.generate_checklist()
            
            # Save everything
            print("\n" + "="*80)
            print("LƯU CAMPAIGN PLAN")
            print("="*80)
            
            json_file, md_file, lp_file = self.save_campaign_plan()
            
            # Summary
            print("\n" + "="*80)
            print("🎉 HOÀN THÀNH!")
            print("="*80)
            
            print("\n📊 TÓM TẮT CHIẾN DỊCH:")
            print(f"   Brand: {self.campaign_data.get('brand_name', 'N/A')}")
            print(f"   Domain: {self.campaign_data.get('domain', 'N/A')}")
            print(f"   Mục tiêu: {self.campaign_data.get('primary_goal', 'N/A')}")
            print(f"   Ngân sách tháng: {self.campaign_data.get('budget', {}).get('monthly_budget', 'N/A')} VNĐ")
            print(f"   Số từ khóa: {sum(len(v) for v in self.campaign_data.get('keywords', {}).values())}")
            print(f"   Số ad groups: {len(self.campaign_data.get('campaign_structure', {}).get('ad_groups', []))}")
            
            print("\n📁 Files đã tạo:")
            print(f"   - JSON: {json_file}")
            print(f"   - Markdown: {md_file}")
            if lp_file:
                print(f"   - Landing Page Analysis: {lp_file}")
            
            # Show landing page insights if available
            if self.landing_page_report:
                print("\n📊 INSIGHTS TỪ LANDING PAGE:")
                proj = self.landing_page_report['campaign_projections']
                metrics = proj['estimated_metrics']
                print(f"   - Avg CPC ước tính: {metrics['avg_cpc']:,} VNĐ")
                print(f"   - Avg CVR ước tính: {metrics['avg_cvr']}%")
                print(f"   - Clicks dự kiến: {metrics['estimated_clicks_per_month']:,}/tháng")
                print(f"   - Conversions dự kiến: {metrics['estimated_conversions_per_month']:,}/tháng")
                print(f"   - CPA dự kiến: {metrics['estimated_cpa']:,} VNĐ")
            
            print("\n💡 BƯỚC TIẾP THEO:")
            print("   1. Review campaign plan trong file Markdown")
            if lp_file:
                print("   2. Review Landing Page Analysis để xem CPC/CVR chi tiết")
                print("   3. Điều chỉnh keywords dựa trên CPC và CVR đề xuất")
                print("   4. Setup Google Ads account")
                print("   5. Implement tracking codes")
                print("   6. Launch campaign!")
            else:
                print("   2. Điều chỉnh nếu cần thiết")
                print("   3. Setup Google Ads account")
                print("   4. Implement tracking codes")
                print("   5. Launch campaign!")
            
            return True  # Return success
            
        except KeyboardInterrupt:
            print("\n\n⏹️  Đã dừng chương trình")
            return False
        except Exception as e:
            print(f"\n❌ Lỗi: {e}")
            import traceback
            traceback.print_exc()
            return False


def main():
    """
    Main function
    """
    planner = AffiliateCampaignPlanner()
    planner.run()


if __name__ == "__main__":
    main()