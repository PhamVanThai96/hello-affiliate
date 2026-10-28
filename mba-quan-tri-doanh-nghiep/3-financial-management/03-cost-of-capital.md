# Cost of Capital – Chi Phí Sử Dụng Vốn (WACC)

> **Mục tiêu**: Hiểu bản chất "giá của tiền" mà doanh nghiệp phải trả cho chủ nợ và cổ đông; biết cách tính WACC, Cost of Equity (CAPM), Cost of Debt từng bước; và biết dùng chúng làm discount rate / hurdle rate trong capital budgeting và định giá doanh nghiệp — đặc biệt cho SME Việt Nam không có dữ liệu thị trường.

---

## I. KHÁI NIỆM & LÝ THUYẾT

### 1. Định nghĩa

**Cost of Capital** (Chi phí sử dụng vốn) là **tỷ suất lợi nhuận tối thiểu** mà doanh nghiệp phải đạt được trên vốn đầu tư để **duy trì giá trị DN** và **thỏa mãn nhà đầu tư** (cả chủ nợ lẫn cổ đông).

> **Nói đơn giản**: Cost of Capital = "Giá thuê tiền". DN vay phải trả lãi (Cost of Debt), huy động cổ đông phải tạo return (Cost of Equity). **WACC = giá trung bình có trọng số của tất cả nguồn vốn.**

**Tại sao khái niệm này tồn tại?** Vấn đề của kế toán truyền thống: Báo cáo kết quả kinh doanh chỉ trừ chi phí lãi vay, còn vốn chủ sở hữu thì "miễn phí" — một quán cà phê lãi kế toán 50 triệu/năm trên 1 tỷ vốn chủ trông có vẻ "có lãi", nhưng chủ quán có thể gửi 1 tỷ đó vào ngân hàng và nhận 60-70 triệu/năm gần như không rủi ro. Nghĩa là về mặt **kinh tế** quán đang lỗ. Cost of Capital đưa **chi phí cơ hội (opportunity cost)** của MỌI nguồn vốn — kể cả vốn chủ — vào bài toán, để trả lời câu hỏi đúng: *"Đồng vốn này làm ra nhiều hơn mức nó có thể kiếm được ở nơi khác với cùng rủi ro hay không?"*

### 2. Bối cảnh lịch sử & nguồn gốc lý thuyết

Trước thập niên 1950, các nhà quản lý dùng "lãi suất ngân hàng" hay "cảm tính" làm tỷ lệ chiết khấu khi thẩm định dự án. Hai bước ngoặt đã đặt nền móng cho khái niệm hiện đại: (1) **Markowitz (1952)** chỉ ra rằng rủi ro của một khoản đầu tư phải được đo trong bối cảnh danh mục — phần rủi ro riêng lẻ có thể bị đa dạng hóa, chỉ phần rủi ro hệ thống mới đáng được "trả công"; (2) **Modigliani & Miller (1958)** chứng minh rằng chi phí vốn của doanh nghiệp được quyết định bởi **rủi ro của tài sản hoạt động**, không phải bởi cách doanh nghiệp chia nguồn vốn. Từ đó Sharpe và Lintner xây dựng CAPM để *định lượng* "phần thưởng cho rủi ro" — cho phép tính Cost of Equity bằng một công thức thay vì đoán.

| Học giả | Đóng góp | Năm |
|---------|----------|-----|
| **Harry Markowitz** | Lý thuyết danh mục đầu tư – rủi ro phải đo theo danh mục (Nobel 1990) | 1952 |
| **Modigliani & Miller** | M&M Proposition I & II – chi phí vốn gắn với rủi ro tài sản, tax shield (xem [04-capital-structure.md](04-capital-structure.md)) | 1958, 1963 |
| **William Sharpe** | CAPM – Capital Asset Pricing Model (Nobel 1990) | 1964 |
| **John Lintner / Jan Mossin** | Phát triển CAPM song song | 1965-66 |
| **Robert Hamada** | Phương trình Hamada – liên hệ Beta với đòn bẩy tài chính | 1972 |
| **Eugene Fama & Kenneth French** | 3-Factor Model → bổ sung/thay thế CAPM | 1993 |
| **Aswath Damodaran** | Chuẩn hóa thực hành ước lượng WACC, Country Risk Premium, dữ liệu Beta ngành công khai | 1990s-nay |

### 3. Vai trò của Cost of Capital

| Vai trò | Giải thích |
|---------|-----------|
| **Discount rate cho NPV** | WACC dùng làm r trong $NPV = \sum CF_t/(1+WACC)^t$ |
| **Hurdle rate** | Dự án phải có IRR > WACC (đã điều chỉnh rủi ro) mới được đầu tư |
| **DCF Valuation** | Enterprise Value = $\sum FCF_t/(1+WACC)^t$ |
| **Optimal capital structure** | Tối thiểu hóa WACC = tối đa hóa giá trị DN (xem [04-capital-structure.md](04-capital-structure.md)) |
| **Performance measurement** | EVA = NOPAT − (Vốn đầu tư × WACC). EVA > 0 = tạo giá trị |
| **Benchmark** | So sánh ROIC vs WACC → DN có thật sự tạo giá trị? |

### 4. Cấu trúc Cost of Capital

```
            ┌────────────────────────────────┐
            │            WACC                │
            │  (Weighted Average Cost        │
            │   of Capital)                  │
            └────────────┬───────────────────┘
                         │
           ┌─────────────┼──────────────┐
           │                            │
      ┌────▼──────┐             ┌──────▼──────┐
      │ Cost of   │             │  Cost of    │
      │ EQUITY    │             │  DEBT       │
      │ (Ke)      │             │  (Kd)       │
      │           │             │             │
      │ CAPM:     │             │ Kd × (1-T)  │
      │ Rf + β×   │             │ (after-tax) │
      │ (Rm - Rf) │             │             │
      └───────────┘             └─────────────┘
           ↑                         ↑
      Cổ đông yêu cầu          Chủ nợ yêu cầu
      return CAO HƠN            return THẤP HƠN
      (rủi ro cao hơn,         (ưu tiên thanh toán,
       residual claim)           tax deductible)
```

### 5. Ba nguyên tắc nền tảng khi ước lượng chi phí vốn

1. **Chi phí cơ hội, không phải chi phí kế toán**: Chi phí vốn là mức lợi nhuận nhà đầu tư có thể kiếm được ở khoản đầu tư thay thế *cùng mức rủi ro* — không phải số tiền đã chi trả trên sổ sách.
2. **Hướng tới tương lai và theo giá thị trường**: Nhà đầu tư quyết định hôm nay dựa trên kỳ vọng, nên dùng lãi suất hiện hành, giá thị trường (không dùng lãi suất khoản vay cũ, không dùng giá trị sổ sách).
3. **Nhất quán giữa dòng tiền và tỷ lệ chiết khấu**: Dòng tiền danh nghĩa (VNĐ, đã gồm lạm phát) ↔ tỷ lệ danh nghĩa VNĐ; dòng tiền sau thuế trước lãi vay (FCFF) ↔ WACC; dòng tiền cho cổ đông (FCFE) ↔ Ke. Trộn lẫn là nguồn gốc của hầu hết sai lầm định giá (xem mục II.F và II.H).

---

## II. CHI TIẾT TỪNG THÀNH PHẦN

### A. WACC – Weighted Average Cost of Capital

#### 1. Tại sao phải "bình quân gia quyền"?

Doanh nghiệp hiếm khi chỉ dùng một nguồn vốn. Mỗi đồng vốn đầu tư vào một dự án thực chất là hỗn hợp: một phần từ chủ nợ (giá rẻ, nhưng bắt buộc trả), một phần từ cổ đông (giá cao, nhưng linh hoạt). Dự án không "biết" tiền của nó đến từ nguồn nào — nó chỉ cần tạo ra đủ lợi nhuận để trả cho **tất cả** các bên cùng lúc. Vì vậy, tỷ lệ chiết khấu hợp lý là **giá trung bình của "giỏ" vốn**, trong đó nguồn nào chiếm tỷ trọng lớn thì ảnh hưởng nhiều hơn. Đây chính là logic của trung bình có trọng số.

#### 2. Công thức WACC

$$WACC = \frac{E}{V} \times K_e + \frac{D}{V} \times K_d \times (1 - T)$$

Trong đó:
- $E$ = Market value of Equity (vốn hóa thị trường)
- $D$ = Market value of Debt (giá trị thị trường nợ vay)
- $V$ = E + D = Total firm value
- $K_e$ = Cost of Equity (chi phí vốn cổ phần)
- $K_d$ = Cost of Debt (chi phí nợ vay trước thuế)
- $T$ = Corporate tax rate (thuế suất TNDN)
- $(1-T)$ = Tax shield factor (lãi vay được khấu trừ thuế nên chi phí thực tế thấp hơn)

**Tại sao chỉ Kd nhân với $(1-T)$ mà Ke thì không?** Lãi vay được tính vào chi phí trước khi tính thuế → mỗi 1 đồng lãi làm giảm $T$ đồng thuế phải nộp, nên chi phí thực của chủ nợ chỉ còn $(1-T)$ đồng. Cổ tức/lợi nhuận kỳ vọng của cổ đông chi trả từ lợi nhuận *sau thuế* → không có khoản "hoàn thuế" tương tự. Bởi vậy WACC là một công thức "sau thuế", khớp với FCFF (dòng tiền cũng đã tính thuế trên EBIT).

#### 3. Tại sao dùng Market Value (không dùng Book Value)?

| | Market Value | Book Value |
|-|-------------|-----------|
| Phản ánh | Kỳ vọng tương lai | Chi phí lịch sử |
| Relevant? | ✅ (đầu tư dựa trên tương lai) | ❌ (past ≠ future) |
| WACC chính xác? | ✅ | ❌ (có thể sai lệch lớn) |

Nhà đầu tư *hôm nay* đòi hỏi lợi suất trên **giá trị họ đang nắm giữ hôm nay** (giá thị trường), không phải số tiền đã góp từ nhiều năm trước. Một công ty có vốn chủ sổ sách 100 tỷ nhưng thị giá 600 tỷ: cổ đông yêu cầu lợi suất trên 600 tỷ, không phải 100 tỷ.

#### 4. Ví dụ tính WACC (Doanh nghiệp ABC)

- Market cap (E) = 600 tỷ VND; Market value Debt (D) = 400 tỷ VND → V = 1.000 tỷ
- Cost of Equity (Ke) = 14%; Cost of Debt (Kd) = 9% (trước thuế); Tax rate = 20%

$$WACC = \frac{600}{1000} \times 14\% + \frac{400}{1000} \times 9\% \times (1-0.20) = 0.6 \times 14\% + 0.4 \times 9\% \times 0.8$$

$$WACC = 8.4\% + 2.88\% = \mathbf{11.28\%}$$

**Diễn giải**: Cứ mỗi 100 đồng vốn, ABC phải tạo ra tối thiểu 11,28 đồng lợi nhuận hoạt động sau thuế để trả đủ cho cả chủ nợ lẫn cổ đông. Dự án nào có IRR < 11,28% (ở mức rủi ro tương đương DN) sẽ làm giảm giá trị.

#### 5. Vấn đề "vòng tròn" (circularity) và cách xử lý

Để có $E$ (giá trị thị trường vốn chủ) cần định giá DN, mà định giá DN lại cần WACC (cần $E$). Cách xử lý thực hành:
- Với DN niêm yết: dùng vốn hóa thị trường hiện tại.
- Với DN chưa niêm yết/SME: dùng **cơ cấu vốn mục tiêu (target capital structure)** — tỷ lệ D/V bình quân của ngành hoặc tỷ lệ DN dự định duy trì dài hạn — thay vì tỷ lệ hiện tại. Cách này cũng tránh được việc WACC "nhảy múa" chỉ vì một năm DN trả bớt nợ.

---

### B. Cost of Equity (Ke) – Chi phí vốn chủ sở hữu

#### 1. Tại sao Ke khó tính nhất?

Chủ nợ có hợp đồng ghi rõ lãi suất; còn cổ đông **không ghi** bất kỳ con số nào — họ chỉ "âm thầm" đòi hỏi mức lợi nhuận tương xứng với rủi ro. Ke là một đại lượng *không quan sát trực tiếp được*, phải ước lượng qua mô hình. Ba mô hình thông dụng nhất: CAPM (dựa trên rủi ro), Gordon/Dividend Growth (dựa trên cổ tức) và Build-up (cộng dồn các phần bù).

#### 2. CAPM – Capital Asset Pricing Model

**Vấn đề CAPM giải quyết**: Làm sao biến câu nói định tính "rủi ro cao thì phải được thưởng cao" thành con số? Sharpe (1964) lập luận: thị trường chỉ trả công cho **rủi ro hệ thống** (systematic risk — rủi ro không thể loại bỏ bằng đa dạng hóa, như lãi suất, lạm phát, suy thoái). Rủi ro riêng của từng công ty (một CEO bỏ đi, một nhà máy cháy) có thể bị triệt tiêu bằng cách nắm giữ nhiều cổ phiếu, nên thị trường không "trả thêm" cho nó. Mức nhạy cảm của một cổ phiếu với rủi ro hệ thống được đo bằng Beta (β).

$$K_e = R_f + \beta \times (R_m - R_f)$$

Trong đó:
- $R_f$ = Risk-free rate (lãi suất phi rủi ro – thường = Government Bond 10 năm)
- $\beta$ = Hệ số đo lường rủi ro hệ thống (systematic risk)
- $R_m$ = Expected market return (return kỳ vọng thị trường)
- $(R_m - R_f)$ = Market Risk Premium (MRP) – phần bù rủi ro thị trường

**Logic công thức** = "Phần thưởng cho thời gian" ($R_f$: chỉ để chờ đợi, không rủi ro) + "Phần thưởng cho rủi ro" ($\beta \times MRP$: mỗi đơn vị rủi ro hệ thống gánh thêm được trả MRP).

```
Ke = Rf + β × (Rm - Rf)
     │     │      │
     │     │      └── Market Risk Premium: Phần bù cổ đông
     │     │          yêu cầu vì đầu tư vào stocks > bonds
     │     │          (trung bình 5-7% cho thị trường phát triển,
     │     │           7-10% cho emerging markets như VN)
     │     │
     │     └── β: Mức biến động so với thị trường
     │         β = 1.0: biến động = thị trường
     │         β > 1.0: biến động CAO hơn (aggressive)
     │         β < 1.0: biến động THẤP hơn (defensive)
     │
     └── Risk-free rate: Return "zero risk"
         VN: Trái phiếu CP 10 năm (~3-4%)
         US: 10-year Treasury (~4-5% hiện tại)
```

**Ví dụ – Vinamilk (VNM)**: Rf = 3,5% (TPCP VN 10 năm); β = 0,75 (cổ phiếu phòng thủ – thực phẩm/đồ uống); MRP VN = 8%

$$K_e = 3.5\% + 0.75 \times 8\% = 3.5\% + 6\% = \mathbf{9.5\%}$$

**Ví dụ – FPT Corporation**: Rf = 3,5%; β = 1,3 (cổ phiếu công nghệ, biến động mạnh hơn); MRP = 8%

$$K_e = 3.5\% + 1.3 \times 8\% = 3.5\% + 10.4\% = \mathbf{13.9\%}$$

**Diễn giải**: Cùng thị trường, cùng Rf, nhưng cổ đông FPT đòi lợi suất cao hơn VNM 4,4 điểm % vì dòng tiền của FPT nhạy với chu kỳ kinh tế hơn. Đây là lý do một dự án công nghệ phải vượt "rào" cao hơn một dự án thực phẩm.

#### 3. Bảng Beta theo ngành (ước tính Việt Nam)

| Ngành | Beta | Ke (Rf=3,5%, MRP=8%) |
|-------|------|---------------------|
| Utilities (Điện) | 0,4-0,6 | 6,7% - 8,3% |
| F&B (Thực phẩm) | 0,6-0,8 | 8,3% - 9,9% |
| Banking | 0,8-1,1 | 9,9% - 12,3% |
| Real Estate | 1,1-1,5 | 12,3% - 15,5% |
| Technology | 1,2-1,6 | 13,1% - 16,3% |
| Startup (early) | 2,0-3,0 | 19,5% - 27,5% |

*(Ke = 3,5% + β × 8%; ví dụ β = 0,4 → 6,7%; β = 3,0 → 27,5%. Đây là khoảng ước tính minh họa, cần cập nhật theo dữ liệu Damodaran/dữ liệu thị trường mới nhất.)*

#### 4. Beta, đòn bẩy tài chính và phương trình Hamada

**Vấn đề cần giải quyết**: Beta quan sát được của một cổ phiếu gồm **hai lớp rủi ro**: (1) rủi ro kinh doanh (business risk) của tài sản và (2) rủi ro tài chính (financial risk) do công ty vay nợ. Nếu công ty so sánh (comparable) vay nhiều hơn công ty bạn, beta của họ sẽ cao hơn — dù ngành nghề giống hệt. Phải "lột" phần đòn bẩy ra (unlever) để thấy rủi ro kinh doanh thuần túy, rồi "đắp" lại (relever) theo cơ cấu vốn của chính bạn. **Robert Hamada (1972)** đưa ra công thức dựa trên khung M&M có thuế:

$$\beta_{Levered} = \beta_{Unlevered} \times \left[1 + (1-T) \times \frac{D}{E}\right]$$

$$\beta_{Unlevered} = \frac{\beta_{Levered}}{1 + (1-T) \times \frac{D}{E}}$$

**Logic**: D/E càng cao, phần vốn chủ càng gánh nhiều biến động (chủ nợ luôn được trả trước) → beta cổ phần tăng. Hệ số $(1-T)$ có mặt vì tax shield làm giảm bớt phần rủi ro tài chính. Công thức giả định beta của nợ ≈ 0 — đủ tốt cho DN ít vay, nhưng sẽ hơi quá khi nợ cao.

**Quy trình 4 bước (dùng nhiều nhất cho DN chưa niêm yết)**:
1. Lấy beta levered và D/E của 3-10 công ty niêm yết cùng ngành.
2. Unlever từng beta bằng Hamada → lấy trung bình (hoặc trung vị) = beta tài sản của ngành.
3. Relever bằng D/E *mục tiêu* của DN bạn.
4. Cắm vào CAPM.

(Ví dụ số đầy đủ ở case SME mục III.3, Bước 2.)

#### 5. Điều chỉnh cho thị trường mới nổi & DN nhỏ

CAPM gốc được xây dựng cho thị trường Mỹ lớn, thanh khoản cao. Khi áp dụng cho Việt Nam cần hai điều chỉnh:

**a) Country Risk Premium (CRP)** – phần bù rủi ro quốc gia:

$$K_e (VN) = R_f (local) + \beta \times MRP_{global} + Country\ Risk\ Premium$$

Hoặc quy đổi từ thị trường Mỹ:

$$K_e (VN) = R_f (US) + \beta \times MRP_{US} + Country\ Risk\ Premium_{VN}$$

Country Risk Premium VN ≈ 2-4% (Damodaran database, cập nhật hàng năm). **Lý do**: nhà đầu tư quốc tế đòi thêm phần bù cho rủi ro tỷ giá, chính sách, thanh khoản thị trường… mà beta không phản ánh hết.

**b) Size Premium / Company-specific Premium** – phần bù quy mô/rủi ro riêng: nghiên cứu thực nghiệm (Ibbotson, Banz 1981) cho thấy công ty nhỏ có lợi suất kỳ vọng cao hơn CAPM dự đoán (khó huy động vốn, phụ thuộc ít khách hàng, phụ thuộc chủ DN). SME thường cộng thêm 2-5%.

#### 6. Các phương pháp thay thế / bổ sung CAPM

| Phương pháp | Công thức | Khi nào dùng? |
|------------|-----------|---------------|
| **Fama-French 3-Factor** | Ke = Rf + β₁(Market) + β₂(SMB) + β₃(HML) | Academic, chính xác hơn; cần dữ liệu thị trường sâu |
| **Build-up Method** | Ke = Rf + ERP + Size Premium + Company Premium | Private company, không có β |
| **Dividend Growth (Gordon)** | Ke = D₁/P₀ + g | DN trả cổ tức ổn định |
| **Bond Yield + Premium** | Ke = Company Bond Yield + 3-5% | Không có dữ liệu thị trường cổ phiếu |

**Giải thích Fama-French**: Fama & French (1993) phát hiện CAPM một nhân tố (thị trường) không giải thích hết lợi suất; công ty **nhỏ (SMB – Small Minus Big)** và công ty **giá trị – giá cổ phiếu thấp so với giá trị sổ sách (HML – High Minus Low)** có lợi suất cao hơn đáng kể. Đây cũng chính là cơ sở lý thuyết của "size premium" ở trên.

**Ví dụ Gordon Growth Model**: Cổ phiếu trả cổ tức năm vừa rồi $D_0$ = 2.400đ, tăng trưởng đều g = 5%/năm, giá hiện tại $P_0$ = 36.000đ.

$$D_1 = 2.400 \times 1,05 = 2.520\text{đ} \Rightarrow K_e = \frac{D_1}{P_0} + g = \frac{2.520}{36.000} + 5\% = 7\% + 5\% = \mathbf{12\%}$$

**Logic**: Giá cổ phiếu = giá trị hiện tại của dòng cổ tức tăng trưởng đều: $P_0 = D_1/(K_e - g)$. Đảo công thức ra để tìm $K_e$ — chính là "lợi suất mà thị trường đang ngầm định".

**Trường hợp phát hành cổ phiếu mới (có chi phí phát hành F = 5%)**: số tiền thực nhận chỉ còn $P_0(1-F)$:

$$K_{e,new} = \frac{D_1}{P_0(1-F)} + g = \frac{2.520}{36.000 \times 0,95} + 5\% = 7,37\% + 5\% = \mathbf{12,37\%}$$

→ Vốn từ **lợi nhuận giữ lại** (retained earnings) có chi phí 12% (không có phí phát hành); vốn từ **phát hành mới** đắt hơn (12,37%). Lợi nhuận giữ lại KHÔNG miễn phí — đó là tiền của cổ đông, họ vẫn đòi lợi suất 12%.

---

### C. Cost of Debt (Kd) – Chi phí nợ vay

#### 1. Tại sao dùng chi phí SAU thuế?

Công ty vay 1.000 đồng với lãi 9% trả 90 đồng lãi/năm. Vì lãi vay được khấu trừ khỏi lợi nhuận chịu thuế, DN tiết kiệm $T \times 90$ thuế. Chi phí *thực sự* DN phải gánh chỉ là $90 \times (1-T)$. Đây là cùng một "lá chắn thuế" (tax shield) đã giải thích ở [04-capital-structure.md](04-capital-structure.md) mục II.C — ở đây ta chỉ dùng nó như một hệ số điều chỉnh chi phí.

$$K_d (after\text{-}tax) = K_d (before\text{-}tax) \times (1 - T)$$

**Ví dụ**: DN vay bank 9%/năm, thuế suất 20% → $K_d = 9\% \times 0,80 = \mathbf{7,2\%}$. Tax Shield: Nhà nước "trợ cấp" 1,8% (9% × 20%).

> **Điều kiện áp dụng**: Tax shield chỉ có giá trị khi DN *thực sự có lợi nhuận chịu thuế* để khấu trừ. Doanh nghiệp đang lỗ thì không được hưởng ngay → dùng Kd trước thuế hoặc ước tính theo kế hoạch lợi nhuận trong tương lai. Ngoài ra, ở Việt Nam, quy định hiện hành (Nghị định 132/2020/NĐ-CP) giới hạn chi phí lãi vay được khấu trừ ở mức 30% EBITDA — DN vay quá nhiều có thể không được khấu trừ hết (nên xác nhận với kế toán/tư vấn thuế theo văn bản mới nhất).

#### 2. Các cách xác định Kd (before-tax)

| Phương pháp | Mô tả | Khi nào dùng |
|------------|-------|--------------|
| **Yield to Maturity (YTM)** | Kd = YTM trái phiếu DN đang lưu hành | DN có trái phiếu niêm yết/giao dịch |
| **Current borrowing rate** | Lãi suất vay ngân hàng hiện tại cho khoản vay *mới* cùng kỳ hạn | SME – phương pháp thực tế nhất |
| **Credit rating + spread** | Rf + Credit Spread (theo rating S&P/Moody's) | DN lớn có xếp hạng tín nhiệm |
| **Interest expense / Total debt** | Ước lượng đơn giản (book value, nhìn lại quá khứ) | Chỉ để tham khảo nhanh |

**Ví dụ YTM**: Trái phiếu DN mệnh giá 1.000.000đ, lãi coupon 10%/năm (100.000đ), kỳ hạn còn 5 năm, giá thị trường hiện tại 950.000đ. YTM là lãi suất r thỏa mãn:

$$950 = \sum_{t=1}^{5}\frac{100}{(1+r)^t} + \frac{1000}{(1+r)^5} \Rightarrow r \approx \mathbf{11,37\%}$$

→ Dù coupon ghi 10%, thị trường đang đòi 11,37% từ DN này. **Kd phải là 11,37% (lãi suất thị trường hiện hành), không phải 10% (coupon lịch sử).** Đây là minh họa cho nguyên tắc "hướng tới tương lai" ở mục I.5.

#### 3. Tại sao Kd < Ke? (Gần như luôn luôn)

```
1. Priority: Chủ nợ được trả TRƯỚC cổ đông (khi phá sản)
   → Risk thấp hơn → Required return thấp hơn

2. Tax advantage: Lãi vay = tax deductible
   → After-tax cost thực sự thấp hơn stated rate

3. Contractual: Lãi suất CỐ ĐỊNH, biết trước
   → Ít uncertainty hơn equity return (residual)

Kết quả: Ke = 12-15% vs Kd(after-tax) = 5-8% (typical)
```

> **Lưu ý**: Không phải vì "nợ rẻ" mà DN nên vay thật nhiều. Nợ rẻ *một phần* vì chủ nợ gánh ít rủi ro hơn; nếu DN vay thêm, phần rủi ro đó dồn lên cổ đông → Ke tăng và Kd cũng tăng (cost of financial distress). Đó là lý do vì sao "WACC thấp hơn nhờ nợ" có giới hạn (U-shape, xem case Toys "R" Us).

---

### D. Project-Specific Discount Rate & Khi nào dùng WACC

#### 1. Vấn đề: một WACC cho mọi dự án?

WACC của DN phản ánh rủi ro **trung bình** của các hoạt động hiện có. Nhưng chi phí vốn là chi phí của **rủi ro của dự án**, không phải của người bỏ tiền ra. Dùng WACC công ty để chiết khấu cho dự án rủi ro hơn → quá lạc quan (chấp nhận dự án xấu); dùng cho dự án an toàn hơn → quá khắt khe (bỏ lỡ dự án tốt). Cơ chế "tự hại" này làm DN dần dịch chuyển về các hoạt động rủi ro nhất mà không hay biết.

$$r_{project} = R_f + \beta_{project} \times MRP \;(+\; \text{các premium nếu có})$$

- Dự án rủi ro cao hơn DN → β cao hơn → r cao hơn
- Dự án rủi ro thấp hơn → β thấp hơn → r thấp hơn

**Ví dụ**: WACC overall = 11%. Dự án R&D mới (β = 2,0) → r = 3,5% + 2,0 × 8% = **19,5%**

**Cách thực hành (đơn giản cho SME)**: lấy WACC công ty rồi cộng một "phần bù rủi ro dự án" theo bậc: dự án mở rộng cùng lĩnh vực +0%; sản phẩm/thị trường mới +2-3%; công nghệ chưa thử nghiệm +4-6%.

#### 2. Khi nào dùng WACC?

| Tình huống | Dùng WACC? | Lý do |
|-----------|-----------|-------|
| DCF valuation (whole firm) | ✅ | Discount FCF to firm → Enterprise Value |
| Capital budgeting (dự án tương tự rủi ro DN) | ✅ | Hurdle rate = WACC |
| Dự án rủi ro KHÁC DN | ❌ | Dùng project-specific cost of capital |
| Evaluating division performance | ⚠️ | Dùng divisional WACC (different β) |
| Leveraged buyout (LBO) | ❌ | Capital structure thay đổi liên tục → APV method |
| Startup valuation | ❌ | No debt, no β → VC method or build-up |

---

### E. Marginal Cost of Capital (MCC) – Chi phí vốn biên

**Vấn đề**: WACC giả định chi phí mỗi nguồn vốn không đổi theo quy mô. Thực tế khi DN huy động càng nhiều: hết vốn giữ lại phải phát hành cổ phiếu mới (có phí phát hành → đắt hơn); vay vượt hạn mức ngân hàng phải chịu lãi cao hơn. **Chi phí vốn của đồng vốn tăng thêm (biên)** mới là thứ cần so với IRR của dự án cuối cùng.

**Ví dụ**: Cơ cấu mục tiêu 60% vốn chủ / 40% nợ, T = 20%. Lợi nhuận giữ lại sẵn có 2.000 triệu (Ke = 15%); vốn chủ phát hành mới có Ke = 16%. Vay ngân hàng được 3.000 triệu đầu tiên với lãi 10%, phần vượt vay với 12%.

- Điểm gãy (break point) vì hết lợi nhuận giữ lại: $2.000 / 0,6 = 3.333$ triệu tổng vốn
- Điểm gãy vì vượt hạn mức vay giá rẻ: $3.000 / 0,4 = 7.500$ triệu tổng vốn

| Tổng vốn huy động | Phép tính MCC | MCC |
|-------------------|---------------|-----|
| 0 – 3.333 triệu | 0,6×15% + 0,4×10%×0,8 = 9% + 3,2% | **12,2%** |
| 3.333 – 7.500 triệu | 0,6×16% + 0,4×10%×0,8 = 9,6% + 3,2% | **12,8%** |
| > 7.500 triệu | 0,6×16% + 0,4×12%×0,8 = 9,6% + 3,84% | **13,44%** |

→ Biểu đồ MCC là đường bậc thang đi lên. Dự án thứ nhất có IRR 13% chỉ nên làm khi quy mô vốn còn nằm trong ngưỡng MCC ≤ 13%; khi huy động quá 7.500 triệu, dự án IRR 13% bị loại.

---

### F. WACC Sensitivity & Tính nhất quán Danh nghĩa – Thực – Ngoại tệ

#### 1. Độ nhạy của định giá theo WACC

$$\text{Enterprise Value} = \sum_{t=1}^{n} \frac{FCF_t}{(1+WACC)^t} + \frac{Terminal\ Value}{(1+WACC)^n}$$

Với DN có FCF năm sau = 700 tỷ, tăng trưởng dài hạn g = 4% (Gordon: $EV = FCF_1 / (WACC - g)$):

| WACC | Enterprise Value | % Change vs base (10%) |
|------|------------------|----------------------|
| 8% | 17.500 tỷ | +50% |
| 9% | 14.000 tỷ | +20% |
| **10%** | **11.667 tỷ** | Base |
| 11% | 10.000 tỷ | −14% |
| 12% | 8.750 tỷ | −25% |
| 13% | 7.778 tỷ | −33% |

→ **WACC thay đổi 1% → Valuation thay đổi 14-20%!** Cực kỳ nhạy, nhất là khi WACC gần g (mẫu số $WACC - g$ nhỏ). Vì vậy: luôn chạy sensitivity ±1-2% và trình bày *khoảng* giá trị, không chỉ một con số.

#### 2. Nguyên tắc nhất quán

- **Danh nghĩa vs Thực (Fisher)**: $(1+r_{nominal}) = (1+r_{real})(1+\pi)$. Dòng tiền VNĐ dự phóng *có* lạm phát → dùng WACC danh nghĩa. Nếu dòng tiền theo giá cố định (không lạm phát) → dùng WACC thực.
- **Ngoại tệ**: Ke tính bằng USD cho DN Việt Nam có dòng tiền VNĐ phải quy đổi theo chênh lệch lạm phát:

$$K_{VND} = (1 + K_{USD}) \times \frac{1 + \pi_{VN}}{1 + \pi_{US}} - 1$$

Ví dụ $K_{USD}$ = 10%, lạm phát VN 4,5%, Mỹ 2,0% → $K_{VND} = 1,10 \times 1,045/1,02 - 1 = \mathbf{12,70\%}$.

---

### G. ROIC vs WACC và EVA – Dùng chi phí vốn để đo hiệu quả

**Vấn đề**: Lợi nhuận kế toán không trừ chi phí vốn chủ → không cho biết DN có "tạo giá trị" hay chỉ "tạo doanh thu". Stern Stewart (thập niên 1980-90) phổ biến **EVA (Economic Value Added)** để khắc phục:

$$ROIC = \frac{NOPAT}{Invested\ Capital}$$

$$EVA = NOPAT - Invested\ Capital \times WACC = Invested\ Capital \times (ROIC - WACC)$$

- **ROIC > WACC** → DN tạo giá trị (mỗi đồng vốn thêm đáng giá hơn 1 đồng).
- **ROIC < WACC** → DN *phá hủy* giá trị dù lợi nhuận kế toán dương.

Ví dụ nhanh: NOPAT = 900, Invested Capital = 6.000, WACC = 12% → ROIC = 15%; EVA = 900 − 6.000 × 12% = **+180**. Case SME mục III.3 sẽ tính EVA đầy đủ hơn.

---

### H. Ưu/nhược điểm, Sai lầm phổ biến & Giới hạn của WACC

#### 1. Ưu điểm WACC/CAPM
1. **Widely accepted** – Chuẩn industry cho DCF, capital budgeting
2. **Intuitive** – "Giá trung bình của vốn" dễ hiểu
3. **Accounts for capital structure** – Phản ánh mix D/E
4. **Tax shield included** – (1−T) factor cho debt
5. **Objective (CAPM)** – Market data-driven, ít subjective
6. **Benchmark** – ROIC > WACC = value creation

#### 2. Nhược điểm
1. **CAPM assumptions unrealistic** – Perfect markets, rational investors, homogeneous expectations
2. **Beta unstable** – β thay đổi over time, khác theo estimation period
3. **MRP controversial** – Market Risk Premium: 5%? 7%? 10%? Experts disagree
4. **Static** – WACC = snapshot. Real capital structure/rates change
5. **Circular logic** – WACC needs E (market cap), but DCF produces E
6. **Emerging markets difficulty** – Rf, β, MRP hard to estimate in VN
7. **Single-rate limitation** – Dùng 1 WACC cho TẤT CẢ dự án → inaccurate

#### 3. Sai lầm phổ biến khi tính WACC

| Sai lầm | Hậu quả | Cách tránh |
|---------|---------|-----------|
| Dùng book value thay market value | WACC sai → valuation sai | Luôn dùng market value weights (hoặc target structure) |
| Dùng lãi vay của khoản tài trợ dự án làm discount rate | Quá lạc quan (bỏ qua chi phí vốn chủ) | Dùng WACC, không dùng lãi vay (xem case SME) |
| Dùng historical β thay forward β | Under/over-estimate risk | Adjust β cho changes in business |
| Ignore country risk (emerging markets) | Ke quá thấp | Thêm Country Risk Premium |
| Dùng risk-free rate ngắn hạn | Mismatch horizon | Dùng 10-year government bond |
| Constant WACC trong LBO/changing structure | Misleading valuation | APV method cho changing D/E |
| Quên unlever/relever β | Wrong β for target structure | Hamada equation |
| Dùng WACC cho dự án rủi ro khác DN | Chấp nhận sai/bỏ lỡ dự án | Project-specific rate |
| Trộn VNĐ và USD, danh nghĩa và thực | Sai hệ thống | Mục II.F.2 |

#### 4. Khi capital structure thay đổi: APV

Trong LBO hoặc DN chuyển đổi cơ cấu vốn mạnh, WACC không còn hằng số. Phương pháp **APV (Adjusted Present Value)** tách riêng: $APV = NPV_{\text{all-equity}} + PV(\text{Tax Shield}) - PV(\text{Distress Costs})$ — mỗi phần chiết khấu bằng tỷ lệ phù hợp. Chi tiết xem [04-capital-structure.md](04-capital-structure.md) và [10-corporate-valuation.md](10-corporate-valuation.md).

---

## III. CASE STUDIES THỰC TẾ

### 1. Case Study Thành công: Apple – Low WACC = Massive Value Creation

#### Bối cảnh

Apple là một trong những công ty có cơ cấu vốn "đặc biệt" nhất: giữ lượng nợ rất nhỏ so với vốn hóa, nhưng vẫn tạo ra ROIC vượt trội nhờ thương hiệu, hệ sinh thái và sức mạnh định giá. Số liệu dưới đây là ước tính minh họa (xấp xỉ thời điểm 2023, cần kiểm chứng khi dùng cho mục đích đầu tư).

#### Số liệu đầu vào

| Thông số | Giá trị | Ghi chú |
|----------|---------|---------|
| Market Cap (E) | ≈ $3.000B | Vốn hóa thị trường |
| Debt (D) | ≈ $110B | Giá trị nợ vay |
| Rf | 4,5% | Lãi suất TPCP Mỹ 10 năm |
| β | 1,2 | Cổ phiếu công nghệ lớn |
| MRP | 5% | Phần bù rủi ro thị trường Mỹ |
| Kd (trước thuế) | 3,5% | Lãi suất vay thấp do tín nhiệm cao |
| Thuế suất | 21% | Thuế TNDN liên bang Mỹ |

#### Diễn giải từng bước

**Bước 1 – Tỷ trọng vốn**: V = 3.000 + 110 = 3.110. E/V = 3.000/3.110 = **96,46%**; D/V = 110/3.110 = **3,54%**.

**Bước 2 – Cost of Equity (CAPM)**: Ke = 4,5% + 1,2 × 5% = 4,5% + 6% = **10,5%**.

**Bước 3 – Cost of Debt sau thuế**: Kd = 3,5% × (1 − 0,21) = 3,5% × 0,79 = **2,765%**.

**Bước 4 – WACC**:

$$WACC = 96,46\% \times 10,5\% + 3,54\% \times 2,765\% = 10,128\% + 0,098\% = \mathbf{10,23\%}$$

**Bước 5 – Phân rã đóng góp**: Nợ chỉ đóng góp 0,098 điểm % vào WACC, trong khi Ke đóng góp 10,128 điểm %. Nghĩa là **WACC của Apple gần như bằng Ke** — đòn bẩy tài chính không phải đòn bẩy giá trị của Apple; chất lượng hoạt động mới là yếu tố quyết định.

**Bước 6 – Độ nhạy theo Beta**: Nếu β = 1,0 → Ke = 9,5% → WACC ≈ 9,26%; nếu β = 1,4 → Ke = 11,5% → WACC ≈ 11,19%. Một thay đổi 0,2 trong Beta làm WACC dịch chuyển ~0,95 điểm %.

#### Value Creation (ROIC vs WACC)

- ROIC Apple ước tính ≈ **55-60%** (return on invested capital); WACC ≈ **10,23%**
- **Spread = ROIC − WACC ≈ 45-50 điểm %** → mức tạo giá trị cực lớn

Với mỗi **100 tỷ USD** vốn đầu tư đang vận hành (minh họa):

$$EVA = 100 \times (55\% - 10,23\%) \approx \$44,8B/\text{năm}$$

*(Lưu ý: số liệu ROIC và vốn đầu tư của Apple dao động theo cách tính — nên xem như thứ tự độ lớn minh họa, không phải số kiểm toán.)*

#### Bài học

1. **Low WACC** (do ít nợ, thương hiệu mạnh → β không cao) giúp dự án đạt NPV dương dễ hơn.
2. **ROIC ≫ WACC** = flywheel tạo giá trị: Điều quyết định giá trị không phải việc WACC thấp hơn 1 điểm, mà là chênh lệch ROIC − WACC rất lớn.
3. Apple giữ minimal debt → E/V ≈ 97% → WACC bị chi phối bởi Ke; tối ưu hóa WACC bằng đòn bẩy ở đây mang lại lợi ích nhỏ so với việc duy trì ROIC cao.
4. **Với SME**: đừng ám ảnh việc "giảm WACC bằng cách vay thêm" khi ROIC của mình còn thấp; ưu tiên nâng ROIC (giá bán, biên lợi nhuận, vòng quay vốn) trước.

---

### 2. Case Study Thất bại: Toys "R" Us – WACC không giảm sau LBO

#### Bối cảnh

- 2005: Leveraged Buyout bởi KKR, Bain Capital và Vornado Realty Trust, tổng giá trị thương vụ khoảng 6,6 tỷ USD, phần lớn được tài trợ bằng nợ.
- Sau LBO, tỷ lệ nợ trên tổng vốn tăng vọt; lãi vay hằng năm vào khoảng 400 triệu USD (con số thường được trích dẫn).
- 2017: nộp đơn phá sản Chapter 11; 2018: thanh lý, hàng chục nghìn lao động mất việc (con số thường được nêu là khoảng 30.000+).

*(Số liệu về cơ cấu vốn trong bảng dưới là ước tính minh họa để giải thích cơ chế, không phải số liệu kiểm toán của Toys "R" Us.)*

#### Số liệu minh họa: WACC trước và sau LBO

| | Before LBO | After LBO |
|-|-----------|-----------|
| D/V | 30% | 85% |
| E/V | 70% | 15% |
| D/E tương ứng | 0,43 | 5,67 |
| Kd (after-tax) | 4% | 7,5% (cao hơn do rủi ro) |
| Ke | 12% | 25% (rủi ro tài chính cực lớn) |
| **WACC** | **9,6%** | **10,1%** |

#### Diễn giải từng bước

**WACC trước LBO**: 0,30 × 4% + 0,70 × 12% = 1,2% + 8,4% = **9,6%**.

**WACC sau LBO**: 0,85 × 7,5% + 0,15 × 25% = 6,375% + 3,75% = **10,125% ≈ 10,1%**.

**Kỳ vọng ngây thơ (naive)**: Nếu cổ đông *vẫn* chỉ đòi Ke = 12% và Kd = 7,5% với cơ cấu 85/15 thì WACC = 0,85 × 7,5% + 0,15 × 12% = 6,375% + 1,8% = **8,175%** — tức giảm gần 1,4 điểm %. Đây là lý do nhiều người tin "càng vay nhiều WACC càng giảm".

**Thực tế**: Ke tăng từ 12% lên 25% (+13 điểm %) và Kd tăng từ 4% lên 7,5% (gần gấp đôi) → toàn bộ lợi ích từ tỷ trọng nợ rẻ bị **xóa sạch**, thậm chí WACC còn tăng nhẹ. Đây đúng là điều M&M Proposition II dự đoán: đòn bẩy làm tăng Ke tương ứng; chỉ có tax shield là lợi ích thuần, nhưng nó bị bù trừ khi xác suất kiệt quệ tài chính tăng.

**Nhưng WACC chỉ là một nửa câu chuyện**: dù WACC gần như không đổi (10,1% vs 9,6%), *mức độ dễ vỡ nợ* khác hoàn toàn. Với D/E = 5,67, chỉ cần EBIT giảm một chút là không đủ trả lãi. Chi phí kiệt quệ tài chính (khách hàng, nhà cung cấp, nhân tài, khả năng đầu tư lại cửa hàng) **không nằm trong công thức WACC** nhưng phá hủy giá trị thật.

#### Kết quả

- Lợi nhuận hoạt động không đủ trang trải chi phí lãi vay (~400 triệu USD/năm)
- Không còn dòng tiền để đầu tư nâng cấp cửa hàng, thương mại điện tử → vị thế cạnh tranh suy yếu trước Amazon, Walmart
- 2017: Chapter 11; 2018: thanh lý

#### Bài học

1. **Tax shield has limits** – Vượt mức đòn bẩy tối ưu, chi phí kiệt quệ > lợi ích thuế.
2. **WACC is U-shaped** – Giảm khi thêm nợ (tax shield) đến một điểm, rồi tăng khi rủi ro vỡ nợ dốc lên.
3. **Operating flexibility crushed** – Nợ cố định cao = mất năng lực đầu tư và ứng phó thay đổi thị trường.
4. **Cost of financial distress** không được phản ánh trong công thức WACC đơn giản — cần kết hợp stress test, Interest Coverage, DSCR (xem [04-capital-structure.md](04-capital-structure.md)).
5. **Với SME**: WACC "đẹp" trên giấy không có nghĩa là cơ cấu vốn an toàn.

---

### 3. Case Study SME: Công ty Nội thất "Tâm An" (Bình Dương) – Tính WACC khi không có dữ liệu thị trường

#### Bối cảnh doanh nghiệp

Công ty TNHH Nội thất **Tâm An** (Bình Dương) sản xuất bàn ghế gỗ cho thị trường nội địa và một phần xuất khẩu. DN **không niêm yết**, nên không có giá cổ phiếu, không có beta riêng. Chủ DN đang cân nhắc hai dự án:

- **Dự án A**: mua dây chuyền CNC, đầu tư **6.000 triệu đồng**, dự kiến tạo dòng tiền tự do (FCFF) sau thuế **1.800 triệu/năm** trong 5 năm, không có giá trị thanh lý. Cùng lĩnh vực với hoạt động hiện tại.
- **Dự án B**: mở dây chuyền xuất khẩu sang EU (chứng nhận FSC, sấy gỗ…), đầu tư **4.000 triệu đồng**, FCFF **1.200 triệu/năm** trong 5 năm. Rủi ro cao hơn (tỷ giá, tiêu chuẩn kỹ thuật, một vài khách lớn).

Ngân hàng đề nghị cho vay 100% vốn dự án A với lãi 10,5%/năm. Chủ DN hỏi: *"Lãi vay 10,5% mà dự án làm ra 15% thì rõ ràng có lời, hay phải dùng tỷ lệ nào để chiết khấu?"*

#### Số liệu đầu vào (giả định)

| Thông số | Giá trị | Nguồn / cách xác định |
|----------|---------|----------------------|
| Rf (TPCP VN 10 năm) | 3,2% | Tra HNX, Bộ Tài chính |
| MRP Việt Nam | 8% | Ước tính gồm cả phần bù quốc gia |
| β levered ngành nội thất niêm yết | 1,15 | Trung bình ngành tham khảo |
| D/E ngành (comparables) | 0,5 | Thị giá |
| Thuế suất TNDN | 20% | |
| Size/company premium | 3% | DN nhỏ, phụ thuộc chủ, ít khách lớn |
| Kd ngân hàng (vay mới, trung hạn) | 10,5% | Báo giá 3 ngân hàng |
| Cơ cấu vốn mục tiêu D/E | 0,6 | Vốn chủ thị giá ước tính 10.000 triệu, nợ 6.000 triệu |

#### Bước 1 – Xác định cơ cấu vốn mục tiêu (trọng số)

- $D/V = 0,6/(1+0,6) = \mathbf{37,5\%}$; $E/V = \mathbf{62,5\%}$ (Vốn chủ 10.000 + Nợ 6.000 = V 16.000 triệu).

**Tại sao dùng giá trị ước tính thị trường?** Dùng giá trị sổ sách vốn chủ 5.000 triệu sẽ cho trọng số 45,5%/54,5% và WACC chỉ khoảng 11,82% — thấp giả tạo vì đánh giá thấp giá trị phần vốn của cổ đông.

#### Bước 2 – Ước tính Beta bằng Hamada (unlever → relever)

*Unlever beta ngành* (D/E = 0,5; T = 20%):

$$\beta_U = \frac{1,15}{1 + 0,8 \times 0,5} = \frac{1,15}{1,4} = \mathbf{0,8214}$$

→ Rủi ro kinh doanh thuần của ngành nội thất (không kể vay nợ) tương ứng β ≈ 0,82.

*Relever theo D/E mục tiêu 0,6 của Tâm An*:

$$\beta_L = 0,8214 \times (1 + 0,8 \times 0,6) = 0,8214 \times 1,48 = \mathbf{1,2157}$$

→ Vì Tâm An vay nhiều hơn mức trung bình ngành (0,6 so với 0,5), beta cổ phần cao hơn ngành (1,2157 so với 1,15).

#### Bước 3 – Cost of Equity (CAPM + Size Premium)

$$K_e = 3,2\% + 1,2157 \times 8\% + 3\% = 3,2\% + 9,726\% + 3\% = \mathbf{15,93\%}$$

**Ý nghĩa**: Chủ DN (và nhà đầu tư nếu gọi vốn) đòi tối thiểu 15,93%/năm trên vốn chủ — cao hơn lãi vay ngân hàng 5,4 điểm % vì rủi ro cao hơn.

#### Bước 4 – Cost of Debt sau thuế

$$K_d(1-T) = 10,5\% \times (1 - 0,2) = \mathbf{8,4\%}$$

(Tax shield: mỗi 6.000 triệu vay → lãi 630 triệu/năm; thuế tiết kiệm 630 × 20% = 126 triệu; chi phí thực 504 triệu = 8,4%.)

#### Bước 5 – Tính WACC

$$WACC = 62,5\% \times 15,93\% + 37,5\% \times 8,4\% = 9,954\% + 3,15\% = \mathbf{13,10\%}$$

#### Bước 6 – Thẩm định Dự án A với WACC = 13,10%

Dòng tiền: −6.000 (t=0), +1.800 mỗi năm t=1..5.

| Năm | Dòng tiền | Hệ số chiết khấu (13,10%) | PV |
|-----|-----------|---------------------------|----|
| 1 | 1.800 | 1/1,1310¹ | 1.591,5 |
| 2 | 1.800 | 1/1,1310² | 1.407,1 |
| 3 | 1.800 | 1/1,1310³ | 1.244,1 |
| 4 | 1.800 | 1/1,1310⁴ | 1.099,9 |
| 5 | 1.800 | 1/1,1310⁵ | 972,5 |
| **Tổng PV dòng tiền vào** | | | **6.315,0** |

$$NPV_A = 6.315,0 - 6.000 = \mathbf{+315,0\ triệu}; \quad IRR_A = \mathbf{15,24\%}$$

**Kết luận**: IRR (15,24%) > WACC (13,10%) → NPV dương, **chấp nhận** dự án A.

#### Bước 7 – "Cái bẫy" khi chọn sai tỷ lệ chiết khấu

| Tỷ lệ chiết khấu dùng | Giá trị | NPV Dự án A | Quyết định | Đánh giá |
|-----------------------|---------|------------|-----------|----------|
| Lãi vay sau thuế | 8,4% | +1.111,7 | Chấp nhận | **Sai: bỏ qua chi phí vốn chủ** |
| Lãi vay trước thuế | 10,5% | +737,1 | Chấp nhận | Sai: bỏ qua chi phí vốn chủ |
| WACC đúng | 13,10% | +315,0 | Chấp nhận | **Đúng** |
| Chỉ Ke | 15,93% | −96,0 | Từ chối | Quá khắt khe (bỏ qua phần vốn vay rẻ) |

**Giải thích**: Dùng lãi vay (8,4% hoặc 10,5%) làm hurdle rate khiến NPV bị thổi phồng gấp 2,3-3,5 lần (1.111,7 và 737,1 so với 315,0). Dự án không "tài trợ 100% bằng vay" trong thực tế: ngân hàng chỉ cho vay vì DN còn có vốn chủ làm đệm, và cổ đông vẫn đòi lợi suất 15,93% trên phần vốn của họ. Dùng chỉ Ke thì ngược lại — bỏ qua lợi ích thực của vốn vay rẻ — từ chối một dự án đáng làm.

#### Bước 8 – Thẩm định Dự án B (rủi ro cao hơn) bằng project-specific rate

Dự án B đầu tư 4.000, FCFF 1.200/năm × 5 năm → IRR = **15,24%** (tình cờ bằng A).

- Nếu dùng WACC công ty 13,10%: NPV_B = **+210,0 triệu** → chấp nhận.
- Nhưng B rủi ro hơn (thị trường EU, tỷ giá, ít khách hàng) → cộng premium +3% → $r_B = 13,10\% + 3\% = \mathbf{16,10\%}$: NPV_B = **−80,3 triệu** → **từ chối**.

→ Cùng một IRR 15,24%, dự án A đáng làm (rủi ro bằng công ty), dự án B thì không (rủi ro cao hơn). Dùng một WACC cho mọi dự án sẽ dẫn đến quyết định sai.

#### Bước 9 – Phân tích độ nhạy

| Kịch bản | Ke | WACC | NPV Dự án A (triệu) |
|----------|----|------|----------------------|
| **Cơ sở** | 15,93% | 13,10% | +315,0 |
| MRP = 7% | 14,71% | 12,34% | +433,7 |
| MRP = 9% | 17,14% | 13,86% | +199,9 |
| Không size premium (0%) | 12,93% | 11,23% | +614,5 |
| Size premium 5% | 17,93% | 14,35% | +127,4 |
| Rf = 4,0% | 16,73% | 13,60% | +238,9 |
| Kd = 9,5% | 15,93% | 12,80% | +361,5 |
| Kd = 12% | 15,93% | 13,55% | +246,4 |

Thêm: WACC +2% (15,10%) → NPV ≈ +19,1; WACC +3% (16,10%) → NPV ≈ −120,5. **Điểm hòa vốn WACC của Dự án A = IRR = 15,24%** — còn "biên an toàn" khoảng 2,1 điểm % so với 13,10%.

**Nhận xét**: Size premium là giả định gây biến động lớn nhất (từ 0% đến 5% làm NPV thay đổi từ +614 đến +127). Chủ DN nên thảo luận kỹ giả định này, không chỉ lấy một con số.

#### Bước 10 – ROIC, WACC và EVA của Tâm An

Giả sử vốn đầu tư hoạt động (sổ sách) 11.000 triệu, NOPAT hiện tại 2.400 triệu:

$$ROIC = \frac{2.400}{11.000} = \mathbf{21,82\%}; \quad EVA = 2.400 - 11.000 \times 13,10\% = 2.400 - 1.441,4 = \mathbf{+958,6\ triệu}$$

→ Hoạt động hiện hữu tạo giá trị (ROIC 21,8% > WACC 13,1%); thêm dự án A (IRR 15,24% > 13,1%) tiếp tục tạo giá trị, nhưng thấp hơn hoạt động cốt lõi, nên không nên mở rộng đại trà.

#### Kết luận và Khuyến nghị

1. **WACC của Tâm An ≈ 13,10%**; dùng đây làm hurdle rate cho dự án cùng rủi ro.
2. **Dự án A**: Chấp nhận (NPV +315 triệu, IRR 15,24%, biên an toàn WACC ≈ 2,1 điểm %). Thương lượng lãi vay để giảm Kd: mỗi giảm 1 điểm % lãi vay tăng NPV khoảng +46 triệu.
3. **Dự án B**: Chưa chấp nhận ở điều kiện hiện tại. Cần cải thiện: bảo hiểm tỷ giá, hợp đồng dài hạn với khách hàng, nâng FCFF lên ≥ 1.250/năm (IRR 17%, NPV tại 16,1% ≈ +83 triệu).
4. **Không dùng lãi vay 10,5% làm tiêu chí quyết định**; luôn nhớ vốn chủ cũng có chi phí.
5. **Hành động tiếp theo**: cập nhật WACC mỗi năm (lãi suất, beta ngành, cơ cấu vốn), và chạy sensitivity trước mỗi quyết định đầu tư lớn.

---

## IV. ỨNG DỤNG CHO SME

### 1. Đặc thù ước lượng chi phí vốn của SME Việt Nam

| Thách thức | Biểu hiện | Cách xử lý thực tế |
|-----------|-----------|--------------------|
| Không có giá cổ phiếu → không có β riêng | Không thể chạy hồi quy beta | Beta ngành → unlever/relever (Hamada) |
| Không có giá trị thị trường vốn chủ | Không xác định E để tính trọng số | Dùng cơ cấu vốn mục tiêu / ước tính từ P/E, EV/EBITDA ngành |
| Vốn chủ thường là tiền chủ DN (và gia đình) | "Vốn miễn phí" trong tâm lý | Quy đổi chi phí cơ hội: Ke tối thiểu ≥ lãi suất kinh doanh thay thế + premium |
| Khó tiếp cận nhiều nguồn vốn | Chủ yếu vay ngân hàng có thế chấp | Kd = lãi suất vay mới thực tế, gồm phí và chi phí tài sản bảo đảm |
| Dòng tiền biến động theo mùa vụ/khách hàng | Rủi ro riêng cao | Thêm size/company-specific premium 2-5% |
| Thiếu dữ liệu lịch sử, báo cáo chưa kiểm toán | Khó thuyết phục ngân hàng/nhà đầu tư | Chuẩn hóa BCTC 2-3 năm, có dự phóng dòng tiền |

### 2. Cách tính "đủ tốt" cho SME – quy trình 6 bước

1. **Xác định Rf**: lãi suất TPCP 10 năm hiện hành (HNX).
2. **Chọn β ngành**: tra Damodaran (Emerging Markets) hoặc 3-5 công ty niêm yết cùng ngành; unlever/relever theo D/E mục tiêu.
3. **Ke = Rf + β × MRP + size premium** (MRP VN thường 7-9%; size premium 2-5%).
4. **Kd = lãi suất vay mới thực tế**; sau thuế = Kd × (1−T).
5. **Trọng số**: theo cơ cấu vốn mục tiêu (tránh dùng sổ sách).
6. **Sanity check**: WACC SME thường trong khoảng **11-18%**; nếu ra < 10% hoặc > 22%, kiểm tra lại giả định.

### 3. Hurdle rate nhanh cho các loại dự án SME (tham khảo, không thay thế tính toán)

| Loại dự án | Rủi ro | Hurdle rate gợi ý (so với WACC) |
|-----------|--------|-------------------------------|
| Thay thế/bảo trì thiết bị (cải thiện chi phí) | Thấp | WACC − 1% |
| Mở rộng công suất cùng ngành, cùng thị trường | Trung bình | WACC |
| Sản phẩm mới trong cùng lĩnh vực | Trung bình-cao | WACC + 2-3% |
| Thị trường mới (xuất khẩu, tỉnh khác) | Cao | WACC + 3-5% |
| Công nghệ/mô hình kinh doanh mới | Rất cao | WACC + 5-8% (hoặc VC method) |

### 4. Sai lầm thường gặp của chủ SME

1. **Lấy lãi suất ngân hàng làm hurdle rate** ("vay 10% thì dự án phải lời hơn 10%") → bỏ qua chi phí vốn chủ, chấp nhận dự án phá hủy giá trị (Bước 7, case III.3).
2. **Coi vốn chủ là miễn phí** ("tiền của mình không phải trả lãi") → chi phí cơ hội vẫn tồn tại.
3. **Chỉ so sánh với lãi tiết kiệm** (6-7%) → bỏ qua phần bù rủi ro kinh doanh.
4. **Dùng một WACC cho mọi dự án** → Bước 8.
5. **Không cập nhật** WACC khi lãi suất, cơ cấu vốn thay đổi.
6. **Chạy theo WACC thấp** bằng cách vay quá mức → rủi ro Toys "R" Us (case III.2).

---

## V. TOOLS & TEMPLATES

### 1. Nguồn dữ liệu và công cụ

| Nguồn/Công cụ | Công dụng | Ghi chú |
|----------------|-----------|---------|
| **HNX / Bộ Tài chính** | Lãi suất TPCP 10 năm (Rf) | Cập nhật theo phiên đấu thầu |
| **Damodaran Online (NYU Stern)** | Beta ngành, ERP/CRP theo quốc gia, spread tín dụng | Miễn phí, cập nhật hàng năm; dùng nhóm Emerging Markets |
| **HOSE/HNX, SSI, VNDirect, Vietstock, CafeF** | VN-Index, P/E, beta, vốn hóa các công ty niêm yết | Tính β comparable, rm dài hạn (10-20 năm) |
| **Ngân hàng thương mại** | Báo giá lãi vay thực tế (Kd) | So sánh tối thiểu 3 ngân hàng |
| **Excel / Google Sheets** | Mô hình WACC, CAPM, NPV, sensitivity | Xem cấu trúc dưới đây |
| **Bloomberg / Refinitiv / FiinPro** | Dữ liệu chuyên nghiệp, beta, spread | Trả phí, phù hợp DN lớn/quỹ |

### 2. Cấu trúc Excel/Google Sheets gợi ý

```
TAB 1 — INPUTS (vùng duy nhất nhập tay, ô màu xanh):
  Rf, MRP, Beta levered comps, D/E comps, T,
  Size premium, Kd (lãi vay mới), D/E mục tiêu

TAB 2 — BETA (Hamada):
  BetaU  = BetaL_comps / (1 + (1-T) * DE_comps)
  BetaL  = BetaU * (1 + (1-T) * DE_target)

TAB 3 — WACC:
  Ke     = Rf + BetaL*MRP + SizePremium
  Kd_at  = Kd * (1-T)
  Wd     = DE_target / (1 + DE_target) ; We = 1 - Wd
  WACC   = We*Ke + Wd*Kd_at

TAB 4 — PROJECT:
  Dòng tiền dự án (FCFF), r dự án = WACC + premium
  NPV  = NPV(r, CF1:CF5) + CF0 ; IRR = IRR(CF0:CF5)

TAB 5 — SENSITIVITY:
  Data Table 2 chiều: WACC (±3%) x Size premium / MRP → NPV
```

**Công thức Excel tham khảo**: `=NPV(WACC, B2:B6)+B1`, `=IRR(B1:B6)`, `=RATE(5,100,-950,1000)` (YTM trái phiếu trả coupon 10%, giá 950), `=SLOPE(ret_stock, ret_market)` (beta từ lợi suất cổ phiếu và VN-Index).

---

## VI. BÀI TẬP THỰC HÀNH

### Bài 1 (Cơ bản — Tính WACC)
DN có vốn chủ thị trường 8.000 triệu, nợ 2.000 triệu, Ke = 14%, Kd = 10% (trước thuế), T = 20%. Tính WACC.

*(Đáp số đã verify bằng Python: E/V = 80%, D/V = 20%, Kd sau thuế = 8%; WACC = 0,8×14% + 0,2×8% = **12,8%**)*

### Bài 2 (Cơ bản — CAPM và size premium)
Rf = 3,5%, MRP = 8%, β = 0,9. (a) Tính Ke theo CAPM. (b) Nếu DN nhỏ nên cộng size premium 2%, Ke bằng bao nhiêu? Giải thích tại sao cần premium này.

*(Đáp số: (a) 3,5% + 0,9×8% = **10,7%**; (b) **12,7%**)*

### Bài 3 (Trung bình — Hamada)
Công ty cùng ngành có β = 1,0, D/E = 0,25, T = 20%. DN của bạn có D/E mục tiêu = 0,5. Tính β phù hợp cho DN bạn.

*(Đáp số: β_U = 1,0/(1+0,8×0,25) = 0,8333; β_L = 0,8333×(1+0,8×0,5) = **1,1667**)*

### Bài 4 (Trung bình — Gordon Growth Model)
Cổ phiếu có $D_0$ = 1.800đ, g = 6%/năm, giá hiện tại 30.000đ. Ước tính Ke. Giải thích tại sao phương pháp này không dùng được cho DN không trả cổ tức.

*(Đáp số: D₁ = 1.908đ; Ke = 1.908/30.000 + 6% = 6,36% + 6% = **12,36%**)*

### Bài 5 (Trung bình — Marginal Cost of Capital)
Cơ cấu mục tiêu 50% vốn chủ / 50% nợ, T = 20%. Lợi nhuận giữ lại 1.500 triệu (Ke = 14%), vốn chủ mới Ke = 15%; nợ 1.000 triệu đầu tiên lãi 9%, phần vượt lãi 11%. Tìm các điểm gãy và MCC từng khoảng.

*(Đáp số đã verify bằng Python: điểm gãy do hết nợ rẻ = 1.000/0,5 = **2.000 triệu**; điểm gãy do hết lợi nhuận giữ lại = 1.500/0,5 = **3.000 triệu**. Khoảng 0-2.000: 0,5×14% + 0,5×9%×0,8 = **10,6%**; 2.000-3.000: 0,5×14% + 0,5×11%×0,8 = **11,4%**; trên 3.000: 0,5×15% + 0,5×11%×0,8 = **11,9%**.)*

### Bài 6 (Nâng cao — Mini Case: chuỗi trà sữa "Mây Xanh")
Chuỗi 5 cửa hàng, chưa niêm yết, muốn mở cửa hàng thứ 6: vốn đầu tư 1.200 triệu, FCFF 380 triệu/năm trong 5 năm. Dữ liệu: Rf = 3,3%, MRP = 8%, size premium 3%, β comparable = 1,1 với D/E = 0,4, D/E mục tiêu = 0,5, Kd = 11%, T = 20%.
(a) Tính β_U, β_L, Ke, WACC. (b) Tính NPV, IRR cửa hàng 6. (c) So sánh quyết định khi dùng WACC đúng vs chỉ dùng Ke vs chỉ dùng lãi vay 11%.

*(Đáp số đã verify bằng Python: β_U = 0,8333; β_L = 1,1667; Ke = 3,3% + 1,1667×8% + 3% = 15,63%; D/V = 33,3%; WACC = 13,36%. NPV@13,36% = **+125,0 triệu**; IRR = **17,57%**; NPV@Ke 15,63% = +54,9; NPV@11% = +204,4. Cả ba đều "chấp nhận", nhưng dùng lãi vay 11% làm NPV bị thổi phồng khoảng 1,6 lần so với WACC đúng.)*

### Bài 7 (Nâng cao — Tự áp dụng)
Tự chọn một doanh nghiệp hoặc ý tưởng kinh doanh của bạn: tính WACC bằng quy trình 6 bước (mục IV.2), chọn một dự án, tính NPV/IRR ở WACC và ở WACC + premium rủi ro, chạy sensitivity với MRP và size premium, rồi viết một đoạn khuyến nghị.

---

## PHỤ LỤC: CHECKLIST COST OF CAPITAL TỔNG HỢP

### Bảng công thức tổng hợp

| Công thức | Ý nghĩa |
|-----------|---------|
| $WACC = \frac{E}{V}K_e + \frac{D}{V}K_d(1-T)$ | Chi phí vốn bình quân gia quyền |
| $K_e = R_f + \beta(R_m - R_f)$ | CAPM – chi phí vốn chủ |
| $K_e = R_f + \beta \times MRP + CRP + Size$ | Mở rộng cho thị trường mới nổi/DN nhỏ |
| $K_e = D_1/P_0 + g$ | Gordon Growth |
| $K_{e,new} = D_1/[P_0(1-F)] + g$ | Chi phí vốn phát hành mới (có phí F) |
| $K_d^{after} = K_d(1-T)$ | Chi phí nợ sau thuế |
| $\beta_L = \beta_U[1+(1-T)D/E]$ | Hamada – relever beta |
| $\beta_U = \beta_L/[1+(1-T)D/E]$ | Hamada – unlever beta |
| $r_{project} = R_f + \beta_{project} \times MRP$ | Tỷ lệ chiết khấu theo dự án |
| $K_{VND} = (1+K_{USD})\frac{1+\pi_{VN}}{1+\pi_{US}} - 1$ | Quy đổi chi phí vốn USD → VND |
| $EVA = NOPAT - IC \times WACC$ | Giá trị kinh tế gia tăng |
| $EV = FCF_1/(WACC-g)$ | Enterprise Value (Gordon) |

### Checklist

```
WACC CALCULATION:
□ Xác định market value E và D? (không dùng book value; SME dùng target structure)
□ Tính E/V và D/V weights?
□ Cost of Equity qua CAPM? (Rf + β × MRP)
□ Rf = 10-year government bond?
□ β estimated correctly? (unlever comps → relever theo D/E mục tiêu)
□ Market Risk Premium source identified?
□ Country Risk Premium nếu emerging market?
□ Size/company premium cho DN nhỏ đã cân nhắc?
□ Cost of Debt = YTM or current borrowing rate (lãi vay MỚI)?
□ After-tax Kd = Kd × (1-T)? (DN có đủ lợi nhuận để hưởng tax shield?)

VALIDATION:
□ WACC reasonable (8-15% cho đa số DN lớn; 11-18% cho SME)?
□ Ke > Kd? (luôn phải đúng)
□ WACC < Ke? (must be true with debt)
□ Consistent with comparable company WACCs?
□ Sensitivity analysis on WACC? (±1-2%)
□ Dòng tiền và tỷ lệ chiết khấu nhất quán (danh nghĩa/thực, VNĐ/USD, FCFF/WACC)?

APPLICATION:
□ Dùng project-specific rate nếu rủi ro khác DN?
□ Không dùng lãi vay làm hurdle rate?
□ APV nếu capital structure thay đổi lớn?
□ ROIC > WACC? (company creating value?)
□ Cập nhật WACC định kỳ (hàng năm / khi lãi suất, cơ cấu vốn đổi)?
```

---

*Tài liệu tham khảo: Sharpe "Capital Asset Prices" 1964; Modigliani & Miller 1958; Damodaran "Investment Valuation" 4th Ed; Brealey, Myers & Allen "Principles of Corporate Finance" 14th Ed; CFA Level I & II – Corporate Issuers*
