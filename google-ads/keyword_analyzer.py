#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Keyword Analyzer Tool - Google Trends API
Phân tích từ khóa: related keywords, popularity, trends, regions
Lưu ý: Không có dữ liệu CPC và exact search volume (Google Trends không cung cấp)
"""

from pytrends.request import TrendReq
import pandas as pd
import time
from datetime import datetime
import json
import random


class KeywordAnalyzer:
    """
    Tool phân tích từ khóa sử dụng Google Trends API
    """
    
    def __init__(self, language='vi', timezone=420, geo='VN'):
        """
        Khởi tạo Keyword Analyzer
        
        Args:
            language (str): Ngôn ngữ
            timezone (int): Múi giờ (420 = GMT+7)
            geo (str): Mã quốc gia (VN, US, etc.)
        """
        self.pytrends = TrendReq(hl=language, tz=timezone, timeout=(10, 25))
        self.geo = geo
        self.language = language
        self.min_delay = 3  # Tăng delay tối thiểu lên 3 giây
        self.max_delay = 8  # Delay tối đa 8 giây
        print(f"✅ Đã khởi tạo Keyword Analyzer (Geo: {geo}, Language: {language})")
    
    def _safe_delay(self):
        """
        Random delay để tránh rate limit
        """
        delay = random.uniform(self.min_delay, self.max_delay)
        time.sleep(delay)
    
    
    def _retry_request(self, func, max_retries=3, *args, **kwargs):
        """
        Retry request với exponential backoff
        
        Args:
            func: Function cần retry
            max_retries: Số lần retry tối đa
            *args, **kwargs: Arguments cho function
        
        Returns:
            Result từ function hoặc None nếu fail
        """
        for attempt in range(max_retries):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                error_msg = str(e)
                
                if '429' in error_msg:
                    wait_time = (2 ** attempt) * 5  # Exponential backoff: 5s, 10s, 20s
                    print(f"   ⚠️  Rate limit (429). Đợi {wait_time}s... (Lần {attempt + 1}/{max_retries})")
                    time.sleep(wait_time)
                elif '500' in error_msg or '503' in error_msg:
                    wait_time = (2 ** attempt) * 3  # Server error: 3s, 6s, 12s
                    print(f"   ⚠️  Server error ({error_msg[:50]}). Đợi {wait_time}s... (Lần {attempt + 1}/{max_retries})")
                    time.sleep(wait_time)
                else:
                    if attempt < max_retries - 1:
                        print(f"   ⚠️  Lỗi: {error_msg[:100]}. Retry... (Lần {attempt + 1}/{max_retries})")
                        time.sleep(3)
                    else:
                        print(f"   ❌ Lỗi: {error_msg[:100]}")
                        return None
        
        print(f"   ❌ Đã thử {max_retries} lần nhưng vẫn thất bại")
        return None
    
    
    def analyze_keyword(self, keyword, timeframe='today 12-m'):
        """
        Phân tích toàn diện một từ khóa
        
        Args:
            keyword (str): Từ khóa cần phân tích
            timeframe (str): Khoảng thời gian
        
        Returns:
            dict: Kết quả phân tích đầy đủ
        """
        print(f"\n{'='*70}")
        print(f"PHÂN TÍCH TỪ KHÓA: '{keyword}'")
        print(f"{'='*70}")
        
        result = {
            'keyword': keyword,
            'timestamp': datetime.now().isoformat(),
            'geo': self.geo,
            'timeframe': timeframe,
            'popularity_score': None,
            'trend_direction': None,
            'estimated_search_volume': None,
            'related_queries': {
                'top': [],
                'rising': []
            },
            'related_topics': {
                'top': [],
                'rising': []
            },
            'top_regions': [],
            'suggestions': [],
            'interest_over_time': []
        }
        
        try:
            # 1. Lấy xu hướng theo thời gian
            print("\n📊 1. Phân tích xu hướng theo thời gian...")
            popularity_data = self._retry_request(self._get_interest_over_time, 3, keyword, timeframe)
            if popularity_data:
                result['popularity_score'] = popularity_data['average_score']
                result['trend_direction'] = popularity_data['trend']
                result['estimated_search_volume'] = popularity_data['estimated_volume']
                result['interest_over_time'] = popularity_data['timeline']
            
            self._safe_delay()
            
            # 2. Lấy từ khóa liên quan
            print("\n🔍 2. Tìm từ khóa liên quan...")
            related = self._retry_request(self._get_related_queries, 3, keyword, timeframe)
            if related:
                result['related_queries'] = related
            
            self._safe_delay()
            
            # 3. Lấy chủ đề liên quan
            print("\n📚 3. Tìm chủ đề liên quan...")
            topics = self._retry_request(self._get_related_topics, 3, keyword, timeframe)
            if topics:
                result['related_topics'] = topics
            
            self._safe_delay()
            
            # 4. Phân tích theo khu vực
            print("\n🌍 4. Phân tích theo khu vực địa lý...")
            regions = self._retry_request(self._get_top_regions, 3, keyword, timeframe)
            if regions:
                result['top_regions'] = regions
            
            self._safe_delay()
            
            # 5. Lấy gợi ý từ khóa
            print("\n💡 5. Lấy gợi ý từ khóa...")
            suggestions = self._retry_request(self._get_suggestions, 3, keyword)
            if suggestions:
                result['suggestions'] = suggestions
            
            # In kết quả
            self._print_analysis_report(result)
            
            return result
            
        except Exception as e:
            print(f"\n❌ Lỗi khi phân tích: {e}")
            return result
    
    
    def _get_interest_over_time(self, keyword, timeframe):
        """
        Lấy xu hướng và ước tính search volume
        """
        try:
            self.pytrends.build_payload([keyword], timeframe=timeframe, geo=self.geo)
            df = self.pytrends.interest_over_time()
            
            if df.empty:
                print("   ⚠️  Không có dữ liệu xu hướng")
                return None
            
            if 'isPartial' in df.columns:
                df = df.drop(columns=['isPartial'])
            
            # Tính toán metrics
            avg_score = df[keyword].mean()
            current_score = df[keyword].iloc[-1]
            first_score = df[keyword].iloc[0]
            
            # Xác định trend
            if current_score > first_score * 1.2:
                trend = "📈 Tăng mạnh"
            elif current_score > first_score:
                trend = "📈 Tăng"
            elif current_score < first_score * 0.8:
                trend = "📉 Giảm mạnh"
            elif current_score < first_score:
                trend = "📉 Giảm"
            else:
                trend = "⚖️  Ổn định"
            
            # Ước tính search volume (công thức tham khảo)
            # Lưu ý: Đây chỉ là ước tính, không phải số chính xác
            estimated_volume = self._estimate_search_volume(avg_score, self.geo)
            
            # Lấy timeline
            timeline = []
            for idx, value in df[keyword].tail(12).items():
                timeline.append({
                    'date': idx.strftime('%Y-%m-%d'),
                    'score': float(value)
                })
            
            print(f"   ✅ Popularity Score: {avg_score:.1f}/100")
            print(f"   ✅ Trend: {trend}")
            print(f"   ✅ Estimated Monthly Searches: {estimated_volume}")
            
            return {
                'average_score': round(avg_score, 2),
                'current_score': float(current_score),
                'trend': trend,
                'estimated_volume': estimated_volume,
                'timeline': timeline
            }
            
        except Exception as e:
            print(f"   ❌ Lỗi: {e}")
            return None
    
    
    def _estimate_search_volume(self, score, geo):
        """
        Ước tính search volume dựa trên popularity score
        Lưu ý: Đây chỉ là ước tính thô, không chính xác
        """
        # Hệ số nhân dựa trên quốc gia (dựa trên population và internet usage)
        multipliers = {
            'VN': 100000,   # Việt Nam: ~70M internet users
            'US': 500000,   # Mỹ: ~300M internet users
            'JP': 300000,   # Nhật: ~100M internet users
            'TH': 80000,    # Thái Lan: ~50M internet users
            'SG': 20000,    # Singapore: ~5M internet users
            '': 1000000     # Global: rất lớn
        }
        
        multiplier = multipliers.get(geo, 50000)
        
        # Công thức: score * multiplier
        # Score 100 ≈ keyword phổ biến nhất
        # Score 50 ≈ keyword phổ biến trung bình
        # Score 10 ≈ keyword ít phổ biến
        
        if score >= 80:
            volume = int(score * multiplier * 1.5)  # Very popular
            range_text = f"{volume:,} - {volume*2:,}"
        elif score >= 50:
            volume = int(score * multiplier)  # Popular
            range_text = f"{volume//2:,} - {volume*2:,}"
        elif score >= 20:
            volume = int(score * multiplier * 0.5)  # Medium
            range_text = f"{volume//2:,} - {volume*2:,}"
        else:
            volume = int(score * multiplier * 0.2)  # Low
            range_text = f"{volume//2:,} - {volume*2:,}"
        
        return f"{range_text} searches/month (ước tính)"
    
    
    def _get_related_queries(self, keyword, timeframe):
        """
        Lấy các truy vấn liên quan
        """
        try:
            self.pytrends.build_payload([keyword], timeframe=timeframe, geo=self.geo)
            related = self.pytrends.related_queries()
            
            if not related or keyword not in related:
                print("   ⚠️  Không có dữ liệu related queries")
                return None
            
            data = related[keyword]
            
            # Kiểm tra data có None không
            if data is None or (data['top'] is None and data['rising'] is None):
                print("   ⚠️  Không có dữ liệu related queries")
                return None
            
            result = {'top': [], 'rising': []}
            
            # Top queries
            if data['top'] is not None and not data['top'].empty:
                for idx, row in data['top'].head(20).iterrows():
                    result['top'].append({
                        'query': row['query'],
                        'value': int(row['value'])
                    })
                print(f"   ✅ Tìm thấy {len(result['top'])} top queries")
            else:
                print("   ⚠️  Không có top queries")
            
            # Rising queries
            if data['rising'] is not None and not data['rising'].empty:
                for idx, row in data['rising'].head(20).iterrows():
                    value = row['value']
                    if value == 'Breakout':
                        result['rising'].append({
                            'query': row['query'],
                            'value': 'Breakout',
                            'growth': '+5000%'
                        })
                    else:
                        result['rising'].append({
                            'query': row['query'],
                            'value': int(value) if isinstance(value, (int, float)) else value,
                            'growth': f"+{value}%" if isinstance(value, (int, float)) else value
                        })
                print(f"   ✅ Tìm thấy {len(result['rising'])} rising queries")
            else:
                print("   ⚠️  Không có rising queries")
            
            # Trả về None nếu không có cả top và rising
            if not result['top'] and not result['rising']:
                return None
            
            return result
            
        except Exception as e:
            raise e  # Re-raise để retry handler xử lý
    
    
    def _get_related_topics(self, keyword, timeframe):
        """
        Lấy các chủ đề liên quan
        """
        try:
            self.pytrends.build_payload([keyword], timeframe=timeframe, geo=self.geo)
            topics = self.pytrends.related_topics()
            
            if not topics or keyword not in topics:
                print("   ⚠️  Không có dữ liệu related topics")
                return None
            
            data = topics[keyword]
            
            # Kiểm tra data có None không
            if data is None or (data['top'] is None and data['rising'] is None):
                print("   ⚠️  Không có dữ liệu related topics")
                return None
            
            result = {'top': [], 'rising': []}
            
            # Top topics
            if data['top'] is not None and not data['top'].empty:
                for idx, row in data['top'].head(10).iterrows():
                    result['top'].append({
                        'topic': row.get('topic_title', 'N/A'),
                        'type': row.get('topic_type', 'N/A'),
                        'value': int(row['value']) if 'value' in row else 0
                    })
                print(f"   ✅ Tìm thấy {len(result['top'])} top topics")
            else:
                print("   ⚠️  Không có top topics")
            
            # Rising topics
            if data['rising'] is not None and not data['rising'].empty:
                for idx, row in data['rising'].head(10).iterrows():
                    value = row['value'] if 'value' in row else 'N/A'
                    result['rising'].append({
                        'topic': row.get('topic_title', 'N/A'),
                        'type': row.get('topic_type', 'N/A'),
                        'value': value if value == 'Breakout' else (int(value) if isinstance(value, (int, float)) else value)
                    })
                print(f"   ✅ Tìm thấy {len(result['rising'])} rising topics")
            else:
                print("   ⚠️  Không có rising topics")
            
            # Trả về None nếu không có cả top và rising
            if not result['top'] and not result['rising']:
                return None
            
            return result
            
        except Exception as e:
            raise e  # Re-raise để retry handler xử lý
    
    
    def _get_top_regions(self, keyword, timeframe):
        """
        Lấy top khu vực quan tâm
        """
        try:
            self.pytrends.build_payload([keyword], timeframe=timeframe, geo=self.geo)
            df = self.pytrends.interest_by_region(resolution='REGION', inc_low_vol=True)
            
            if df is None or df.empty:
                print("   ⚠️  Không có dữ liệu khu vực")
                return None
            
            df = df.sort_values(by=keyword, ascending=False)
            
            # Lọc bỏ các region có score = 0
            df_filtered = df[df[keyword] > 0]
            
            if df_filtered.empty:
                print("   ⚠️  Không có khu vực nào có dữ liệu đáng kể")
                return None
            
            regions = []
            for idx, (region, row) in enumerate(df_filtered.head(10).iterrows(), 1):
                score = row[keyword]
                regions.append({
                    'rank': idx,
                    'region': region,
                    'score': float(score)
                })
            
            print(f"   ✅ Tìm thấy {len(regions)} top regions")
            return regions
            
        except Exception as e:
            raise e  # Re-raise để retry handler xử lý
    
    
    def _get_suggestions(self, keyword):
        """
        Lấy gợi ý từ khóa (autocomplete)
        """
        try:
            suggestions_data = self.pytrends.suggestions(keyword=keyword)
            
            if not suggestions_data or len(suggestions_data) == 0:
                print("   ⚠️  Không có gợi ý")
                return None
            
            suggestions = []
            for s in suggestions_data[:15]:
                suggestions.append({
                    'keyword': s['title'],
                    'type': s['type']
                })
            
            print(f"   ✅ Tìm thấy {len(suggestions)} suggestions")
            return suggestions
            
        except Exception as e:
            raise e  # Re-raise để retry handler xử lý
    
    
    def _print_analysis_report(self, result):
        """
        In báo cáo phân tích
        """
        print(f"\n{'='*70}")
        print("📊 BÁO CÁO PHÂN TÍCH")
        print(f"{'='*70}")
        
        # 1. Thông tin cơ bản
        print(f"\n🔑 TỪ KHÓA: {result['keyword']}")
        print(f"🌍 KHU VỰC: {result['geo']}")
        print(f"📅 THỜI GIAN: {result['timeframe']}")
        
        # 2. Popularity & Trend
        if result['popularity_score']:
            print(f"\n📊 POPULARITY SCORE: {result['popularity_score']}/100")
            print(f"📈 XU HƯỚNG: {result['trend_direction']}")
            print(f"🔢 ƯỚC TÍNH TRAFFIC: {result['estimated_search_volume']}")
            print("   ⚠️  Lưu ý: Đây là ước tính, không phải số chính xác")
        
        # 3. Related Queries (Top)
        if result['related_queries']['top']:
            print(f"\n🔝 TOP 15 TỪ KHÓA LIÊN QUAN PHỔ BIẾN:")
            for i, q in enumerate(result['related_queries']['top'][:15], 1):
                print(f"   {i:2d}. {q['query']:<40} (Score: {q['value']})")
        
        # 4. Related Queries (Rising)
        if result['related_queries']['rising']:
            print(f"\n📈 TOP 15 TỪ KHÓA LIÊN QUAN ĐANG TĂNG:")
            for i, q in enumerate(result['related_queries']['rising'][:15], 1):
                growth = q.get('growth', q['value'])
                emoji = "🚀" if q['value'] == 'Breakout' else "📈"
                print(f"   {emoji} {i:2d}. {q['query']:<40} ({growth})")
        
        # 5. Related Topics
        if result['related_topics']['top']:
            print(f"\n📚 TOP 10 CHỦ ĐỀ LIÊN QUAN:")
            for i, t in enumerate(result['related_topics']['top'][:10], 1):
                print(f"   {i:2d}. {t['topic']:<40} ({t['type']})")
        
        # 6. Top Regions
        if result['top_regions']:
            print(f"\n🌍 TOP 10 KHU VỰC QUAN TÂM:")
            for r in result['top_regions']:
                print(f"   {r['rank']:2d}. {r['region']:<30} (Score: {r['score']:.1f})")
        
        # 7. Suggestions
        if result['suggestions']:
            print(f"\n💡 GỢI Ý TỪ KHÓA (Autocomplete):")
            for i, s in enumerate(result['suggestions'][:10], 1):
                print(f"   {i:2d}. {s['keyword']:<40} ({s['type']})")
        
        # 8. Lưu ý về CPC
        print(f"\n{'='*70}")
        print("⚠️  LƯU Ý QUAN TRỌNG:")
        print("{'='*70}")
        print("❌ Google Trends KHÔNG cung cấp:")
        print("   • CPC (Cost Per Click)")
        print("   • Exact search volume")
        print("   • Competition level (Low/Medium/High)")
        print("   • Suggested bid")
        print("\n✅ Để có dữ liệu CPC, bạn cần:")
        print("   • Google Ads Keyword Planner (cần tài khoản Ads)")
        print("   • SEMrush, Ahrefs (trả phí)")
        print("   • Ubersuggest (có free tier)")
        print(f"{'='*70}")
    
    
    def save_report(self, result, output_format='json'):
        """
        Lưu báo cáo ra file
        
        Args:
            result (dict): Kết quả phân tích
            output_format (str): 'json' hoặc 'csv'
        """
        import os
        
        # Tạo folder report nếu chưa có
        report_dir = 'report'
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
            print(f"📁 Đã tạo folder: {report_dir}/")
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        keyword_safe = result['keyword'].replace(' ', '_').replace('/', '_')
        
        if output_format == 'json':
            filename = f"{report_dir}/keyword_analysis_{keyword_safe}_{timestamp}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            print(f"\n✅ Đã lưu báo cáo JSON: {filename}")
        
        elif output_format == 'csv':
            # Lưu related queries ra CSV
            if result['related_queries']['top']:
                filename = f"{report_dir}/related_queries_{keyword_safe}_{timestamp}.csv"
                
                # Kết hợp top và rising
                data = []
                for q in result['related_queries']['top']:
                    data.append({
                        'keyword': q['query'],
                        'type': 'Top',
                        'score': q['value'],
                        'growth': ''
                    })
                
                for q in result['related_queries']['rising']:
                    data.append({
                        'keyword': q['query'],
                        'type': 'Rising',
                        'score': q['value'],
                        'growth': q.get('growth', '')
                    })
                
                df = pd.DataFrame(data)
                df.to_csv(filename, index=False, encoding='utf-8-sig')
                print(f"✅ Đã lưu related queries CSV: {filename}")
        
        return filename


def main():
    """
    Main function - Interactive keyword analysis
    """
    print("="*70)
    print("KEYWORD ANALYZER - GOOGLE TRENDS API")
    print("="*70)
    print("\n⚠️  LƯU Ý:")
    print("   • Tool này KHÔNG cung cấp CPC (Google Trends không có)")
    print("   • Search volume là ƯỚC TÍNH, không chính xác 100%")
    print("   • Dữ liệu là TƯƠNG ĐỐI (0-100), không phải số tuyệt đối")
    print("="*70)
    
    # Cấu hình
    print("\n📍 CHỌN KHU VỰC:")
    print("   1. Việt Nam (VN)")
    print("   2. Toàn cầu (Global)")
    print("   3. Mỹ (US)")
    print("   4. Khác...")
    
    geo_choice = input("\nNhập lựa chọn (1-4) [mặc định: 1]: ").strip() or '1'
    
    geo_map = {
        '1': 'VN',
        '2': '',
        '3': 'US'
    }
    
    if geo_choice in geo_map:
        geo = geo_map[geo_choice]
    else:
        geo = input("Nhập mã quốc gia (VD: TH, JP, SG): ").strip().upper()
    
    # Khởi tạo analyzer
    analyzer = KeywordAnalyzer(language='vi', timezone=420, geo=geo)
    
    # Loop phân tích
    while True:
        print("\n" + "="*70)
        keyword = input("\n🔍 Nhập từ khóa cần phân tích (hoặc 'quit' để thoát): ").strip()
        
        if keyword.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Cảm ơn bạn đã sử dụng Keyword Analyzer!")
            break
        
        if not keyword:
            print("⚠️  Vui lòng nhập từ khóa!")
            continue
        
        # Chọn timeframe
        print("\n📅 CHỌN KHOẢNG THỜI GIAN:")
        print("   1. 3 tháng qua (today 3-m)")
        print("   2. 12 tháng qua (today 12-m) [đề xuất]")
        print("   3. 5 năm qua (today 5-y)")
        
        time_choice = input("\nNhập lựa chọn (1-3) [mặc định: 2]: ").strip() or '2'
        
        time_map = {
            '1': 'today 3-m',
            '2': 'today 12-m',
            '3': 'today 5-y'
        }
        
        timeframe = time_map.get(time_choice, 'today 12-m')
        
        # Phân tích
        result = analyzer.analyze_keyword(keyword, timeframe)
        
        # Lưu báo cáo
        save = input("\n💾 Lưu báo cáo? (y/n) [mặc định: n]: ").strip().lower()
        
        if save == 'y':
            print("\n📁 CHỌN FORMAT:")
            print("   1. JSON (đầy đủ nhất)")
            print("   2. CSV (chỉ related queries)")
            
            format_choice = input("\nNhập lựa chọn (1-2) [mặc định: 1]: ").strip() or '1'
            
            output_format = 'json' if format_choice == '1' else 'csv'
            analyzer.save_report(result, output_format)
        
        # Tiếp tục?
        continue_analysis = input("\n🔄 Phân tích từ khóa khác? (y/n) [mặc định: y]: ").strip().lower() or 'y'
        
        if continue_analysis != 'y':
            print("\n👋 Cảm ơn bạn đã sử dụng Keyword Analyzer!")
            break


if __name__ == "__main__":
    main()
