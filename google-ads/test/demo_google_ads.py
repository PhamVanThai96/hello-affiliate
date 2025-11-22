#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo Google Ads API - Keyword Analysis
Ví dụ sử dụng google_ads_analyzer.py để phân tích từ khóa
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google_ads_analyzer import GoogleAdsKeywordAnalyzer
import json

# Determine the absolute path to the configuration file
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
CONFIG_FILE_PATH = os.path.join(PROJECT_DIR, 'config', 'google-ads.yaml')

print(f"🔍 Config file path: {CONFIG_FILE_PATH}")
print(f"📂 Config file exists: {os.path.exists(CONFIG_FILE_PATH)}\n")

def demo_basic_search():
    """Demo 1: Tìm kiếm cơ bản"""
    print("\n" + "="*80)
    print("DEMO 1: TÌM KIẾM CƠ BẢN")
    print("="*80)
    
    analyzer = GoogleAdsKeywordAnalyzer(config_file=CONFIG_FILE_PATH)
    
    if not analyzer.is_connected():
        print("❌ Không thể kết nối Google Ads API")
        print("   Vui lòng chạy: python3 get_new_token.py")
        return
    
    # Tìm keyword ideas
    keywords = ['gốm sứ', 'sứ cao cấp']
    results = analyzer.get_keyword_ideas(keywords, page_size=20)
    
    if results:
        print(f"\n📊 Top 10 keywords:")
        for i, kw in enumerate(results[:10], 1):
            print(f"\n{i}. {kw['keyword']}")
            print(f"   📈 Monthly Searches: {kw['avg_monthly_searches']:,}")
            print(f"   💰 CPC: ${kw['avg_cpc_usd']:.2f} USD (~{kw['avg_cpc_vnd']:,.0f} VND)")
            print(f"   🎯 Competition: {kw['competition']} ({kw['competition_index']}/100)")


def demo_detailed_analysis():
    """Demo 2: Phân tích chi tiết"""
    print("\n" + "="*80)
    print("DEMO 2: PHÂN TÍCH CHI TIẾT MỘT TỪ KHÓA")
    print("="*80)
    
    analyzer = GoogleAdsKeywordAnalyzer(config_file=CONFIG_FILE_PATH)
    
    if not analyzer.is_connected():
        return
    
    # Phân tích từ khóa cụ thể
    keyword = "gốm sứ minh long"
    print(f"\n🔍 Phân tích: '{keyword}'")
    
    result = analyzer.analyze_keyword(keyword)
    
    if result:
        print("\n" + "-"*80)
        print("THÔNG TIN CHI TIẾT")
        print("-"*80)
        
        main = result['main_keyword']
        print(f"\n📝 Từ khóa chính: {main['keyword']}")
        print(f"📈 Lượt tìm kiếm/tháng: {main['avg_monthly_searches']:,}")
        print(f"💰 CPC trung bình: ${main['avg_cpc_usd']:.2f} USD")
        print(f"💵 CPC (VND): ~{main['avg_cpc_vnd']:,.0f} VND")
        print(f"🎯 Mức độ cạnh tranh: {main['competition']}")
        print(f"⭐ Điểm cơ hội: {main['opportunity_score']}/100")
        
        if result['related_keywords']:
            print(f"\n📋 Từ khóa liên quan ({len(result['related_keywords'])} keywords):")
            for i, kw in enumerate(result['related_keywords'][:5], 1):
                print(f"\n   {i}. {kw['keyword']}")
                print(f"      Searches: {kw['avg_monthly_searches']:,} | CPC: ${kw['avg_cpc_usd']:.2f}")


def demo_compare_keywords():
    """Demo 3: So sánh nhiều từ khóa"""
    print("\n" + "="*80)
    print("DEMO 3: SO SÁNH NHIỀU TỪ KHÓA")
    print("="*80)
    
    analyzer = GoogleAdsKeywordAnalyzer(config_file=CONFIG_FILE_PATH)
    
    if not analyzer.is_connected():
        return
    
    # Danh sách từ khóa cần so sánh
    keywords_to_compare = [
        'gốm sứ',
        'sứ cao cấp',
        'bình gốm sứ',
        'đồ gốm mỹ nghệ',
        'gốm sứ bát tràng'
    ]
    
    print(f"\n📊 So sánh {len(keywords_to_compare)} từ khóa...")
    
    comparison = []
    for kw in keywords_to_compare:
        results = analyzer.get_keyword_ideas([kw], page_size=1)
        if results:
            comparison.append(results[0])
    
    # Sắp xếp theo opportunity score
    comparison.sort(key=lambda x: (x['avg_monthly_searches'], -x['avg_cpc_usd']), reverse=True)
    
    print("\n" + "-"*80)
    print("KẾT QUẢ SO SÁNH (sắp xếp theo volume)")
    print("-"*80)
    
    print(f"\n{'Từ khóa':<25} {'Searches':<12} {'CPC (USD)':<12} {'Competition':<15}")
    print("-"*80)
    
    for kw in comparison:
        print(f"{kw['keyword']:<25} {kw['avg_monthly_searches']:<12,} ${kw['avg_cpc_usd']:<11.2f} {kw['competition']:<15}")


def demo_export_report():
    """Demo 4: Xuất báo cáo"""
    print("\n" + "="*80)
    print("DEMO 4: XUẤT BÁO CÁO")
    print("="*80)
    
    analyzer = GoogleAdsKeywordAnalyzer(config_file=CONFIG_FILE_PATH)
    
    if not analyzer.is_connected():
        return
    
    keyword = "gốm sứ cao cấp"
    print(f"\n📄 Tạo báo cáo cho: '{keyword}'")
    
    result = analyzer.export_report(keyword)
    
    if result:
        print(f"\n✅ Báo cáo đã được lưu:")
        print(f"   📁 JSON: {result['json_file']}")
        print(f"   📁 CSV: {result['csv_file']}")


def demo_high_volume_keywords():
    """Demo 5: Tìm từ khóa volume cao"""
    print("\n" + "="*80)
    print("DEMO 5: TÌM TỪ KHÓA VOLUME CAO")
    print("="*80)
    
    analyzer = GoogleAdsKeywordAnalyzer(config_file=CONFIG_FILE_PATH)
    
    if not analyzer.is_connected():
        return
    
    # Tìm keyword ideas
    seed_keywords = ['gốm sứ']
    results = analyzer.get_keyword_ideas(seed_keywords, page_size=50)
    
    # Lọc keywords có volume > 1000
    high_volume = [kw for kw in results if kw['avg_monthly_searches'] >= 1000]
    
    # Sắp xếp theo volume giảm dần
    high_volume.sort(key=lambda x: x['avg_monthly_searches'], reverse=True)
    
    print(f"\n📊 Tìm thấy {len(high_volume)} keywords có volume ≥ 1,000/tháng")
    print("\nTop 10:")
    print("-"*80)
    
    for i, kw in enumerate(high_volume[:10], 1):
        print(f"\n{i}. {kw['keyword']}")
        print(f"   📈 {kw['avg_monthly_searches']:,} searches/month")
        print(f"   💰 ${kw['avg_cpc_usd']:.2f} CPC")
        print(f"   🎯 {kw['competition']}")


def demo_low_competition():
    """Demo 6: Tìm từ khóa cạnh tranh thấp"""
    print("\n" + "="*80)
    print("DEMO 6: TÌM TỪ KHÓA CẠNH TRANH THẤP")
    print("="*80)
    
    analyzer = GoogleAdsKeywordAnalyzer(config_file=CONFIG_FILE_PATH)
    
    if not analyzer.is_connected():
        return
    
    seed_keywords = ['gốm sứ', 'đồ gốm']
    results = analyzer.get_keyword_ideas(seed_keywords, page_size=50)
    
    # Lọc keywords LOW competition
    low_comp = [kw for kw in results if kw['competition'] == 'LOW']
    
    # Sắp xếp theo volume
    low_comp.sort(key=lambda x: x['avg_monthly_searches'], reverse=True)
    
    print(f"\n📊 Tìm thấy {len(low_comp)} keywords có cạnh tranh THẤP")
    
    if low_comp:
        print("\nTop 10 (cạnh tranh thấp + volume cao):")
        print("-"*80)
        
        for i, kw in enumerate(low_comp[:10], 1):
            print(f"\n{i}. {kw['keyword']}")
            print(f"   📈 {kw['avg_monthly_searches']:,} searches")
            print(f"   💰 ${kw['avg_cpc_usd']:.2f}")
            print(f"   🎯 Competition Index: {kw['competition_index']}/100")


def main():
    """Chạy tất cả demos"""
    print("="*80)
    print("GOOGLE ADS API - KEYWORD ANALYSIS DEMOS")
    print("="*80)
    
    demos = [
        ("Tìm kiếm cơ bản", demo_basic_search),
        ("Phân tích chi tiết", demo_detailed_analysis),
        ("So sánh từ khóa", demo_compare_keywords),
        ("Xuất báo cáo", demo_export_report),
        ("Từ khóa volume cao", demo_high_volume_keywords),
        ("Từ khóa cạnh tranh thấp", demo_low_competition),
    ]
    
    print("\nChọn demo muốn chạy:")
    for i, (name, _) in enumerate(demos, 1):
        print(f"{i}. {name}")
    print("0. Chạy tất cả")
    
    try:
        choice = input("\nNhập số (0-6): ").strip()
        
        if choice == '0':
            # Chạy tất cả
            for name, func in demos:
                func()
                input("\n👉 Nhấn Enter để tiếp tục...")
        elif choice.isdigit() and 1 <= int(choice) <= len(demos):
            # Chạy demo được chọn
            demos[int(choice) - 1][1]()
        else:
            print("❌ Lựa chọn không hợp lệ")
            
    except KeyboardInterrupt:
        print("\n\n👋 Đã hủy!")
    except Exception as e:
        print(f"\n❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
