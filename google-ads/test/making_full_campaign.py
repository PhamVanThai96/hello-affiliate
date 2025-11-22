#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full Campaign Maker - Tạo chiến dịch affiliate marketing hoàn chỉnh
Phân tích landing page và tạo campaign plan với commission-based CPC
"""

import sys
import os
import json

# Add parent directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from planner.landing_page_analyzer import LandingPageAnalyzer
from planner.affiliate_campaign_planner import AffiliateCampaignPlanner

def analyze_landing_page_only(brand_name, domain, monthly_budget=10000000, commission_rate=8.0, allow_brand_keywords=True):
    """
    Chỉ phân tích landing page và tạo keyword suggestions
    
    Args:
        brand_name: Tên thương hiệu (vd: JUNO, Vascara)
        domain: Domain website (vd: https://juno.vn/)
        monthly_budget: Ngân sách tháng (VNĐ)
        commission_rate: Tỷ lệ hoa hồng (%)
        allow_brand_keywords: Cho phép từ khóa brand (True) hoặc chỉ generic keywords (False)
    """
    print("="*80)
    print(f"LANDING PAGE ANALYSIS - {brand_name.upper()}")
    print("="*80)
    
    print(f"\n📋 CONFIGURATION:")
    print(f"   - Brand: {brand_name}")
    print(f"   - URL: {domain}")
    print(f"   - Monthly Budget: {monthly_budget:,} VNĐ")
    print(f"   - Commission Rate: {commission_rate}%")
    print(f"   - Brand Keywords: {'Allowed (SEM brand)' if allow_brand_keywords else 'NOT Allowed (No brand SEM)'}")
    print(f"   - Avg Product Price: Auto-detect from landing page")
    
    # Create analyzer
    analyzer = LandingPageAnalyzer()
    
    # Analyze
    print("\n🚀 Starting analysis...")
    result = analyzer.analyze_landing_page(
        url=domain,
        monthly_budget=monthly_budget,
        commission_rate=commission_rate,
        avg_product_price=None  # Auto-detect
    )
    
    if not result:
        print("\n❌ Analysis failed!")
        return None
    
    # Display results
    print("\n" + "="*80)
    print("📊 ANALYSIS RESULTS")
    print("="*80)
    
    # Commission settings
    if 'commission_settings' in result:
        cs = result['commission_settings']
        print(f"\n💰 HOA HỒNG:")
        print(f"   - Tỷ lệ: {cs['commission_rate']}%")
        print(f"   - Giá TB sản phẩm: {cs['avg_product_price']:,} VNĐ")
        print(f"   - Hoa hồng/đơn: {cs['commission_per_sale']:,} VNĐ")
    
    # Industry
    print(f"\n🏷️  NGÀNH HÀNG: {result['industry_detected']}")
    
    # Keywords summary
    keywords = result['keyword_suggestions']
    
    # Filter out brand keywords if not allowed
    if not allow_brand_keywords:
        brand_terms = brand_name.lower().split()
        filtered_keywords = []
        excluded_count = 0
        
        for kw in keywords:
            keyword_lower = kw['keyword'].lower()
            # Check if any brand term appears in the keyword
            has_brand = any(term in keyword_lower for term in brand_terms if len(term) > 2)
            
            if not has_brand:
                filtered_keywords.append(kw)
            else:
                excluded_count += 1
        
        keywords = filtered_keywords
        result['keyword_suggestions'] = filtered_keywords
        
        # Update top keywords lists after filtering
        result['top_keywords_by_cpc'] = sorted(
            filtered_keywords,
            key=lambda x: x['estimated_avg_cpc'],
            reverse=True
        )[:10]
        
        result['top_keywords_by_cvr'] = sorted(
            filtered_keywords,
            key=lambda x: x['estimated_cvr'],
            reverse=True
        )[:10]
        
        print(f"\n🚫 BRAND KEYWORD FILTERING:")
        print(f"   - Excluded: {excluded_count} keywords containing brand name")
        print(f"   - Kept: {len(filtered_keywords)} generic keywords")
    
    print(f"\n🔑 TỪ KHÓA: {len(keywords)} suggestions")
    
    # Top 10 keywords by CPC
    print(f"\n📈 TOP 10 KEYWORDS BY CPC:")
    for i, kw in enumerate(result['top_keywords_by_cpc'][:10], 1):
        print(f"   {i}. '{kw['keyword']}'")
        print(f"      CPC: {kw['estimated_avg_cpc']:,} VNĐ | CVR: {kw['estimated_cvr']}% | Competition: {kw['competition']}")
        if 'estimated_clicks_per_conversion' in kw:
            print(f"      Clicks/conversion: {kw['estimated_clicks_per_conversion']}")
    
    # Campaign projections
    proj = result['campaign_projections']
    print(f"\n📊 PAID SEARCH PROJECTIONS:")
    print(f"   - Budget: {proj['monthly_budget']:,} VNĐ")
    print(f"   - Avg CPC: {proj['estimated_metrics']['avg_cpc']:,} VNĐ")
    print(f"   - Avg CVR: {proj['estimated_metrics']['avg_cvr']}%")
    print(f"   - Est. Clicks: {proj['estimated_metrics']['estimated_clicks_per_month']:,}")
    print(f"   - Est. Conversions: {proj['estimated_metrics']['estimated_conversions_per_month']}")
    print(f"   - Est. CPA: {proj['estimated_metrics']['estimated_cpa']:,} VNĐ")
    
    # Calculate ROI for paid search
    conversions = proj['estimated_metrics']['estimated_conversions_per_month']
    if 'commission_settings' in result:
        commission_per_sale = result['commission_settings']['commission_per_sale']
        total_revenue = conversions * commission_per_sale
        roi = ((total_revenue - monthly_budget) / monthly_budget) * 100 if monthly_budget > 0 else 0
        
        print(f"\n💵 PAID SEARCH ROI:")
        print(f"   - Total Commission: {total_revenue:,} VNĐ")
        print(f"   - Ad Spend: {monthly_budget:,} VNĐ")
        print(f"   - Profit: {total_revenue - monthly_budget:,} VNĐ")
        print(f"   - ROI: {roi:.1f}%")
        
        # Organic search estimation
        print(f"\n🌱 ORGANIC SEARCH ESTIMATION:")
        print(f"   (Based on SEO optimization for the same keywords)")
        
        # Estimate organic traffic (typically 3-5x paid traffic for established sites)
        # Conservative estimate: 2x for new affiliate sites
        organic_multiplier = 2.0
        organic_clicks = int(proj['estimated_metrics']['estimated_clicks_per_month'] * organic_multiplier)
        
        # Organic CVR is typically slightly lower than paid (less intent)
        organic_cvr = proj['estimated_metrics']['avg_cvr'] * 0.8  # 80% of paid CVR
        organic_conversions = int(organic_clicks * (organic_cvr / 100))
        
        # Organic revenue
        organic_revenue = organic_conversions * commission_per_sale
        
        # SEO cost estimate (content creation, backlinks, technical SEO)
        seo_monthly_cost = monthly_budget * 0.3  # 30% of paid budget for SEO efforts
        organic_profit = organic_revenue - seo_monthly_cost
        organic_roi = ((organic_revenue - seo_monthly_cost) / seo_monthly_cost) * 100 if seo_monthly_cost > 0 else 0
        
        print(f"   - Est. Organic Clicks: {organic_clicks:,}/month (2x paid traffic)")
        print(f"   - Est. Organic CVR: {organic_cvr:.1f}% (80% của paid CVR)")
        print(f"   - Est. Organic Conversions: {organic_conversions}/month")
        print(f"   - Est. SEO Cost: {int(seo_monthly_cost):,} VNĐ/month (content + backlinks)")
        print(f"   - Est. Organic Revenue: {int(organic_revenue):,} VNĐ")
        print(f"   - Est. Organic Profit: {int(organic_profit):,} VNĐ")
        print(f"   - Est. Organic ROI: {organic_roi:.1f}%")
        
        # Direct & Social traffic estimation
        print(f"\n🔗 DIRECT & SOCIAL TRAFFIC ESTIMATION:")
        print(f"   (Based on brand awareness and social media presence)")
        
        # Direct traffic: Typically 10-15% of organic for new affiliates
        direct_clicks = int(organic_clicks * 0.12)
        direct_cvr = proj['estimated_metrics']['avg_cvr'] * 1.3  # Higher intent (direct brand search)
        direct_conversions = int(direct_clicks * (direct_cvr / 100))
        direct_revenue = direct_conversions * commission_per_sale
        
        # Social traffic: Typically 5-8% of organic for active social presence
        social_clicks = int(organic_clicks * 0.06)
        social_cvr = proj['estimated_metrics']['avg_cvr'] * 0.7  # Lower intent (browsing)
        social_conversions = int(social_clicks * (social_cvr / 100))
        social_revenue = social_conversions * commission_per_sale
        
        # Social marketing cost (content creation, ads on social platforms)
        social_monthly_cost = monthly_budget * 0.15  # 15% of paid budget
        
        print(f"   - Direct Traffic Clicks: {direct_clicks:,}/month (12% of organic)")
        print(f"   - Direct CVR: {direct_cvr:.1f}% (higher brand intent)")
        print(f"   - Direct Conversions: {direct_conversions}/month")
        print(f"   - Direct Revenue: {int(direct_revenue):,} VNĐ (zero cost)")
        print(f"\n   - Social Traffic Clicks: {social_clicks:,}/month (6% of organic)")
        print(f"   - Social CVR: {social_cvr:.1f}% (browsing intent)")
        print(f"   - Social Conversions: {social_conversions}/month")
        print(f"   - Social Cost: {int(social_monthly_cost):,} VNĐ/month (content + ads)")
        print(f"   - Social Revenue: {int(social_revenue):,} VNĐ")
        print(f"   - Social ROI: {((social_revenue - social_monthly_cost) / social_monthly_cost * 100):.1f}%")
        
        # Combined performance (ALL channels)
        print(f"\n🎯 COMBINED (ALL CHANNELS) PERFORMANCE:")
        total_clicks = proj['estimated_metrics']['estimated_clicks_per_month'] + organic_clicks + direct_clicks + social_clicks
        total_conversions = conversions + organic_conversions + direct_conversions + social_conversions
        total_cost = monthly_budget + seo_monthly_cost + social_monthly_cost
        total_revenue_combined = total_revenue + organic_revenue + direct_revenue + social_revenue
        total_profit = total_revenue_combined - total_cost
        combined_roi = ((total_revenue_combined - total_cost) / total_cost) * 100 if total_cost > 0 else 0
        
        # Calculate percentages
        paid_click_percentage = (proj['estimated_metrics']['estimated_clicks_per_month'] / total_clicks) * 100 if total_clicks > 0 else 0
        organic_click_percentage = (organic_clicks / total_clicks) * 100 if total_clicks > 0 else 0
        direct_click_percentage = (direct_clicks / total_clicks) * 100 if total_clicks > 0 else 0
        social_click_percentage = (social_clicks / total_clicks) * 100 if total_clicks > 0 else 0
        
        print(f"   - Total Clicks: {total_clicks:,}/month")
        print(f"     • Paid Search: {proj['estimated_metrics']['estimated_clicks_per_month']:,} ({paid_click_percentage:.1f}%)")
        print(f"     • Organic SEO: {organic_clicks:,} ({organic_click_percentage:.1f}%)")
        print(f"     • Direct: {direct_clicks:,} ({direct_click_percentage:.1f}%)")
        print(f"     • Social: {social_clicks:,} ({social_click_percentage:.1f}%)")
        print(f"   - Total Conversions: {total_conversions}/month")
        print(f"   - Total Cost: {int(total_cost):,} VNĐ (Paid ads + SEO + Social)")
        print(f"   - Total Commission: {int(total_revenue_combined):,} VNĐ")
        print(f"   - Total Profit: {int(total_profit):,} VNĐ")
        print(f"   - Combined ROI: {combined_roi:.1f}%")
        
        print(f"\n📈 CHANNEL COMPARISON:")
        print(f"   {'Channel':<15} {'Clicks':<12} {'% of Total':<12} {'Conv':<8} {'Cost':<15} {'Revenue':<15} {'ROI':<10}")
        print(f"   {'-'*105}")
        print(f"   {'Paid Search':<15} {proj['estimated_metrics']['estimated_clicks_per_month']:>11,} {paid_click_percentage:>11.1f}% {conversions:>7} {monthly_budget:>14,} {int(total_revenue):>14,} {roi:>9.1f}%")
        print(f"   {'Organic SEO':<15} {organic_clicks:>11,} {organic_click_percentage:>11.1f}% {organic_conversions:>7} {int(seo_monthly_cost):>14,} {int(organic_revenue):>14,} {organic_roi:>9.1f}%")
        print(f"   {'Direct':<15} {direct_clicks:>11,} {direct_click_percentage:>11.1f}% {direct_conversions:>7} {0:>14,} {int(direct_revenue):>14,} {'∞':>9}")
        print(f"   {'Social':<15} {social_clicks:>11,} {social_click_percentage:>11.1f}% {social_conversions:>7} {int(social_monthly_cost):>14,} {int(social_revenue):>14,} {((social_revenue - social_monthly_cost) / social_monthly_cost * 100):>9.1f}%")
        print(f"   {'-'*105}")
        print(f"   {'TOTAL':<15} {total_clicks:>11,} {'100.0%':>11} {total_conversions:>7} {int(total_cost):>14,} {int(total_revenue_combined):>14,} {combined_roi:>9.1f}%")
    
    # Recommendations
    if 'recommendations' in proj:
        print(f"\n💡 PAID SEARCH RECOMMENDATIONS:")
        for rec in proj['recommendations']:
            print(f"   [{rec['type'].upper()}] {rec['category']}: {rec['message']}")
    
    # SEO Strategy recommendations
    print(f"\n💡 ORGANIC SEARCH STRATEGY:")
    print(f"   [TIMELINE] Month 1-3: Foundation")
    print(f"      - Create high-quality content for target keywords")
    print(f"      - Optimize on-page SEO (title, meta, headers)")
    print(f"      - Build initial backlink profile")
    print(f"      - Expected results: 20-30% of estimated traffic")
    print(f"\n   [TIMELINE] Month 4-6: Growth")
    print(f"      - Scale content production")
    print(f"      - Guest posting and PR for backlinks")
    print(f"      - Technical SEO improvements")
    print(f"      - Expected results: 50-70% of estimated traffic")
    print(f"\n   [TIMELINE] Month 7-12: Maturity")
    print(f"      - Maintain content freshness")
    print(f"      - Competitive link building")
    print(f"      - Authority building")
    print(f"      - Expected results: 80-100% of estimated traffic")
    print(f"\n   [STRATEGY] Hybrid Approach:")
    print(f"      - Use paid search for immediate results and data collection")
    print(f"      - Build SEO foundation for long-term sustainable traffic")
    print(f"      - Gradually shift budget from paid to SEO as organic grows")
    print(f"      - Target 70% organic / 30% paid ratio by month 12")
    
    # Ask if user wants to save report
    print("\n" + "="*80)
    save_report = input("💾 Lưu report vào file? (y/n) [default: y]: ").strip().lower()
    
    if save_report in ['', 'y', 'yes']:
        output_dir = os.path.join(parent_dir, 'report', 'campaign_plans')
        os.makedirs(output_dir, exist_ok=True)
        
        # Sanitize brand name for filename
        safe_brand_name = brand_name.lower().replace(' ', '_').replace('/', '_')
        output_file = os.path.join(output_dir, f'{safe_brand_name}_landing_page_analysis.json')
        
        # Add organic/paid comparison to result
        if 'commission_settings' in result:
            commission_per_sale = result['commission_settings']['commission_per_sale']
            conversions = proj['estimated_metrics']['estimated_conversions_per_month']
            total_revenue = conversions * commission_per_sale
            
            # Organic estimates
            organic_multiplier = 2.0
            organic_clicks = int(proj['estimated_metrics']['estimated_clicks_per_month'] * organic_multiplier)
            organic_cvr = proj['estimated_metrics']['avg_cvr'] * 0.8
            organic_conversions = int(organic_clicks * (organic_cvr / 100))
            organic_revenue = organic_conversions * commission_per_sale
            seo_monthly_cost = monthly_budget * 0.3
            
            # Direct & Social estimates
            direct_clicks = int(organic_clicks * 0.12)
            direct_cvr = proj['estimated_metrics']['avg_cvr'] * 1.3
            direct_conversions = int(direct_clicks * (direct_cvr / 100))
            direct_revenue = direct_conversions * commission_per_sale
            
            social_clicks = int(organic_clicks * 0.06)
            social_cvr = proj['estimated_metrics']['avg_cvr'] * 0.7
            social_conversions = int(social_clicks * (social_cvr / 100))
            social_revenue = social_conversions * commission_per_sale
            social_monthly_cost = monthly_budget * 0.15
            
            # Calculate total and percentages (ALL channels)
            total_clicks = proj['estimated_metrics']['estimated_clicks_per_month'] + organic_clicks + direct_clicks + social_clicks
            paid_click_percentage = (proj['estimated_metrics']['estimated_clicks_per_month'] / total_clicks) * 100 if total_clicks > 0 else 0
            organic_click_percentage = (organic_clicks / total_clicks) * 100 if total_clicks > 0 else 0
            direct_click_percentage = (direct_clicks / total_clicks) * 100 if total_clicks > 0 else 0
            social_click_percentage = (social_clicks / total_clicks) * 100 if total_clicks > 0 else 0
            
            result['channel_comparison'] = {
                'paid_search': {
                    'clicks': proj['estimated_metrics']['estimated_clicks_per_month'],
                    'click_percentage': round(paid_click_percentage, 1),
                    'conversions': conversions,
                    'cost': monthly_budget,
                    'revenue': int(total_revenue),
                    'profit': int(total_revenue - monthly_budget),
                    'roi': round(((total_revenue - monthly_budget) / monthly_budget) * 100, 1) if monthly_budget > 0 else 0
                },
                'organic_search': {
                    'clicks': organic_clicks,
                    'click_percentage': round(organic_click_percentage, 1),
                    'conversions': organic_conversions,
                    'cvr': round(organic_cvr, 1),
                    'cost': int(seo_monthly_cost),
                    'revenue': int(organic_revenue),
                    'profit': int(organic_revenue - seo_monthly_cost),
                    'roi': round(((organic_revenue - seo_monthly_cost) / seo_monthly_cost) * 100, 1) if seo_monthly_cost > 0 else 0,
                    'notes': 'Estimated at 2x paid traffic with 80% CVR. Timeline: 3-12 months to reach full potential'
                },
                'direct_traffic': {
                    'clicks': direct_clicks,
                    'click_percentage': round(direct_click_percentage, 1),
                    'conversions': direct_conversions,
                    'cvr': round(direct_cvr, 1),
                    'cost': 0,
                    'revenue': int(direct_revenue),
                    'profit': int(direct_revenue),
                    'roi': 'infinite',
                    'notes': 'Brand awareness traffic, 12% of organic, higher intent'
                },
                'social_media': {
                    'clicks': social_clicks,
                    'click_percentage': round(social_click_percentage, 1),
                    'conversions': social_conversions,
                    'cvr': round(social_cvr, 1),
                    'cost': int(social_monthly_cost),
                    'revenue': int(social_revenue),
                    'profit': int(social_revenue - social_monthly_cost),
                    'roi': round(((social_revenue - social_monthly_cost) / social_monthly_cost) * 100, 1) if social_monthly_cost > 0 else 0,
                    'notes': 'Facebook, Instagram, TikTok traffic, 6% of organic'
                },
                'combined': {
                    'total_clicks': total_clicks,
                    'total_conversions': conversions + organic_conversions + direct_conversions + social_conversions,
                    'total_cost': int(monthly_budget + seo_monthly_cost + social_monthly_cost),
                    'total_revenue': int(total_revenue + organic_revenue + direct_revenue + social_revenue),
                    'total_profit': int((total_revenue + organic_revenue + direct_revenue + social_revenue) - (monthly_budget + seo_monthly_cost + social_monthly_cost)),
                    'combined_roi': round((((total_revenue + organic_revenue + direct_revenue + social_revenue) - (monthly_budget + seo_monthly_cost + social_monthly_cost)) / (monthly_budget + seo_monthly_cost + social_monthly_cost)) * 100, 1)
                }
            }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Đã lưu report: {output_file}")
    else:
        print("⏭️  Bỏ qua việc lưu report")
    
    return result

def run_full_campaign_planner():
    """
    Chạy interactive campaign planner đầy đủ với keyword analysis chi tiết
    """
    print("="*80)
    print("FULL CAMPAIGN PLANNER - INTERACTIVE MODE")
    print("="*80)
    print("\n⚠️  Interactive mode: You will be prompted for all inputs")
    print("💡 Sử dụng landing page analyzer để đề xuất keywords, CPC, headlines")
    
    # Create planner
    planner = AffiliateCampaignPlanner()
    
    # Start planning with enhanced keyword analysis
    print("\n🚀 Starting campaign planner...")
    result = planner.run()
    
    # After planning, generate detailed keyword report with headlines
    if result and planner.landing_page_report:
        print("\n" + "="*80)
        print("📊 DETAILED KEYWORD & HEADLINE REPORT")
        print("="*80)
        
        generate_keyword_headline_report(
            planner.campaign_data,
            planner.landing_page_report,
            planner.campaign_data.get('brand_name', 'Brand')
        )
    
    return result

def show_campaign_summary(brand_name, domain, commission_rate, avg_price, budget, allow_brand_keywords=True):
    """
    Hiển thị tóm tắt chiến dịch dự kiến
    """
    print("\n" + "="*80)
    print(f"📋 {brand_name.upper()} CAMPAIGN SUMMARY (Expected)")
    print("="*80)
    
    print(f"\n💼 BRAND INFO:")
    print(f"   - Name: {brand_name}")
    print(f"   - Domain: {domain}")
    print(f"   - Type: E-commerce")
    print(f"   - Brand Keywords: {'Allowed (SEM brand)' if allow_brand_keywords else 'NOT Allowed (No brand SEM)'}")
    
    commission_per_sale = avg_price * (commission_rate / 100)
    
    print(f"\n💰 COMMISSION SETTINGS:")
    print(f"   - Commission Rate: {commission_rate}%")
    print(f"   - Avg Product Price: ~{avg_price:,} VNĐ")
    print(f"   - Commission/sale: ~{commission_per_sale:,} VNĐ")
    
    # Estimate CPC based on commission
    brand_cpc = (commission_per_sale * 0.5) / 20  # Brand keywords
    product_cpc = (commission_per_sale * 0.5) / 30  # Product keywords
    longtail_cpc = (commission_per_sale * 0.5) / 50  # Long-tail
    
    avg_cpc = (brand_cpc + product_cpc + longtail_cpc) / 3
    
    print(f"\n🎯 CAMPAIGN GOALS:")
    print(f"   - Goal: Conversions (affiliate sales)")
    print(f"   - Monthly Budget: {budget:,} VNĐ")
    
    if allow_brand_keywords:
        print(f"\n🔑 KEYWORD STRATEGY (Commission-based CPC):")
        print(f"   - Brand keywords: ~{int(brand_cpc):,} VNĐ CPC, 3.6% CVR, 20 clicks/conv")
        print(f"   - Product keywords: ~{int(product_cpc):,} VNĐ CPC, 2.6% CVR, 30 clicks/conv")
        print(f"   - Long-tail phrases: ~{int(longtail_cpc):,} VNĐ CPC, 3.4% CVR, 50 clicks/conv")
    else:
        print(f"\n🔑 KEYWORD STRATEGY (Commission-based CPC - NO BRAND):")
        print(f"   - Generic product keywords: ~{int(product_cpc):,} VNĐ CPC, 2.6% CVR, 30 clicks/conv")
        print(f"   - Long-tail phrases: ~{int(longtail_cpc):,} VNĐ CPC, 3.4% CVR, 50 clicks/conv")
        print(f"   - Category keywords: ~{int((product_cpc + longtail_cpc)/2):,} VNĐ CPC, 3.0% CVR, 40 clicks/conv")
        print(f"\n   ⚠️  Brand keywords EXCLUDED to comply with affiliate policy")
    
    # Projections
    est_clicks = int(budget / avg_cpc)
    est_cvr = 2.7  # Average
    est_conversions = int(est_clicks * (est_cvr / 100))
    est_cpa = int(budget / est_conversions) if est_conversions > 0 else 0
    est_revenue = est_conversions * commission_per_sale
    roi = ((est_revenue - budget) / budget) * 100 if budget > 0 else 0
    
    print(f"\n📊 PROJECTIONS ({int(budget/1000000)}M budget):")
    print(f"   - Avg CPC: ~{int(avg_cpc):,} VNĐ")
    print(f"   - Avg CVR: {est_cvr}%")
    print(f"   - Est. Clicks: {est_clicks:,}/month")
    print(f"   - Est. Conversions: {est_conversions}/month")
    print(f"   - Est. CPA: {est_cpa:,} VNĐ")
    print(f"   - Est. Revenue: {est_conversions} × {int(commission_per_sale):,} = {int(est_revenue):,} VNĐ commission")
    print(f"   - ROI: ({int(est_revenue/1000000)}M - {int(budget/1000000)}M) / {int(budget/1000000)}M = {roi:.0f}%")
    
    print(f"\n✅ COMMISSION-BASED CPC BENEFITS:")
    print(f"   - CPC capped based on affiliate economics")
    print(f"   - Ensures profitability at each keyword level")
    print(f"   - Realistic expectations for affiliate marketers")
    print(f"   - Maximum CPC never exceeds 50% of commission per conversion")
    
    # Ask if user wants to save summary
    print("\n" + "="*80)
    save_summary = input("💾 Lưu summary vào file? (y/n) [default: y]: ").strip().lower()
    
    if save_summary in ['', 'y', 'yes']:
        output_dir = os.path.join(parent_dir, 'report', 'campaign_plans')
        os.makedirs(output_dir, exist_ok=True)
        
        # Sanitize brand name for filename
        safe_brand_name = brand_name.lower().replace(' ', '_').replace('/', '_')
        output_file = os.path.join(output_dir, f'{safe_brand_name}_campaign_summary.json')
        
        # Create summary data
        summary_data = {
            'brand_name': brand_name,
            'domain': domain,
            'allow_brand_keywords': allow_brand_keywords,
            'commission_settings': {
                'commission_rate': commission_rate,
                'avg_product_price': int(avg_price),
                'commission_per_sale': int(commission_per_sale)
            },
            'campaign_goals': {
                'monthly_budget': int(budget)
            },
            'keyword_strategy': {
                'brand_keywords': {
                    'cpc': int(brand_cpc),
                    'cvr': 3.6,
                    'clicks_per_conversion': 20
                },
                'product_keywords': {
                    'cpc': int(product_cpc),
                    'cvr': 2.6,
                    'clicks_per_conversion': 30
                },
                'longtail_keywords': {
                    'cpc': int(longtail_cpc),
                    'cvr': 3.4,
                    'clicks_per_conversion': 50
                }
            },
            'projections': {
                'avg_cpc': int(avg_cpc),
                'avg_cvr': est_cvr,
                'estimated_clicks': est_clicks,
                'estimated_conversions': est_conversions,
                'estimated_cpa': est_cpa,
                'estimated_revenue': int(est_revenue),
                'roi': round(roi, 1)
            }
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(summary_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Đã lưu summary: {output_file}")
    else:
        print("⏭️  Bỏ qua việc lưu summary")

def parse_number(input_str, default_value):
    """
    Parse number input, handling Vietnamese format
    Supports:
    - Comma as thousand separator: 1,000,000 -> 1000000
    - Comma as decimal separator: 4,5 -> 4.5
    - Dot as thousand separator: 1.000.000 -> 1000000
    - Dot as decimal separator: 4.5 -> 4.5
    """
    if not input_str or not input_str.strip():
        return default_value
    
    cleaned = input_str.strip()
    
    try:
        # Count commas and dots
        comma_count = cleaned.count(',')
        dot_count = cleaned.count('.')
        
        # Case 1: Has multiple commas or dots -> thousand separator
        # Example: 1,000,000 or 1.000.000
        if comma_count > 1 or dot_count > 1:
            # Remove all commas and dots (thousand separators)
            cleaned = cleaned.replace(',', '').replace('.', '')
            return int(cleaned)
        
        # Case 2: Has both comma and dot
        # Determine which is decimal separator (comes last)
        elif comma_count > 0 and dot_count > 0:
            comma_pos = cleaned.rfind(',')
            dot_pos = cleaned.rfind('.')
            
            if comma_pos > dot_pos:
                # Comma is decimal: 1.000,50 -> remove dots, replace comma with dot
                cleaned = cleaned.replace('.', '').replace(',', '.')
            else:
                # Dot is decimal: 1,000.50 -> remove commas
                cleaned = cleaned.replace(',', '')
            
            return float(cleaned)
        
        # Case 3: Only comma(s)
        elif comma_count > 0:
            # Check if it's decimal or thousand separator
            # If only one comma and less than 3 digits after it -> decimal
            parts = cleaned.split(',')
            if len(parts) == 2 and len(parts[1]) <= 2:
                # Decimal: 4,5 -> 4.5
                cleaned = cleaned.replace(',', '.')
                return float(cleaned)
            else:
                # Thousand separator: 1,000,000
                cleaned = cleaned.replace(',', '')
                return int(cleaned)
        
        # Case 4: Only dot(s)
        elif dot_count > 0:
            # Check if it's decimal or thousand separator
            # If only one dot and less than 3 digits after it -> decimal
            parts = cleaned.split('.')
            if len(parts) == 2 and len(parts[1]) <= 2:
                # Decimal: 4.5
                return float(cleaned)
            else:
                # Thousand separator: 1.000.000
                cleaned = cleaned.replace('.', '')
                return int(cleaned)
        
        # Case 5: No comma or dot
        else:
            return int(cleaned)
    
    except ValueError:
        return default_value

def generate_keyword_headline_report(campaign_data, landing_page_report, brand_name):
    """
    Tạo báo cáo chi tiết về keywords và headlines với estimates
    """
    keywords = landing_page_report.get('keyword_suggestions', [])
    
    # Filter brand keywords if needed
    allow_brand = campaign_data.get('allow_brand_keywords', True)
    if not allow_brand:
        brand_terms = brand_name.lower().split()
        keywords = [kw for kw in keywords if not any(term in kw['keyword'].lower() for term in brand_terms if len(term) > 2)]
    
    # Ensure we have 10-50 keywords
    if len(keywords) < 10:
        print(f"\n⚠️  Chỉ tìm thấy {len(keywords)} keywords (tối thiểu 10)")
    
    keywords = keywords[:50]  # Max 50
    
    print(f"\n🔑 DETAILED KEYWORDS ({len(keywords)} keywords)")
    print("="*120)
    
    # Calculate monthly budget for click estimates
    monthly_budget = campaign_data.get('budget', {}).get('monthly_budget', 10000000)
    if isinstance(monthly_budget, str):
        monthly_budget = int(monthly_budget.replace(',', ''))
    
    print(f"\n{'#':<4} {'Keyword':<40} {'CPC Range':<20} {'Est. Clicks':<15} {'CVR':<8} {'Competition':<12}")
    print("-" * 120)
    
    for i, kw in enumerate(keywords, 1):
        min_cpc = kw['estimated_cpc_range']['min']
        max_cpc = kw['estimated_cpc_range']['max']
        avg_cpc = kw['estimated_avg_cpc']
        cvr = kw['estimated_cvr']
        comp = kw['competition']
        
        # Estimate clicks if we spend proportional budget on this keyword
        # Assume even distribution across all keywords
        keyword_budget = monthly_budget / len(keywords)
        est_clicks = int(keyword_budget / avg_cpc)
        
        print(f"{i:<4} {kw['keyword']:<40} {min_cpc:>8,}-{max_cpc:>8,} {est_clicks:>14,} {cvr:>7}% {comp:<12}")
    
    # Generate headlines from top keywords
    print(f"\n📰 AD HEADLINES & DESCRIPTIONS (Top 10)")
    print("="*120)
    
    # Take top 10 keywords by CVR for headlines
    top_keywords = sorted(keywords, key=lambda x: x['estimated_cvr'], reverse=True)[:10]
    
    for i, kw in enumerate(top_keywords, 1):
        keyword = kw['keyword']
        cvr = kw['estimated_cvr']
        cpc = kw['estimated_avg_cpc']
        
        # Generate headline variations
        headline = generate_headline(keyword, brand_name)
        description = generate_description(keyword, campaign_data, kw)
        
        print(f"\n{i}. HEADLINE: {headline}")
        print(f"   DESCRIPTION: {description}")
        print(f"   KEYWORD: '{keyword}' | CVR: {cvr}% | CPC: {cpc:,} VNĐ | Competition: {kw['competition']}")
        print(f"   CLICK ESTIMATE: {int(monthly_budget / len(keywords) / cpc):,}/month per keyword")
    
    # Save detailed report
    output_dir = os.path.join(parent_dir, 'report', 'campaign_plans')
    os.makedirs(output_dir, exist_ok=True)
    
    safe_brand = brand_name.lower().replace(' ', '_').replace('/', '_')
    output_file = os.path.join(output_dir, f'{safe_brand}_detailed_keywords_headlines.json')
    
    detailed_report = {
        'brand_name': brand_name,
        'total_keywords': len(keywords),
        'allow_brand_keywords': allow_brand,
        'monthly_budget': monthly_budget,
        'keywords': [
            {
                'keyword': kw['keyword'],
                'cpc_range': kw['estimated_cpc_range'],
                'avg_cpc': kw['estimated_avg_cpc'],
                'estimated_clicks': int(monthly_budget / len(keywords) / kw['estimated_avg_cpc']),
                'cvr': kw['estimated_cvr'],
                'competition': kw['competition'],
                'source': kw['source']
            }
            for kw in keywords
        ],
        'headlines': [
            {
                'headline': generate_headline(kw['keyword'], brand_name),
                'description': generate_description(kw['keyword'], campaign_data, kw),
                'keyword': kw['keyword'],
                'cvr': kw['estimated_cvr'],
                'avg_cpc': kw['estimated_avg_cpc'],
                'competition': kw['competition'],
                'estimated_clicks': int(monthly_budget / len(keywords) / kw['estimated_avg_cpc'])
            }
            for kw in top_keywords
        ]
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(detailed_report, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Đã lưu detailed report: {output_file}")

def generate_headline(keyword, brand_name):
    """
    Tạo headline từ keyword và brand name
    """
    # Capitalize keyword properly
    words = keyword.split()
    
    # Headline templates
    templates = [
        f"{keyword.title()} | {brand_name}",
        f"Mua {keyword.title()} Chính Hãng - {brand_name}",
        f"{keyword.title()} Giá Tốt | {brand_name}",
        f"{brand_name} - {keyword.title()} Ưu Đãi",
        f"{keyword.title()} - Miễn Phí Vận Chuyển"
    ]
    
    # Choose template based on keyword length
    if len(words) <= 2:
        return templates[1]  # "Mua X Chính Hãng"
    elif len(words) <= 4:
        return templates[0]  # "X | Brand"
    else:
        return templates[2]  # "X Giá Tốt"

def generate_description(keyword, campaign_data, keyword_data):
    """
    Tạo description từ keyword và campaign data
    """
    commission = campaign_data.get('affiliate_commission', 8.0)
    
    # Description templates
    templates = [
        f"{keyword.title()} chất lượng cao, giá tốt. Miễn phí vận chuyển toàn quốc. Đặt hàng ngay!",
        f"Khám phá {keyword} với ưu đãi đặc biệt. Giao hàng nhanh, thanh toán an toàn.",
        f"{keyword.title()} - Sản phẩm chính hãng, bảo hành đầy đủ. Mua ngay hôm nay!",
        f"Giảm giá lên đến {int(commission * 2)}% cho {keyword}. Số lượng có hạn, đặt ngay!",
        f"{keyword.title()} - Đa dạng mẫu mã, giá cả phải chăng. Trả góp 0% lãi suất."
    ]
    
    # Choose based on competition
    comp = keyword_data.get('competition', 'MEDIUM')
    if comp == 'LOW':
        return templates[0]  # Basic quality message
    elif comp == 'MEDIUM':
        return templates[1]  # Features + benefits
    else:  # HIGH
        return templates[3]  # Discount/urgency

def main():
    """
    Main function - cho phép chọn mode
    """
    print("\n" + "="*80)
    print("🎯 AFFILIATE CAMPAIGN MAKER")
    print("="*80)
    print("\nChọn mode:")
    print("1. Quick Analysis - Chỉ phân tích landing page + keyword suggestions")
    print("2. Full Campaign Planner - Interactive mode (đầy đủ 8 bước)")
    print("3. Show Summary - Xem tóm tắt campaign dự kiến")
    
    mode = input("\nChọn mode (1/2/3): ").strip()
    
    if mode == "1":
        # Quick analysis mode
        print("\n" + "="*80)
        print("QUICK ANALYSIS MODE")
        print("="*80)
        
        brand_name = input("\nNhập tên brand (vd: JUNO, Vascara): ").strip()
        domain = input("Nhập domain (vd: https://juno.vn/): ").strip()
        
        # Ensure domain has protocol
        if not domain.startswith('http'):
            domain = 'https://' + domain
        
        # Optional parameters with defaults
        budget_input = input("Nhập budget tháng (VNĐ) [default: 10,000,000]: ").strip()
        monthly_budget = parse_number(budget_input, 10000000)
        
        commission_input = input("Nhập tỷ lệ hoa hồng (%) [default: 8]: ").strip()
        commission_rate = parse_number(commission_input, 8.0)
        
        # Ask about brand keywords policy
        print("\n⚠️  AFFILIATE POLICY - Brand Keywords:")
        print("   Một số chương trình affiliate không cho phép SEM brand name")
        brand_allowed = input("Cho phép từ khóa chứa brand name? (y/n) [default: n]: ").strip().lower()
        allow_brand_keywords = brand_allowed in ['y', 'yes']
        
        if not allow_brand_keywords:
            print("   ✅ Sẽ loại bỏ tất cả từ khóa chứa brand name")
        else:
            print("   ✅ Sẽ bao gồm cả từ khóa brand")
        
        # Run analysis
        result = analyze_landing_page_only(brand_name, domain, monthly_budget, commission_rate, allow_brand_keywords)
        
        if result:
            print("\n✅ Analysis completed successfully!")
        
    elif mode == "2":
        # Full interactive mode
        run_full_campaign_planner()
        
    elif mode == "3":
        # Show summary
        print("\n" + "="*80)
        print("CAMPAIGN SUMMARY MODE")
        print("="*80)
        
        brand_name = input("\nNhập tên brand: ").strip()
        domain = input("Nhập domain: ").strip()
        
        if not domain.startswith('http'):
            domain = 'https://' + domain
        
        commission_input = input("Nhập tỷ lệ hoa hồng (%) [default: 8]: ").strip()
        commission_rate = parse_number(commission_input, 8.0)
        
        # Auto-detect price from landing page
        print("\n💡 Đang tự động phát hiện giá trung bình từ landing page...")
        analyzer = LandingPageAnalyzer()
        
        # Quick fetch to get price
        avg_price = 500000  # Default
        try:
            html_content = analyzer.fetch_page_content(domain)
            if html_content:
                page_info = analyzer.extract_page_info(html_content, domain)
                if page_info.get('avg_price', 0) > 0:
                    avg_price = page_info['avg_price']
                    print(f"✅ Đã phát hiện giá trung bình: {avg_price:,} VNĐ")
                else:
                    print("⚠️  Không phát hiện được giá, sử dụng default: 500,000 VNĐ")
        except Exception as e:
            print(f"⚠️  Lỗi khi phát hiện giá: {e}")
            print("   Sử dụng giá default: 500,000 VNĐ")
        
        # Allow manual override
        price_input = input(f"\nGiá trung bình sản phẩm [{avg_price:,} VNĐ] (Enter để dùng giá đã phát hiện): ").strip()
        if price_input:
            avg_price = parse_number(price_input, avg_price)
        
        budget_input = input("Nhập budget tháng (VNĐ) [default: 10,000,000]: ").strip()
        budget = parse_number(budget_input, 10000000)
        
        # Ask about brand keywords policy
        print("\n⚠️  AFFILIATE POLICY - Brand Keywords:")
        print("   Một số chương trình affiliate không cho phép SEM brand name")
        brand_allowed = input("Cho phép từ khóa chứa brand name? (y/n) [default: n]: ").strip().lower()
        allow_brand_keywords = brand_allowed in ['y', 'yes']
        
        if not allow_brand_keywords:
            print("   ✅ Sẽ tính toán với generic keywords only")
        else:
            print("   ✅ Sẽ bao gồm cả từ khóa brand")
        
        show_campaign_summary(brand_name, domain, commission_rate, avg_price, budget, allow_brand_keywords)
        
    else:
        print("\n❌ Invalid mode selection!")
        return

if __name__ == "__main__":
    main()
