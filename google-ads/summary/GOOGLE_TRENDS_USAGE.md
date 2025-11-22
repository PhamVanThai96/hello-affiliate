# Google Trends API - Hướng Dẫn Sử Dụng

## Giới Thiệu

Google Trends API (sử dụng thư viện **pytrends**) cho phép bạn truy cập dữ liệu xu hướng tìm kiếm của Google một cách miễn phí. Đây là giải pháp thay thế hoàn hảo cho Google Ads Keyword Planner khi bạn muốn nghiên cứu từ khóa mà không cần chi phí.

### ✅ Ưu Điểm
- **Hoàn toàn miễn phí** - Không cần tài khoản Google Ads
- **Không giới hạn API key** - Sử dụng tự do
- **Dữ liệu phong phú** - Xu hướng, khu vực, từ khóa liên quan
- **Dễ sử dụng** - API Python đơn giản

### ⚠️ Hạn Chế
- **Dữ liệu tương đối** - Không phải số tuyệt đối
- **Rate limiting** - Cần delay giữa các request
- **Không chính thức** - Google có thể thay đổi bất kỳ lúc nào

---

## Cài Đặt

### 1. Cài Đặt Thư Viện

```bash
cd /home/worker/SimilarWeb/google_ads
pip install -r requirements.txt
```

Hoặc cài đặt trực tiếp:

```bash
pip install pytrends pandas requests
```

### 2. Kiểm Tra Cài Đặt

```bash
python3 -c "from pytrends.request import TrendReq; print('✅ Pytrends installed successfully!')"
```

---

## Tính Năng Chính

### 📊 1. Interest Over Time (Xu Hướng Theo Thời Gian)

Theo dõi mức độ quan tâm của từ khóa qua các khoảng thời gian.

**Ứng dụng:**
- Phát hiện xu hướng tăng/giảm
- Xác định mùa vụ kinh doanh
- So sánh nhiều từ khóa

**Khoảng thời gian:**
- `now 1-H` - 1 giờ qua
- `now 7-d` - 7 ngày qua
- `today 1-m` - 1 tháng qua
- `today 3-m` - 3 tháng qua
- `today 12-m` - 12 tháng qua
- `today 5-y` - 5 năm qua
- `all` - Từ 2004 đến nay

**Ví dụ:**

```python
from pytrends.request import TrendReq

pytrends = TrendReq(hl='vi', tz=420)
pytrends.build_payload(['bitcoin', 'ethereum'], timeframe='today 12-m', geo='VN')
df = pytrends.interest_over_time()
print(df)
```

---

### 🌍 2. Interest By Region (Xu Hướng Theo Khu Vực)

Xem từ khóa phổ biến ở khu vực địa lý nào.

**Ứng dụng:**
- Xác định thị trường tiềm năng
- Lập kế hoạch marketing địa phương
- Phân tích cạnh tranh theo vùng

**Độ phân giải:**
- `COUNTRY` - Theo quốc gia
- `REGION` - Theo tỉnh/bang
- `CITY` - Theo thành phố
- `DMA` - Metro areas (chỉ US)

**Ví dụ:**

```python
pytrends.build_payload(['shopee'], timeframe='today 3-m', geo='VN')
df = pytrends.interest_by_region(resolution='REGION', inc_low_vol=True)
print(df.sort_values(by='shopee', ascending=False))
```

---

### 🔍 3. Related Queries (Truy Vấn Liên Quan)

Tìm các từ khóa mà người dùng tìm kiếm cùng với từ khóa chính.

**Ứng dụng:**
- Mở rộng danh sách từ khóa
- Tìm từ khóa long-tail
- Hiểu ý định tìm kiếm

**Dữ liệu trả về:**
- **Top** - Các truy vấn phổ biến nhất
- **Rising** - Các truy vấn đang tăng mạnh

**Ví dụ:**

```python
pytrends.build_payload(['iphone'], timeframe='today 3-m', geo='VN')
related = pytrends.related_queries()

print("Top queries:")
print(related['iphone']['top'])

print("\nRising queries:")
print(related['iphone']['rising'])
```

---

### 📚 4. Related Topics (Chủ Đề Liên Quan)

Các chủ đề mà người dùng quan tâm khi tìm kiếm từ khóa.

**Ứng dụng:**
- Hiểu ngữ cảnh tìm kiếm
- Tạo nội dung liên quan
- Phân tích xu hướng rộng hơn

**Ví dụ:**

```python
pytrends.build_payload(['covid'], timeframe='today 3-m', geo='VN')
topics = pytrends.related_topics()

print("Top topics:")
print(topics['covid']['top'])

print("\nRising topics:")
print(topics['covid']['rising'])
```

---

### 🔥 5. Trending Searches (Tìm Kiếm Thịnh Hành)

Các từ khóa đang thịnh hành hôm nay.

**Ứng dụng:**
- Tìm chủ đề viral
- Content marketing kịp thời
- Theo dõi tin tức hot

**Quốc gia hỗ trợ:**
- `vietnam` - Việt Nam
- `united_states` - Mỹ
- `japan` - Nhật Bản
- `singapore` - Singapore
- Và nhiều quốc gia khác...

**Ví dụ:**

```python
df = pytrends.trending_searches(pn='vietnam')
print("Top 20 trending searches in Vietnam:")
print(df.head(20))
```

---

### 💡 6. Suggestions (Gợi Ý Từ Khóa)

Gợi ý tự động như Google Autocomplete.

**Ứng dụng:**
- Tìm biến thể từ khóa
- Phát hiện từ khóa mới
- Tối ưu SEO

**Ví dụ:**

```python
suggestions = pytrends.suggestions(keyword='machine learning')
for s in suggestions:
    print(f"{s['title']} - Type: {s['type']}")
```

---

### 🏆 7. Top Charts (Bảng Xếp Hạng)

Top từ khóa tìm kiếm theo năm.

**Ứng dụng:**
- Phân tích xu hướng dài hạn
- So sánh các năm
- Lập kế hoạch chiến lược

**Ví dụ:**

```python
df = pytrends.top_charts(2024, hl='vi', tz=420, geo='VN')
print(df)
```

---

### ⚖️ 8. Compare Keywords (So Sánh Từ Khóa)

So sánh 2-5 từ khóa cùng lúc.

**Ứng dụng:**
- Phân tích đối thủ
- Chọn từ khóa tốt nhất
- Xác định leader thị trường

**Ví dụ:**

```python
pytrends.build_payload(['shopee', 'lazada', 'tiki'], timeframe='today 12-m', geo='VN')
df = pytrends.interest_over_time()

# Tính trung bình
for col in ['shopee', 'lazada', 'tiki']:
    print(f"{col}: {df[col].mean():.2f}")
```

---

### 📂 9. Categories (Danh Mục)

Lọc kết quả theo danh mục cụ thể.

**Danh mục phổ biến:**
- `0` - Tất cả
- `3` - Arts & Entertainment
- `12` - Business & Industrial
- `47` - Computers & Electronics
- `71` - Finance
- `45` - Food & Drink
- `26` - Shopping
- `67` - Travel

**Ví dụ:**

```python
# Tìm kiếm trong category Finance
pytrends.build_payload(['bitcoin'], timeframe='today 3-m', geo='', cat=71)
df = pytrends.interest_over_time()
```

---

## Chạy Demo

### Chạy Tất Cả Demo

```bash
cd /home/worker/SimilarWeb/google_ads
python3 google_trends_demo.py
```

Chọn `0` để chạy tất cả demo, hoặc chọn số `1-7` để chạy từng demo riêng.

### Các Demo Có Sẵn

1. **Demo 1: Sử dụng cơ bản** - Lấy xu hướng theo thời gian
2. **Demo 2: Nghiên cứu từ khóa** - Gợi ý, truy vấn và chủ đề liên quan
3. **Demo 3: Phân tích đối thủ** - So sánh các competitor
4. **Demo 4: Chủ đề thịnh hành** - Trending searches
5. **Demo 5: Phân tích địa lý** - Xu hướng theo vùng
6. **Demo 6: Categories** - Làm việc với danh mục
7. **Demo 7: Xuất dữ liệu** - Export CSV, JSON, Excel

---

## Use Cases Thực Tế

### 🎯 Use Case 1: Keyword Research cho SEO

**Mục tiêu:** Tìm từ khóa tốt nhất để tối ưu website.

```python
from pytrends.request import TrendReq

pytrends = TrendReq(hl='vi', tz=420)

# 1. Lấy gợi ý từ khóa
keyword = 'bất động sản'
suggestions = pytrends.suggestions(keyword)
print("Gợi ý:", [s['title'] for s in suggestions[:10]])

# 2. Lấy related queries
pytrends.build_payload([keyword], timeframe='today 12-m', geo='VN')
related = pytrends.related_queries()

# Chọn top rising queries
rising = related[keyword]['rising']
if rising is not None:
    print("\nTừ khóa đang tăng nhanh:")
    print(rising.head(20))
```

### 📈 Use Case 2: Phân Tích Đối Thủ Cạnh Tranh

**Mục tiêu:** So sánh thương hiệu của bạn với đối thủ.

```python
# So sánh các thương hiệu
brands = ['brand_a', 'brand_b', 'brand_c', 'your_brand']

pytrends.build_payload(brands, timeframe='today 12-m', geo='VN')
df_time = pytrends.interest_over_time()

# Phân tích
for brand in brands:
    avg = df_time[brand].mean()
    trend = "📈" if df_time[brand].iloc[-1] > df_time[brand].iloc[0] else "📉"
    print(f"{brand}: Avg={avg:.2f} {trend}")

# Xem theo vùng
df_region = pytrends.interest_by_region(resolution='REGION')
print("\nThị trường mạnh nhất của brand_a:")
print(df_region.sort_values(by='brand_a', ascending=False).head(10))
```

### 🛍️ Use Case 3: Lập Kế Hoạch Marketing Mùa Vụ

**Mục tiêu:** Xác định thời điểm tốt nhất để chạy campaign.

```python
# Phân tích xu hướng theo mùa
keyword = 'điều hòa'

pytrends.build_payload([keyword], timeframe='today 5-y', geo='VN')
df = pytrends.interest_over_time()

# Tìm tháng có search volume cao nhất
df['month'] = df.index.month
monthly_avg = df.groupby('month')[keyword].mean()

print("Mức độ tìm kiếm trung bình theo tháng:")
print(monthly_avg.sort_values(ascending=False))

# Tháng 3-6 có lẽ là mùa cao điểm cho điều hòa
```

### 🌏 Use Case 4: Phân Tích Thị Trường Địa Lý

**Mục tiêu:** Tìm thị trường tiềm năng để mở rộng kinh doanh.

```python
# Phân tích sản phẩm theo khu vực
product = 'cafe sạch'

pytrends.build_payload([product], timeframe='today 12-m', geo='VN')
df_region = pytrends.interest_by_region(resolution='REGION', inc_low_vol=True)

# Top 10 tỉnh thành tiềm năng
top_regions = df_region.sort_values(by=product, ascending=False).head(10)
print("Top 10 thị trường tiềm năng:")
print(top_regions)

# Lời khuyên: Tập trung marketing vào các tỉnh này
```

### 📱 Use Case 5: Content Marketing Strategy

**Mục tiêu:** Tạo nội dung dựa trên xu hướng tìm kiếm.

```python
# Tìm trending topics
df_trending = pytrends.trending_searches(pn='vietnam')
trending_keywords = df_trending[0].tolist()[:10]

print("Top 10 trending topics hôm nay:")
for i, kw in enumerate(trending_keywords, 1):
    print(f"{i}. {kw}")
    
    # Lấy related queries cho mỗi trending topic
    pytrends.build_payload([kw], timeframe='now 1-d', geo='VN')
    related = pytrends.related_queries()
    
    if kw in related and related[kw]['rising'] is not None:
        print(f"   → Subtopics: {related[kw]['rising']['query'].head(3).tolist()}")
    
    time.sleep(2)  # Avoid rate limit

# Tạo content dựa trên các topics này
```

---

## Best Practices

### ✅ Tránh Rate Limiting

Google có thể chặn nếu bạn gửi quá nhiều request.

```python
import time

# Delay giữa các request
time.sleep(2)  # 2 giây

# Hoặc sử dụng random delay
import random
time.sleep(random.uniform(1, 3))
```

### ✅ Xử Lý Lỗi

```python
try:
    pytrends.build_payload(['keyword'], timeframe='today 3-m')
    df = pytrends.interest_over_time()
    
    if df.empty:
        print("Không có dữ liệu")
    else:
        print(df)
        
except Exception as e:
    print(f"Lỗi: {e}")
    # Retry hoặc skip
```

### ✅ Lưu Dữ Liệu

```python
# Lưu CSV
df.to_csv('trends_data.csv')

# Lưu JSON
df.to_json('trends_data.json', orient='records', date_format='iso')

# Lưu Excel
df.to_excel('trends_data.xlsx')
```

### ✅ Batch Processing

Khi có nhiều từ khóa cần phân tích:

```python
keywords = ['keyword1', 'keyword2', 'keyword3', ..., 'keyword100']

# Chia thành batch (tối đa 5 từ khóa/request)
batch_size = 5
results = []

for i in range(0, len(keywords), batch_size):
    batch = keywords[i:i+batch_size]
    
    try:
        pytrends.build_payload(batch, timeframe='today 3-m', geo='VN')
        df = pytrends.interest_over_time()
        results.append(df)
        
        time.sleep(2)  # Delay
    except Exception as e:
        print(f"Error processing batch {i}: {e}")
        continue

# Merge results
import pandas as pd
final_df = pd.concat(results, axis=1)
```

---

## Giới Hạn và Lưu Ý

### ⚠️ Dữ Liệu Tương Đối

- Google Trends trả về **điểm tương đối** (0-100), không phải số tuyệt đối
- 100 = mức độ phổ biến cao nhất trong khoảng thời gian
- 50 = phổ biến bằng 50% so với điểm cao nhất
- 0 = không đủ dữ liệu

### ⚠️ Rate Limiting

- Google giới hạn số lượng request
- Nếu request quá nhanh sẽ bị chặn tạm thời
- Khuyến nghị: Delay 1-3 giây giữa các request

### ⚠️ Dữ Liệu Mẫu

- Với từ khóa ít người tìm, dữ liệu có thể không chính xác
- Kết quả có thể thay đổi giữa các lần chạy
- Nên test với từ khóa phổ biến trước

### ⚠️ API Không Chính Thức

- Pytrends là reverse-engineered API
- Google có thể thay đổi mà không thông báo
- Không dùng cho production critical systems

---

## Troubleshooting

### Lỗi: "The request failed: Google returned a response with code 429"

**Nguyên nhân:** Quá nhiều request trong thời gian ngắn.

**Giải pháp:**
```python
# Tăng delay
time.sleep(5)

# Hoặc retry với exponential backoff
import time
from functools import wraps

def retry_on_429(max_retries=3, delay=5):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if '429' in str(e) and i < max_retries - 1:
                        wait_time = delay * (2 ** i)
                        print(f"Rate limited. Waiting {wait_time}s...")
                        time.sleep(wait_time)
                    else:
                        raise
        return wrapper
    return decorator
```

### Lỗi: "No data available for this query"

**Nguyên nhân:** Từ khóa quá ít người tìm hoặc geo không phù hợp.

**Giải pháp:**
- Thử với từ khóa phổ biến hơn
- Mở rộng geo (VN → '' = toàn cầu)
- Tăng timeframe (today 1-m → today 12-m)

### Lỗi: Module not found

**Giải pháp:**
```bash
pip install --upgrade pytrends pandas
```

---

## So Sánh với Google Ads Keyword Planner

| Tính Năng | Google Trends (pytrends) | Google Ads Keyword Planner |
|-----------|-------------------------|---------------------------|
| **Chi phí** | ✅ Miễn phí | ⚠️ Cần chi tiêu ads |
| **Dữ liệu** | Tương đối (0-100) | Số tuyệt đối (search volume) |
| **Xu hướng** | ✅ Chi tiết theo thời gian | ⚠️ Trung bình tháng |
| **Địa lý** | ✅ Chi tiết đến city | ✅ Chi tiết |
| **Related keywords** | ✅ Có | ✅ Có |
| **Competition** | ❌ Không có | ✅ Có (Low/Med/High) |
| **CPC data** | ❌ Không có | ✅ Có |
| **Real-time** | ✅ Có (now 1-H) | ❌ Không |
| **Trending topics** | ✅ Có | ❌ Không |
| **API official** | ❌ Không chính thức | ✅ Có |

**Kết luận:**
- **Google Trends**: Tốt cho nghiên cứu xu hướng, phân tích đối thủ, content strategy
- **Keyword Planner**: Tốt cho SEO/SEM campaigns, keyword bidding, ROI analysis

---

## Tài Nguyên Bổ Sung

### 📚 Documentation
- [Pytrends GitHub](https://github.com/GeneralMills/pytrends)
- [Google Trends Official](https://trends.google.com)

### 🛠️ Tools Liên Quan
- **Ubersuggest** - Keyword research tool
- **AnswerThePublic** - Question-based keywords
- **Google Search Console** - Actual search data từ website của bạn
- **SEMrush / Ahrefs** - Professional SEO tools

### 💡 Tips
1. Kết hợp Google Trends với Google Search Console để có cái nhìn toàn diện
2. Sử dụng multiple data sources để verify insights
3. Theo dõi competitors thường xuyên (weekly/monthly)
4. Lưu historical data để phân tích long-term trends

---

## Liên Hệ & Hỗ Trợ

Nếu gặp vấn đề hoặc cần hỗ trợ:

1. Kiểm tra lại code trong `google_trends_demo.py`
2. Đọc error messages cẩn thận
3. Search Google với error message
4. Kiểm tra GitHub Issues của pytrends

---

## Changelog

- **v1.0** (2025-11-17): Phiên bản đầu tiên
  - Đầy đủ 9 tính năng chính
  - 7 demo examples
  - 5 use cases thực tế
  - Best practices và troubleshooting

---

**Chúc bạn thành công với Google Trends API! 🚀**
