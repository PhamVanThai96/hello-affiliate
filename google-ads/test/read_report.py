#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Read and Convert Campaign Report JSON to HTML
Đọc file JSON báo cáo campaign và chuyển đổi sang HTML hiển thị trên trình duyệt
"""

import json
import os
import glob
from pathlib import Path
from datetime import datetime


class ReportToHTML:
    """
    Chuyển đổi JSON report thành HTML
    """
    
    def __init__(self):
        self.report_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'report', 'campaign_plans'
        )
        self.output_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'report', 'html_reports'
        )
        
        # Tạo thư mục output nếu chưa có
        os.makedirs(self.output_dir, exist_ok=True)
    
    def get_available_reports(self):
        """
        Lấy danh sách các file JSON có sẵn
        """
        json_files = glob.glob(os.path.join(self.report_dir, '*.json'))
        reports = []
        
        for json_file in json_files:
            filename = os.path.basename(json_file)
            file_size = os.path.getsize(json_file)
            reports.append({
                'filename': filename,
                'path': json_file,
                'size': file_size
            })
        
        return sorted(reports, key=lambda x: x['filename'])
    
    def load_report(self, json_path):
        """
        Tải file JSON report
        """
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                report = json.load(f)
            return report
        except Exception as e:
            print(f"❌ Lỗi khi tải file: {e}")
            return None
    
    def format_number(self, num):
        """
        Format số với dấu phân cách hàng nghìn
        """
        if isinstance(num, (int, float)):
            return f"{int(num):,}".replace(',', '.')
        return str(num)
    
    def generate_html(self, report, brand_name):
        """
        Tạo HTML từ report data
        """
        html = f"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Campaign Report - {brand_name}</title>
    <style>
        @charset "UTF-8";
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', 'Trebuchet MS', 'Arial', 'Helvetica', 'DejaVu Sans', sans-serif;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            text-rendering: optimizeLegibility;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px 30px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}
        
        .header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        
        .content {{
            padding: 30px;
        }}
        
        .section {{
            margin-bottom: 40px;
            border-bottom: 2px solid #f0f0f0;
            padding-bottom: 30px;
        }}
        
        .section:last-child {{
            border-bottom: none;
        }}
        
        .section-title {{
            font-size: 1.8em;
            color: #667eea;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
            display: inline-block;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        
        .stat-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
            transition: transform 0.3s ease;
        }}
        
        .stat-card:hover {{
            transform: translateY(-5px);
        }}
        
        .stat-label {{
            font-size: 0.9em;
            opacity: 0.9;
            margin-bottom: 8px;
            font-weight: 600;
        }}
        
        .stat-value {{
            font-size: 2em;
            font-weight: bold;
        }}
        
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        
        .info-box {{
            background: #f8f9ff;
            border-left: 4px solid #667eea;
            padding: 20px;
            border-radius: 6px;
        }}
        
        .info-box h3 {{
            color: #667eea;
            margin-bottom: 12px;
            font-size: 1.1em;
        }}
        
        .info-item {{
            margin: 8px 0;
            font-size: 0.95em;
            word-break: break-word;
        }}
        
        .info-label {{
            color: #666;
            font-weight: 600;
        }}
        
        .info-value {{
            color: #333;
            font-weight: 500;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background: white;
        }}
        
        th {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
            border: none;
        }}
        
        td {{
            padding: 12px 15px;
            border-bottom: 1px solid #f0f0f0;
            word-break: break-word;
        }}
        
        tr:hover {{
            background: #f8f9ff;
        }}
        
        .keyword-col {{
            font-weight: 600;
            color: #667eea;
            max-width: 300px;
        }}
        
        .cpc-col {{
            color: #e74c3c;
            font-weight: 600;
        }}
        
        .cvr-col {{
            color: #27ae60;
            font-weight: 600;
        }}
        
        .competition-low {{
            background: #d4edda;
            color: #155724;
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: 600;
        }}
        
        .competition-medium {{
            background: #fff3cd;
            color: #856404;
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: 600;
        }}
        
        .competition-high {{
            background: #f8d7da;
            color: #721c24;
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: 600;
        }}
        
        .recommendation {{
            background: #e8f4f8;
            border-left: 4px solid #3498db;
            padding: 15px;
            margin: 10px 0;
            border-radius: 4px;
        }}
        
        .recommendation.success {{
            background: #d4edda;
            border-left-color: #27ae60;
        }}
        
        .recommendation.warning {{
            background: #fff3cd;
            border-left-color: #f39c12;
        }}
        
        .recommendation.info {{
            background: #d1ecf1;
            border-left-color: #3498db;
        }}
        
        .emoji {{
            margin-right: 8px;
        }}
        
        .footer {{
            text-align: center;
            padding: 20px;
            color: #999;
            font-size: 0.9em;
            border-top: 1px solid #f0f0f0;
        }}
        
        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 1.8em;
            }}
            
            .stats-grid {{
                grid-template-columns: 1fr;
            }}
            
            .info-grid {{
                grid-template-columns: 1fr;
            }}
            
            table {{
                font-size: 0.9em;
            }}
            
            th, td {{
                padding: 10px;
            }}
            
            .keyword-col {{
                max-width: 150px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        {self._generate_header(report, brand_name)}
        {self._generate_landing_page_section(report)}
        {self._generate_commission_section(report)}
        {self._generate_projections_section(report)}
        {self._generate_keywords_section(report)}
        {self._generate_recommendations_section(report)}
        {self._generate_footer(report)}
    </div>
</body>
</html>
"""
        return html
    
    def _generate_header(self, report, brand_name):
        """
        Tạo phần header
        """
        return f"""
        <div class="header">
            <h1>📊 Campaign Report</h1>
            <p><strong>{brand_name}</strong> - {report.get('analysis_date', 'N/A')}</p>
        </div>
"""
    
    def _generate_landing_page_section(self, report):
        """
        Tạo phần thông tin landing page
        """
        lp = report.get('landing_page', {})
        
        html = '<div class="section">'
        html += '<h2 class="section-title">🌐 Landing Page Information</h2>'
        
        html += '<div class="info-grid">'
        
        # Thông tin cơ bản
        html += f"""
        <div class="info-box">
            <h3>📝 Page Details</h3>
            <div class="info-item">
                <span class="info-label">URL:</span>
                <span class="info-value"><a href="{lp.get('url', '')}" target="_blank">{lp.get('url', 'N/A')}</a></span>
            </div>
            <div class="info-item">
                <span class="info-label">Title:</span>
                <span class="info-value">{lp.get('title', 'N/A')}</span>
            </div>
            <div class="info-item">
                <span class="info-label">Target Age:</span>
                <span class="info-value">{lp.get('target_age_range', 'N/A')}</span>
            </div>
            <div class="info-item">
                <span class="info-label">Products Count:</span>
                <span class="info-value">{lp.get('product_count', 0)}</span>
            </div>
        </div>
        """
        
        # Giá cả
        avg_price = lp.get('avg_product_price', 0)
        html += f"""
        <div class="info-box">
            <h3>💰 Pricing</h3>
            <div class="info-item">
                <span class="info-label">Avg Product Price:</span>
                <span class="info-value">{self.format_number(avg_price)} VNĐ</span>
            </div>
        </div>
        """
        
        html += '</div>'
        
        # Danh sách sản phẩm mẫu
        products = lp.get('sample_products', [])
        if products:
            html += '<h3 style="margin-top: 20px; color: #667eea;">Sample Products:</h3>'
            html += '<ul style="margin-left: 20px; margin-top: 10px;">'
            for product in products:
                html += f'<li style="margin: 5px 0;">{product}</li>'
            html += '</ul>'
        
        html += '</div>'
        return html
    
    def _generate_commission_section(self, report):
        """
        Tạo phần thông tin hoa hồng
        """
        comm = report.get('commission_settings', {})
        
        html = '<div class="section">'
        html += '<h2 class="section-title">💵 Commission Settings</h2>'
        
        html += '<div class="stats-grid">'
        html += f"""
        <div class="stat-card">
            <div class="stat-label">Commission Rate</div>
            <div class="stat-value">{comm.get('commission_rate', 0)}%</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Avg Product Price</div>
            <div class="stat-value">{self.format_number(comm.get('avg_product_price', 0))} VNĐ</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Commission per Sale</div>
            <div class="stat-value">{self.format_number(comm.get('commission_per_sale', 0))} VNĐ</div>
        </div>
        """
        html += '</div>'
        html += '</div>'
        return html
    
    def _generate_projections_section(self, report):
        """
        Tạo phần dự báo campaign
        """
        proj = report.get('campaign_projections', {})
        metrics = proj.get('estimated_metrics', {})
        
        html = '<div class="section">'
        html += '<h2 class="section-title">📈 Campaign Projections</h2>'
        
        # Budget info
        budget = proj.get('monthly_budget', 0)
        html += f'<p style="font-size: 1.1em; margin-bottom: 20px;"><strong>Monthly Budget: {self.format_number(budget)} VNĐ</strong></p>'
        
        # Key metrics
        html += '<div class="stats-grid">'
        html += f"""
        <div class="stat-card">
            <div class="stat-label">Average CPC</div>
            <div class="stat-value">{self.format_number(metrics.get('avg_cpc', 0))} VNĐ</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Average CVR</div>
            <div class="stat-value">{metrics.get('avg_cvr', 0)}%</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Clicks/Month</div>
            <div class="stat-value">{self.format_number(metrics.get('estimated_clicks_per_month', 0))}</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Conversions/Month</div>
            <div class="stat-value">{self.format_number(metrics.get('estimated_conversions_per_month', 0))}</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">CPA</div>
            <div class="stat-value">{self.format_number(metrics.get('estimated_cpa', 0))} VNĐ</div>
        </div>
        <div class="stat-card">
            <div class="stat-label">Impressions</div>
            <div class="stat-value">{self.format_number(metrics.get('estimated_impressions', 0))}</div>
        </div>
        """
        html += '</div>'
        
        # Keyword distribution
        kw_dist = proj.get('keyword_distribution', {})
        html += '<h3 style="margin-top: 20px; margin-bottom: 15px; color: #667eea;">Keyword Distribution</h3>'
        html += f"""
        <div class="info-grid">
            <div class="info-box">
                <h3>📊 By Competition</h3>
        """
        for comp, count in kw_dist.get('by_competition', {}).items():
            html += f'<div class="info-item"><span class="info-label">{comp}:</span> <span class="info-value">{count}</span></div>'
        html += '</div>'
        
        html += '<div class="info-box"><h3>📌 By Source</h3>'
        for source, count in kw_dist.get('by_source', {}).items():
            html += f'<div class="info-item"><span class="info-label">{source}:</span> <span class="info-value">{count}</span></div>'
        html += '</div></div>'
        
        html += '</div>'
        return html
    
    def _generate_keywords_section(self, report):
        """
        Tạo phần danh sách từ khóa
        """
        keywords = report.get('keyword_suggestions', [])
        
        html = '<div class="section">'
        html += '<h2 class="section-title">🔑 Keyword Suggestions</h2>'
        html += f'<p style="margin-bottom: 15px;"><strong>Total Keywords: {len(keywords)}</strong></p>'
        
        # Top keywords by CPC
        html += '<h3 style="margin-top: 20px; margin-bottom: 15px; color: #667eea;">Top 10 Keywords by CPC</h3>'
        html += self._generate_keywords_table(report.get('top_keywords_by_cpc', []))
        
        # Top keywords by CVR
        html += '<h3 style="margin-top: 20px; margin-bottom: 15px; color: #667eea;">Top 10 Keywords by CVR</h3>'
        html += self._generate_keywords_table(report.get('top_keywords_by_cvr', []))
        
        html += '</div>'
        return html
    
    def _generate_keywords_table(self, keywords):
        """
        Tạo bảng từ khóa
        """
        html = '<table><thead><tr>'
        html += '<th>Keyword</th>'
        html += '<th>CPC Range</th>'
        html += '<th>Avg CPC</th>'
        html += '<th>CVR</th>'
        html += '<th>Competition</th>'
        html += '<th>Source</th>'
        html += '</tr></thead><tbody>'
        
        for kw in keywords:
            cpc_range = kw.get('estimated_cpc_range', {})
            comp = kw.get('competition', '').upper()
            
            comp_class = f'competition-{comp.lower()}'
            
            html += f"""
            <tr>
                <td class="keyword-col">{kw.get('keyword', 'N/A')}</td>
                <td>{self.format_number(cpc_range.get('min', 0))} - {self.format_number(cpc_range.get('max', 0))}</td>
                <td class="cpc-col">{self.format_number(kw.get('estimated_avg_cpc', 0))} VNĐ</td>
                <td class="cvr-col">{kw.get('estimated_cvr', 0)}%</td>
                <td><span class="{comp_class}">{comp}</span></td>
                <td>{kw.get('source', 'N/A')}</td>
            </tr>
            """
        
        html += '</tbody></table>'
        return html
    
    def _generate_recommendations_section(self, report):
        """
        Tạo phần khuyến nghị
        """
        proj = report.get('campaign_projections', {})
        recommendations = proj.get('recommendations', [])
        
        if not recommendations:
            return ''
        
        html = '<div class="section">'
        html += '<h2 class="section-title">💡 Recommendations</h2>'
        
        for rec in recommendations:
            rec_type = rec.get('type', 'info').lower()
            emoji_map = {
                'success': '✅',
                'warning': '⚠️',
                'info': 'ℹ️'
            }
            emoji = emoji_map.get(rec_type, 'ℹ️')
            
            html += f"""
            <div class="recommendation {rec_type}">
                <span class="emoji">{emoji}</span>
                <strong>[{rec.get('category', 'Info')}]</strong> {rec.get('message', '')}
            </div>
            """
        
        html += '</div>'
        return html
    
    def _generate_footer(self, report):
        """
        Tạo phần footer
        """
        return f"""
        <div class="footer">
            <p>Report generated on {report.get('analysis_date', 'N/A')}</p>
            <p>© 2024 Campaign Planning System</p>
        </div>
"""
    
    def save_html(self, html, brand_name):
        """
        Lưu HTML file
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{brand_name}_report_{timestamp}.html"
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        
        return filepath


def main():
    """
    Main function
    """
    converter = ReportToHTML()
    
    print("="*80)
    print("📊 CAMPAIGN REPORT - JSON TO HTML CONVERTER")
    print("="*80)
    
    # Lấy danh sách báo cáo
    reports = converter.get_available_reports()
    
    if not reports:
        print(f"\n❌ Không tìm thấy file JSON nào trong: {converter.report_dir}")
        return
    
    print(f"\n📁 Available Reports ({len(reports)}):")
    print("-" * 80)
    
    for i, report in enumerate(reports, 1):
        print(f"{i}. {report['filename']} ({report['size']:,} bytes)")
    
    # Chọn file
    print("\n" + "-" * 80)
    choice = input("\nChọn số report (hoặc 'all' để convert tất cả, 'q' để thoát): ").strip()
    
    if choice.lower() == 'q':
        print("\n👋 Tạm biệt!")
        return
    
    selected_reports = []
    
    if choice.lower() == 'all':
        selected_reports = reports
    elif choice.isdigit() and 1 <= int(choice) <= len(reports):
        selected_reports = [reports[int(choice) - 1]]
    else:
        print("❌ Lựa chọn không hợp lệ!")
        return
    
    # Convert selected reports
    print(f"\n🔄 Đang convert {len(selected_reports)} report(s)...")
    print("-" * 80)
    
    for report_info in selected_reports:
        print(f"\n📖 Đang xử lý: {report_info['filename']}")
        
        # Load JSON
        report_data = converter.load_report(report_info['path'])
        if not report_data:
            continue
        
        # Extract brand name from filename
        brand_name = report_info['filename'].replace('_landing_page_analysis.json', '').replace('_analysis', '')
        
        # Generate HTML
        html = converter.generate_html(report_data, brand_name)
        
        # Save HTML
        output_path = converter.save_html(html, brand_name)
        
        print(f"✅ Đã tạo HTML: {os.path.basename(output_path)}")
        
        # Open in browser
        open_browser = input("   Mở trên trình duyệt? (y/n) [mặc định: y]: ").strip().lower() or 'y'
        if open_browser == 'y':
            import webbrowser
            webbrowser.open('file://' + output_path)
            print(f"   🌐 Đã mở trên trình duyệt")
    
    print("\n" + "="*80)
    print("✅ Hoàn thành!")
    print(f"📂 Output directory: {converter.output_dir}")
    print("="*80)


if __name__ == "__main__":
    main()
