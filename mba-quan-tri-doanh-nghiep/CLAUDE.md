# MBA Knowledge Base - Context cho Claude

## Mục đích

Knowledge base này là **tài liệu tham khảo MBA ứng dụng** với trọng tâm:
- **Quản trị doanh nghiệp vừa và nhỏ (SME)** tại Việt Nam
- Frameworks MBA chuẩn với **case studies thực tế**
- Hướng dẫn **triển khai công cụ** cụ thể, có giá thành
- Kết nối lý thuyết MBA với **thực tiễn kinh doanh VN**

**Target audience**: Chủ SME, startup founders, MBA learners

---

## Cấu trúc Knowledge Base

```
MBA/
├── CLAUDE.md                                    # File này
├── quan-tri-doanh-nghiep-vua-va-nho.md         # Quản trị SME tổng quan (từ con số 0)
├── cong-cu-quan-tri-doanh-nghiep-sme.md        # Công cụ & phần mềm cho SME
│
├── 1-strategic/                                 # 7 topics - Chiến lược doanh nghiệp
│   ├── 01-phan-tich-moi-truong-ben-ngoai.md   # PESTEL + Porter's 5 Forces
│   ├── 02-phan-tich-noi-bo.md                 # Value Chain + VRIO
│   ├── 03-chien-luoc-canh-tranh.md            # Porter's Generic Strategies
│   ├── 04-chien-luoc-tang-truong.md           # Ansoff Matrix + Growth Strategies
│   ├── 05-blue-ocean-strategy.md              # Chiến lược đại dương xanh
│   ├── 06-balanced-scorecard.md               # BSC - đo lường hiệu quả
│   └── 07-scenario-planning.md                # Kế hoạch kịch bản
│
├── 2-marketing/                                 # 10 topics - Marketing
│   ├── 01-stp-segmentation-targeting-positioning.md
│   ├── 02-marketing-mix-4p-7p.md
│   ├── 03-customer-lifetime-value.md           # CLV + Retention
│   ├── 04-brand-management.md                  # Brand Equity + Identity
│   ├── 05-digital-marketing-growth-hacking.md
│   ├── 06-consumer-behavior.md                 # Hành vi người tiêu dùng
│   ├── 07-marketing-research.md
│   ├── 08-integrated-marketing-communications.md
│   ├── 09-product-life-cycle.md
│   └── 10-pricing-strategies.md
│
├── 3-financial/                                 # 10 topics - Tài chính doanh nghiệp
│   ├── 01-time-value-of-money.md               # PV, FV, NPV, IRR
│   ├── 02-capital-budgeting.md                 # Quyết định đầu tư
│   ├── 03-cost-of-capital.md                   # WACC, Cost of Equity/Debt
│   ├── 04-capital-structure.md                 # Cấu trúc vốn tối ưu
│   ├── 05-financial-statement-analysis.md      # Phân tích BCTC
│   ├── 06-working-capital-management.md        # Quản trị vốn lưu động
│   ├── 07-dividend-policy.md                   # Chính sách cổ tức
│   ├── 08-risk-and-return.md                   # Portfolio Theory
│   ├── 09-mergers-and-acquisitions.md          # M&A
│   └── 10-corporate-valuation.md               # Định giá DN
│
├── case-studies/                                # 🆕 Case studies thực tế
│   ├── 01-quan-cafe-specialty-saigon.md        # Quán cà phê Q.1 HCMC - Full analysis
│   ├── 02-nha-hang-pho-modern-hanoi.md         # Nhà hàng phở Hà Nội - Turnaround strategy
│   └── 03-quan-hai-san-binh-dan-danang.md     # Quán hải sản Đà Nẵng - Niche & Cost Focus
│
└── templates/                                   # 🆕 Templates có thể tái sử dụng
    ├── business-plan-template-sme.md            # Business plan template SME VN
    └── financial-model-excel-guide.md           # Hướng dẫn build financial model Excel
    ├── 07-dividend-policy.md                   # Chính sách cổ tức
    ├── 08-risk-and-return.md                   # Portfolio Theory
    ├── 09-mergers-and-acquisitions.md          # M&A
    └── 10-corporate-valuation.md               # Định giá DN
```

**Tổng cộng**: 27 topics MBA + 2 guides thực tiễn

---

## Đặc điểm Nội dung

### 1. Format chuẩn cho mỗi topic

Mỗi file markdown tuân thủ structure:

```markdown
# [Tên Framework/Topic]

> **Mục tiêu**: Câu tóm tắt ngắn gọn

## I. Khái niệm & Lý thuyết
- Định nghĩa
- Origin (ai tạo ra, năm nào)
- Framework diagram/table

## II. Chi tiết từng thành phần
- Phân tích sâu từng phần
- Công thức (nếu có)
- Tables so sánh

## III. Case Studies thực tế
- VD từ doanh nghiệp Việt Nam
- VD quốc tế (Apple, Amazon, Vinamilk, etc.)
- Detailed scenarios

## IV. Ứng dụng cho SME
- Cách áp dụng cho SME/startup
- Templates thực tế
- Common mistakes to avoid

## V. Tools & Templates
- Công cụ hỗ trợ
- Excel/Google Sheets templates
- Software suggestions

## VI. Bài tập thực hành
- Practice questions
- Mini case studies

## PHỤ LỤC: CHECKLIST [TÊN TOPIC] TỔNG HỢP
- Section cuối cùng, sau mục VI (không đánh số La Mã, dùng tiêu đề "PHỤ LỤC:")
- Checklist thực tế dạng gạch đầu dòng (□ ...) để người đọc tự rà soát trước khi áp dụng
- Nếu file gốc có bảng "Công thức tổng hợp" riêng, gộp chung vào đây (không tách thành mục/file khác)
```

**Lưu ý về heading nesting trong mục III (Case Studies)**: mỗi case study là 1 heading `###` (ví dụ `### 1. Case Study Thành công: ...`), các phần con bên trong case đó (Bối cảnh, Diễn giải từng bước, Bài học...) PHẢI là `####` — lỗi thường gặp khi sửa file cũ là để các phần con này cùng cấp `###` với tiêu đề case study, cần rà soát và sửa lại cho đúng cấp lồng nhau.

### 2. Style & Conventions

**Language**: Tiếng Việt, thuật ngữ Anh trong ngoặc
- ✅ "Phân khúc thị trường (Segmentation)"
- ✅ "Giá trị thời gian của tiền (Time Value of Money)"

**Examples**: 
- 🇻🇳 Case VN: Vinamilk, Viettel, The Coffee House, Highlands Coffee
- 🌍 Case Quốc tế: Apple, Amazon, Nike, Tesla
- 🏪 Case SME: Quán cà phê, nhà hàng phở, shop online

**Numbers & Data**: 
- Số liệu thực tế từ Việt Nam
- Giá cả theo VNĐ + USD (nếu cần)
- Chi phí công cụ/phần mềm cụ thể

**Tables & Diagrams**:
- Heavy use of markdown tables
- ASCII art cho diagrams/flowcharts
- Structured comparisons

**Formulas**: 
- LaTeX format cho công thức tài chính
- Giải thích từng biến số
- Ví dụ tính toán step-by-step

---

## Nội dung Các File Chính

### quan-tri-doanh-nghiep-vua-va-nho.md (861 lines)

**Roadmap toàn diện** từ 0 → scaling SME:

1. **Giai đoạn Ý tưởng & Nghiên cứu**: TAM/SAM/SOM, Customer Persona
2. **Lập Kế hoạch**: Business Plan, Business Model Canvas
3. **Pháp lý & Thành lập**: Các loại hình DN tại VN, thủ tục đăng ký
4. **Huy động vốn**: Bootstrapping, Angel, VC, Bank loans
5. **Thiết lập Operations**: Tổ chức bộ máy, quy trình
6. **Marketing & Bán hàng**: Customer Acquisition, Sales Funnel
7. **Quản lý Tài chính**: Cash flow, P&L, Balance Sheet
8. **Nhân sự**: Tuyển dụng, đào tạo, KPI
9. **Tăng trưởng & Scale**: Growth strategies
10. **Exit Strategy**: M&A, IPO

### cong-cu-quan-tri-doanh-nghiep-sme.md (710 lines)

**Catalog chi tiết** công cụ & phần mềm cho SME VN:

**Categories**:
1. **Công cụ chung**: Kế toán (MISA, Fast), HRM (Base HRM), CRM
2. **Quán Cà Phê**: POS (Sapo, KiotViet), Loyalty, Kho
3. **Nhà Hàng**: POS (iPos, Foody), Kitchen Display, Booking
4. **E-commerce**: Shopify, Haravan, Facebook Shop, TikTok Shop

**Thông tin mỗi tool**:
- Tên phần mềm + link
- Chi phí cụ thể (VNĐ/năm hoặc USD/tháng)
- Công dụng chi tiết
- Phù hợp với loại hình nào
- Case study ứng dụng thực tế

**Value**: So sánh chi phí, lộ trình triển khai từng giai đoạn

---

## Topics Coverage

### Strategic Management (7 topics)

| File | Framework | Application |
|------|-----------|-------------|
| 01 | PESTEL + Porter's 5 Forces | Phân tích môi trường vĩ mô & ngành |
| 02 | Value Chain + VRIO | Phân tích nội bộ, lợi thế cạnh tranh |
| 03 | Porter's Generic Strategies | Cost Leadership, Differentiation, Focus |
| 04 | Ansoff Matrix | Market Penetration/Development, Product Dev |
| 05 | Blue Ocean Strategy | Tạo thị trường mới, Strategy Canvas, ERRC |
| 06 | Balanced Scorecard | Đo lường KPI 4 perspectives |
| 07 | Scenario Planning | Lập kế hoạch cho tương lai bất định |

**Depth**: Mỗi file 300-400 lines, chi tiết frameworks, examples, templates

### Marketing (10 topics)

| File | Framework | Application |
|------|-----------|-------------|
| 01 | STP | Segmentation → Targeting → Positioning |
| 02 | Marketing Mix | 4P (Product, Price, Place, Promotion) + 3P Services |
| 03 | CLV | Customer Lifetime Value, RFM, Cohort Analysis |
| 04 | Brand Management | Brand Equity, Keller's CBBE, Brand Identity |
| 05 | Digital Marketing | SEO, SEM, Social, Content, Growth Hacking (AARRR) |
| 06 | Consumer Behavior | Decision Process, Maslow, Buying Influences |
| 07 | Marketing Research | Primary/Secondary, Survey Design, Data Analysis |
| 08 | IMC | Integrated Marketing Communications |
| 09 | Product Life Cycle | Introduction → Growth → Maturity → Decline |
| 10 | Pricing Strategies | Cost-based, Value-based, Competition-based |

**Practical focus**: 
- Mỗi framework có **SME application section**
- Templates cho Excel/Google Sheets
- Tool recommendations (Google Analytics, Facebook Ads, etc.)

### Financial Management (10 topics)

| File | Concepts | Key Formulas |
|------|----------|--------------|
| 01 | Time Value of Money | PV, FV, NPV, IRR, Payback Period |
| 02 | Capital Budgeting | NPV, IRR, PI, MIRR for project evaluation |
| 03 | Cost of Capital | WACC, Cost of Equity (CAPM), Cost of Debt |
| 04 | Capital Structure | M&M Theorem, Trade-off Theory, Optimal Structure |
| 05 | Financial Statement Analysis | Ratio Analysis (Liquidity, Leverage, Profitability) |
| 06 | Working Capital | Cash Conversion Cycle, Inventory/AR/AP Management |
| 07 | Dividend Policy | Payout Ratio, Dividend Theories, Stock Buyback |
| 08 | Risk & Return | Portfolio Theory, CAPM, Beta, Sharpe Ratio |
| 09 | M&A | Valuation methods, Synergies, Deal Structure |
| 10 | Corporate Valuation | DCF, Multiples (P/E, EV/EBITDA), Terminal Value |

**Calculation focus**:
- Step-by-step examples với số liệu thực tế
- Excel formulas provided
- SME applications (ví dụ: tính NPV cho mở thêm chi nhánh)

---

## Use Cases cho Claude

### 1. Học MBA Concepts

**Prompt examples**:
```
"Giải thích Blue Ocean Strategy với ví dụ từ doanh nghiệp Việt Nam"
→ Claude reads @05-blue-ocean-strategy.md

"So sánh Cost Leadership vs Differentiation, khi nào dùng strategy nào?"
→ Claude reads @03-chien-luoc-canh-tranh.md

"Cách tính NPV cho dự án mở thêm quán cà phê, vốn đầu tư 500 triệu?"
→ Claude reads @01-time-value-of-money.md + @cong-cu-quan-tri-doanh-nghiep-sme.md
```

### 2. Applied SME Consulting

**Scenario-based prompts**:
```
"Tôi muốn mở quán cà phê ở Q.1, HCM. Cần phân tích gì trước khi quyết định?"
→ Claude reads: @PESTEL, @Porter's-5-Forces, @STP, @quan-tri-doanh-nghiep-vua-va-nho.md

"Quán tôi đang bị lỗ, revenue giảm 20%. Phân tích financial statements thế nào?"
→ Claude reads: @05-financial-statement-analysis.md, @06-working-capital-management.md

"Cần setup công cụ gì cho nhà hàng 50 bàn, 20 nhân viên?"
→ Claude reads: @cong-cu-quan-tri-doanh-nghiep-sme.md (section Nhà hàng)
```

### 3. Business Plan Creation

```
"Viết business plan cho startup food delivery targeting Gen Z Hà Nội"
→ Claude reads: @quan-tri-doanh-nghiep-vua-va-nho.md, @STP, @marketing-mix, @customer-lifetime-value

"Tạo financial projections 3 năm cho shop online thời trang"
→ Claude reads: @time-value-of-money, @capital-budgeting, @working-capital-management
```

### 4. Framework Comparison

```
"Khi nào dùng Ansoff Matrix vs Blue Ocean Strategy?"
→ Claude reads: @04-chien-luoc-tang-truong.md, @05-blue-ocean-strategy.md

"4P vs 7P Marketing Mix, khác biệt thế nào? Khi nào dùng 7P?"
→ Claude reads: @02-marketing-mix-4p-7p.md
```

### 5. Tool & Software Selection

```
"Phần mềm kế toán nào phù hợp cho SME 10 nhân viên, ngân sách <5 triệu/năm?"
→ Claude reads: @cong-cu-quan-tri-doanh-nghiep-sme.md

"So sánh Sapo vs KiotViet cho quán trà sữa"
→ Claude reads: @cong-cu-quan-tri-doanh-nghiep-sme.md (section Quán Cà Phê)
```

---

## Reference Patterns

### Khi cần strategy frameworks
```
@1-strategic/ - Scan tất cả strategic topics
@PESTEL - External environment
@Value-Chain - Internal analysis
@Blue-Ocean - Innovation strategy
```

### Khi cần marketing guidance
```
@2-marketing/ - Scan tất cả marketing topics
@STP - Market segmentation & positioning
@4P-7P - Marketing mix
@Digital-Marketing - Online channels
```

### Khi cần financial analysis
```
@3-financial/ - Scan tất cả financial topics
@time-value-of-money - NPV, IRR calculations
@financial-statement-analysis - Ratio analysis
@capital-budgeting - Investment decisions
```

### Khi cần practical implementation
```
@quan-tri-doanh-nghiep-vua-va-nho.md - SME roadmap
@cong-cu-quan-tri-doanh-nghiep-sme.md - Tools & software
```

---

## Current Status

**Completion**: 
- ✅ 27/27 topics completed
- ✅ 2/2 practical guides completed
- ✅ All files reviewed & formatted

**Quality**:
- Mỗi file 300-400+ lines
- Comprehensive frameworks với examples
- SME applications cho mỗi concept
- Tools & templates provided

**Last Updated**: Initial creation (date unknown, needs timestamp)

**Coverage**: Complete MBA foundation trong 3 areas: Strategy, Marketing, Finance

---

## Case Studies - Applied MBA Frameworks

### Case Study 1: Quán Cà Phê Specialty "The Roastery" - Q.1 Sài Gòn

**File**: `case-studies/01-quan-cafe-specialty-saigon.md` (~600 lines)

**Scenario**: Startup quán cà phê specialty targeting Gen Z/Millennials  
**Investment**: 1.2 tỷ VNĐ  
**Location**: Quận 1, HCMC (prime location, high competition)

**Frameworks Applied**:
- ✅ **PESTEL Analysis**: Political, economic, social trends affecting F&B
- ✅ **Porter's 5 Forces**: Industry attractiveness analysis (scored 6-9/10 threat levels)
- ✅ **STP Strategy**: Segmentation (3 tiers), Targeting (Coffee Enthusiasts), Positioning (accessible specialty)
- ✅ **Marketing Mix 4P**: Product (menu design), Price (value-based 50-78k), Place (80m² layout), Promotion (15M/month budget)
- ✅ **Financial Analysis**: Full 3-year projections, NPV +1,847M, IRR 48%, Break-even Month 9

**Key Insights**:
- Competitive intensity VERY HIGH (9/10) - 50+ cafes within 1km
- Differentiation strategy: Local roasting + vibrant ambiance + transparent pricing
- Pricing strategy: Positioned 15-20% below competitors while maintaining quality
- Expected Year 3 EBITDA margin: 16.5%

**Use Cases for Claude**:
```
"Analyze profitability của quán cà phê với rent 80M/tháng"
→ Read case study, extract P&L analysis

"So sánh Porter's 5 Forces cho F&B vs Tech startup"
→ Use this case study + general framework

"Tạo financial model cho quán trà sữa, similar to The Roastery"
→ Adapt assumptions from this case
```

---

### Case Study 2: Nhà Hàng Phở Modern "Phở Ơi" - Hà Nội

**File**: `case-studies/02-nha-hang-pho-modern-hanoi.md` (~550 lines)

**Scenario**: **Turnaround strategy** for restaurant after 6 months, revenue 60% of target  
**Challenge**: Good traffic at peak hours, empty during off-peak  
**Focus**: Growth strategy to hit 430M/month (from 180M)

**Frameworks Applied**:
- ✅ **Blue Ocean Strategy**: ERRC Grid (Eliminate paper menus, Create subscription model)
- ✅ **Pricing Innovation**: Modular pricing (base 40k + add-ons), Subscription "Phở Pass" 999k/month, Dynamic off-peak pricing
- ✅ **Digital Marketing & Growth Hacking**: UGC campaigns, referral program, corporate B2B channel
- ✅ **CLV Analysis**: Before (392k) vs After (2,363k) - **503% increase**

**Key Innovations**:
1. **Phở Pass Subscription**: First in Vietnam - 999k/tháng unlimited phở
2. **Modular Pricing**: Base (40k) + choose proteins/toppings (fair pricing, upsell opportunity)
3. **DIY Kits**: Extend brand beyond restaurant (150k/kit for 2 people)
4. **Corporate Catering**: B2B channel for bulk orders

**Financial Impact**:
- Revenue: 180M → 430M/month (+139%)
- EBITDA margin: 8.3% → 30% (+263%)
- LTV:CAC: 1.4 → 13.1 (from unhealthy to excellent)

**Use Cases for Claude**:
```
"Blue Ocean Strategy cho nhà hàng truyền thống"
→ Read ERRC grid from this case

"Làm sao tăng CLV cho F&B business?"
→ Study the CLV improvement tactics (subscription, loyalty, retention)

"Pricing strategy nào phù hợp cho restaurant with varied menu?"
→ Learn modular pricing approach
```

---

### Case Study 3: Quán Hải Sản Bình Dân "Biển Xanh" - Đà Nẵng 🆕

**File**: `case-studies/03-quan-hai-san-binh-dan-danang.md` (~1,100 lines) ⬆️ Updated with competitor analysis

**Scenario**: Khởi nghiệp quán hải sản bình dân targeting gia đình local  
**Investment**: 850M VNĐ (<1 tỷ)  
**Location**: Thanh Khê, Đà Nẵng (residential area, NOT tourist zone)

**Frameworks Applied**:
- ✅ **Niche Market Analysis**: Budget seafood for locals (150-250k/người) vs tourist high-end
- ✅ **Porter's Generic Strategies**: Cost Focus (cost leadership within narrow segment)
- ✅ **Competitive Analysis**: Deep-dive competitor "Đảnh Năm" (Thọ Quang, 120m²) ⭐ NEW
- ✅ **Operations Management**: Daily-fresh model, lean staff (5 people), supply chain optimization
- ✅ **Menu Engineering**: 30-dish detailed menu with costing & margins
- ✅ **Local Marketing**: Grassroots approach (60% offline, 40% online), community building

**Detailed Coverage**:
- **Niche Analysis**: Scored 44/60 attractiveness, 40% of market underserved
- **Cost Leadership Tactics**: 
  - Direct supplier relationships (20-30% cost savings)
  - Lean operations (5 staff, minimal tech)
  - Menu engineering (high-margin item push)
  - Waste reduction (<5% target)
- **MENU CHI TIẾT - 30 MÓN**:
  - 15 món hải sản chính (tôm, cua, ghẹ, mực, cá, nghêu, ốc, bào ngư)
  - 3 món lẩu (tổng hợp, cá, ghẹ)
  - 5 món ăn kèm (cơm, bún, bánh tráng, khoai chiên, chả giò)
  - 4 món rau & canh
  - 3 loại đồ uống
  - **Mỗi món bao gồm**: Định lượng, chi phí NVL, thời gian chế biến, giá bán, biên lợi nhuận
  - **4 Combo meals**: Gia đình (420k/4 người), Nhậu (560k/6 người), Lẩu (450k/5-6 người), Tiết kiệm (200k/2 người)
  - **Menu Engineering Matrix**: STARS/WORKHORSES/PUZZLES/DOGS analysis
  - **Upselling tactics**: Scripts, conversion targets, add-on strategies
- **COMPETITOR ANALYSIS - Quán Đảnh Năm** ⭐ NEW:
  - Full menu analysis (80-100 món vs Biển Xanh 30 món)
  - Pricing comparison (Đảnh Năm 150k/người vs Biển Xanh 200k/người)
  - Strengths: Variety, location near Thọ Quang market, flexible pricing
  - Weaknesses: Menu overload, no combos, no hot pot, opaque "thời giá"
  - Positioning map: Quality/Service axis
  - **5 Differentiation Strategies**: Transparent pricing, Service excellence, Hot pot focus, Combo meals, Ambiance
  - **Learning từ đối thủ**: Menu flexibility, protein variety (thêm món thịt), seasonal adaptation
  - **Defensive moves**: How to counter if competitor imitates
  - **Coexist strategy**: Serve different customer segments
- **Operations SOPs**: 
  - Daily supply chain (4:30AM market visits)
  - Order-to-serve <18 minutes
  - Quality control checkpoints
- **Marketing Strategy**:
  - Pre-launch: Community visits (200 households), soft opening
  - Ongoing: Referral program, VIP customers, monthly events
  - Paid ads only after Month 6 (lean budget 5M/month)

**Financial Outcome**:
- Break-even: Month 2 (26 customers/day)
- Year 1: Revenue 1,764M (loss -86M while ramping up)
- Year 3: Revenue 2,975M, EBITDA margin 8.1%
- NPV: +1,147M, IRR: 36%, Payback: 3.8 years

**Key Insights**:
- **Niche selection critical**: Budget locals vs high-end tourists = completely different business
- **Location strategy**: Residential Thanh Khê (lower rent, loyal customers) vs Mỹ Khê beach (high rent, seasonal)
- **Daily-fresh model**: Eliminates inventory risk, ensures quality, requires 4:30AM commitment
- **Transparent pricing**: "Giá gốc + 30%" builds trust in price-sensitive market

**Use Cases for Claude**:
```
"Phân tích niche market cho quán ăn local vs tourist"
→ Study the segmentation and niche attractiveness scoring

"Cost leadership strategies cho SME F&B với budget constraints"
→ Learn supplier negotiations, lean operations, waste reduction tactics

"Operations management cho quán hải sản: daily fresh supply chain"
→ Review daily flow from 4:30AM market to evening service

"Làm menu cho quán hải sản với chi phí chi tiết từng món"
→ Use the 30-dish menu template with ingredient costs, prep time, selling price

"Menu engineering: phân loại món ăn theo profitability và popularity"
→ Apply STARS/WORKHORSES/PUZZLES/DOGS matrix

"Upselling strategies cho nhà hàng: combo meals, add-ons, drinks"
→ Study the detailed scripts and tactics with conversion targets

"Phân tích đối thủ cạnh tranh trong cùng phân khúc"
→ Read competitor analysis of Đảnh Năm (menu, pricing, positioning)

"Chiến lược differentiation khi đối thủ có thế mạnh về giá/variety"
→ Learn 5 differentiation tactics (transparency, service, combos, hot pot, ambiance)

"Coexist strategy: làm sao cạnh tranh mà không đua giá"
→ Study positioning statement and target different customer segments

"Marketing strategy với budget <5M/month cho local restaurant"
→ Grassroots tactics, referral program, VIP customer approach
```

---

## Templates - Reusable Documents

### Template 1: Business Plan for SME Vietnam

**File**: `templates/business-plan-template-sme.md` (~700 lines)

**Purpose**: Comprehensive business plan template cho SME/Startup tại VN, dùng cho:
- Pitching to investors (Angel/VC)
- Bank loan applications
- Internal strategic planning

**Structure** (11 major sections):
1. **Executive Summary** (write last) - 1-2 trang tóm tắt
2. **Company Description** - Business model, value prop, history
3. **Market Analysis** - PESTEL, TAM/SAM/SOM, competitive landscape
4. **Organization & Management** - Team, org chart, staffing plan
5. **Products & Services** - Product lineup, roadmap, IP
6. **Marketing & Sales Strategy** - STP, 4P, customer acquisition
7. **Financial Projections** - 3-year P&L, Cash Flow, Balance Sheet, KPIs
8. **Funding Request** - Amount, use of funds, terms, ROI projections
9. **Risk Analysis** - Key risks + mitigation plans
10. **Milestones & Timeline** - 12-month roadmap
11. **Appendices** - Supporting documents

**Key Features**:
- ✅ Vietnamese market context (legal structures, tax rates, regulations)
- ✅ Instructions for different audiences (investors vs banks vs internal)
- ✅ Example data and ranges for sanity checks
- ✅ Common mistakes to avoid
- ✅ Tips on length (exec summary 2 pages, total <30 pages)

**Use Cases**:
```
"Tạo business plan cho startup food delivery"
→ Fill in template sections with specifics

"Section nào quan trọng nhất khi xin vốn ngân hàng?"
→ Template explains emphasis for bank loans (financial projections, collateral)

"Làm sao tính TAM/SAM/SOM cho thị trường VN?"
→ Template provides formula and Vietnamese market examples
```

---

### Template 2: Financial Model Excel Guide

**File**: `templates/financial-model-excel-guide.md` (~800 lines)

**Purpose**: Hướng dẫn step-by-step xây dựng financial model trong Excel cho SME

**Workbook Structure** (11 tabs):
1. **Cover** - Dashboard with summary metrics + health indicators
2. **Assumptions** - All inputs (single source of truth)
3. **Revenue** - Customer growth, AOV, frequency → Revenue build-up
4. **COGS** - Variable costs by category
5. **Opex** - Fixed and semi-variable operating expenses
6. **P&L** - Profit & Loss statement (monthly Y1, annual Y2-Y3)
7. **Cash Flow** - Operating, Investing, Financing activities
8. **Balance Sheet** - Assets, Liabilities, Equity
9. **Metrics** - KPIs (CAC, LTV, margins, returns, efficiency)
10. **Scenarios** - Sensitivity analysis (best/base/worst case)
11. **Charts** - Visualizations for presentations

**Key Formulas Provided**:
- Revenue modeling (new customers, churn, retention)
- Break-even analysis
- NPV, IRR, Payback Period
- Unit economics (LTV:CAC, contribution margin)
- Financial ratios (Current Ratio, ROE, ROA, etc.)

**Validation Checks**:
- Formula checks (Revenue = COGS + GP, Balance Sheet must balance)
- Sanity checks (GP margin 40-70% for F&B, LTV:CAC >3.0)

**Pro Features**:
- Color coding system (blue = input, white = calculated)
- Named ranges for easier formulas
- Conditional formatting for alerts (cash runway < 6 months)
- Data tables for scenario analysis

**Use Cases**:
```
"Build 3-year financial model cho retail shop"
→ Follow tab-by-tab structure, adapt assumptions

"Công thức tính break-even cho business với fixed + variable costs"
→ Tab 10: Break-even analysis section

"KPIs nào quan trọng nhất cho SME F&B?"
→ Tab 9: Metrics - shows LTV, CAC, margins, efficiency ratios
```

---

## Current Status Update

**Completion**: 
- ✅ 27/27 MBA framework topics
- ✅ 2/2 practical SME guides
- ✅ 3/3 case studies (comprehensive real-world applications)
- ✅ 2/2 templates (business plan + financial model)

**Total Content**: 33 files, ~15,700+ lines

**Quality**:
- Theory: All frameworks explained với definitions, diagrams, formulas
- Practice: Every concept has SME application section
- Examples: Vietnamese context (Vinamilk, The Coffee House) + International (Apple, Amazon)
- Tools: Specific software recommendations với pricing
- Templates: Ready-to-use, comprehensive
- Competitive Analysis: Real competitor deep-dive với actual menu data

**Latest Updates** (2026-05-05):
- ✅ Added 2 comprehensive case studies (600+ lines each) - Morning session
- ✅ Created business plan template (700 lines, 11 sections) - Morning session
- ✅ Created financial model Excel guide (800 lines, 11 tabs) - Morning session
- ✅ Added case study 3: Quán hải sản Đà Nẵng (700→900 lines) - Afternoon session
- ✅ Enhanced case study 3 with detailed 30-dish menu (all Vietnamese) - Evening session
  - 15 seafood mains + 3 hot pots + 5 sides + 4 vegetables + 3 beverages
  - Each dish: quantity specs, ingredient costs, prep time, selling price, margins
  - 4 combo meals with detailed costing
  - Menu engineering matrix (STARS/WORKHORSES/PUZZLES/DOGS)
  - Upselling scripts and tactics
- ✅ Added competitor analysis: Quán Đảnh Năm (Thọ Quang) - Evening session 🆕
  - Full menu breakdown (80-100 món analyzed from actual photos)
  - Pricing comparison table
  - Strengths/Weaknesses matrix
  - 5 differentiation strategies
  - Coexist vs compete decision framework
  - 6-month action plan

---

## Next Steps & TODOs

### Potential Enhancements

- [ ] Add **Operations Management** section (Supply Chain, Lean, Six Sigma)
- [ ] Add **Organizational Behavior** section (Leadership, Motivation, Culture)
- [ ] Add **Business Law** section (Luật DN, Thuế VN, IP Protection)
- [x] Create **mini case studies** folder với detailed scenarios ✅ DONE (3 case studies)
- [x] Add **Excel templates** folder (Financial models, Marketing calculators) ✅ DONE
- [ ] Create **index.md** với search functionality
- [ ] Add **quiz questions** cho mỗi topic
- [ ] More case studies: E-commerce, SaaS, Retail, Services (non-F&B industries)

### Maintenance

- [ ] Update costs trong tools guide (inflatio, new pricing)
- [ ] Add new tools/software xuất hiện
- [ ] Update case studies với examples mới
- [ ] Review VN market data accuracy

---

## Yêu cầu & Phong cách khi Review/Update File (Quan trọng — đọc trước khi chỉnh sửa bất kỳ file nào)

Khi user yêu cầu "review và update chi tiết hơn" một file trong knowledge base này (ví dụ: *"review và update chi tiết hơn nội dung file X, giải thích bằng tiếng Việt, case study phân tích chi tiết chứ không phải tóm tắt, sắp xếp lại cấu trúc file rõ ràng, bổ sung case phân tích làm rõ tại sao lại có công thức/chỉ số"*), áp dụng các nguyên tắc sau:

### 1. Case study phải "phân tích chi tiết", không phải tóm tắt
- ❌ KHÔNG chấp nhận: case study chỉ có 1 bảng số liệu + 1-2 câu kết luận ngắn.
- ✅ YÊU CẦU: mỗi case study phải có bối cảnh cụ thể → số liệu cụ thể → **từng bước tính toán** (step-by-step, hiển thị phép tính) → diễn giải ý nghĩa kinh doanh của kết quả → kết luận/bài học/khuyến nghị hành động.
- Case study mới tự tạo ra (ví dụ số liệu BCTC của 1 SME giả định) phải **tự nhất quán về mặt số học/logic** (vd: Balance Sheet phải cân Assets = Liabilities + Equity, Cash Flow Statement phải khớp với thay đổi tiền mặt giữa 2 kỳ) — **bắt buộc chạy `python3 -c "..."` (qua bash) để verify các phép tính trước khi ghi vào file**, không được bịa số liệu không khớp phép tính; verify lại 1 lần cuối sau khi hoàn thiện, không chỉ tin vào tính nhẩm.
- Nếu phát hiện case study cũ có nội dung lặp/trùng (copy-paste lỗi), phải xóa triệt để, chỉ giữ 1 bản duy nhất, viết lại cho mạch lạc hơn thay vì chỉ xóa phần dư.
- Khi mục III (Case Studies) của file gốc chỉ có case "Thành công" + case "Thất bại" (thường là ví dụ quốc tế/doanh nghiệp lớn), **luôn bổ sung thêm 1 case study hoàn toàn mới dạng SME Việt Nam** (tự thiết kế bối cảnh, tên doanh nghiệp, số liệu) áp dụng đúng framework của bài, để người đọc SME Việt Nam có ví dụ gần gũi hơn — đây là mục case study thứ 3 trở lên trong mục III, không thay thế 2 case cũ.

### 2. Luôn giải thích "TẠI SAO", không chỉ liệt kê công thức
- Với mọi công thức/chỉ số/framework, trước khi đưa bảng công thức, phải có đoạn giải thích: *vấn đề kinh doanh nào nó giải quyết, logic đằng sau công thức được xây dựng như vậy, nguồn gốc lịch sử nếu có (ai tạo ra, năm nào, trong bối cảnh nào)*.
- Mục tiêu: người đọc là người MỚI (beginner) phải hiểu được **bản chất**, không chỉ học thuộc công thức để áp dụng máy móc.
- Ví dụ cách làm đúng: giải thích tại sao Quick Ratio loại bỏ Inventory ra khỏi Current Assets, tại sao mô hình DuPont (do công ty DuPont phát triển năm 1920s) lại tách ROE thành 3 thành phần thay vì nhìn 1 con số tổng.

### 3. Sắp xếp lại cấu trúc rõ ràng, rành mạch
- Luôn tuân thủ đúng khung 6 phần chuẩn I–VI đã quy định ở mục "Format chuẩn cho mỗi topic" phía trên — không tự ý tạo cấu trúc khác.
- Nếu file hiện tại bị lệch chuẩn (thiếu mục IV/V/VI, heading sai cấp, đánh số nhảy/trùng, hoặc có đoạn bị dính/lỗi định dạng), phải **tái cấu trúc lại toàn bộ** theo đúng chuẩn, không chỉ vá từng chỗ nhỏ.
- Khi file có nhiều heading con, đảm bảo cấp heading (`#`/`##`/`###`...) nhất quán theo chiều sâu lồng nhau thực sự, và số thứ tự (2.1, 2.1.1...) không trùng/nhảy.
- **User không muốn tạo file phụ lục/file riêng khi được yêu cầu "update vào file X"** — toàn bộ nội dung bổ sung phải nằm trong chính file được chỉ định, không tách ra file khác (trừ khi là case study/template thuộc thư mục `case-studies/` hoặc `templates/` đã có quy ước riêng từ trước).

### 4. Độ dài & độ sâu sau khi update
- File sau khi update thường sẽ dài hơn đáng kể so với bản gốc (có thể tăng 50-100%+ số dòng) do thêm case study chi tiết + phần giải thích "tại sao" + các mục còn thiếu (IV/V/VI) — đây là điều BÌNH THƯỜNG và ĐÚNG Ý, không cần cắt gọn lại cho ngắn nếu nội dung thêm vào có giá trị thực chất.
- Tuy vậy vẫn phải mạch lạc, không lan man, không lặp ý giữa các phần.

### 5. Quy trình làm việc khuyến nghị
- Đọc toàn bộ file cần sửa + CLAUDE.md này + 1-2 file liền kề cùng thư mục (để tham chiếu độ dài/văn phong tương đương) trước khi viết lại.
- Với các file lớn (>400-500 dòng) cần viết lại sâu, nên giao việc viết nội dung cho background agent với bối cảnh đầy đủ (trích dẫn chuẩn CLAUDE.md, liệt kê rõ heading hiện tại của file, liệt kê rõ vấn đề cần sửa, yêu cầu cụ thể từng phần I-VI + PHỤ LỤC) để tiết kiệm thời gian, sau đó **luôn tự kiểm tra lại độc lập bằng grep/view trực tiếp trên file** (không chỉ tin vào báo cáo của agent) — kiểm tra heading structure (`grep -n "^#"`), kiểm tra không còn đoạn lặp (đếm số lần xuất hiện tiêu đề/section nghi trùng), kiểm tra dòng `*Tài liệu tham khảo: ...*` cuối file còn nguyên vẹn, kiểm tra số liệu case study tự nhất quán.
- Khi user yêu cầu update **nhiều file cùng lúc** (ví dụ "update các file còn lại trong thư mục"), có thể giao song song nhiều background agent (mỗi agent 1 file, prompt đầy đủ ngữ cảnh riêng cho file đó) để tăng tốc, miễn là các file độc lập với nhau — vẫn phải verify độc lập từng file sau khi các agent hoàn tất, không gộp verify.
- Nếu một file có cấu trúc/mục đích khác biệt về bản chất (ví dụ file tổng hợp nhiều topic/nhiều case study tích hợp như `11-integrated-corporate-finance-guide.md`, không phải dạng "1 topic/1 file"), **không ép buộc theo đúng khuôn I-VI** — ghi nhận lý do và giữ nguyên cấu trúc hiện có của file đó.
- **Luôn ghi log các file đã thay đổi vào `/home/worker/WORKs/R-Estate/DOC/MBA/NOTE-CHANGE.md`** sau khi hoàn tất 1 batch công việc: thêm mục mới theo ngày (`## Date - DD Mon YYYY`), liệt kê từng file đã update kèm số dòng trước→sau và tóm tắt ngắn gọn thay đổi chính (case study mới thêm, mục nào mở rộng).
  - *Lưu ý*: đường dẫn trên là của máy Linux cũ, không tồn tại trên máy macOS hiện tại. Nếu đường dẫn không có, KHÔNG tự đoán vị trí khác — hỏi người dùng muốn ghi log ở đâu (lần update thư mục `3-financial-management` ngày 2026-10-28 chưa ghi log vì lý do này).
- **File tích hợp (như file 11) vẫn phải được update** khi user yêu cầu "tất cả file còn lại": giữ cấu trúc theo chương nhưng vẫn áp dụng các rule khác (case từng bước, giải thích "tại sao", sửa heading, thêm case SME, thêm PHỤ LỤC cuối file).
- **Dữ liệu thực của công ty quốc tế** (Apple, Grab, AWS, LTCM, GE...) mà không kiểm chứng được nguồn: giữ nhưng ghi chú rõ "ước tính/minh họa"; số tự thiết kế cho phần định lượng phải gắn nhãn "giả định minh họa". Không bịa số liệu thật.
- **Khi giao nhiều agent ghi file cùng lúc**: kiểm tra lỗi ký tự điều khiển trong LaTeX (vd `\frac` bị mất `\f` thành form-feed, `\times` bị tab) bằng cách grep ký tự `\x0c`/tab trong công thức.

---

## Notes for Claude Sessions

**Token efficiency**:
- Mỗi file 300-400 lines → ~1,500-2,000 tokens
- Nếu cần overview: Đọc CLAUDE.md này (file này ~500 lines)
- Nếu cần specific topic: Reference exact file (@filename.md)
- Tránh scan toàn bộ @MBA/ (27 files = ~50K+ tokens)

**Best practices**:
1. Start với CLAUDE.md để hiểu context
2. Identify relevant category (Strategic/Marketing/Financial/Practical)
3. Reference specific files based on query
4. Cross-reference giữa theory (frameworks) và practice (tools guide)

**Common query patterns**:
- "Explain [concept]" → Read relevant framework file
- "How to [business task]" → Read practical guides + relevant frameworks
- "Compare [A vs B]" → Read both specific files
- "Case study [scenario]" → Combine multiple files (strategy + marketing + financial)

---

**Knowledge Base Version**: 2.5 ⬆️ (bổ sung quy ước PHỤ LỤC trailing section, case SME bắt buộc, verify Python, log NOTE-CHANGE.md, ngoại lệ file tích hợp)  
**Total Files**: 33 (27 frameworks + 2 guides + 3 case studies + 2 templates)
**Total Lines**: ~15,700+ lines across all files  
**Language**: Vietnamese (with English technical terms)  
**Audience**: SME owners, Startup founders, MBA students  
**Last Updated**: 2026-10-28 (Bổ sung lưu ý đường dẫn NOTE-CHANGE, file tích hợp, dữ liệu quốc tế chưa kiểm chứng, lỗi LaTeX; trước đó 2026-10-20: Thêm mục "Yêu cầu & Phong cách khi Review/Update File" — đúc kết từ lần update file 05-financial-statement-analysis.md: ưu tiên case study chi tiết từng bước thay vì tóm tắt, giải thích "tại sao" đằng sau công thức, tái cấu trúc đúng chuẩn I-VI, không tạo file phụ lục riêng)
**Maintenance**: Review quarterly for tool updates

---

*This MBA knowledge base bridges theory and practice for real-world SME success.* 🎯📊💼
