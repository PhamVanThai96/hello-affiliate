# Risk and Return – Rủi Ro & Lợi Nhuận (CAPM, Beta)

> **Mục tiêu**: Hiểu mối quan hệ giữa rủi ro và lợi nhuận (Risk-Return), đa dạng hóa (Diversification), Đường biên hiệu quả (Efficient Frontier), mô hình CAPM, Beta và các thước đo hiệu suất điều chỉnh theo rủi ro (Sharpe, Treynor, Jensen's Alpha) – nền tảng cho mọi quyết định đầu tư và cho việc tính chi phí vốn chủ sở hữu (Ke) của doanh nghiệp, đặc biệt là SME Việt Nam.

---

## I. KHÁI NIỆM & LÝ THUYẾT

### 1. Định nghĩa

**Rủi ro (Risk)** trong tài chính là **sự không chắc chắn** về lợi nhuận tương lai: kết quả thực tế có thể lệch khỏi kỳ vọng, cả theo hướng xấu lẫn tốt. Rủi ro thường được đo bằng **phương sai (Variance)** hoặc **độ lệch chuẩn (Standard Deviation)** của tỷ suất sinh lời.

**Lợi nhuận (Return)** là **phần thưởng** nhà đầu tư nhận được khi chấp nhận rủi ro. Nó gồm hai phần: thu nhập định kỳ (cổ tức, lãi) và chênh lệch giá (lãi vốn - Capital Gain).

> **Nguyên lý cốt lõi**: **Rủi ro cao hơn → Lợi nhuận kỳ vọng cao hơn**. Không có "bữa trưa miễn phí" (No free lunch): muốn lợi nhuận kỳ vọng cao hơn thì phải chấp nhận khả năng thua lỗ lớn hơn. Nhưng chiều ngược lại **không** đúng: chịu rủi ro cao không đảm bảo lợi nhuận cao, nó chỉ đảm bảo **kết quả phân tán rộng hơn**.

**Tại sao đây là câu hỏi trung tâm của tài chính?** Mọi quyết định của doanh nghiệp đều là đặt cược vào tương lai: mở thêm chi nhánh, mua máy móc, giữ tiền gửi hay mua vàng, vay hay không vay. Nếu chỉ nhìn vào lợi nhuận kỳ vọng (ví dụ "dự án này lời 20%/năm") mà bỏ qua mức độ chắc chắn, ta sẽ so sánh những thứ không cùng loại: 10% **gần như chắc chắn** (tiền gửi tiết kiệm) hoàn toàn khác 10% **trung bình của một khoảng từ -40% đến +60%** (cổ phiếu nhỏ). Lý thuyết Risk-Return cung cấp ngôn ngữ chung (số liệu hóa) để so sánh hai thứ đó trên cùng một thang đo.

### 2. Bối cảnh lịch sử: Từ "đừng bỏ trứng vào một giỏ" đến Giải Nobel

Trước thập niên 1950, nhà đầu tư vẫn chọn cổ phiếu theo kiểu "chọn cổ phiếu tốt nhất" và có một lời khuyên dân gian: *đừng bỏ tất cả trứng vào một giỏ*. Nhưng chưa ai **định lượng** được: bao nhiêu giỏ là đủ? Chia tỷ lệ thế nào? Giỏ nào "tốt" khi đặt cạnh các giỏ khác?

- **Năm 1952**, Harry Markowitz (khi đó là nghiên cứu sinh Đại học Chicago) công bố bài báo "Portfolio Selection". Đột phá của ông: **rủi ro của một danh mục KHÔNG bằng trung bình rủi ro của từng tài sản**, mà phụ thuộc vào **mức độ các tài sản biến động cùng nhau (tương quan - Correlation)**. Đây là lần đầu tiên "đa dạng hóa" được biến thành một công thức toán học.
- **Năm 1964-1966**, William Sharpe (và độc lập John Lintner, Jan Mossin) đặt câu hỏi tiếp theo: *nếu mọi nhà đầu tư đều làm theo Markowitz, thì giá của từng tài sản sẽ hình thành thế nào?* Câu trả lời là **CAPM** – chỉ phần rủi ro **không thể đa dạng hóa** mới được thị trường trả công.
- **Năm 1990**, Markowitz, Sharpe và Merton Miller cùng nhận Giải Nobel Kinh tế vì nền tảng tài chính hiện đại này.

| Học giả | Đóng góp | Năm |
|---------|----------|-----|
| **Harry Markowitz** | Lý thuyết danh mục hiện đại (Modern Portfolio Theory - MPT), Đa dạng hóa | 1952 |
| **James Tobin** | Định lý tách biệt (Separation Theorem): kết hợp tài sản phi rủi ro với danh mục rủi ro tối ưu | 1958 |
| **William Sharpe** | CAPM (Capital Asset Pricing Model) | 1964 |
| **John Lintner / Jan Mossin** | CAPM (phát triển độc lập) | 1965-1966 |
| **Eugene Fama** | Giả thuyết thị trường hiệu quả (Efficient Market Hypothesis) | 1970 |
| **Stephen Ross** | APT (Arbitrage Pricing Theory) | 1976 |
| **Fama & French** | Mô hình 3 nhân tố (thị trường, quy mô, giá trị) | 1993 |

### 3. Các loại rủi ro: Hệ thống và Phi hệ thống

**Tại sao phải tách rủi ro làm hai loại?** Vì hai loại này khác nhau về bản chất kinh tế: một loại nhà đầu tư **tự loại bỏ được gần như miễn phí** (chỉ bằng cách đa dạng hóa), loại kia thì **không**. Thị trường sẽ không trả công cho thứ mà ai cũng có thể tự loại bỏ miễn phí. Đây chính là mấu chốt của toàn bộ CAPM.

```
┌──────────────────────────────────────────────────────────────┐
│                    TỔNG RỦI RO (TOTAL RISK)                   │
│              (Độ lệch chuẩn - Standard Deviation σ)           │
├──────────────────────────┬───────────────────────────────────┤
│                          │                                   │
│  RỦI RO HỆ THỐNG         │  RỦI RO PHI HỆ THỐNG              │
│  (Systematic / Market)   │  (Specific / Idiosyncratic)       │
│  β × biến động thị trường│  Sự kiện riêng của từng DN        │
│                          │                                   │
│  • Suy thoái kinh tế     │  • Scandal của CEO                │
│  • Lãi suất tăng/giảm    │  • Thu hồi sản phẩm               │
│  • Lạm phát              │  • Kiện tụng                      │
│  • Chiến tranh/Dịch bệnh │  • Đối thủ mới gia nhập           │
│  • Chính sách Nhà nước   │  • Báo cáo lợi nhuận thất vọng    │
│                          │                                   │
│  KHÔNG đa dạng hóa được! │  CÓ THỂ đa dạng hóa được!         │
│  → Được thị trường trả   │  → KHÔNG được trả công            │
│    công (có phần bù)     │    (không có phần bù)             │
│                          │                                   │
│  Đo bằng: BETA (β)       │  Loại bỏ bằng: ~20-30 cổ phiếu    │
│                          │                                   │
└──────────────────────────┴───────────────────────────────────┘
```

### 4. Biểu đồ Diversification (Đa dạng hóa)

```
Tổng rủi ro (σ)
  │
  │  ●
  │    ●
  │      ●  ← Rủi ro phi hệ thống (có thể đa dạng hóa)
  │        ●
  │          ●
  │            ●
  │              ●───●───●────●────●────── → tiến gần mức rủi ro thị trường
  │─────────────────────────────────────── ← Rủi ro hệ thống (β)
  │                                            (không thể loại bỏ)
  │
  └──┬────┬────┬────┬────┬────┬────┬────→ Số cổ phiếu trong danh mục
     1    5   10   15   20   25   30

Các nghiên cứu thực nghiệm trên thị trường Mỹ cho thấy phần lớn rủi ro phi hệ thống
được loại bỏ với khoảng 20-30 cổ phiếu (con số mang tính tham khảo, phụ thuộc thị trường,
giai đoạn và mức tương quan giữa các cổ phiếu).
```

**Lưu ý với thị trường Việt Nam**: thị trường chứng khoán Việt Nam có độ tập trung ngành cao (ngân hàng, bất động sản, chứng khoán chiếm tỷ trọng lớn) và các cổ phiếu thường biến động **cùng chiều khá mạnh** (tương quan cao), nên 20-30 mã cùng ngành **không** đạt hiệu quả đa dạng hóa như con số tham khảo trên. Quan trọng không phải là *số lượng*, mà là *tương quan thấp* giữa các tài sản.

---

## II. CHI TIẾT TỪNG THÀNH PHẦN

### A. Đo lường lợi nhuận (Return Measurement)

#### 1. Lợi nhuận một kỳ (Single Period Return)

$$R = \frac{P_1 - P_0 + D}{P_0} = \frac{\text{Lãi vốn} + \text{Thu nhập}}{\text{Giá ban đầu}}$$

Trong đó $P_0$ là giá mua, $P_1$ là giá cuối kỳ, $D$ là cổ tức/lãi nhận được trong kỳ.

**Tại sao lại chia cho giá ban đầu $P_0$?** Vì nhà đầu tư quan tâm *mỗi đồng bỏ ra* sinh lời bao nhiêu, không phải số tiền tuyệt đối. Lãi 10 triệu trên vốn 100 triệu (10%) rất khác lãi 10 triệu trên vốn 1 tỷ (1%). Chuẩn hóa theo vốn ban đầu giúp so sánh các khoản đầu tư có quy mô khác nhau.

#### 2. Lợi nhuận kỳ vọng của danh mục (Expected Return)

$$E(R_p) = \sum_{i=1}^{n} w_i \times E(R_i)$$

Trong đó $w_i$ là tỷ trọng (weight) của tài sản $i$ trong danh mục ($\sum w_i = 1$). Lợi nhuận kỳ vọng của danh mục **chính xác bằng trung bình có trọng số** của lợi nhuận kỳ vọng từng tài sản. (Khác với rủi ro - xem mục C.)

**Lợi nhuận kỳ vọng khi có nhiều kịch bản**: với các kịch bản $s$ có xác suất $p_s$:

$$E(R) = \sum_{s} p_s \times R_s$$

#### 3. Trung bình cộng (Arithmetic) vs Trung bình nhân (Geometric)

| | Arithmetic (cộng) | Geometric (nhân) |
|-|-----------|-----------|
| Công thức | $(R_1 + R_2 + ... + R_n) / n$ | $[(1+R_1)(1+R_2)...(1+R_n)]^{1/n} - 1$ |
| Dùng để | Ước lượng lợi nhuận **kỳ vọng** một kỳ tương lai | Đo lợi nhuận **thực tế đã đạt** trong quá khứ (tăng trưởng gộp) |
| Luôn | Cao hơn hoặc bằng | Thấp hơn hoặc bằng |

**Tại sao cần hai loại trung bình?** Vì lợi nhuận được *nhân gộp* (lãi mẹ đẻ lãi con), còn trung bình cộng coi các kỳ như độc lập và bỏ qua hiệu ứng gộp. Biến động càng lớn, khoảng cách giữa hai loại càng rộng - gọi là "volatility drag" (lực kéo của biến động).

**Ví dụ**: Năm 1: +50%, Năm 2: -50%
- Arithmetic: (50% + (-50%))/2 = **0%** ← gây hiểu lầm!
- Geometric: $[(1,5)(0,5)]^{1/2} - 1$ = **-13,4%** ← thực tế là lỗ
- Tiền thật: 100 → 150 → 75 (**mất 25%** sau hai năm, tức -13,4%/năm)

> **Bài học cho SME**: khi chủ doanh nghiệp nghe "quỹ này trung bình lời 15%/năm", phải hỏi đó là trung bình cộng hay nhân. Nếu quỹ biến động mạnh, con số nhân (CAGR - tốc độ tăng trưởng gộp hằng năm) mới là thứ tiền trong túi bạn thực sự tăng.

---

### B. Đo lường rủi ro (Risk Measurement)

#### 1. Phương sai và Độ lệch chuẩn (Variance & Standard Deviation)

$$\sigma^2 = \sum_{s=1}^{n} p_s \times [R_s - E(R)]^2 \qquad\qquad \sigma = \sqrt{\sigma^2}$$

**Tại sao lại bình phương độ lệch?** (1) Độ lệch dương và âm sẽ triệt tiêu nhau nếu cộng thẳng (tổng độ lệch quanh trung bình luôn bằng 0), bình phương loại bỏ dấu. (2) Bình phương **phạt nặng các sai lệch lớn** - đúng với trực giác rằng một khoản lỗ -40% đáng sợ hơn nhiều so với bốn khoản lỗ -10%. (3) Phương sai có tính chất toán học "đẹp" (cộng được với danh mục, xem mục C). Độ lệch chuẩn $\sigma$ là căn bậc hai của phương sai để trả về **cùng đơn vị với lợi nhuận** (phần trăm), dễ diễn giải hơn.

**Hạn chế**: σ coi biến động lên và xuống như nhau, trong khi nhà đầu tư chỉ "sợ" biến động xuống (xem mục H - Downside Deviation).

#### 2. Hệ số biến thiên (Coefficient of Variation - CV)

$$CV = \frac{\sigma}{E(R)}$$

**Tại sao cần CV?** σ chỉ cho biết *độ lớn* của rủi ro, nhưng khi so sánh hai khoản đầu tư có lợi nhuận kỳ vọng khác nhau thì phải hỏi: *mỗi 1% lợi nhuận kỳ vọng phải chịu bao nhiêu % rủi ro?* CV trả lời đúng câu hỏi này (rủi ro trên mỗi đơn vị lợi nhuận). CV càng thấp càng tốt.

| Khoản đầu tư | E(R) | σ | CV | Hiệu quả điều chỉnh rủi ro? |
|-----------|------|---|---|---------------------|
| Stock A | 15% | 25% | 1,67 | |
| Stock B | 12% | 15% | 1,25 | ✅ Ít rủi ro nhất trên mỗi đơn vị lợi nhuận |
| Stock C | 20% | 40% | 2,00 | |

> Lưu ý: CV bất ổn khi E(R) gần 0 hoặc âm (mẫu số nhỏ làm CV "nổ"), lúc đó dùng Sharpe Ratio (mục F).

#### 3. Hiệp phương sai và Hệ số tương quan (Covariance & Correlation)

$$Cov(R_A, R_B) = \sum_{s} p_s [R_{A,s} - E(R_A)][R_{B,s} - E(R_B)] \qquad\qquad \rho_{AB} = \frac{Cov(R_A, R_B)}{\sigma_A \sigma_B}$$

**Tại sao cần?** Để biết hai tài sản có "đi cùng nhau" không. $Cov > 0$: khi A vượt kỳ vọng thì B thường cũng vượt. Vì độ lớn của Cov phụ thuộc vào đơn vị, ta chuẩn hóa bằng cách chia cho $\sigma_A\sigma_B$ để được hệ số tương quan $\rho$ nằm trong khoảng $[-1, +1]$ - đây là "nguyên liệu" quyết định hiệu quả của đa dạng hóa.

---

### C. Lý thuyết danh mục hiện đại (Portfolio Theory - Markowitz, 1952)

#### 1. Rủi ro của danh mục hai tài sản

$$\sigma_p^2 = w_A^2\sigma_A^2 + w_B^2\sigma_B^2 + 2w_Aw_B\sigma_A\sigma_B\rho_{AB}$$

- $\rho_{AB}$ = Hệ số tương quan ($-1 \le \rho \le +1$)
- $\rho = +1$: Tương quan dương hoàn hảo (**không** có lợi ích đa dạng hóa)
- $\rho = 0$: Không tương quan (đa dạng hóa tốt)
- $\rho = -1$: Tương quan âm hoàn hảo (có thể loại bỏ **toàn bộ** rủi ro)

**Tại sao công thức có số hạng thứ ba?** Đây là điểm tinh tế nhất của Markowitz. Hai số hạng đầu là "rủi ro riêng" của từng tài sản, tính theo tỷ trọng. Số hạng thứ ba là **hiệu ứng tương tác**: nếu hai tài sản thường tăng giảm *cùng lúc* ($\rho$ dương), chúng cộng hưởng làm tăng rủi ro; nếu chúng bù trừ nhau ($\rho$ âm), rủi ro bị khử bớt. Chỉ khi $\rho = +1$ thì $\sigma_p = w_A\sigma_A + w_B\sigma_B$ (bằng trung bình có trọng số). Với mọi $\rho < 1$, **rủi ro danh mục nhỏ hơn trung bình rủi ro các thành phần** - "bữa trưa miễn phí" duy nhất trong tài chính.

Bảng minh họa (2 tài sản, mỗi tài sản $\sigma = 15\%$, tỷ trọng 50/50), kết quả đã kiểm chứng bằng Python:

| Tương quan $\rho$ | Rủi ro danh mục $\sigma_p$ | Giảm so với 15% |
|---|---|---|
| +1,0 | 15,00% | 0% (không lợi ích) |
| +0,8 | 14,23% | -5,1% |
| +0,5 | 12,99% | -13,4% |
| +0,2 | 11,62% | -22,5% |
| 0,0 | 10,61% | -29,3% |
| -0,5 | 7,50% | -50,0% |

#### 2. Ví dụ tính tay: sức mạnh của đa dạng hóa

Cổ phiếu A: E(R) = 12%, σ = 20%. Cổ phiếu B: E(R) = 8%, σ = 15%. $\rho$ = 0,3. Danh mục 50/50:

- $E(R_p) = 0{,}5(12\%) + 0{,}5(8\%) = 10\%$
- $\sigma_p^2 = 0{,}25(0{,}04) + 0{,}25(0{,}0225) + 2(0{,}25)(0{,}20)(0{,}15)(0{,}3) = 0{,}01 + 0{,}005625 + 0{,}0045 = 0{,}020125$
- $\sigma_p = \sqrt{0{,}020125} = 14{,}19\%$

→ σ danh mục = 14,19% < trung bình có trọng số của σ (17,5%) → **Đa dạng hóa đã giảm rủi ro** mà lợi nhuận kỳ vọng vẫn là trung bình có trọng số.

#### 3. Đường biên hiệu quả (Efficient Frontier)

```
E(Return)
  │              ╭── Đường biên hiệu quả
  │            ╱ │
  │          ╱   │
  │        ╱     │ ← Lợi nhuận cao nhất cho mỗi mức rủi ro
  │      ╱       │
  │    ●╱        │ ← Danh mục phương sai nhỏ nhất (Minimum Variance Portfolio - MVP)
  │   ╱│         │
  │  ╱  │        │
  │ ╱   ● ← Từng cổ phiếu riêng lẻ (nằm dưới đường biên = kém hiệu quả)
  │╱    │
  │     │
  └─────┼────────────────→ Rủi ro (σ)
        │
   Chỉ các danh mục NẰM TRÊN đường biên mới "hiệu quả"
   (lợi nhuận tối đa cho mức rủi ro đã cho)
```

**Tại sao có hình "viên đạn" cong?** Khi thay đổi tỷ trọng giữa các tài sản, ta tạo ra vô số danh mục, mỗi danh mục là một điểm (σ, E(R)). Do hiệu ứng đa dạng hóa, đường nối các tỷ trọng cong về phía trái (rủi ro giảm nhanh hơn lợi nhuận). Điểm trái nhất là MVP. Nhánh trên của MVP là **đường biên hiệu quả**: không ai nên chọn nhánh dưới vì luôn có danh mục cùng rủi ro mà lợi nhuận cao hơn.

**Danh mục phương sai nhỏ nhất (hai tài sản)**: tỷ trọng tài sản A để rủi ro cực tiểu:

$$w_A^{MVP} = \frac{\sigma_B^2 - Cov(A,B)}{\sigma_A^2 + \sigma_B^2 - 2\,Cov(A,B)}$$

---

### D. Mô hình định giá tài sản vốn (CAPM) – Sharpe (1964)

#### 1. Vấn đề CAPM giải quyết

Markowitz cho biết *cách xây dựng danh mục*, nhưng chưa trả lời câu hỏi thực dụng: **một tài sản cụ thể nên đòi hỏi mức lợi nhuận tối thiểu bao nhiêu?** Doanh nghiệp cần con số này để: (1) tính chi phí vốn chủ sở hữu Ke cho WACC; (2) quyết định có nên thực hiện một dự án (lợi nhuận kỳ vọng phải cao hơn lợi nhuận yêu cầu); (3) đánh giá cổ phiếu đang rẻ hay đắt.

**Logic của Sharpe**: nếu mọi nhà đầu tư đều đa dạng hóa tốt thì rủi ro phi hệ thống của từng tài sản đã bị triệt tiêu trong danh mục - nên thị trường **chỉ trả công cho phần rủi ro hệ thống** (Beta). Lợi nhuận yêu cầu = lãi suất phi rủi ro (bù cho giá trị thời gian của tiền) + Beta × phần bù rủi ro thị trường (bù cho rủi ro hệ thống).

#### 2. Công thức

$$E(R_i) = R_f + \beta_i \times [E(R_m) - R_f]$$

Trong đó:
- $E(R_i)$ = Lợi nhuận kỳ vọng (yêu cầu) của tài sản $i$
- $R_f$ = Lãi suất phi rủi ro (risk-free rate)
- $\beta_i$ = Beta của tài sản $i$ (thước đo rủi ro hệ thống)
- $E(R_m)$ = Lợi nhuận kỳ vọng của thị trường
- $[E(R_m) - R_f]$ = Phần bù rủi ro thị trường (Market Risk Premium - MRP)

#### 3. Beta (β) – Thước đo rủi ro hệ thống

$$\beta_i = \frac{Cov(R_i, R_m)}{Var(R_m)} = \frac{\rho_{i,m} \times \sigma_i}{\sigma_m}$$

**Tại sao Beta được định nghĩa như vậy?** Beta là **độ dốc** khi hồi quy lợi nhuận của tài sản $i$ theo lợi nhuận thị trường: nếu thị trường tăng thêm 1%, tài sản $i$ *trung bình* tăng thêm $\beta$%. Chia Cov cho Var của thị trường nghĩa là đo "mức nhạy với thị trường" trên một đơn vị biến động thị trường. Dạng thứ hai cho thấy Beta = (tương quan với thị trường) × (tỷ lệ biến động của tài sản so với thị trường): tài sản vừa biến động mạnh vừa đi cùng thị trường thì Beta cao.

| Giá trị β | Ý nghĩa | Ví dụ |
|---------|---------|---------|
| β = 0 | Không có rủi ro hệ thống | Tài sản phi rủi ro (tín phiếu, tiền gửi) |
| β = 0,5 | Biến động bằng một nửa thị trường | Điện nước, hàng tiêu dùng thiết yếu |
| β = 1,0 | Đi cùng thị trường | Quỹ chỉ số (S&P 500, VN30 ETF) |
| β = 1,5 | Biến động 1,5 lần thị trường | Công nghệ, tài chính |
| β = 2,0 | Biến động 2 lần thị trường | DN đòn bẩy cao, small-cap tăng trưởng |
| β < 0 | Đi NGƯỢC thị trường | Vàng (đôi khi), VIX |

#### 4. Đường thị trường chứng khoán (Security Market Line - SML)

```
E(Return)
  │                             ╱ SML
  │                           ╱
  │                 ●       ╱ ← Bị định giá thấp! (trên SML: lợi nhuận > mức hợp lý so với rủi ro)
  │               ╱       ╱
  │             ╱       ╱
  │           ╱   ●  ╱ ← Định giá hợp lý (nằm trên SML)
  │ E(Rm)──╱─────╱──────
  │       ╱    ╱
  │     ╱  ● ╱ ← Bị định giá cao! (dưới SML: lợi nhuận < mức hợp lý so với rủi ro)
  │   ╱   ╱
  │ Rf──╱─────────── (β=0: lãi suất phi rủi ro)
  │   ╱
  └──┼────┼────┼────┼────────→ Beta (β)
     0   0.5  1.0  1.5  2.0
```

#### 5. Ví dụ tính CAPM

**Giả định**: Rf = 4%, E(Rm) = 10%, MRP = 6%

| Cổ phiếu | β | E(R) = Rf + β × MRP | Diễn giải |
|-------|---|---------------------|----------------|
| Điện nước | 0,4 | 4% + 0,4×6% = **6,4%** | Rủi ro thấp, lợi nhuận thấp |
| Chỉ số thị trường | 1,0 | 4% + 1,0×6% = **10%** | Bằng lợi nhuận thị trường |
| Công nghệ | 1,5 | 4% + 1,5×6% = **13%** | Rủi ro cao, lợi nhuận cao |
| Startup | 2,5 | 4% + 2,5×6% = **19%** | Rủi ro/lợi nhuận rất cao |

---

### E. Đường thị trường vốn (CML) so với SML

**Tại sao có hai đường?** Hai đường trả lời hai câu hỏi khác nhau. **CML** (Capital Market Line) mô tả sự đánh đổi lợi nhuận - **tổng rủi ro** cho các danh mục *hiệu quả* (kết hợp tài sản phi rủi ro với danh mục thị trường, theo Định lý tách biệt của Tobin). **SML** mô tả lợi nhuận hợp lý của *bất kỳ* tài sản nào theo **rủi ro hệ thống (Beta)**, vì rủi ro riêng đã bị đa dạng hóa.

| | CML | SML |
|-|-----|-----|
| Trục X | Tổng rủi ro (σ) | Rủi ro hệ thống (β) |
| Trục Y | E(Return) | E(Return) |
| Áp dụng cho | Chỉ danh mục hiệu quả | MỌI tài sản và danh mục |
| Độ dốc | Sharpe Ratio của thị trường | Phần bù rủi ro thị trường (MRP) |
| Công thức | $E(R_p) = R_f + \frac{E(R_m)-R_f}{\sigma_m} \times \sigma_p$ | $E(R_i) = R_f + \beta_i \times MRP$ |

---

### F. Các thước đo hiệu suất điều chỉnh theo rủi ro (Performance Measures)

**Vấn đề giải quyết**: Quỹ A lời 14%, quỹ B lời 11% - quỹ A "tốt hơn"? Chưa chắc: nếu A chịu rủi ro gấp đôi thì lợi nhuận cao hơn là điều dễ hiểu, không phải do giỏi hơn. Cần một thước đo chia lợi nhuận *vượt trội* cho *rủi ro đã chịu*. Đây là lý do ra đời của ba thước đo kinh điển (đều thập niên 1960), mỗi cái dùng một loại "mẫu số rủi ro" khác nhau.

#### 1. Sharpe Ratio (Sharpe, 1966) - dùng tổng rủi ro

$$Sharpe = \frac{R_p - R_f}{\sigma_p}$$

→ Lợi nhuận vượt phi rủi ro **trên mỗi đơn vị tổng rủi ro**. Càng cao càng tốt. Tử số là "phần thưởng cho việc chấp nhận rủi ro" (loại bỏ phần lãi suất gửi ngân hàng ai cũng nhận được), mẫu số là rủi ro. Đây chính là độ dốc của đường nối $R_f$ với danh mục - nên danh mục có Sharpe cao nhất là điểm tiếp xúc trên đường biên hiệu quả.

#### 2. Treynor Ratio (Treynor, 1965) - dùng rủi ro hệ thống

$$Treynor = \frac{R_p - R_f}{\beta_p}$$

→ Lợi nhuận vượt phi rủi ro **trên mỗi đơn vị rủi ro hệ thống**. Phù hợp khi danh mục là *một phần* của danh mục lớn đã đa dạng hóa (rủi ro riêng không còn quan trọng).

#### 3. Jensen's Alpha (Jensen, 1968) - chênh lệch so với CAPM

$$\alpha = R_p - [R_f + \beta_p(R_m - R_f)]$$

→ $\alpha > 0$: danh mục thực tế sinh lời **cao hơn** mức CAPM dự đoán với rủi ro hệ thống đã chịu (kỹ năng của người quản lý, hoặc may mắn). $\alpha < 0$: kém hơn mức hợp lý.

#### 4. So sánh

| Thước đo | Rủi ro sử dụng | Phù hợp nhất để |
|---------|----------|----------|
| **Sharpe** | Tổng σ | So sánh các danh mục chưa đa dạng hóa / toàn bộ tài sản của nhà đầu tư |
| **Treynor** | Hệ thống β | So sánh các danh mục đã đa dạng hóa tốt |
| **Jensen's Alpha** | Hệ thống β | Đánh giá kỹ năng của nhà quản lý |
| **Information Ratio** | Sai lệch so với chuẩn (Tracking error) | Nhà quản lý chủ động so với chỉ số chuẩn |

---

### G. Lưu ý phương pháp: Vấn đề khi ước lượng Beta

**Tại sao phải quan tâm?** CAPM đẹp về lý thuyết nhưng Beta không "có sẵn": nó phải được **ước lượng** từ dữ liệu lịch sử, và kết quả nhạy với cách làm. Hai người ước lượng Beta cho cùng một công ty có thể ra hai con số khá khác nhau, dẫn đến Ke chênh nhau vài điểm phần trăm và có thể đảo ngược quyết định đầu tư.

| Vấn đề | Hệ quả | Cách xử lý |
|-------|---------|---------|
| **Khoảng thời gian** | 2 năm vs 5 năm cho Beta khác nhau | Dùng dữ liệu tuần/tháng 3-5 năm |
| **Chỉ số đại diện thị trường** | S&P 500? MSCI World? VN-Index? | Chọn chỉ số đúng thị trường mà doanh nghiệp hoạt động |
| **Hồi quy về trung bình** | Beta có xu hướng tiến dần về 1,0 | Adjusted β = 2/3 × (raw β) + 1/3 × 1,0 (Blume) |
| **Thay đổi hoạt động kinh doanh** | DN đổi ngành → Beta đổi | Dùng Beta ngành/DN tương đồng (peer β) |
| **Hiệu ứng đòn bẩy** | D/E thay đổi → Beta thay đổi | Tách/gộp đòn bẩy (Hamada): $\beta_L = \beta_U[1+(1-T)D/E]$ |
| **Thanh khoản thấp** (thị trường nhỏ như VN) | Cổ phiếu ít giao dịch → Beta bị lệch thấp | Dùng dữ liệu tuần/tháng, so sánh với Beta ngành quốc tế |

---

### H. Các thước đo rủi ro ngoài σ và β

| Thước đo | Định nghĩa | Phù hợp hơn cho |
|---------|-----------|-----------|
| **VaR** (Value at Risk) | Mức lỗ tối đa ở một mức tin cậy x% trong một kỳ | Ngân hàng, quy định giám sát |
| **CVaR** (Conditional VaR) | Mức lỗ kỳ vọng **khi đã vượt VaR** | Rủi ro đuôi (tail risk) |
| **Max Drawdown** | Mức sụt giảm lớn nhất từ đỉnh xuống đáy | Đánh giá quỹ, chịu đựng tâm lý |
| **Downside Deviation** | σ chỉ của các lợi nhuận âm | Sortino Ratio |
| **Skewness** (Độ lệch) | Tính bất đối xứng của lợi nhuận | Ưa thích độ lệch dương |
| **Kurtosis** (Độ nhọn) | Đuôi dày (leptokurtic) | Đánh giá rủi ro đuôi |

**Tại sao cần các thước đo này?** σ giả định lợi nhuận phân phối chuẩn (hình chuông đối xứng). Thực tế thị trường có **đuôi dày** (sự kiện cực đoan xảy ra nhiều hơn dự báo của phân phối chuẩn) và nhà đầu tư không lo ngại biến động *tăng*. Case LTCM ở mục III.2 là minh chứng đắt giá cho giới hạn của σ và VaR.

---

### I. Ưu điểm và nhược điểm của CAPM/MPT

#### ✅ Ưu điểm
1. **Đơn giản và trực quan** - quan hệ tuyến tính, dễ tính
2. **Được sử dụng rộng rãi** - tiêu chuẩn để tính Ke, đánh giá hiệu suất
3. **Tập trung vào rủi ro hệ thống** - chỉ trả công cho rủi ro không đa dạng hóa được (có logic kinh tế)
4. **Chuẩn so sánh** - SML cho mức lợi nhuận hợp lý ứng với rủi ro
5. **Hướng dẫn xây dựng danh mục** - Efficient Frontier chỉ ra phân bổ tối ưu
6. **Có bằng chứng thực nghiệm (một phần)** - Beta cao hơn → lợi nhuận trung bình cao hơn (dài hạn)

#### ❌ Nhược điểm
1. **Chỉ một nhân tố** - Fama-French cho thấy quy mô, giá trị cũng quan trọng
2. **Beta không ổn định** - thay đổi theo thời gian và theo kỳ ước lượng
3. **Tính hướng tới tương lai (ex-ante) vs kiểm chứng bằng quá khứ (ex-post)** - CAPM nói về kỳ vọng nhưng kiểm định bằng dữ liệu lịch sử
4. **Giả định phi thực tế** - thị trường hoàn hảo, nhà đầu tư duy lý, kỳ vọng đồng nhất
5. **Danh mục thị trường không quan sát được** - "thị trường" thật gồm MỌI tài sản (cổ phiếu, trái phiếu, bất động sản, vốn nhân lực)
6. **Dị thường thực nghiệm** - cổ phiếu Beta thấp thường vượt trội (Betting Against Beta)
7. **Ước lượng MRP** - 5%? 7%? 10%? Tranh cãi lớn, ảnh hưởng mọi phép tính
8. **Mô hình một kỳ** - tĩnh, không phản ánh rủi ro động

#### Các mô hình thay thế CAPM

| Mô hình | Nhân tố | Cải tiến |
|-------|---------|-------------|
| **Fama-French 3 nhân tố** | Thị trường + SMB (quy mô) + HML (giá trị) | Giải thích phần bù quy mô và giá trị |
| **Carhart 4 nhân tố** | + Momentum (WML) | Giải thích hiệu ứng quán tính |
| **Fama-French 5 nhân tố** | + RMW (khả năng sinh lời) + CMA (đầu tư) | Toàn diện hơn |
| **APT** | Nhiều nhân tố vĩ mô | Linh hoạt, ít giả định hơn |
| **Black-Litterman** | Cân bằng thị trường + quan điểm nhà đầu tư | Tối ưu danh mục tốt hơn |

---

## III. CASE STUDIES THỰC TẾ

### 1. Case Study Thành công: Yale Endowment – MPT & Đa dạng hóa trong thực tế

#### Bối cảnh
- Quỹ tài trợ Đại học Yale (Yale Endowment): Giám đốc đầu tư (CIO) David Swensen, nắm quyền từ năm 1985 đến 2021.
- Chiến lược: áp dụng MPT với mức đa dạng hóa **cực đoan** sang các tài sản thay thế (alternative assets), thay vì mô hình truyền thống "60% cổ phiếu / 40% trái phiếu".
- Kết quả theo tài liệu gốc: lợi nhuận bình quân khoảng 13,7%/năm (1985-2021) so với khoảng 9,9% của S&P 500.

> **Lưu ý kiểm chứng**: các con số Yale ở mục này lấy từ tài liệu gốc của knowledge base, mang tính minh họa về độ lớn; người dùng nên đối chiếu báo cáo thường niên chính thức của Yale Investments Office trước khi trích dẫn.

#### Bước 1: Hiểu bài toán mà Swensen đối mặt

Một quỹ tài trợ phải đáp ứng hai mục tiêu mâu thuẫn: (1) chi một phần ổn định mỗi năm cho trường (khoảng 4-5% tài sản), (2) bảo toàn giá trị thực của vốn vĩnh viễn (phải thắng lạm phát). Danh mục 60/40 truyền thống có hai nhược điểm: cổ phiếu và trái phiếu chỉ có hai nguồn lợi nhuận chính, và khi khủng hoảng, cổ phiếu giảm sâu kéo cả danh mục. Swensen áp dụng thẳng bài học của Markowitz: **thêm tài sản có lợi nhuận kỳ vọng cao mà tương quan thấp với cổ phiếu sẽ đẩy danh mục ra phía trái-trên của đường biên hiệu quả**.

#### Bước 2: Phân bổ tài sản (theo số liệu gốc)

| Loại tài sản | Yale | Quỹ tài trợ điển hình | Tương quan với S&P (minh họa) |
|-------------|----------------|-------------------|---------------------|
| Cổ phiếu Mỹ | 2,3% | 25% | 1,00 |
| Cổ phiếu nước ngoài | 11,4% | 20% | 0,85 |
| Vốn tư nhân (Private Equity) | 41,0% | 10% | 0,60 |
| Tài sản thực (Real Assets) | 9,8% | 5% | 0,30 |
| Hedge fund (Absolute Return) | 23,5% | 10% | 0,20 |
| Trái phiếu | 4,5% | 25% | -0,20 |
| Tiền mặt | 7,5% | 5% | 0,00 |
| **Tổng** | **100%** | **100%** | |

> Ghi chú biên tập: cột "điển hình" trong tài liệu gốc cộng thành 105%, đã điều chỉnh cổ phiếu Mỹ từ 30% xuống 25% để tổng bằng 100%.

**Cách đọc**: Yale chỉ giữ 2,3% cổ phiếu Mỹ niêm yết - gần như đảo ngược danh mục truyền thống. Gần 74% (41,0 + 23,5 + 9,8) nằm ở ba lớp tài sản có tương quan thấp với thị trường chứng khoán đại chúng.

#### Bước 3: Giải thích bằng toán - vì sao tương quan thấp lại quan trọng đến vậy

Dùng công thức hai tài sản với $\sigma_A = \sigma_B = 15\%$, tỷ trọng 50/50 (kết quả đã kiểm chứng ở bảng mục II.C): nếu hai lớp tài sản tương quan 0,8 (như cổ phiếu Mỹ và cổ phiếu nước ngoài) thì $\sigma_p = 14,23\%$ (chỉ giảm 5% so với 15%); nếu tương quan 0,2 (như cổ phiếu và hedge fund theo bảng trên) thì $\sigma_p = 11,62\%$ (giảm 22,5%); nếu tương quan 0 thì $\sigma_p = 10,61\%$. Nghĩa là chuyển từ tài sản "cùng họ" sang tài sản "khác họ" giúp **cắt thêm khoảng 2,6-3,6 điểm phần trăm rủi ro mà không hy sinh lợi nhuận kỳ vọng**. Swensen khai thác chính "bữa trưa miễn phí" này ở quy mô cả danh mục.

#### Bước 4: Hiệu suất (theo số liệu gốc)

| Chỉ tiêu | Yale | Danh mục 60/40 | Chênh lệch |
|-------------|------|----------------|-------------|
| Lợi nhuận bình quân 20 năm | 11,3% | 7,5% | +3,8%/năm |
| Khủng hoảng 2008 (năm tài chính 2009) | -24,6% | -22% | Tệ hơn chút (do kém thanh khoản) |
| 2009-2021 | +14,5%/năm | +11%/năm | +3,5%/năm |
| Rủi ro (σ) | 12% | 10% | Cao hơn nhẹ |
| Sharpe Ratio | 0,75 | 0,55 | Tốt hơn nhiều |

**Diễn giải Sharpe**: Sharpe 0,75 so với 0,55 nghĩa là với mỗi 1% rủi ro, Yale kiếm được 0,75% lợi nhuận vượt phi rủi ro so với 0,55% của danh mục 60/40, tức hiệu quả điều chỉnh theo rủi ro **cao hơn khoảng 36%** ($0{,}75/0{,}55 - 1 \approx 36{,}4\%$). Quan trọng: σ của Yale (12%) chỉ cao hơn 60/40 (10%) chút ít, nhưng lợi nhuận cao hơn rất nhiều - đó là dấu hiệu của đa dạng hóa hiệu quả chứ không phải đơn thuần "chịu rủi ro nhiều hơn".

**Điểm cần nhìn thẳng**: năm 2008-2009 Yale **lỗ nặng hơn** 60/40 (-24,6% so với -22%). Đa dạng hóa không bảo vệ tuyệt đối trong khủng hoảng vì tài sản kém thanh khoản (vốn tư nhân) không bán được để cơ cấu lại, và tương quan tăng lên trong khủng hoảng (xem case LTCM).

#### Bước 5: Vì sao chiến lược hoạt động (lập luận MPT)

1. **Tương quan thấp** - Vốn tư nhân, tài sản thực, hedge fund có $\rho$ thấp với thị trường đại chúng.
2. **Đẩy đường biên hiệu quả** - Thêm tài sản thay thế → lợi nhuận cao hơn cho cùng mức σ.
3. **Phần bù thiếu thanh khoản (Illiquidity premium)** - Chấp nhận khóa vốn nhiều năm → được bù thêm khoảng 3-5%/năm (ước tính phổ biến trong giới học thuật).
4. **Tái cân bằng kỷ luật (Rebalancing)** - Bán tài sản đã tăng mạnh, mua tài sản đã giảm: hành vi ngược số đông, tạo lợi nhuận bổ sung.

#### Bài học
1. **Đa dạng hóa hiệu quả** - đặc biệt với các tài sản thực sự không tương quan.
2. **Phần bù thiếu thanh khoản là có thật** - chấp nhận khóa vốn = lợi nhuận bổ sung; nhưng chỉ nhà đầu tư dài hạn (như quỹ vĩnh viễn) mới "đủ sức" khai thác.
3. **Đường biên hiệu quả đạt được nhưng đòi hỏi chuyên môn và khả năng tiếp cận** - kết quả của Yale phụ thuộc rất lớn vào việc chọn được nhà quản lý quỹ xuất sắc, khó sao chép đối với nhà đầu tư nhỏ.
4. **Tầm nhìn dài hạn** - quỹ tài trợ có thể làm điều nhà đầu tư cá nhân không làm được (khóa vốn 10 năm). SME thì thường **không** có "vốn vĩnh viễn" - nhu cầu thanh khoản của SME là ràng buộc cứng (xem mục IV).

---

### 2. Case Study Thất bại: Long-Term Capital Management (LTCM) – Khi mô hình sụp đổ

#### Bối cảnh
- 1994-1998: LTCM - quỹ phòng hộ (hedge fund) do John Meriwether sáng lập, có hai người sau đó đoạt Nobel Kinh tế (Robert Merton và Myron Scholes, giải năm 1997) là thành viên đối tác.
- Chiến lược: giao dịch chênh lệch giá định lượng (quantitative arbitrage), đặt cược vào việc các chênh lệch giá bất thường sẽ "hội tụ" về mức bình thường - được coi là gần như phi rủi ro.
- Đòn bẩy: khoảng 25:1 và cao hơn nữa nếu tính các vị thế phái sinh.
- Kết quả: mất khoảng 4,6 tỷ USD trong vài tháng, bị 14 ngân hàng cứu trợ dưới sự điều phối của Cục Dự trữ Liên bang New York để tránh làm lung lay hệ thống tài chính toàn cầu.

#### Bước 1: Hiểu "bất ngờ" bắt đầu từ đâu

LTCM mua các trái phiếu "rẻ" và bán khống các trái phiếu "đắt" tương tự, kỳ vọng chênh lệch (spread) thu hẹp. Mỗi giao dịch riêng lẻ kiếm rất ít (vài phần trăm của 1%), nên để có lợi nhuận đáng kể họ phải **dùng đòn bẩy rất lớn**. Mô hình rủi ro của họ dựa trên dữ liệu lịch sử với giả định các vị thế ở nhiều thị trường **ít tương quan nhau** (đa dạng hóa tốt) và lợi nhuận **phân phối chuẩn**.

#### Bước 2: Phép tính đòn bẩy - vì sao "một thay đổi nhỏ" đủ giết chết quỹ

Vốn chủ khoảng 4,7 tỷ USD, tổng tài sản khoảng 125 tỷ USD, tức đòn bẩy khoảng $125/4{,}7 \approx 26{,}6$ lần. Hệ quả toán học:

- Tài sản giảm giá chỉ $1/26{,}6 \approx 3{,}76\%$ là **mất toàn bộ vốn chủ**.
- Với đòn bẩy đúng 25:1: tài sản giảm 4% xóa sạch 100% vốn chủ ($1/25 = 4\%$). Ví dụ: vốn chủ 100 đồng, tài sản 2.500 đồng, giảm 4% = mất 100 đồng.
- LTCM đã mất khoảng 4,6 trên 4,7 tỷ USD, tức khoảng $4{,}6/4{,}7 \approx 97{,}9\%$ vốn chủ.

Đây chính là bài học tương tự phần đòn bẩy tài chính ở file Capital Structure: đòn bẩy cao khuếch đại cả lãi và lỗ.

#### Bước 3: Giả định của LTCM vs thực tế

| Giả định của LTCM | Thực tế |
|----------------|---------|
| **Tương quan ổn định** | Khi khủng hoảng, MỌI tương quan → 1,0 (mọi thứ cùng giảm!) |
| **Phân phối chuẩn** | Đuôi dày: các sự kiện "6 sigma" xảy ra nhiều lần |
| **Thị trường duy lý** | Bán tháo hoảng loạn, lây lan, vòng xoáy thanh khoản |
| **Dữ liệu quá khứ = tương lai** | Khủng hoảng Nga 1998 chưa có tiền lệ trong dữ liệu |
| **Đa dạng hóa hiệu quả** | Trong khủng hoảng, đa dạng hóa THẤT BẠI (mọi tài sản đồng loạt giảm) |
| **Đòn bẩy kiểm soát được** | 25:1 → biến động nhỏ = lỗ khổng lồ → margin call → buộc bán tháo |

#### Bước 4: Dòng thời gian sụp đổ (số liệu làm tròn, mang tính minh họa)

| Thời điểm | Sự kiện | Vốn chủ LTCM |
|------|-------|-------------|
| Đầu 1998 | Đỉnh | ~4,7 tỷ USD |
| Tháng 5/1998 | Khủng hoảng Nga bắt đầu | ~4,0 tỷ USD |
| Tháng 8/1998 | Nga vỡ nợ (tuyên bố không trả nợ nội tệ) | ~2,3 tỷ USD |
| Tháng 9/1998 | Tương quan tăng vọt lên gần 1,0 | ~0,6 tỷ USD |
| 23/9/1998 | Các ngân hàng cứu trợ do Fed New York điều phối | ~0,4 tỷ USD (thoát khỏi phá sản) |
| Tổng thiệt hại | | **khoảng -4,6 tỷ USD trong khoảng 5 tháng** |

#### Bước 5: Phân tích - mô hình sai ở đâu (liên hệ từng khái niệm trong bài)

```
1. TƯƠNG QUAN KHÔNG HẰNG SỐ:
   Thời bình: ρ = 0,3 (đa dạng hóa hiệu quả)
   Khủng hoảng: ρ → 1,0 (MỌI THỨ cùng giảm!)
   → Mô hình dùng ρ lịch sử THẤT BẠI khi khủng hoảng.
   (Quay lại công thức Markowitz: khi ρ → 1 thì σ_p → trung bình có trọng số σ,
    lợi ích đa dạng hóa BIẾN MẤT đúng lúc cần nhất.)

2. ĐUÔI DÀY GIẾT NGƯỜI:
   Phân phối chuẩn: sự kiện lệch 4σ về một phía có xác suất ≈ 3,17×10⁻⁵ mỗi ngày
   (≈ 1 lần trong 31.574 ngày giao dịch, tức khoảng 125 năm giao dịch; với 5σ-6σ
   còn hiếm hơn nhiều bậc).
   Thực tế: các cú sốc cỡ này xảy ra nhiều lần trong vài thập kỷ.
   → VaR và mô hình Gauss ĐÁNH GIÁ THẤP rủi ro đuôi.

3. ĐÒN BẨY KHUẾCH ĐẠI MỌI THỨ:
   25:1: lỗ 4% tài sản → mất 100% vốn chủ.
   Sự kiện "bất khả thi" xảy ra → quỹ bị hủy diệt ngay lập tức.

4. RỦI RO THANH KHOẢN ≠ RỦI RO THỊ TRƯỜNG:
   Có thể "đúng" về giá trị nhưng không sống nổi qua các lệnh gọi ký quỹ.
   → "Thị trường có thể phi lý lâu hơn thời gian bạn có thể trụ vững" – Keynes (câu nói được quy cho ông)

5. RỦI RO MÔ HÌNH:
   Người đoạt Nobel với mô hình tốt nhất vẫn thất bại
   → Mô hình là bản đồ, không phải lãnh thổ.

6. RỦI RO HỆ THỐNG:
   Quản trị rủi ro của từng tổ chức ≠ ổn định của hệ thống.
   Khi mọi người dùng cùng mô hình → giao dịch đông đúc → cùng thoát một lúc.
```

#### Bài học
1. **Đừng tin tuyệt đối vào con số σ, β, ρ lịch sử** - chúng chỉ đúng trong "thời bình". Luôn chạy kịch bản xấu (stress test) với tương quan = 1.
2. **Đòn bẩy là nhân tử của sai lầm** - mọi mô hình rủi ro đều sai ở đâu đó; đòn bẩy quyết định sai lầm đó là "bài học" hay là "phá sản".
3. **Thanh khoản là rủi ro riêng** - cần dự trữ tiền mặt để không bị buộc bán tháo ở đáy.
4. **Với SME**: bài học trực tiếp nhất là "đừng đặt cược toàn bộ vốn lưu động hay vay ngân hàng để đầu tư tài chính", bởi kịch bản tồi tệ không cần là "6 sigma" mới xảy ra với một doanh nghiệp nhỏ.

---

### 3. Case Study SME: Phân bổ 2 tỷ đồng vốn nhàn rỗi của Công ty "Nội thất Gỗ Việt" (Bình Dương)

#### Bối cảnh doanh nghiệp

Công ty TNHH Nội thất Gỗ Việt là SME sản xuất đồ gỗ nội thất xuất khẩu tại Bình Dương, hoạt động 9 năm. Cuối năm, nhờ thu được khoản tiền từ đơn hàng lớn, công ty có **2.000 triệu đồng (2 tỷ VNĐ)** nhàn rỗi. Theo kế hoạch, số tiền này **chưa cần dùng trong 12 tháng tới**, nhưng chủ doanh nghiệp, ông Hòa, muốn tối ưu hơn là gửi ngân hàng. Công ty không vay nợ để đầu tư số tiền này.

Ông Hòa cân nhắc 3 kênh:
- **Tiết kiệm ngân hàng 12 tháng**: lãi suất giả định cho bài **6%/năm**, gần như phi rủi ro (dùng làm $R_f$).
- **Quỹ chỉ số cổ phiếu VN30 (ETF/quỹ mở)**: đại diện cho thị trường (β = 1 theo định nghĩa trong bài).
- **Vàng**: tài sản phòng thủ.

Phân tích 5 kịch bản kinh tế trong 12 tháng tới, do ông Hòa tham vấn một công ty chứng khoán (số liệu giả định cho bài học, không phải dự báo thị trường):

| Kịch bản | Xác suất | Lợi nhuận Quỹ cổ phiếu (E) | Lợi nhuận Vàng (G) |
|---|---|---|---|
| Tăng trưởng mạnh | 15% | +40% | -3% |
| Tăng trưởng khá | 30% | +22% | +10% |
| Đi ngang | 25% | +10% | +5% |
| Suy giảm nhẹ | 20% | -5% | +14% |
| Khủng hoảng | 10% | -25% | +8% |

Ngoài ra, ông Hòa muốn trả lời hai câu hỏi phụ: (1) Chi phí vốn chủ sở hữu Ke của chính công ty (làm ngưỡng hiệu quả cho các dự án đầu tư mở rộng sau này) là bao nhiêu? (2) Sau 1 năm, danh mục thực tế có thực sự "giỏi" hay chỉ may mắn?

#### Bước 1: Lợi nhuận kỳ vọng của từng kênh

$$E(R_E) = 0{,}15(40) + 0{,}30(22) + 0{,}25(10) + 0{,}20(-5) + 0{,}10(-25) = 6{,}0 + 6{,}6 + 2{,}5 - 1{,}0 - 2{,}5 = 11{,}6\%$$

$$E(R_G) = 0{,}15(-3) + 0{,}30(10) + 0{,}25(5) + 0{,}20(14) + 0{,}10(8) = -0{,}45 + 3{,}0 + 1{,}25 + 2{,}8 + 0{,}8 = 7{,}4\%$$

→ Quỹ cổ phiếu kỳ vọng 11,6%, vàng 7,4%, tiết kiệm 6%. Phần bù rủi ro thị trường: $MRP = 11{,}6 - 6 = 5{,}6\%$.

#### Bước 2: Độ lệch chuẩn của từng kênh

Bảng tính phương sai quỹ cổ phiếu (độ lệch so với 11,6%):

| Kịch bản | Độ lệch $(R-E)$ | Bình phương | × Xác suất |
|---|---|---|---|
| Tăng trưởng mạnh | 28,4 | 806,56 | 120,984 |
| Tăng trưởng khá | 10,4 | 108,16 | 32,448 |
| Đi ngang | -1,6 | 2,56 | 0,640 |
| Suy giảm nhẹ | -16,6 | 275,56 | 55,112 |
| Khủng hoảng | -36,6 | 1.339,56 | 133,956 |
| **Tổng = phương sai** | | | **343,14** |

$$\sigma_E = \sqrt{343{,}14} = 18{,}52\%$$

Tương tự cho vàng (độ lệch so với 7,4%: -10,4; 2,6; -2,4; 6,6; 0,6 → bình phương × xác suất = 16,224 + 2,028 + 1,44 + 8,712 + 0,036):

$$\sigma_G^2 = 28{,}44 \Rightarrow \sigma_G = \sqrt{28{,}44} = 5{,}33\%$$

**Hệ số biến thiên**: $CV_E = 18{,}52/11{,}6 = 1{,}60$; $CV_G = 5{,}33/7{,}4 = 0{,}72$. Tính theo "rủi ro trên mỗi đơn vị lợi nhuận", vàng hiệu quả hơn quỹ cổ phiếu, dù lợi nhuận kỳ vọng thấp hơn.

#### Bước 3: Hiệp phương sai, tương quan và Beta của vàng

Tích độ lệch (E × G) × xác suất:

| Kịch bản | $(R_E-E)(R_G-G)$ | × Xác suất |
|---|---|---|
| Tăng trưởng mạnh | 28,4 × (-10,4) = -295,36 | -44,304 |
| Tăng trưởng khá | 10,4 × 2,6 = 27,04 | 8,112 |
| Đi ngang | -1,6 × (-2,4) = 3,84 | 0,960 |
| Suy giảm nhẹ | -16,6 × 6,6 = -109,56 | -21,912 |
| Khủng hoảng | -36,6 × 0,6 = -21,96 | -2,196 |
| **Tổng = Cov(E, G)** | | **-59,34** |

$$\rho_{EG} = \frac{-59{,}34}{18{,}52 \times 5{,}33} = -0{,}60 \qquad\qquad \beta_G = \frac{Cov(E,G)}{Var(E)} = \frac{-59{,}34}{343{,}14} = -0{,}173$$

**Diễn giải**: tương quan âm (-0,60) nghĩa là khi quỹ cổ phiếu giảm, vàng thường tăng (và ngược lại) - tài sản "phòng thủ" điển hình. Beta của vàng bằng -0,173 (so với thị trường): rủi ro hệ thống **âm nhẹ**, tức vàng hơi hoạt động như "bảo hiểm" cho danh mục cổ phiếu.

#### Bước 4: Rủi ro và lợi nhuận của các tỷ trọng khác nhau (chỉ xét phần 1.500 triệu rủi ro)

Công ty giữ lại **500 triệu** tiền gửi tiết kiệm làm quỹ dự phòng thanh khoản (lý do ở mục kết luận). Phần **1.500 triệu** còn lại chia giữa quỹ cổ phiếu (tỷ trọng $w$) và vàng ($1-w$).

Ví dụ tính tay cho phương án **30% cổ phiếu / 70% vàng**:

$$E(R_p) = 0{,}3(11{,}6) + 0{,}7(7{,}4) = 3{,}48 + 5{,}18 = 8{,}66\%$$

$$\sigma_p^2 = 0{,}3^2(343{,}14) + 0{,}7^2(28{,}44) + 2(0{,}3)(0{,}7)(-59{,}34) = 30{,}8826 + 13{,}9356 - 24{,}9228 = 19{,}8954$$

$$\sigma_p = \sqrt{19{,}8954} = 4{,}46\%$$

Bảng so sánh các tỷ trọng (đã kiểm chứng bằng Python), Sharpe = $(E(R_p) - 6)/\sigma_p$:

| Cổ phiếu / Vàng | $E(R_p)$ | $\sigma_p$ | Sharpe |
|---|---|---|---|
| 100% / 0% | 11,60% | 18,52% | 0,302 |
| 80% / 20% | 10,76% | 14,20% | 0,335 |
| 60% / 40% | 9,92% | 9,98% | 0,393 |
| 50% / 50% | 9,50% | 7,95% | 0,440 |
| 40% / 60% | 9,08% | 6,06% | 0,509 |
| 30% / 70% | 8,66% | 4,46% | 0,596 |
| 20% / 80% | 8,24% | 3,60% | 0,623 |
| 0% / 100% | 7,40% | 5,33% | 0,263 |

**Phát hiện then chốt**: (1) Tỷ trọng 50/50 có $\sigma_p = 7,95\%$, thấp hơn nhiều so với trung bình có trọng số của σ ($0{,}5 \times 18{,}52 + 0{,}5 \times 5{,}33 = 11{,}93\%$) - đó là sức mạnh của tương quan âm. (2) Thậm chí **100% vàng ($\sigma = 5,33\%$) rủi ro cao hơn** danh mục 30/70 ($\sigma = 4,46\%$) - thêm một ít tài sản rủi ro hơn (cổ phiếu) lại **giảm** rủi ro tổng. Đây là hiện tượng tiêu biểu của Markowitz.

**Danh mục phương sai nhỏ nhất (MVP)**:

$$w_E^{MVP} = \frac{28{,}44 - (-59{,}34)}{343{,}14 + 28{,}44 - 2(-59{,}34)} = \frac{87{,}78}{490{,}26} = 17{,}9\%$$

→ MVP: 17,9% cổ phiếu / 82,1% vàng, $E(R_p) = 8{,}15\%$, $\sigma_p = 3{,}57\%$ (rủi ro nhỏ nhất có thể có với hai tài sản này).

#### Bước 5: Beta của danh mục và Ke của chính công ty (CAPM)

**Beta của danh mục** là trung bình có trọng số của Beta từng thành phần (khác với σ, Beta cộng tuyến tính): $\beta_p = 0{,}3(1{,}0) + 0{,}7(-0{,}173) = 0{,}179$. Theo CAPM, một tài sản có Beta 0,179 chỉ cần kỳ vọng $6\% + 0{,}179 \times 5{,}6\% = 7{,}0\%$; trong khi danh mục 30/70 kỳ vọng 8,66%, cao hơn 1,66 điểm phần trăm. Nguyên nhân: trong bộ kịch bản tự thiết kế, vàng có lợi nhuận kỳ vọng (7,4%) **cao hơn** mức CAPM đòi hỏi với Beta âm (khoảng 5,0%), tức vàng nằm *trên* SML. Bài học: **CAPM chỉ đúng khi mọi tài sản nằm trên SML**; số liệu kịch bản có thể lệch SML, và khi lệch thì đó là cơ hội (hoặc dấu hiệu giả định kịch bản quá lạc quan, cần kiểm tra lại).

**Beta của chính công ty** (phục vụ tính Ke): công ty chưa niêm yết nên ông Hòa lấy một DN nội thất niêm yết tương đồng làm "peer" và hồi quy lợi nhuận hằng năm của cổ phiếu peer theo VN-Index (số liệu giả định cho bài):

| Năm | VN-Index (%) | Cổ phiếu peer (%) |
|---|---|---|
| 1 | 22 | 30 |
| 2 | -8 | -2 |
| 3 | 15 | 10 |
| 4 | 30 | 34 |
| 5 | -12 | -24 |
| 6 | 10 | 14 |
| **Trung bình** | 9,5 | 10,33 |

Tổng tích độ lệch = 1.685; tổng bình phương độ lệch của thị trường = 1.375,5:

$$\beta_{raw} = \frac{1.685}{1.375{,}5} = 1{,}225 \qquad\qquad \beta_{adj} = \frac{2}{3}(1{,}225) + \frac{1}{3}(1{,}0) = 1{,}150$$

$$K_e = R_f + \beta_{adj} \times MRP = 6\% + 1{,}150 \times 5{,}6\% = 12{,}44\%$$

→ Mọi dự án mở rộng của công ty (cùng ngành, cùng đòn bẩy) phải có tỷ suất sinh lời kỳ vọng **tối thiểu khoảng 12,4%** mới hợp lý. So sánh: danh mục tài chính kỳ vọng 8,66% - **thấp hơn** ngưỡng này, nghĩa là nếu công ty có dự án mở rộng kinh doanh đạt ≥ 12,4% thì nên ưu tiên hơn việc đầu tư tài chính. (Điểm này được giải thích thêm ở mục IV.)

#### Bước 6: Stress test và giá trị tuyệt đối

Ông Hòa quan tâm tới số tiền cụ thể. Lợi nhuận danh mục (trên 1.500 triệu) theo từng kịch bản:

| Kịch bản | 100% cổ phiếu | 50/50 | 30/70 |
|---|---|---|---|
| Tăng trưởng mạnh | +40% | +18,5% | +9,9% |
| Tăng trưởng khá | +22% | +16,0% | +13,6% |
| Đi ngang | +10% | +7,5% | +6,5% |
| Suy giảm nhẹ | -5% | +4,5% | +8,3% |
| Khủng hoảng | -25% | -8,5% | -1,9% |

Tính bằng tiền với 1.500 triệu: kịch bản **khủng hoảng** làm 100% cổ phiếu lỗ $1.500 \times 25\% = 375$ triệu; 50/50 lỗ khoảng 127,5 triệu; 30/70 chỉ lỗ khoảng 28,5 triệu. Ước tính VaR tham số 95% (giả định phân phối chuẩn, $E - 1{,}645\sigma$) trên 1.500 triệu: 100% cổ phiếu khoảng -283 triệu; 50/50 khoảng -53,7 triệu; 30/70 khoảng **+19,8 triệu** (nghĩa là gần như không lỗ). *Lưu ý: VaR tham số là xấp xỉ - như bài học LTCM, đuôi thực tế dày hơn.*

#### Bước 7: Đánh giá hiệu suất sau 1 năm (Treynor, Jensen's Alpha)

Giả sử sau 12 tháng, VN30 thực tế sinh lời 10%, vàng thực tế 11%. Danh mục 30/70 sinh lời $0{,}3(10) + 0{,}7(11) = 10{,}7\%$.

- Treynor: $Treynor_p = (10{,}7 - 6)/0{,}179 = 26{,}3$ so với thị trường $(10 - 6)/1 = 4{,}0$.
- Mức CAPM kỳ vọng với $R_m = 10\%$: $6 + 0{,}179 \times (10 - 6) = 6{,}72\%$.
- $\alpha = 10{,}7 - 6{,}72 = +3{,}98\%$.

**Diễn giải thận trọng**: Treynor rất cao vì Beta gần bằng 0 - mẫu số nhỏ làm tỷ số "phóng đại", nên không nên diễn giải như "kỹ năng". Alpha +3,98% phần lớn đến từ việc vàng (một lớp tài sản không nằm trong thị trường cổ phiếu) tăng tốt, không phải "kỹ năng chọn cổ phiếu". Một năm quá ngắn để kết luận về kỹ năng.

#### Kết luận và Khuyến nghị

**Khuyến nghị cho Gỗ Việt**: phân bổ 2.000 triệu như sau:
- **500 triệu** (25%): tiền gửi tiết kiệm 12 tháng - dự phòng thanh khoản.
- **450 triệu** (22,5%): quỹ chỉ số VN30.
- **1.050 triệu** (52,5%): vàng (miếng/tài khoản vàng đáng tin cậy).

Chỉ số của toàn bộ 2.000 triệu (tiền gửi là phi rủi ro): $E(R) = 0{,}25(6) + 0{,}75(8{,}66) = 7{,}995\% \approx 8{,}0\%$ (tương đương khoảng **159,9 triệu đồng**/năm, so với 120 triệu nếu gửi hết tiết kiệm), $\sigma = 0{,}75 \times 4{,}46 = 3{,}35\%$, Sharpe = $(7{,}995 - 6)/3{,}345 = 0{,}596$ (giữ nguyên Sharpe của phần rủi ro - minh họa Định lý tách biệt: trộn tiền gửi với danh mục rủi ro đi trên một đường thẳng giống CML).

Lý do chọn phương án này:
1. **Sharpe 0,596 so với 0,302** (100% cổ phiếu): hiệu quả điều chỉnh rủi ro gần gấp đôi.
2. **Không chọn tỷ trọng 20/80** (Sharpe cao nhất 0,623) vì Sharpe chênh nhỏ trong khi 30/70 giữ lợi nhuận kỳ vọng cao hơn (8,66% so với 8,24%) - đánh đổi hợp lý.
3. **Lỗ tối đa kịch bản khủng hoảng** chỉ khoảng 28,5 triệu (1,4% trên tổng 2.000 triệu) - doanh nghiệp chịu được.
4. **Quỹ dự phòng 500 triệu** vì vốn nhàn rỗi của SME khác quỹ tài trợ vĩnh viễn: nhu cầu vốn lưu động đột xuất (đơn hàng lớn, nợ thuế, lương) là ràng buộc cứng, và tài sản kém thanh khoản hoặc đang lỗ sẽ buộc phải bán đáy (bài học Yale/LTCM).
5. **Ngưỡng Ke = 12,44%**: nếu trong 12 tháng xuất hiện dự án mở rộng sản xuất có thể đạt ≥ 12,4%, ưu tiên rút từ phần đầu tư tài chính (vàng/quỹ có thể thanh khoản) để thực hiện dự án kinh doanh cốt lõi.

> **Ghi chú phương pháp**: Toàn bộ số liệu (E, σ, Cov, ρ, Beta, MVP, Sharpe, hồi quy Beta) đã được kiểm tra chéo bằng Python để đảm bảo nhất quán số học. Kịch bản lợi nhuận và dữ liệu peer là giả định cho mục đích học tập; chủ DN cần thay bằng số liệu thực và tham vấn chuyên gia trước khi quyết định. Đây không phải lời khuyên đầu tư cá nhân.

---

## IV. ỨNG DỤNG CHO SME

### 1. Đặc thù của Risk-Return đối với SME Việt Nam

| Khía cạnh | Công ty đại chúng / Quỹ lớn | SME Việt Nam | Hệ quả |
|---|---|---|---|
| **Đa dạng hóa** | Dễ dàng (nhiều tài sản, chi phí giao dịch thấp) | Rất khó: phần lớn tài sản (và tài sản cá nhân của chủ) dồn vào **một doanh nghiệp** | Chủ SME chịu rủi ro phi hệ thống rất cao, không được thị trường "trả công" thêm |
| **Beta của DN** | Quan sát được từ giá cổ phiếu | Không có (chưa niêm yết) | Phải dùng **Beta ngành/peer + hiệu chỉnh đòn bẩy** (xem Excel mục V) |
| **Rủi ro thanh khoản** | Bán tài sản nhanh | Tiền thường bị kẹt (hàng tồn, công nợ) | Phải dự trữ thanh khoản trước khi tính đến tối ưu hóa lợi nhuận |
| **Chi phí vốn** | Ke từ CAPM | CAPM + phần bù quy mô nhỏ + phần bù thiếu thanh khoản | Ke SME thường cao hơn công ty niêm yết cùng ngành vài điểm phần trăm |
| **Chi phí giao dịch & thông tin** | Thấp | Cao, ít công cụ phòng hộ | Nên chọn công cụ đơn giản, minh bạch (quỹ chỉ số, tiết kiệm) |

**Ý nghĩa**: lợi ích lớn nhất của lý thuyết này với SME không phải là "đầu tư chứng khoán" mà là **tư duy**: (1) tránh tập trung quá mức - một khách hàng, một sản phẩm, một nhà cung cấp, một thị trường (đa dạng hóa trong chính kinh doanh); (2) định giá chi phí vốn đúng; (3) tách bạch vốn kinh doanh cốt lõi và vốn nhàn rỗi.

### 2. Hướng dẫn thực tế: 5 bước áp dụng Risk-Return cho quyết định của chủ SME

**Bước 1 - Xác định mục tiêu và ràng buộc thanh khoản**
- Số tiền cần dùng trong 3, 6, 12 tháng tới (thuế, lương, trả nợ, mua hàng)? Phần này đi vào tiền gửi/tài sản thanh khoản.
- Mức lỗ tối đa chấp nhận được (tính bằng triệu đồng, không phải %).

**Bước 2 - Liệt kê các lựa chọn và xây dựng kịch bản**
- Ít nhất 3-5 kịch bản (tốt, khá, trung bình, xấu, khủng hoảng) với xác suất hợp lý. Luôn có kịch bản khủng hoảng.
- Với kinh doanh: dùng kịch bản doanh thu -10%, -20%, -30%.

**Bước 3 - Tính E(R), σ, tương quan; so sánh bằng CV/Sharpe**
- Dùng bảng tính (mục V). Không so sánh chỉ bằng lợi nhuận kỳ vọng.

**Bước 4 - Tính chi phí vốn Ke cho dự án kinh doanh**
- Ke = Rf + β × MRP + phần bù (quy mô/thanh khoản nếu có). Dự án đáng làm chỉ khi lợi nhuận kỳ vọng > Ke (hoặc NPV dương với chiết khấu bằng WACC dựa trên Ke).

**Bước 5 - Stress test và theo dõi**
- Giả sử tương quan = 1 (mọi thứ cùng xấu) và mất 30% giá trị: DN có sống được không?
- Xem lại hằng quý, tái cân bằng khi tỷ trọng lệch quá 5-10 điểm phần trăm.

### 3. Các sai lầm phổ biến (Common Mistakes)

| Sai lầm | Vì sao sai | Cách tránh |
|---|---|---|
| Chạy theo "lợi nhuận cao" mà không hỏi rủi ro | Lợi nhuận cao thường là phần bù của rủi ro cao | Luôn tính CV/Sharpe, hỏi "tối đa lỗ bao nhiêu?" |
| Đa dạng hóa giả (cùng ngành, cùng chuỗi cung ứng) | Tương quan cao → lợi ích thấp | Chọn tài sản/ngành có tương quan thấp thực sự |
| Dùng tiền vay hoặc vốn lưu động để đầu tư tài chính | Đòn bẩy + thiếu thanh khoản (bài học LTCM) | Chỉ đầu tư bằng **vốn nhàn rỗi thực sự** |
| Tin Beta/σ quá khứ là bất biến | Beta và tương quan thay đổi theo thời gian, nhất là khủng hoảng | Stress test, cập nhật định kỳ |
| Dùng trung bình cộng để kỳ vọng tăng trưởng dài hạn | Bỏ qua hiệu ứng gộp (volatility drag) | Dùng CAGR (trung bình nhân) cho dài hạn |
| So sánh hiệu suất mà không điều chỉnh rủi ro | Quỹ lời cao có thể chỉ vì rủi ro cao | Dùng Sharpe/Treynor/Alpha |
| Chọn MRP tùy tiện | Làm Ke lệch hàng điểm % | Dùng khoảng (5-8%), phân tích độ nhạy |

### 4. Bảng tham chiếu sơ bộ: nhóm tài sản và đặc điểm rủi ro (mang tính định tính)

| Nhóm tài sản | Rủi ro (định tính) | Thanh khoản | Phù hợp SME cho |
|---|---|---|---|
| Tiền gửi tiết kiệm / chứng chỉ tiền gửi | Rất thấp | Cao (có thể mất lãi nếu rút sớm) | Quỹ dự phòng, vốn lưu động nhàn rỗi |
| Trái phiếu chính phủ / quỹ trái phiếu | Thấp - trung bình | Trung bình - cao | Vốn nhàn rỗi 1-3 năm |
| Vàng | Trung bình, tương quan thấp/âm với cổ phiếu | Cao | Phòng thủ, đa dạng hóa |
| Quỹ chỉ số cổ phiếu (VN30 ETF) | Cao | Cao | Vốn dài hạn >3-5 năm |
| Cổ phiếu riêng lẻ | Rất cao (rủi ro riêng) | Trung bình | Chỉ với số vốn nhỏ, chấp nhận mất |
| Bất động sản | Trung bình - cao | Thấp | Vốn dài hạn, có đòn bẩy cần thận trọng |
| Dự án kinh doanh cốt lõi | Cao (tập trung) | Thấp | Ưu tiên đầu tư nếu lợi nhuận kỳ vọng > Ke |

---

## V. TOOLS & TEMPLATES

### 1. Công cụ và nguồn dữ liệu

| Công cụ / Nguồn | Công dụng | Chi phí / Ghi chú |
|---|---|---|
| **Excel / Google Sheets** | Tính E(R), σ, Cov, Beta, Sharpe; mô phỏng danh mục | Miễn phí (Google Sheets) hoặc theo gói Microsoft 365 |
| **Damodaran Online (NYU Stern)** | Beta trung bình theo ngành, Phần bù rủi ro quốc gia (country risk premium) | Miễn phí, cập nhật hằng năm |
| **HNX / Bộ Tài chính** | Lãi suất trái phiếu chính phủ kỳ hạn 10 năm (làm $R_f$) | Miễn phí |
| **HOSE, SSI iBoard, VNDirect, Vietstock, CafeF** | Dữ liệu giá VN-Index, VN30, cổ phiếu để tính Beta, σ | Miễn phí cơ bản; dữ liệu nâng cao có phí |
| **Yahoo Finance / Google Finance** | Dữ liệu giá lịch sử (tải về CSV) | Miễn phí |
| **Python (pandas, numpy)** | Tự động hóa tính Beta, tối ưu danh mục | Miễn phí |

### 2. Cấu trúc Excel/Google Sheet đề xuất (4 tab)

```
TAB 1 - KỊCH BẢN & XÁC SUẤT:
  - Cột: Kịch bản | Xác suất p | R_tài sản A | R_tài sản B | ...
  - Kiểm tra: tổng xác suất = 100%

TAB 2 - THỐNG KÊ TỪNG TÀI SẢN:
  - E(R)     = SUMPRODUCT(p, R)
  - Phương sai = SUMPRODUCT(p, (R - E)^2)
  - σ        = SQRT(phương sai)
  - CV       = σ / E(R)
  - Cov(A,B) = SUMPRODUCT(p, (R_A - E_A) * (R_B - E_B))
  - ρ        = Cov / (σ_A * σ_B)

TAB 3 - DANH MỤC (bảng tỷ trọng 0%, 10%, ..., 100%):
  - E(R_p) = w*E_A + (1-w)*E_B
  - σ_p    = SQRT(w^2*Var_A + (1-w)^2*Var_B + 2*w*(1-w)*Cov_AB)
  - Sharpe = (E_p - Rf) / σ_p
  - Conditional formatting: tô xanh dòng có Sharpe cao nhất; tô đỏ nếu lỗ kịch bản xấu > mức chấp nhận

TAB 4 - BETA & KE:
  - Dữ liệu lợi nhuận kỳ (tuần/tháng/năm) của DN peer và VN-Index
  - Beta = SLOPE(R_peer, R_market)    (hoặc COVARIANCE.S / VAR.S)
  - Adjusted Beta = 2/3*Beta + 1/3
  - Unlever: β_U = β_L / (1 + (1-T)*D/E peer)
  - Relever: β_L = β_U * (1 + (1-T)*D/E của DN)
  - Ke = Rf + β * MRP  (+ phần bù quy mô/thanh khoản nếu có)
```

### 3. Mẫu tờ quyết định phân bổ vốn nhàn rỗi (Template)

| Hạng mục | Điền số liệu |
|---|---|
| Số vốn nhàn rỗi (triệu đồng) | |
| Thời gian chưa cần dùng (tháng) | |
| Quỹ dự phòng thanh khoản giữ lại (tối thiểu 3-6 tháng chi phí cố định) | |
| Mức lỗ tối đa chấp nhận (triệu đồng) | |
| Ngưỡng Ke của DN (lợi nhuận tối thiểu dự án kinh doanh) | |
| Tỷ trọng kênh 1 / 2 / 3 | |
| E(R), σ, Sharpe của danh mục | |
| Kết quả stress test (kịch bản khủng hoảng, tương quan = 1) | |
| Thời điểm rà soát và tái cân bằng | |

---

## VI. BÀI TẬP THỰC HÀNH

### Bài 1 (Cơ bản - Trung bình cộng vs trung bình nhân)
Một quỹ có lợi nhuận 3 năm liên tiếp là +30%, -20%, +10%. Tính lợi nhuận trung bình cộng và trung bình nhân. Giải thích bằng lời vì sao chúng khác nhau.

*(Đáp số đã verify bằng Python: trung bình cộng = 6,67%; trung bình nhân = 4,59%/năm)*

### Bài 2 (Cơ bản - Hệ số biến thiên)
Ba khoản đầu tư: X (E = 18%, σ = 27%), Y (E = 12%, σ = 15%), Z (E = 9%, σ = 9%). Tính CV và xếp hạng theo hiệu quả rủi ro.

*(Đáp số đã verify: CV_X = 1,50; CV_Y = 1,25; CV_Z = 1,00 → Z hiệu quả nhất theo CV, nhưng cần xem thêm lợi nhuận tuyệt đối và Sharpe)*

### Bài 3 (Trung bình - Rủi ro danh mục 2 tài sản)
Tài sản A: E = 14%, σ = 22%; tài sản B: E = 8%, σ = 12%; $\rho_{AB} = 0{,}25$. Danh mục 60% A / 40% B. Tính E(R_p), σ_p và so sánh σ_p với trung bình có trọng số của σ.

*(Đáp số đã verify bằng Python: E(R_p) = 11,6%; Var = 0,022896 → σ_p = 15,13%; trung bình có trọng số σ = 18,0% → đa dạng hóa giảm khoảng 2,9 điểm phần trăm)*

### Bài 4 (Trung bình - CAPM và SML)
Rf = 5%, MRP = 6%. Cổ phiếu K có Beta 1,4 và các nhà phân tích kỳ vọng sinh lời 12%. Tính lợi nhuận yêu cầu theo CAPM; cổ phiếu K đang bị định giá cao hay thấp so với SML? Giải thích.

*(Đáp số đã verify: lợi nhuận yêu cầu = 5% + 1,4 × 6% = 13,4%; lợi nhuận kỳ vọng 12% thấp hơn 1,4 điểm phần trăm → nằm dưới SML → bị định giá cao / không hấp dẫn)*

### Bài 5 (Nâng cao - Sharpe, Treynor, Alpha)
Rf = 4%, Rm = 10%. Quỹ A: Rp = 14%, σ = 16%, β = 1,2. Quỹ B: Rp = 11%, σ = 8%, β = 0,6. Tính Sharpe, Treynor và Jensen's Alpha cho mỗi quỹ. Quỹ nào tốt hơn theo từng thước đo?

*(Đáp số đã verify bằng Python: Quỹ A: Sharpe = 0,625; Treynor = 8,33; Alpha = +2,8%. Quỹ B: Sharpe = 0,875; Treynor = 11,67; Alpha = +3,4%. Quỹ B tốt hơn theo cả ba thước đo.)*

### Bài 6 (Nâng cao - Beta, hiệu chỉnh đòn bẩy và Ke cho SME)
Một xưởng sản xuất bao bì tại Long An tham chiếu hai DN niêm yết tương đồng. Rf = 4,5%, MRP = 7%, thuế suất 20%.
- (a) DN tham chiếu 1 có Beta thô 1,5. Tính Ke nếu dùng Beta thô và nếu dùng Beta hiệu chỉnh theo Blume.
- (b) DN tham chiếu 2 có Beta 1,2 và D/E = 0,5. Xưởng dự kiến vận hành với D/E = 1,0. Tính Beta không đòn bẩy (Hamada), Beta của xưởng sau khi gộp đòn bẩy và Ke tương ứng.

*(Đáp số đã verify bằng Python: (a) Ke với Beta thô = 4,5% + 1,5 × 7% = 15,0%; Beta hiệu chỉnh = 1,333 → Ke = 13,83%. (b) β_U = 1,2/(1 + 0,8 × 0,5) = 0,857; β_L = 0,857 × (1 + 0,8 × 1,0) = 1,543; Ke = 4,5% + 1,543 × 7% = 15,3%)*

### Bài 7 (Nâng cao - Tự thực hành với doanh nghiệp của chính bạn)
Áp dụng toàn bộ quy trình 7 bước ở case study mục III.3 (Gỗ Việt) cho khoản vốn nhàn rỗi của doanh nghiệp bạn: xác định quỹ dự phòng thanh khoản, xây dựng ít nhất 3 kênh đầu tư và 5 kịch bản (có kịch bản khủng hoảng), tính E, σ, tương quan, Sharpe cho các tỷ trọng khác nhau, tính Ke của DN bằng Beta peer, rồi stress test trước khi đưa ra khuyến nghị.

---

## PHỤ LỤC: CHECKLIST RISK & RETURN TỔNG HỢP

### Bảng công thức tổng hợp

| Khái niệm | Công thức | Ý nghĩa |
|---|---|---|
| Lợi nhuận một kỳ | $R = \frac{P_1 - P_0 + D}{P_0}$ | Lợi nhuận trên mỗi đồng vốn |
| Lợi nhuận kỳ vọng | $E(R) = \sum p_s R_s$ | Trung bình có trọng số xác suất |
| Lợi nhuận danh mục | $E(R_p) = \sum w_i E(R_i)$ | Trung bình có trọng số tỷ trọng |
| Trung bình nhân | $\left[\prod (1+R_t)\right]^{1/n} - 1$ | Tốc độ tăng trưởng gộp thực tế |
| Phương sai / Độ lệch chuẩn | $\sigma^2 = \sum p_s [R_s - E(R)]^2$ | Thước đo tổng rủi ro |
| Hệ số biến thiên | $CV = \sigma / E(R)$ | Rủi ro trên mỗi đơn vị lợi nhuận |
| Hiệp phương sai / Tương quan | $\rho_{AB} = Cov(A,B)/(\sigma_A\sigma_B)$ | Mức đi cùng nhau của hai tài sản |
| Rủi ro danh mục (2 tài sản) | $\sigma_p^2 = w_A^2\sigma_A^2 + w_B^2\sigma_B^2 + 2w_Aw_B\sigma_A\sigma_B\rho_{AB}$ | Hiệu ứng đa dạng hóa |
| Tỷ trọng MVP (2 tài sản) | $w_A = \frac{\sigma_B^2 - Cov}{\sigma_A^2 + \sigma_B^2 - 2Cov}$ | Danh mục rủi ro thấp nhất |
| Beta | $\beta_i = Cov(R_i, R_m)/Var(R_m)$ | Độ nhạy với thị trường |
| Beta hiệu chỉnh (Blume) | $\beta_{adj} = \frac{2}{3}\beta_{raw} + \frac{1}{3}$ | Hồi quy về trung bình |
| Hamada | $\beta_L = \beta_U[1+(1-T)D/E]$ | Tách/gộp đòn bẩy tài chính |
| CAPM | $E(R_i) = R_f + \beta_i(E(R_m) - R_f)$ | Lợi nhuận yêu cầu (Ke) |
| CML | $E(R_p) = R_f + \frac{E(R_m)-R_f}{\sigma_m}\sigma_p$ | Đường danh mục hiệu quả |
| Sharpe | $(R_p - R_f)/\sigma_p$ | Lợi nhuận vượt trên mỗi đơn vị tổng rủi ro |
| Treynor | $(R_p - R_f)/\beta_p$ | Lợi nhuận vượt trên mỗi đơn vị rủi ro hệ thống |
| Jensen's Alpha | $\alpha = R_p - [R_f + \beta_p(R_m - R_f)]$ | Hiệu suất vượt mức CAPM |

### Checklist tổng hợp

```
HIỂU KHÁI NIỆM:
□ Phân biệt được rủi ro hệ thống và phi hệ thống?
□ Hiểu lợi ích của đa dạng hóa (và vì sao nó phụ thuộc vào tương quan)?
□ Biết mối quan hệ: rủi ro cao hơn → lợi nhuận kỳ vọng cao hơn?
□ Diễn giải được Beta? (β = 1,3 nghĩa là gì)
□ Hiểu khái niệm Đường biên hiệu quả và danh mục MVP?

TÍNH TOÁN:
□ Tính được E(R_p) của danh mục?
□ Tính được σ_p danh mục 2 tài sản (có Cov / ρ)?
□ Áp dụng được CAPM: E(R) = Rf + β × MRP?
□ Ước lượng được Beta bằng hồi quy (SLOPE) và hiệu chỉnh (Blume, Hamada)?
□ Tính được Sharpe, Treynor và diễn giải được Jensen's Alpha?

ỨNG DỤNG:
□ Dùng CAPM để tính Chi phí vốn chủ sở hữu (Ke) cho DN?
□ Đánh giá hiệu suất danh mục có điều chỉnh rủi ro?
□ Xây dựng danh mục đa dạng hóa (tương quan thấp thực sự)?
□ Hiểu khi nào các giả định CAPM/MPT bị phá vỡ?
□ Biết các mô hình thay thế (Fama-French, APT)?
□ Đã tách vốn nhàn rỗi và vốn lưu động trước khi đầu tư tài chính?

QUẢN TRỊ RỦI RO:
□ Không dùng đòn bẩy/vốn vay cho đầu tư tài chính?
□ Đã stress test cho kịch bản cực đoan (tương quan = 1)?
□ Hiểu sự bất ổn của tương quan trong khủng hoảng?
□ Biết về rủi ro đuôi (fat tails) và giới hạn của VaR?
□ Duy trì quỹ dự phòng thanh khoản (3-6 tháng chi phí cố định)?
□ Đặt lịch rà soát và tái cân bằng danh mục định kỳ?
```

---

*Tài liệu tham khảo: Markowitz "Portfolio Selection" (1952); Sharpe "Capital Asset Prices" (1964); Fama & French "Common Risk Factors" (1993); Lowenstein "When Genius Failed" (LTCM); CFA Level I – Portfolio Management & Equity Investments*
