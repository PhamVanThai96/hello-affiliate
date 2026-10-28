# Time Value of Money – Giá Trị Thời Gian Của Tiền

> **Mục tiêu**: Hiểu bản chất và cách tính PV, FV, Annuity, Perpetuity, NPV, IRR – nền tảng quan trọng nhất của toàn bộ tài chính doanh nghiệp – để chủ SME có thể tự đánh giá khoản đầu tư, khoản vay và phương án thanh toán bằng con số thay vì cảm tính.

---

## I. KHÁI NIỆM & LÝ THUYẾT

### 1. Định nghĩa

**Time Value of Money (TVM – Giá trị thời gian của tiền)** là nguyên lý tài chính nền tảng nhất: **1 đồng tiền nhận được hôm nay có giá trị CAO HƠN 1 đồng tiền nhận được trong tương lai**.

> **"A dollar today is worth more than a dollar tomorrow."** – Nguyên lý cốt lõi nhất của Finance

TVM là xương sống của MỌI quyết định tài chính: từ gửi tiết kiệm, vay mua nhà, mở thêm chi nhánh, mua máy móc trả góp, đến định giá doanh nghiệp hàng tỷ đô.

**Vấn đề kinh doanh mà TVM giải quyết**: Trong kinh doanh, tiền chi ra và tiền thu về hiếm khi xảy ra cùng lúc. Bạn bỏ 800 triệu hôm nay để mở chi nhánh, nhưng tiền lời đến rải rác trong 5 năm. Nếu chỉ cộng trừ số học đơn thuần (tổng thu 1.410 triệu − chi 800 triệu = lời 610 triệu) bạn đang coi 1 đồng năm thứ 5 ngang với 1 đồng hôm nay – một sai lầm khiến rất nhiều chủ SME đánh giá quá cao dự án dài hạn và đánh giá thấp chi phí của việc "trả góp". TVM cung cấp "thước đo chung" để quy mọi dòng tiền ở các thời điểm khác nhau về cùng một mốc thời gian, rồi mới so sánh được.

### 2. Nguồn gốc lý thuyết

| Học giả | Đóng góp | Năm |
|---------|----------|-----|
| **Eugen von Böhm-Bawerk** | "Positive Theory of Capital" – lý thuyết ưu tiên thời gian (time preference): con người vốn thích tiêu dùng hiện tại hơn tương lai | 1889 |
| **Irving Fisher** | "The Theory of Interest" – lãi suất là giá của việc đánh đổi giữa tiêu dùng hôm nay và mai; tách lãi suất danh nghĩa và thực (Fisher equation) | 1930 |
| **John Burr Williams** | "The Theory of Investment Value" – lần đầu đề xuất định giá tài sản bằng chiết khấu dòng tiền (DCF) | 1938 |
| **Modigliani & Miller** | Áp dụng TVM vào cấu trúc vốn & chi phí vốn | 1958 |

**Bối cảnh**: Từ thời cổ đại, con người đã cho vay lấy lãi (Babylon, La Mã), nhưng đến cuối thế kỷ 19 mới có lời giải thích lý thuyết "vì sao lãi suất tồn tại". Böhm-Bawerk cho rằng người ta đánh giá hàng hóa hiện tại cao hơn hàng hóa tương lai; Fisher (1930) chính thức hóa bằng mô hình toán học; và Williams (1938) – ngay sau cuộc Đại suy thoái, khi giới đầu tư đã quá nhiều lần bị tổn thất vì mua cổ phiếu theo "đầu cơ" – đề xuất rằng giá trị thực của một cổ phiếu chính là tổng giá trị hiện tại của cổ tức tương lai. Từ đó nảy sinh toàn bộ trường phái DCF mà ngày nay NPV, IRR, WACC, định giá doanh nghiệp đều dựa vào.

### 3. Tại sao 1 đồng hôm nay > 1 đồng ngày mai?

| Lý do | Giải thích | Ví dụ |
|-------|-----------|-------|
| **Opportunity Cost (Chi phí cơ hội)** | Tiền hôm nay có thể đầu tư → sinh lời | 100 triệu gửi ngân hàng 8% → 108 triệu sau 1 năm |
| **Inflation (Lạm phát)** | Lạm phát làm giảm sức mua | Tô phở 50k hôm nay, 55k sau 1 năm nếu lạm phát 10% |
| **Risk/Uncertainty (Rủi ro)** | Tương lai bất định, tiền hứa trả sau có thể không đến | Khách hàng hứa trả 100 triệu sau 2 năm → có thể phá sản |
| **Consumption Preference (Ưa thích tiêu dùng hiện tại)** | Con người thiên về hưởng thụ ngay (impatience) | Mua iPhone bây giờ vs đợi 2 năm |
| **Reinvestment Risk (Rủi ro tái đầu tư)** | Lãi suất tương lai không chắc bằng hôm nay | Lãi 8% hôm nay, năm sau có thể chỉ 5% |

Trong 5 lý do này, **chi phí cơ hội** là lý do quan trọng nhất cho quyết định kinh doanh: nếu bạn nhận tiền sớm, bạn có thể đem đi làm một việc khác sinh lời – nên chờ đợi luôn có "giá". Lãi suất $r$ (hay tỷ lệ chiết khấu) trong các công thức dưới đây chính là cách định lượng "giá của sự chờ đợi" đó.

### 4. Sơ đồ tổng quan TVM

```
                        TIME VALUE OF MONEY
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
     ┌────▼────┐       ┌─────▼─────┐       ┌─────▼─────┐
     │ Present │       │  Future   │       │  Discount │
     │  Value  │       │  Value    │       │   Rate    │
     │  (PV)   │       │  (FV)     │       │   (r)     │
     └────┬────┘       └─────┬─────┘       └─────┬─────┘
          │                  │                   │
          └──────────────────┼───────────────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
    ┌────▼────┐        ┌────▼────┐        ┌─────▼─────┐
    │  NPV    │        │  IRR    │        │ Annuity   │
    │(Net PV) │        │(Internal│        │ Perpetuity│
    │         │        │ Return) │        │           │
    └─────────┘        └─────────┘        └───────────┘
         │                   │                   │
    ┌────▼────────────┐ ┌───▼───────────┐ ┌────▼──────────┐
    │Capital Budgeting│ │ Project       │ │ Loan/Mortgage │
    │DCF Valuation    │ │ Evaluation    │ │ Bond Pricing  │
    │M&A Pricing      │ │ Performance   │ │ Retirement    │
    └─────────────────┘ └───────────────┘ └───────────────┘
```

**Cách đọc**: Ba "viên gạch" cơ bản là PV, FV và tỷ lệ chiết khấu $r$. Từ đó xây ra ba nhóm công cụ: (1) NPV – dùng để quyết định có đầu tư hay không; (2) IRR – cho biết "lãi suất thực" của dự án; (3) Annuity/Perpetuity – công thức rút gọn cho các dòng tiền đều (khoản vay trả góp, tiền thuê mặt bằng, cổ tức…). Các mục dưới đây đi lần lượt theo thứ tự đó.

### 5. Hai "quy tắc vàng" trước khi tính bất kỳ bài toán TVM nào

1. **Nhất quán đơn vị thời gian**: Nếu lãi suất tính theo năm thì $n$ tính theo năm; nếu trả góp hàng tháng thì phải đổi lãi suất sang tháng ($r_{tháng} = r_{năm}/12$ hoặc $(1+r_{năm})^{1/12}-1$) và $n$ sang tháng.
2. **Vẽ trục thời gian (Timeline) trước khi tính**: Xác định rõ mỗi dòng tiền xảy ra ở thời điểm nào (đầu kỳ hay cuối kỳ), dấu âm (chi) hay dương (thu). 90% sai sót trong TVM đến từ việc đặt sai thời điểm dòng tiền, không phải sai công thức.

```
Ví dụ timeline đầu tư 800 triệu, thu về 5 năm:

 t=0         t=1       t=2       t=3       t=4       t=5
  │           │         │         │         │         │
-800        +180      +230      +280      +300      +420
```

---

## II. CHI TIẾT TỪNG THÀNH PHẦN

### A. Future Value (FV) – Giá trị tương lai

#### 1. Định nghĩa
FV là giá trị của một khoản tiền **tại một thời điểm trong tương lai**, sau khi được đầu tư/gửi với lãi suất $r$ trong $n$ kỳ.

#### 2. Tại sao công thức lại có dạng lũy thừa $(1+r)^n$? — Bản chất của "lãi kép"
Nếu bạn gửi 100 triệu với lãi 8%/năm, sau năm 1 bạn có $100 \times 1{,}08 = 108$ triệu. Sang năm thứ 2, bạn **không** nhận lãi 8% chỉ trên 100 triệu gốc, mà nhận lãi trên **cả 108 triệu** (gồm gốc + lãi năm 1): $108 \times 1{,}08 = 116{,}64$. Cứ như vậy, mỗi năm số tiền được nhân thêm với $(1+r)$ – sau $n$ năm là nhân $n$ lần, tức lũy thừa $n$. Đó là lý do công thức có dạng mũ chứ không phải cộng tuyến tính. "Lãi trên lãi" chính là nguồn gốc sức mạnh của lãi kép (compound interest): càng để lâu, phần lãi sinh ra từ lãi càng lấn át phần lãi từ gốc.

#### 3. Công thức cơ bản (Lãi kép – Compound Interest)

$$FV = PV \times (1 + r)^n$$

Trong đó:
- $PV$ = Giá trị hiện tại (Present Value)
- $r$ = Lãi suất mỗi kỳ (interest rate per period)
- $n$ = Số kỳ (number of periods)
- $(1 + r)^n$ = **Compounding Factor** (hệ số tích lũy)

#### 4. Công thức mở rộng – Lãi kép nhiều lần trong năm

$$FV = PV \times \left(1 + \frac{r}{m}\right)^{m \times n}$$

- $m$ = Số lần ghép lãi trong 1 năm (tháng: m=12, quý: m=4, ngày: m=365)

**Tại sao cần?** Ngân hàng và các hợp đồng vay thực tế thường tính lãi theo tháng hoặc quý chứ không chỉ theo năm. Mỗi lần ghép lãi, phần lãi vừa sinh ra lập tức được cộng vào gốc để sinh lãi tiếp – nên ghép càng thường xuyên, lãi thực nhận càng cao dù lãi suất "danh nghĩa" ghi trên hợp đồng không đổi.

#### 5. Công thức – Continuous Compounding (Ghép lãi liên tục)

$$FV = PV \times e^{r \times n}$$

Đây là giới hạn toán học khi $m \to \infty$ (ghép lãi vô hạn lần). Dù trong thực tế gần như không ngân hàng nào ghép lãi liên tục, công thức này rất quan trọng trong tài chính định lượng (định giá quyền chọn Black-Scholes) và cho thấy ghép lãi có "trần" – không thể tăng vô hạn.

#### 6. Ví dụ – So sánh các phương pháp ghép lãi

**Bài toán**: Gửi 100 triệu VND, lãi suất 12%/năm, kỳ hạn 5 năm.

| Phương pháp | Công thức | Kết quả |
|------------|-----------|---------|
| Lãi đơn (Simple) | 100 × (1 + 0,12×5) | 160,00 triệu |
| Lãi kép năm (Annual) | 100 × (1,12)⁵ | 176,23 triệu |
| Lãi kép quý (Quarterly) | 100 × (1,03)²⁰ | 180,61 triệu |
| Lãi kép tháng (Monthly) | 100 × (1,01)⁶⁰ | 181,67 triệu |
| Lãi kép liên tục (Continuous) | 100 × e^(0,6) | 182,21 triệu |

→ **Ghép lãi càng thường xuyên → FV càng lớn** (nhưng lợi ích tăng thêm giảm dần – diminishing returns: từ năm → quý thêm 4,38 triệu, nhưng từ tháng → liên tục chỉ thêm 0,54 triệu).

#### 7. Sức mạnh của Lãi Kép (Compound Interest)

```
Gửi 100 triệu, lãi 8%/năm (compound annually):

Năm 1:   108,0 triệu    (+8,0)
Năm 5:   146,9 triệu    (+46,9)
Năm 10:  215,9 triệu    (+115,9)
Năm 20:  466,1 triệu    (+366,1)  ← Gấp gần 5 lần!
Năm 30:  1.006,3 triệu  (+906,3)  ← Gấp 10 lần!
Năm 40:  2.172,5 triệu  (+2.072,5) ← Gấp 21,7 lần!

→ "Compound interest is the eighth wonder of the world."
  (câu nói thường được gán cho Einstein – chưa có bằng chứng xác thực)
```

#### 8. Rule of 72 (Quy tắc 72)

**Tại sao có quy tắc này?** Muốn biết bao lâu thì tiền gấp đôi, lẽ ra phải giải $(1+r)^n = 2$, tức $n = \ln 2 / \ln(1+r)$ – cần máy tính. Vì $\ln 2 \approx 0{,}693$ và $\ln(1+r) \approx r$ khi $r$ nhỏ, ta có $n \approx 69{,}3/r\%$; các nhà tài chính chọn **72** thay vì 69,3 vì 72 chia hết cho nhiều số (2, 3, 4, 6, 8, 9, 12) nên tính nhẩm dễ hơn và bù trừ sai số cho mức lãi suất phổ biến 6–10%.

$$n \approx \frac{72}{r\%}$$

| Lãi suất | Thời gian gấp đôi (Rule 72) | Chính xác ($\ln 2 / \ln(1+r)$) |
|----------|-------------------|--------------------|
| 6% | 12 năm | 11,90 năm |
| 8% | 9 năm | 9,01 năm |
| 10% | 7,2 năm | 7,27 năm |
| 12% | 6 năm | 6,12 năm |
| 15% | 4,8 năm | 4,96 năm |
| 20% | 3,6 năm | 3,80 năm |

*(Lưu ý: bản cũ ghi "8% → 8,66 năm" là sai; giá trị chính xác là 9,01 năm.)*

**Ứng dụng nhanh cho SME**: Lạm phát 7%/năm → sức mua của tiền mặt giảm một nửa sau khoảng $72/7 \approx 10{,}3$ năm. Một khoản vay lãi 18%/năm (thẻ tín dụng, vay tiêu dùng) sẽ làm nợ gấp đôi sau $72/18 = 4$ năm nếu không trả.

---

### B. Present Value (PV) – Giá trị hiện tại

#### 1. Định nghĩa
PV là giá trị **hiện tại** của một khoản tiền sẽ nhận được trong tương lai, được chiết khấu (discount) về hôm nay.

#### 2. Tại sao PV chính là "FV đảo ngược"? — Và tại sao gọi là "chiết khấu"
FV trả lời: "100 triệu hôm nay sẽ thành bao nhiêu sau $n$ năm?". PV trả lời câu ngược lại: "để có 500 triệu sau 5 năm, hôm nay cần bỏ ra bao nhiêu?" – nên chỉ cần chia (thay vì nhân) cho hệ số tích lũy. Lãi suất dùng ở đây gọi là **tỷ lệ chiết khấu (discount rate)**, vì nó "chiết" (giảm) giá trị của dòng tiền xa. Trong kinh doanh, tỷ lệ chiết khấu không phải lãi suất tiết kiệm đơn thuần mà là **tỷ suất sinh lời tối thiểu bạn đòi hỏi** cho mức rủi ro của khoản tiền đó (thường lấy bằng WACC hoặc chi phí vốn – xem file 03).

#### 3. Công thức

$$PV = \frac{FV}{(1 + r)^n} = FV \times (1 + r)^{-n}$$

#### 4. Bảng Discount Factor

| Năm | r = 5% | r = 8% | r = 10% | r = 12% | r = 15% |
|-----|--------|--------|---------|---------|---------|
| 1 | 0,9524 | 0,9259 | 0,9091 | 0,8929 | 0,8696 |
| 3 | 0,8638 | 0,7938 | 0,7513 | 0,7118 | 0,6575 |
| 5 | 0,7835 | 0,6806 | 0,6209 | 0,5674 | 0,4972 |
| 10 | 0,6139 | 0,4632 | 0,3855 | 0,3220 | 0,2472 |
| 20 | 0,3769 | 0,2145 | 0,1486 | 0,1037 | 0,0611 |
| 30 | 0,2314 | 0,0994 | 0,0573 | 0,0334 | 0,0151 |

→ Tiền càng xa tương lai, giá trị hiện tại càng nhỏ. 1 triệu sau 30 năm (r = 15%) chỉ đáng 15.100 VND hôm nay!

→ Cũng nhận thấy: **tỷ lệ chiết khấu càng cao, tác động lên dòng tiền xa càng mạnh** – ở r = 15% dòng tiền năm 10 chỉ còn 24,7%, còn ở r = 5% vẫn còn 61,4%. Đây là lý do các dự án có dòng tiền đến muộn (bất động sản, startup công nghệ) cực kỳ nhạy cảm với việc chọn tỷ lệ chiết khấu.

#### 5. Ví dụ thực tế

**Bài toán**: Đối tác hứa trả 500 triệu sau 5 năm. Discount rate = 10%. Giá trị thực hôm nay?

$$PV = \frac{500}{(1{,}10)^5} = \frac{500}{1{,}6105} = 310{,}46 \text{ triệu VND}$$

**Diễn giải**: Lời hứa 500 triệu sau 5 năm chỉ tương đương 310,46 triệu hôm nay. Nếu đối tác đề nghị "trả ngay 300 triệu thay vì chờ 5 năm" và bạn đòi hỏi lợi suất 10%/năm, thì đề nghị đó **gần như hợp lý** (300 < 310,46: bạn chịu thiệt nhẹ 10,46 triệu). Nếu họ đề xuất trả ngay 350 triệu thì bạn nên nhận.

---

### C. Annuity & Perpetuity – Chuỗi dòng tiền đều

#### 1. Tại sao cần công thức riêng?
Rất nhiều dòng tiền trong kinh doanh lặp lại đều đặn: tiền trả góp xe, tiền thuê mặt bằng, lương cố định, cổ tức ổn định, tiền hoàn vốn hàng tháng. Nếu tính từng khoản bằng công thức PV riêng, ví dụ khoản vay 60 tháng sẽ phải cộng 60 số hạng. **Annuity** (niên kim – chuỗi $n$ khoản trả bằng nhau, cách đều thời gian) có thể gộp thành một công thức rút gọn nhờ tổng cấp số nhân.

#### 2. Ordinary Annuity (Niên kim cuối kỳ)

$$PV_{Annuity} = PMT \times \frac{1 - (1+r)^{-n}}{r}$$

- $PMT$ = khoản thanh toán đều mỗi kỳ (payment), phát sinh vào **cuối** mỗi kỳ
- Thừa số $\frac{1 - (1+r)^{-n}}{r}$ gọi là **Annuity Factor**
- Nếu thanh toán ở **đầu** kỳ (Annuity Due – ví dụ tiền thuê nhà trả trước) thì nhân thêm $(1+r)$.

**FV của annuity** (dùng cho bài toán tiết kiệm định kỳ):

$$FV_{Annuity} = PMT \times \frac{(1+r)^n - 1}{r}$$

**Ví dụ PV**: Nhận 150 triệu mỗi năm cuối kỳ trong 5 năm, r = 10%.
$PV = 150 \times \frac{1 - 1{,}1^{-5}}{0{,}10} = 150 \times 3{,}7908 = 568{,}62$ triệu (trong khi tổng số học là 750 triệu – chênh lệch cho thấy rõ "chi phí thời gian").

**Ví dụ FV (tiết kiệm)**: Mỗi tháng trích 20 triệu vào quỹ tái đầu tư, lãi 6%/năm (0,5%/tháng), trong 60 tháng:
$FV = 20 \times \frac{(1{,}005)^{60} - 1}{0{,}005} = 20 \times 69{,}77 = 1.395{,}40$ triệu (tổng gốc bỏ ra 1.200 triệu, lãi 195,40 triệu).

#### 3. Perpetuity (Niên kim vĩnh viễn)

$$PV_{Perpetuity} = \frac{PMT}{r}$$

**Tại sao đơn giản vậy?** Khi $n \to \infty$, $(1+r)^{-n} \to 0$, nên annuity factor chỉ còn $1/r$. Trực giác: nếu gửi $X$ đồng lãi $r$%/năm thì mỗi năm nhận lãi $X \times r$ mà gốc nguyên vẹn – nên để nhận mãi $PMT$ mỗi năm, cần gốc $= PMT/r$. Ví dụ: muốn nhận mãi 144 triệu/năm (12 triệu/tháng) từ khoản đầu tư với lợi suất 12%/năm, cần gốc $144/0{,}12 = 1.200$ triệu.

#### 4. Growing Perpetuity – Mô hình Gordon (Gordon Growth Model)

$$PV = \frac{CF_1}{r - g} \quad (r > g)$$

- $CF_1$ = dòng tiền năm kế tiếp, $g$ = tốc độ tăng trưởng đều hằng năm (mãi mãi)
- **Nguồn gốc**: Myron Gordon (1959) phát triển mô hình này để định giá cổ phiếu có cổ tức tăng đều; nay là nền tảng của giá trị cuối kỳ (Terminal Value) trong DCF – xem file 10-corporate-valuation.
- **Điều kiện bắt buộc $r > g$**: nếu $g \ge r$ mô hình cho giá trị âm hoặc vô cực – vô nghĩa, vì không thể có doanh nghiệp tăng trưởng nhanh hơn nền kinh tế mãi mãi.
- **Ví dụ**: Dòng tiền năm 1 = 60 triệu, tăng 4%/năm, r = 14% → $PV = 60/(0{,}14-0{,}04) = 600$ triệu.

**Cảnh báo độ nhạy**: Cùng $CF_1 = 100$, $g = 3\%$: nếu $r = 8\%$ thì $PV = 2.000$; $r = 10\%$ thì $1.428{,}6$; $r = 12\%$ thì $1.111{,}1$. Chỉ thay đổi $r$ vài điểm % làm giá trị thay đổi gần 45% – bài học về độ nhạy của định giá với tỷ lệ chiết khấu (xem mục II.I).

---

### D. Net Present Value (NPV) – Giá trị hiện tại ròng

#### 1. Định nghĩa
NPV = Tổng PV của TẤT CẢ dòng tiền tương lai TRỪ đi vốn đầu tư ban đầu.

> **NPV là "Gold Standard" – chỉ số QUAN TRỌNG NHẤT trong quyết định đầu tư.**

#### 2. Tại sao NPV là tiêu chí tốt nhất? — Logic "tạo ra giá trị"
Một dự án chỉ đáng làm nếu nó tạo ra nhiều giá trị hơn số tiền bỏ vào. Nhưng "nhiều hơn" phải so sánh ở **cùng một thời điểm** – nên ta đưa mọi dòng tiền về hiện tại (bằng PV) rồi trừ đi vốn gốc. Tỷ lệ chiết khấu $r$ chính là lợi suất đòi hỏi: nếu NPV = 0, dự án vừa đủ sinh lời bằng chi phí vốn (không thiệt không lợi); NPV > 0 nghĩa là sau khi đã "trả công" đầy đủ cho vốn, vẫn còn thặng dư – thặng dư đó chính là **giá trị tăng thêm cho chủ sở hữu, tính bằng tiền hôm nay**. Điều này khác với "lợi nhuận kế toán" vốn bỏ qua giá trị thời gian và chi phí cơ hội của vốn.

**Nguồn gốc**: Ý tưởng NPV gắn với Irving Fisher (1930), người chứng minh rằng ở thị trường vốn hoàn hảo, mọi chủ sở hữu đều đồng ý chọn dự án có NPV cao nhất bất kể sở thích tiêu dùng cá nhân – "Fisher Separation Theorem".

#### 3. Công thức

$$NPV = -C_0 + \sum_{t=1}^{n} \frac{CF_t}{(1+r)^t}$$

- $C_0$ = vốn đầu tư ban đầu (t = 0), $CF_t$ = dòng tiền ròng năm $t$, $r$ = tỷ lệ chiết khấu (WACC hoặc lợi suất đòi hỏi), $n$ = vòng đời dự án.

#### 4. Quy tắc quyết định

```
NPV > 0  →  DỰ ÁN TẠO GIÁ TRỊ         →  ĐẦU TƯ ✅
NPV = 0  →  Hòa vốn (risk-adjusted)   →  TÙY CHIẾN LƯỢC ⚠️
NPV < 0  →  PHÁ HỦY GIÁ TRỊ           →  TỪ CHỐI ❌
```

#### 5. Ví dụ chi tiết – Mở chuỗi cà phê

| Năm | CF (triệu VND) | Discount Factor (r=12%) | PV (triệu VND) |
|-----|-----------------|------------------------|----------------|
| 0 | -500 | 1,0000 | -500,00 |
| 1 | +120 | 0,8929 | +107,14 |
| 2 | +150 | 0,7972 | +119,58 |
| 3 | +180 | 0,7118 | +128,12 |
| 4 | +200 | 0,6355 | +127,10 |
| 5 | +250 | 0,5674 | +141,84 |
| **NPV** | | | **+123,78** (≈ 123,80 nếu không làm tròn hệ số) |

**Diễn giải**: Tổng thu nhập 5 năm là 900 triệu (lãi số học 400 triệu), nhưng sau khi đòi hỏi lợi suất 12%/năm, giá trị tăng thêm thực chỉ còn khoảng 123,8 triệu quy về hôm nay. Dự án vẫn đáng làm.

#### 6. Tính chất cộng (Additivity) của NPV
NPV của hai dự án độc lập bằng tổng NPV từng dự án: $NPV(A+B) = NPV(A) + NPV(B)$. Đây là lý do NPV phù hợp với mục tiêu "tối đa hóa giá trị cho cổ đông" – các quyết định nhỏ cộng lại thành giá trị công ty (IRR không có tính chất này).

---

### E. Internal Rate of Return (IRR) và MIRR

#### 1. Định nghĩa
IRR là **tỷ lệ chiết khấu mà tại đó NPV = 0**. Đo "lãi suất thực" mà dự án tạo ra trên vốn đang đầu tư.

$$0 = -C_0 + \sum_{t=1}^{n} \frac{CF_t}{(1+IRR)^t}$$

#### 2. Tại sao nhà quản lý ưa chuộng IRR?
Con người dễ so sánh một tỷ lệ phần trăm ("dự án sinh lời 20%/năm") hơn một con số tuyệt đối ("NPV = 123,8 triệu"). IRR cho phép so sánh trực tiếp với lãi vay ngân hàng, WACC hay kỳ vọng của nhà đầu tư. **Quy tắc**: IRR > WACC (hoặc lợi suất đòi hỏi) → đầu tư ✅; IRR < WACC → từ chối ❌.

Không có công thức đóng cho IRR (phải giải phương trình đa thức bậc $n$), nên cần dò thử – trong Excel dùng hàm `=IRR()`.

#### 3. NPV Profile (Đường NPV theo tỷ lệ chiết khấu)

NPV Profile vẽ NPV của dự án theo các giá trị $r$ khác nhau; điểm cắt trục hoành chính là IRR. Với dự án cà phê ở mục D:

| r (tỷ lệ chiết khấu) | 5% | 8% | 12% | 15% | 18% | 22% | 25% |
|---|---|---|---|---|---|---|---|
| NPV (triệu) | 266,3 | 199,8 | 123,8 | 74,8 | 31,4 | -19,0 | -52,0 |

```
NPV (triệu)
 270│•
 200│   •
 124│       •←── r=12%: NPV=123,8
  75│           •
  31│              •
   0│──────────────────•──── ←── IRR ≈ 20,4%
 -52│                       •
    └─┬──┬──┬──┬──┬──┬──┬──→ r(%)
      5  8  12 15 18 22 25
```

*(Bản cũ ghi IRR ≈ 21,5%; kiểm tra lại cho kết quả chính xác 20,4%.)*

**Đọc biểu đồ**: Đường NPV dốc xuống vì $r$ tăng làm mọi PV nhỏ đi. IRR = 20,4% có nghĩa: nếu chi phí vốn của bạn dưới 20,4% thì dự án có lời; nếu hơn, dự án lỗ. Khoảng cách giữa IRR và WACC (ở đây 20,4% − 12% = 8,4%) gọi là **biên an toàn (margin of safety)**.

#### 4. Các "bẫy" của IRR (và vì sao NPV vẫn là chuẩn mực)

| Bẫy | Giải thích | Cách xử lý |
|---|---|---|
| **Multiple IRR** | Khi dòng tiền đổi dấu nhiều lần (ví dụ: -, +, -, +) phương trình có nhiều nghiệm → không biết IRR nào đúng | Dùng NPV hoặc MIRR |
| **Scale-blind (Mù quy mô)** | Dự án nhỏ IRR 50% (đầu tư 10 triệu) "hơn" dự án lớn IRR 25% (đầu tư 1 tỷ), nhưng NPV dự án lớn có thể cao hơn nhiều | So sánh NPV, hoặc NPV của dự án chênh lệch (incremental) |
| **Giả định tái đầu tư sai** | IRR ngầm giả định mọi dòng tiền trung gian được tái đầu tư đúng bằng IRR – phi thực tế với IRR rất cao | Dùng MIRR |
| **Xếp hạng mâu thuẫn với NPV** | Với dự án loại trừ nhau, IRR và NPV có thể xếp hạng ngược nhau | Tin NPV |

#### 5. MIRR (Modified IRR)
MIRR giải quyết giả định tái đầu tư của IRR bằng cách **gộp tất cả dòng tiền dương về FV tại cuối vòng đời với lãi suất tái đầu tư (thường là WACC)**, rồi tìm lãi suất biến vốn đầu tư (PV các dòng âm) thành FV đó:

$$MIRR = \left(\frac{FV_{\text{dòng tiền dương}}}{PV_{\text{dòng tiền âm}}}\right)^{1/n} - 1$$

Ví dụ ở case SME mục III.3: IRR = 19,27% nhưng MIRR (tái đầu tư ở 14%) = 17,22% – thấp hơn, thực tế hơn.

---

### F. Payback Period và Discounted Payback

- **Payback Period (Thời gian hoàn vốn)**: số năm để dòng tiền tích lũy bù lại vốn đầu tư, bỏ qua giá trị thời gian của tiền. Dễ hiểu, phổ biến với SME vì phản ánh "khi nào lấy lại vốn" và đo rủi ro thanh khoản.
- **Discounted Payback**: tương tự nhưng dùng dòng tiền đã chiết khấu – chính xác hơn, luôn dài hơn payback thường.

**Tại sao không nên dùng riêng Payback?** Nó bỏ qua toàn bộ dòng tiền sau ngày hoàn vốn (dự án thu 10 năm vs 3 năm có thể có payback bằng nhau) và (với bản không chiết khấu) bỏ qua giá trị thời gian. Dùng như bộ lọc rủi ro bổ sung cho NPV chứ không thay thế NPV.

---

### G. Lãi suất hiệu dụng (EAR) và Khoản vay trả góp (Loan Amortization)

#### 1. Vấn đề: "Lãi suất 11%/năm" thực ra là bao nhiêu?
Hai ngân hàng cùng ghi "lãi 8%/năm", nhưng một nơi ghép lãi theo năm, nơi kia theo tháng, thì chi phí/lợi suất thực khác nhau. **EAR (Effective Annual Rate – lãi suất hiệu dụng năm)** quy mọi lãi suất về cùng một cơ sở – cho phép so sánh công bằng:

$$EAR = \left(1 + \frac{APR}{m}\right)^{m} - 1$$

- APR (Annual Percentage Rate) = lãi suất danh nghĩa ghi trên hợp đồng; $m$ = số lần ghép lãi/năm.
- Ví dụ: 8% ghép tháng → $EAR = (1 + 0{,}08/12)^{12} - 1 = 8{,}30\%$; 12% ghép tháng → $12{,}68\%$; 12% ghép liên tục → $e^{0{,}12} - 1 = 12{,}75\%$.

**Đổi lãi suất năm sang tháng đúng cách**: nếu có EAR thì $r_{tháng} = (1 + EAR)^{1/12} - 1$; nếu chỉ có APR ghép tháng thì $r_{tháng} = APR/12$. Ví dụ EAR 14% → $r_{tháng} = 1{,}14^{1/12} - 1 = 1{,}0979\%$ (không phải 14%/12 = 1,1667%).

#### 2. Công thức khoản trả đều (PMT) cho khoản vay
Từ công thức PV của annuity, khoản vay $L$ trả đều $n$ kỳ với lãi suất kỳ $i$ thỏa $L = PMT \times \frac{1-(1+i)^{-n}}{i}$, suy ra:

$$PMT = L \times \frac{i}{1 - (1+i)^{-n}}$$

**Lý do khoản trả đều nhưng cơ cấu thay đổi**: mỗi kỳ, lãi = số dư nợ đầu kỳ × $i$; phần còn lại của PMT là trả gốc. Vì số dư nợ giảm dần nên lãi giảm, gốc tăng (xem bảng khấu hao nợ ở case III.3). Đây là khác biệt với phương pháp "lãi tính trên dư nợ ban đầu" (flat rate) – flat rate 11%/năm thực ra đắt gần gấp đôi (xem mục IV.2).

---

### H. Lãi suất danh nghĩa vs thực (Fisher Equation) – Xử lý lạm phát

#### 1. Vấn đề
Lãi suất 14%/năm có đáng giá khi lạm phát 4% không? Tiền thu về nhiều hơn nhưng mua được ít hơn. Để phản ánh sức mua, Irving Fisher (1930) đề xuất:

$$(1 + r_{nominal}) = (1 + r_{real}) \times (1 + \pi) \quad \Rightarrow \quad r_{real} = \frac{1 + r_{nominal}}{1 + \pi} - 1$$

- $\pi$ = tỷ lệ lạm phát. Ví dụ: $r_{nominal} = 14\%$, $\pi = 4\%$ → $r_{real} = 1{,}14/1{,}04 - 1 = 9{,}62\%$ (không phải 14% − 4% = 10% – xấp xỉ đơn giản chỉ đúng khi lãi và lạm phát nhỏ).

#### 2. Nguyên tắc nhất quán
- Dòng tiền **danh nghĩa** (đã gồm lạm phát, như giá bán tăng 5%/năm) → chiết khấu bằng tỷ lệ **danh nghĩa**.
- Dòng tiền **thực** (giữ giá cố định theo năm gốc) → chiết khấu bằng tỷ lệ **thực**.
- Trộn lẫn hai loại cho NPV sai lệch hệ thống: dòng tiền thực + tỷ lệ danh nghĩa → NPV bị đánh giá thấp; dòng tiền danh nghĩa + tỷ lệ thực → NPV bị thổi phồng.

---

### I. Phân tích độ nhạy (Sensitivity) – Đo mức độ tin cậy của NPV

NPV phụ thuộc vào hai nhóm đầu vào không chắc chắn: dòng tiền dự báo và tỷ lệ chiết khấu. Phân tích độ nhạy thay đổi từng đầu vào để xem NPV biến động ra sao, qua đó xác định biến số then chốt cần theo dõi. Cách làm cơ bản:
1. Lập bảng NPV theo lưới (CF × 80%/90%/100%) × (r thấp/cơ sở/cao) – xem case III.3 để biết ví dụ cụ thể.
2. Tìm **break-even** của từng biến số (ví dụ CF giảm bao nhiêu % thì NPV = 0).
3. Lập kịch bản Best/Base/Worst và gán xác suất để tính NPV kỳ vọng.

---

### J. Ưu điểm và nhược điểm của phương pháp NPV/IRR

#### ✅ Ưu điểm
1. **Gold standard** – Hầu hết các chương trình MBA và tập đoàn lớn sử dụng.
2. **Time value** – Phản ánh đúng: 1 đồng năm 1 ≠ 1 đồng năm 10.
3. **Risk-adjusted** – Tỷ lệ chiết khấu phản ánh rủi ro dự án.
4. **Additive** – NPV(A) + NPV(B) = NPV(Portfolio).
5. **Objective** – Dựa trên dòng tiền thực, không bị "make-up" bởi các quy ước kế toán (khấu hao, phân bổ).
6. **Wealth maximization** – NPV > 0 = tăng giá trị tài sản cổ đông.

#### ❌ Nhược điểm
1. **Phụ thuộc r** – Thay đổi r 2% → NPV có thể thay đổi 20–50%.
2. **Dự báo CF khó** – Dòng tiền 5–10 năm sai số lớn.
3. **Multiple IRR** – Dòng tiền đổi dấu nhiều lần → nhiều IRR (dùng MIRR/NPV).
4. **Scale-blind (IRR)** – Không tính đến quy mô dự án.
5. **Ignore intangibles** – Giá trị chiến lược, thương hiệu không nằm trong CF.
6. **Ignore flexibility** – Quyền mở rộng/trì hoãn (Real Options) không được định giá.

---

### K. Những lưu ý quan trọng khi áp dụng

#### 1. Sai lầm phổ biến

| Sai lầm | Cách tránh |
|---------|-----------|
| Dùng lãi suất danh nghĩa với dòng tiền thực (hoặc ngược lại) | Nhất quán: nominal + nominal HOẶC real + real |
| Tính cả sunk cost (chi phí đã chìm) | Sunk cost không liên quan, chỉ tính incremental CF |
| Chọn tỷ lệ chiết khấu "cảm tính" | Dùng WACC, CAPM, hoặc lãi suất vay + phần bù rủi ro |
| Lạc quan quá mức trong dự báo CF | Kiểm chứng độc lập, base case thận trọng |
| Quên thay đổi vốn lưu động | ΔWC là dòng tiền chi thực |
| Chỉ dùng một con số NPV duy nhất | Luôn làm sensitivity + scenario analysis |
| Nhầm lẫn thời điểm dòng tiền (đầu kỳ/cuối kỳ) | Vẽ timeline trước khi tính |
| Bỏ quên giá trị thanh lý cuối dự án | Đưa Salvage Value vào năm cuối |

#### 2. Best Practices

```
✅ NPV làm công cụ quyết định chính
✅ Kết hợp NPV + IRR + Payback
✅ Sensitivity Analysis (tornado diagram)
✅ Scenario Analysis (best/base/worst)
✅ Ghi chép MỌI giả định

❌ Chỉ dùng IRR một mình
❌ Giả định tỷ lệ chiết khấu không đổi mãi mãi
❌ Tin vào một con số NPV duy nhất
❌ Quên đánh giá sau đầu tư (post-investment audit)
```

---

## III. CASE STUDIES THỰC TẾ

### 1. Case Study Thành công: GRAB – "Đốt tiền" chiếm thị phần và bài toán NPV dài hạn

#### Bối cảnh
- 2012: Grab (trước là MyTeksi) ra đời tại Malaysia, sau mở rộng ra Đông Nam Á.
- 2014–2018: Chi hàng tỷ USD khuyến mãi (subsidy) cho tài xế và khách hàng để giành thị phần trước Uber và các đối thủ; dòng tiền ngắn hạn âm sâu.
- Năm 2017: Grab huy động khoảng 2 tỷ USD trở lên từ SoftBank và Didi (con số công bố và IRR kỳ vọng ~28% là ước tính từ bản cũ, chưa kiểm chứng được nguồn gốc).
- 12/2021: Niêm yết trên NASDAQ qua SPAC, vốn hóa lúc niêm yết khoảng 40 tỷ USD; Grab công bố Adjusted EBITDA dương lần đầu vào khoảng cuối 2023 (số liệu cần đối chiếu lại báo cáo của Grab).

*Lưu ý: bảng dòng tiền bên dưới là **mô hình minh họa (stylized)** do tác giả thiết kế để giải thích tư duy NPV, không phải số liệu nội bộ của Grab.*

#### Vấn đề: Làm thế nào để một nhà đầu tư chấp nhận dòng tiền âm 4 năm liền?
Nếu chỉ nhìn lợi nhuận kế toán, Grab "lỗ triền miên" và không đáng đầu tư. Nhưng NPV buộc nhà đầu tư hỏi: tổng giá trị hiện tại của các dòng tiền **cả đời dự án** (kể cả giá trị cuối kỳ) có lớn hơn vốn bỏ ra không? Với mô hình mạng lưới (network effects) – càng nhiều tài xế, khách càng chờ ít và càng đông – người thắng đầu tiên có thể thu "lợi nhuận độc quyền" kéo dài, nên dòng tiền đến muộn nhưng rất lớn.

#### Mô hình minh họa NPV (triệu USD, discount rate 15%)

Giả sử SoftBank rót vốn đợt đầu 2.000 và tiếp tục góp thêm trong các năm lỗ; dòng tiền tự do (FCF) cải thiện dần; cuối năm 10 có thể bán/niêm yết với giá trị cuối kỳ (TV):

| Năm | FCF | Hệ số chiết khấu 15% | PV |
|---|---|---|---|
| 0 | -2.000 | 1,0000 | -2.000,0 |
| 1 | -800 | 0,8696 | -695,7 |
| 2 | -800 | 0,7561 | -604,9 |
| 3 | -500 | 0,6575 | -328,8 |
| 4 | -200 | 0,5718 | -114,4 |
| 5 | +200 | 0,4972 | +99,4 |
| 6 | +500 | 0,4323 | +216,2 |
| 7 | +900 | 0,3759 | +338,3 |
| 8 | +1.300 | 0,3269 | +425,0 |
| 9 | +1.700 | 0,2843 | +483,2 |
| 10 | +2.100 | 0,2472 | +519,1 |
| **Tổng PV (chưa có TV)** | | | **−1.662,4** |

**Bước 1 – Chỉ xét dòng tiền hoạt động**: NPV = −1.662,4 → nếu không có giá trị cuối kỳ, dự án rõ ràng bị loại.
**Bước 2 – Thêm giá trị cuối kỳ (TV) tại năm 10**: PV(TV) = TV × 0,2472.
- TV = 8.000 → PV = 1.977,5 → NPV = −1.662,4 + 1.977,5 = **+315,1**.
- TV = 12.000 → NPV ≈ +1.303,8.
**Bước 3 – Tìm TV hòa vốn**: để NPV = 0 cần TV ≈ **6.725** triệu USD (= 1.662,4 / 0,2472).
**Bước 4 – IRR khi TV = 8.000**: ≈ 16,1% (cao hơn 15% chiết khấu – dự án vừa đủ có lời).

#### Diễn giải
- **Phần lớn giá trị đến từ tương lai xa**: PV(TV) chiếm trên 100% NPV – dự án chỉ có giá trị nếu Grab thật sự trở thành người dẫn đầu và duy trì được vị thế (quy mô giá trị cuối kỳ hợp lý).
- **Độ nhạy cực cao với discount rate**: với cùng TV = 8.000, NPV ở r = 12% là +1.328,9, ở r = 15% là +315,1 và ở r = 18% là −445,9. Chỉ thay đổi 3% tỷ lệ chiết khấu đảo ngược quyết định đầu tư.
- Kết quả thực tế: IPO NASDAQ 12/2021 với vốn hóa khoảng 40 tỷ USD (giá trị cao khi niêm yết nhưng sau đó vốn hóa giảm mạnh – cho thấy rủi ro của TV).

#### Bài học
1. **Tư duy NPV dài hạn** cho phép chấp nhận lỗ giai đoạn đầu nếu có cơ sở tin vào lợi thế cạnh tranh bền vững.
2. **Network effects** biến "đốt tiền" thành đầu tư vào tài sản vô hình có thể sinh lời cao – "Winner-take-most".
3. **Điều kiện để áp dụng tư duy này cho SME**: phải có (a) lợi thế quy mô/mạng lưới rõ ràng, (b) nguồn vốn đủ dài để chịu lỗ, (c) kịch bản thoát vốn xác định. Quán cà phê mới mở đốt tiền khuyến mãi mà không có lợi thế mạng lưới thì chỉ "đốt tiền" thật.

---

### 2. Case Study Thất bại: WeWork – NPV sai hoàn toàn vì đầu vào sai

#### Bối cảnh
- Mô hình: thuê dài hạn mặt bằng văn phòng (hợp đồng 10–15 năm), cải tạo, rồi cho thuê lại ngắn hạn (theo tháng) cho doanh nghiệp/freelancer.
- Định giá đỉnh khoảng 47 tỷ USD (đầu 2019, vòng gọi vốn của SoftBank) → IPO bị hoãn (9/2019) → định giá rơi mạnh → nộp đơn phá sản Chapter 11 (11/2023).

#### Cấu trúc rủi ro: Lệch pha giữa dòng tiền ra và dòng tiền vào
Dòng tiền ra (tiền thuê mặt bằng dài hạn, cố định) kéo dài hàng chục năm, trong khi dòng tiền vào (tiền thuê ngắn hạn) có thể biến mất rất nhanh khi kinh tế suy thoái. Đây là rủi ro dòng tiền không đối xứng mà NPV chỉ phản ánh được nếu mô hình đầu vào đúng.

#### Minh họa: Tại sao chọn discount rate quá thấp là sai lầm chí tử?
Cam kết thuê 60 triệu USD/năm trong 10 năm (annuity):
- Chiết khấu 6%: $PV = 60 \times \frac{1-1{,}06^{-10}}{0{,}06} = 441{,}6$ triệu USD.
- Chiết khấu 12%: $PV = 60 \times 5{,}6502 = 339{,}0$ triệu USD.
→ Dùng tỷ lệ thấp đánh giá giá trị hiện tại của dòng tiền *thu* cao hơn (và nghĩa vụ dài hạn nhẹ hơn). Chênh lệch 102,6 triệu USD (tương đương 30% khi so với PV ở 12%) chỉ vì chọn rate. Với công ty đang lỗ nặng, rủi ro rất cao, rate đúng phải cao hơn nhiều so với 10–12% mà mô hình lạc quan sử dụng.

#### Tại sao phân tích NPV của WeWork thất bại?
1. **Garbage In, Garbage Out** – Dòng tiền dự báo phi thực tế (tăng trưởng 50%+ mãi mãi).
2. **Discount rate quá thấp** – Dùng r = 10–12% cho công ty lỗ nặng, thay vì mức phản ánh rủi ro startup (20%+).
3. **Bỏ qua unit economics** – NPV từng địa điểm (location) có thể âm khi tính đủ chi phí thuê, cải tạo, tỷ lệ lấp đầy; nhân rộng thêm địa điểm chỉ nhân rộng khoản lỗ.
4. **Không có kịch bản xấu** – Chỉ có bull case, không stress-test với suy thoái, tỷ lệ lấp đầy giảm.
5. **"Community Adjusted EBITDA"** – chỉ số tự chế loại bỏ nhiều chi phí thực (marketing, chi phí bán hàng, một phần chi phí tổng hợp) khiến dòng tiền trông tốt hơn thực tế.

#### Bài học
- NPV chỉ tốt khi **đầu vào đúng**. Cần kiểm chứng độc lập và giả định thận trọng.
- Luôn xem xét **cấu trúc kỳ hạn** của dòng tiền ra/vào, không chỉ NPV tổng.
- Kiểm tra NPV trên **đơn vị cơ sở** (từng cửa hàng/địa điểm) trước khi nhân bản.
- Cảnh giác với các chỉ số "điều chỉnh" làm đẹp dòng tiền.

*(Số liệu định giá và thời điểm nêu trên theo thông tin công khai phổ biến; cần đối chiếu nguồn gốc khi trích dẫn chính thức.)*

---

### 3. Case Study SME: "Cà Phê Nhà Vườn Tây Nguyên" – Mở chi nhánh, chọn cách mua máy rang và vay vốn

#### Bối cảnh doanh nghiệp
Công ty TNHH Cà Phê Nhà Vườn Tây Nguyên (Buôn Ma Thuột, Đắk Lắk) – chuyên rang xay và bán cà phê đóng gói + quán cà phê tại chỗ. Cơ sở hiện hữu ổn định. Chủ doanh nghiệp, anh Hùng, đang cân nhắc 3 quyết định có liên quan đến Time Value of Money:

1. **Quyết định 1**: Mở chi nhánh tại TP.HCM, vốn đầu tư ban đầu **800 triệu**, dự báo dòng tiền 5 năm.
2. **Quyết định 2**: Mua máy rang công nghiệp – 3 phương án thanh toán.
3. **Quyết định 3**: Vay 300 triệu bổ sung vốn lưu động – hiểu cơ cấu trả nợ thực.

**Tỷ lệ chiết khấu**: Anh Hùng yêu cầu lợi suất tối thiểu **14%/năm** (lãi vay ngân hàng ~11%/năm cộng phần bù rủi ro mở thị trường mới ~3%). Lạm phát dự kiến 4%/năm.

#### Phần 1: Đánh giá dự án chi nhánh bằng NPV, IRR, MIRR và Payback

**Dữ liệu dòng tiền (triệu VNĐ)**:

| Năm | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Dòng tiền | −800 | +180 | +230 | +280 | +300 | +320 (hoạt động) + 100 (thanh lý thiết bị) = +420 |

**Bước 1 – Tính hệ số chiết khấu $1/(1{,}14)^t$ và PV từng năm**:
- Năm 1: $1/1{,}14 = 0{,}8772$ → $180 \times 0{,}8772 = 157{,}89$
- Năm 2: $1/1{,}14^2 = 0{,}7695$ → $230 \times 0{,}7695 = 176{,}98$
- Năm 3: $1/1{,}14^3 = 0{,}6750$ → $280 \times 0{,}6750 = 188{,}99$
- Năm 4: $1/1{,}14^4 = 0{,}5921$ → $300 \times 0{,}5921 = 177{,}62$
- Năm 5: $1/1{,}14^5 = 0{,}5194$ → $420 \times 0{,}5194 = 218{,}13$

**Bước 2 – Cộng PV các năm và trừ vốn đầu tư**:
- Tổng PV dòng tiền thu = 157,89 + 176,98 + 188,99 + 177,62 + 218,13 = **919,61**
- $NPV = -800 + 919{,}61 = \mathbf{+119{,}62}$ triệu VNĐ

**Bước 3 – Diễn giải NPV**: Tổng thu 5 năm là 1.410 triệu (lãi kế toán 610 triệu), nhưng giá trị tăng thêm thực – sau khi đã trả công đủ 14%/năm cho vốn – là khoảng **119,6 triệu quy về hôm nay**. NPV > 0 → dự án tạo giá trị.

**Bước 4 – Tính IRR** (dò tìm bằng Excel `=IRR()` hoặc thử-sai): NPV tại r = 18% là +26,46; tại r = 20% là −14,78 → IRR nằm giữa, ≈ **19,27%**. IRR (19,27%) > yêu cầu 14% → biên an toàn 5,27 điểm %.

**Bước 5 – Tính MIRR** (dòng tiền dương được tái đầu tư ở 14%):
- $FV = 180 \times 1{,}14^4 + 230 \times 1{,}14^3 + 280 \times 1{,}14^2 + 300 \times 1{,}14 + 420 = 1.770{,}66$
- $MIRR = (1.770{,}66/800)^{1/5} - 1 = \mathbf{17{,}22\%}$ → thấp hơn IRR vì thực tế không thể tái đầu tư tiền thu về với lãi 19,27%; MIRR là thước đo thực tế hơn.

**Bước 6 – Thời gian hoàn vốn**:

| Năm | CF | Lũy kế CF | PV (14%) | Lũy kế PV |
|---|---|---|---|---|
| 0 | −800 | −800 | −800,00 | −800,00 |
| 1 | +180 | −620 | +157,89 | −642,11 |
| 2 | +230 | −390 | +176,98 | −465,13 |
| 3 | +280 | −110 | +188,99 | −276,14 |
| 4 | +300 | +190 | +177,62 | −98,51 |
| 5 | +420 | +610 | +218,13 | +119,62 |

- Payback (thường): hoàn vốn giữa năm 3 và 4: $3 + 110/300 = \mathbf{3{,}37}$ năm.
- Discounted Payback: $4 + 98{,}51/218{,}13 = \mathbf{4{,}45}$ năm.
- Khoảng cách 1,08 năm giữa hai chỉ số cho thấy "chi phí thời gian" – nếu chỉ nhìn payback thường, anh Hùng sẽ tưởng hoàn vốn nhanh hơn thực tế.

**Bước 7 – Phân tích độ nhạy (NPV, triệu VNĐ)**:

| Dòng tiền thu / r | 12% | 14% | 16% |
|---|---|---|---|
| 100% dự báo | +172,3 | +119,6 | +71,1 |
| 90% dự báo | +75,1 | +27,7 | −16,0 |
| 80% dự báo | −22,1 | −64,3 | −103,1 |

**Diễn giải độ nhạy**: Chỉ cần dòng tiền thực tế thấp hơn dự báo 10% và chi phí vốn tăng lên 16%, dự án chuyển từ lời sang lỗ nhẹ (−16,0). Nếu doanh thu chỉ bằng 80% dự báo, dự án lỗ ở **mọi** mức chiết khấu trong bảng (kể cả 12%). Kết luận: dự án đáng làm nhưng *không dư dả an toàn*; anh Hùng cần kiểm chứng kỹ dự báo doanh thu (khảo sát thị trường TP.HCM, thử nghiệm điểm bán nhỏ) trước khi xuống tiền.

**Bước 8 – Quy đổi thực/danh nghĩa**: Lãi suất 14% danh nghĩa tương đương lãi thực $1{,}14/1{,}04 - 1 = \mathbf{9{,}62\%}$ khi lạm phát 4%. Nếu mô hình dòng tiền đã tính tăng giá bán hằng năm (danh nghĩa) thì dùng 14%; nếu dòng tiền giữ giá cố định thì phải dùng 9,62%, tránh trộn lẫn.

#### Phần 2: Chọn phương án thanh toán máy rang công nghiệp

Nhà cung cấp chào 3 phương án (giá niêm yết tương đương 600 triệu):

| Phương án | Điều kiện | Tổng tiền trả (danh nghĩa) |
|---|---|---|
| **A** | Trả tiền mặt ngay, giảm giá còn 540 triệu | 540 triệu |
| **B** | Trả góp 5 năm, mỗi cuối năm 150 triệu | 750 triệu |
| **C** | Trả góp 36 tháng, mỗi cuối tháng 19 triệu | 684 triệu |

*Nhìn nhanh theo tổng danh nghĩa, A < C < B. Nhưng đó là cách so sánh sai vì bỏ qua thời điểm trả tiền.*

**Bước 1 – Quy tất cả về giá trị hiện tại với chi phí vốn 14%/năm (EAR)**:
- **A**: PV = 540,00 (trả ngay).
- **B**: $PV = 150 \times \frac{1 - 1{,}14^{-5}}{0{,}14} = 150 \times 3{,}4331 = \mathbf{514{,}96}$ triệu.
- **C**: lãi suất tháng tương đương $r_m = 1{,}14^{1/12} - 1 = 1{,}0979\%$; $PV = 19 \times \frac{1 - (1{,}010979)^{-36}}{0{,}010979} = \mathbf{562{,}49}$ triệu.

**Bước 2 – So sánh**: B (514,96) < A (540,00) < C (562,49). **Phương án B có chi phí hiện tại thấp nhất**, rẻ hơn A khoảng 25 triệu, dù tổng danh nghĩa (750) cao nhất.

**Bước 3 – Tìm "lãi suất ẩn" mỗi phương án trả góp so với trả ngay 540**:
- B: giải $540 = 150 \times AF(r, 5)$ → $r = \mathbf{12{,}05\%/năm}$ – thấp hơn mức 14% anh Hùng kiếm được từ tiền → *nên mua trả góp*, giữ 540 triệu tiền mặt để đầu tư sinh lời 14%.
- C: giải $540 = 19 \times AF(r_m, 36)$ → $r_m = 1{,}338\%$/tháng → EAR $= 1{,}01338^{12} - 1 = \mathbf{17{,}29\%}$ (lãi danh nghĩa $12 \times 1{,}338\% = 16{,}06\%$) – cao hơn 14% → *không nên chọn*, nên trả tiền mặt (A) hoặc B.

**Kết luận Phần 2**: Chọn **phương án B**. Nếu anh Hùng không có khả năng sinh lời 14% từ tiền nhàn rỗi (chi phí vốn thấp, ví dụ 8%), thì A hấp dẫn hơn B. Quy tắc: **trả góp là rẻ khi lãi suất ẩn < chi phí cơ hội của tiền; đắt khi ngược lại**.

#### Phần 3: Khoản vay 300 triệu – 36 tháng, 11%/năm, trả đều hàng tháng

**Bước 1 – Lãi suất tháng**: $i = 11\%/12 = 0{,}9167\%$.
**Bước 2 – Khoản trả đều**: $PMT = 300 \times \frac{0{,}009167}{1 - (1{,}009167)^{-36}} = \mathbf{9{,}8216}$ triệu/tháng.
**Bước 3 – Tổng tiền lãi**: $9{,}8216 \times 36 - 300 = \mathbf{53{,}58}$ triệu.
**Bước 4 – EAR**: $(1 + 0{,}11/12)^{12} - 1 = \mathbf{11{,}57\%}$ – cao hơn lãi suất ghi trên hợp đồng 0,57 điểm %.

**Bước 5 – Bảng khấu hao nợ (triệu VNĐ)**:

| Tháng | Dư nợ đầu kỳ | Lãi (= dư nợ × 0,9167%) | Gốc (= PMT − lãi) | Dư nợ cuối kỳ |
|---|---|---|---|---|
| 1 | 300,000 | 2,750 | 7,072 | 292,928 |
| 2 | 292,928 | 2,685 | 7,136 | 285,792 |
| 12 | – | 2,003 | 7,818 | 210,729 |
| 24 | – | 1,099 | 8,723 | 111,127 |
| 36 | – | 0,089 | 9,732 | 0,000 |

**Tiền lãi theo năm**: Năm 1 = 28,59; Năm 2 = 18,26; Năm 3 = 6,73 (tổng 53,58).

**Diễn giải**: Khoản trả 9,82 triệu/tháng không đổi, nhưng tháng đầu 28% là lãi (2,75/9,82) còn tháng cuối chỉ 0,9% là lãi. Do đó nếu anh Hùng thanh toán sớm vào cuối năm 1, lãi tiết kiệm được lớn hơn nhiều so với thanh toán sớm vào năm thứ 3. Ngoài ra, kiểm tra: PV của 36 khoản trả ở 11%/12 = 300 triệu (khớp).

**Kiểm tra bằng TVM**: dùng EAR 14% (chi phí vốn của anh Hùng) chiết khấu 36 khoản 9,8216 → PV = 290,77 triệu < 300 triệu. Nghĩa là vay 300 triệu với lãi 11% rẻ hơn chi phí vốn 14% của anh Hùng khoảng 9,23 triệu về giá trị hiện tại – vay hợp lý nếu dùng vốn sinh lời hơn 11,57%.

**Phần 4 (bổ sung) – Quỹ tái đầu tư**: Trích 20 triệu/tháng vào quỹ lãi 6%/năm trong 60 tháng → FV = 1.395,4 triệu. Muốn đạt đúng mục tiêu 800 triệu sau 5 năm với cùng lãi suất, chỉ cần trích **11,47 triệu/tháng** ($800 / 69{,}77$).

#### Kết luận và Khuyến nghị hành động cho anh Hùng
1. **Mở chi nhánh**: NPV +119,6 triệu, IRR 19,27%, MIRR 17,22%, Payback 3,37 năm (chiết khấu 4,45 năm) → chấp nhận *có điều kiện*; kiểm chứng doanh thu năm 1 ≥ 90% dự báo vì ngưỡng an toàn mỏng.
2. **Mua máy rang**: chọn **phương án B** (trả góp 5 năm, PV 514,96 triệu) vì lãi ẩn 12,05% < chi phí vốn 14%; tránh phương án C (EAR 17,29%).
3. **Vay vốn lưu động**: chấp nhận khoản vay 300 triệu (EAR 11,57%) nếu có kế hoạch sử dụng vốn sinh lời > 11,57%; theo dõi bảng khấu hao nợ, ưu tiên trả sớm vào năm đầu để cắt lãi.
4. **Rủi ro cần theo dõi**: nếu lãi vay tăng hoặc doanh thu thấp 10%, NPV giảm mạnh (bảng độ nhạy).

---

## IV. ỨNG DỤNG CHO SME

### 1. Khi nào chủ SME cần tính TVM?

| Tình huống | Công cụ TVM | Câu hỏi cần trả lời |
|---|---|---|
| Mở chi nhánh, mua máy móc | NPV, IRR, Payback | Dự án có tạo giá trị trên chi phí vốn không? |
| Mua trả góp vs trả ngay | PV của chuỗi trả góp + tìm lãi ẩn | Trả góp đắt hay rẻ? |
| Vay ngân hàng | PMT, EAR, bảng khấu hao nợ | Chi phí vay thực sự là bao nhiêu? |
| Gửi tiết kiệm/quỹ dự phòng | FV, FV annuity | Cần góp bao nhiêu mỗi tháng để đạt mục tiêu? |
| Thuê vs mua mặt bằng | PV của tiền thuê vs giá mua | Phương án nào rẻ hơn về giá trị hiện tại? |
| Định giá doanh nghiệp/nhượng quyền | Perpetuity, Gordon Growth, DCF | Công ty đáng giá bao nhiêu? |
| Chiết khấu cho khách trả sớm | PV, EAR | Giảm giá 2% nếu trả trong 10 ngày thay vì 30 ngày có lợi không? |

### 2. Cảnh giác với lãi suất "flat" và chiết khấu thanh toán sớm

**Lãi suất flat (cố định trên dư nợ gốc)**: Nhiều công ty tài chính/trả góp quảng cáo "lãi 0,8%/tháng" hoặc "9,6%/năm" tính trên **số tiền vay ban đầu** suốt kỳ hạn. Ví dụ vay 300 triệu, 36 tháng, flat 11%/năm: lãi mỗi năm = 33 triệu, tổng lãi 99 triệu, trả đều $(300+99)/36 = 11{,}083$ triệu/tháng. Lãi suất thực tương ứng (giải từ dòng tiền 36 khoản × 11,083 triệu so với 300 triệu) là khoảng **19,6%/năm (APR), tức EAR ≈ 21,4%** – gần gấp đôi lãi suất ngân hàng dư nợ giảm dần cùng mức 11% (khoản trả 9,82 triệu). Luôn yêu cầu quy đổi sang EAR hoặc APR trên dư nợ giảm dần; kiểm tra bằng Excel `=RATE(36, -11.0833, 300)*12`.

**Chiết khấu thanh toán sớm "2/10 net 30"**: Nhà cung cấp cho giảm 2% nếu trả trong 10 ngày thay vì 30 ngày. Chi phí vốn hàm ý của việc *không* hưởng chiết khấu $= \frac{2}{98} \times \frac{365}{20} = 37{,}2\%$/năm (không ghép lãi) – rất đắt, nên nếu có tiền (hoặc vay được lãi suất thấp hơn nhiều) nên trả sớm để hưởng chiết khấu.

### 3. Chọn tỷ lệ chiết khấu thực tế cho SME

SME thường không có WACC chính thức. Cách ước lượng thực dụng:
1. Lãi vay ngân hàng bình quân của DN (ví dụ 10–12%/năm) làm mức sàn.
2. Cộng phần bù rủi ro theo mức độ không chắc chắn: dự án mở rộng sản phẩm hiện có +2–3%; thị trường mới +4–6%; ngành hoàn toàn mới/startup +8–15%.
3. Cân nhắc lợi suất thay thế: thay vì đầu tư dự án này, chủ DN có thể gửi tiết kiệm (~5–6%), mua vàng, hay trả bớt nợ vay (tiết kiệm chính lãi suất vay).
4. Kiểm tra độ nhạy ở r thấp/cao hơn 2 điểm % để chắc kết luận không đảo ngược.

### 4. Những sai lầm thường gặp của SME

| Sai lầm | Hậu quả | Cách tránh |
|---|---|---|
| So sánh tổng tiền danh nghĩa của các phương án trả góp | Chọn sai (ví dụ phương án C ở case SME) | Luôn quy về PV |
| Chỉ nhìn lợi nhuận kế toán, bỏ qua thời gian hoàn vốn | Thiếu vốn lưu động giữa chừng | Lập dòng tiền theo tháng, tính cả vốn lưu động |
| Dự báo doanh thu lạc quan, không kiểm tra độ nhạy | NPV âm khi thực tế kém 10% | Luôn làm bảng 3×3 độ nhạy |
| Dùng lãi suất ngân hàng ghi trên hợp đồng, không tính EAR | Đánh giá thấp chi phí vay | Tính EAR; xem phí phụ (bảo hiểm, phí thẩm định) |
| Quên giá trị thanh lý/giá trị còn lại | Đánh giá thấp dự án | Đưa vào năm cuối |
| Không điều chỉnh lạm phát | Trộn danh nghĩa/thực | Nhất quán |

---

## V. TOOLS & TEMPLATES

### 1. Hàm Excel / Google Sheets cho TVM

| Mục đích | Hàm | Ví dụ |
|---|---|---|
| FV | `=FV(rate, nper, pmt, [pv], [type])` | `=FV(0.08, 10, 0, -100)` → 215,89 |
| PV | `=PV(rate, nper, pmt, [fv], [type])` | `=PV(0.10, 5, 0, -500)` → 310,46 |
| NPV | `=NPV(rate, CF1:CFn) + CF0` | Chú ý: Excel `NPV()` chiết khấu từ kỳ 1, phải cộng CF0 riêng |
| IRR | `=IRR(CF0:CFn)` | `=IRR(B2:B7)` |
| MIRR | `=MIRR(values, finance_rate, reinvest_rate)` | `=MIRR(B2:B7, 0.11, 0.14)` |
| PMT | `=PMT(rate, nper, pv)` | `=PMT(0.11/12, 36, -300)` → 9,82 |
| Lãi suất ẩn | `=RATE(nper, pmt, pv)` | `=RATE(36, -19, 540)` → 1,338% |
| EAR | `=EFFECT(nominal_rate, npery)` | `=EFFECT(0.11, 12)` → 11,57% |
| Số kỳ | `=NPER(rate, pmt, pv)` | Tính số tháng trả hết nợ |
| Lãi / gốc từng kỳ | `=IPMT()`, `=PPMT()` | Lập bảng khấu hao nợ |

**Lỗi hay gặp**: dấu của PV/PMT phải ngược nhau (tiền chi âm, tiền thu dương); `NPV()` trong Excel không tính kỳ 0; đổi lãi suất năm sang tháng nhất quán.

### 2. Template bảng tính NPV/IRR đơn giản

```
Sheet "Assumptions":
  B1  Chi phí vốn (r)           14%
  B2  Lạm phát                  4%
  B3  Vốn đầu tư ban đầu        800 (triệu)

Sheet "Cashflow":
  Cột A: Năm (0..5)
  Cột B: Dòng tiền thu
  Cột C: Hệ số chiết khấu       =1/(1+Assumptions!$B$1)^A2
  Cột D: PV                     =B2*C2
  Cột E: Lũy kế CF              =SUM($B$2:B2)
  Cột F: Lũy kế PV              =SUM($D$2:D2)

  NPV    =SUM(D2:D7)
  IRR    =IRR(B2:B7)
  Payback=năm cuối có lũy kế âm + |lũy kế âm|/CF năm kế tiếp

Sheet "Sensitivity":
  Bảng 2 chiều (Data Table): hàng = r (10%..20%), cột = % CF (70%..110%) → NPV
```

### 3. Công cụ hỗ trợ khác
- **Máy tính tài chính** (HP 12C, Texas BA II Plus): dùng 5 phím N, I/Y, PV, PMT, FV.
- **Google Sheets**: dùng chung các hàm trên, miễn phí, chia sẻ với kế toán/ngân hàng.
- **Phần mềm kế toán** (MISA, Fast): xuất dữ liệu doanh thu, chi phí thực tế để lập dòng tiền dự báo chính xác.
- **Python** (`numpy_financial`): hàm `npv`, `irr`, `pmt` cho phân tích nhiều kịch bản (xem file 10-corporate-valuation).

---

## VI. BÀI TẬP THỰC HÀNH

### Bài 1 (Cơ bản – FV)
Bạn gửi 200 triệu VNĐ lãi 9%/năm ghép hằng năm trong 8 năm. Tính FV. Sau đó dùng Rule of 72 ước lượng sau bao nhiêu năm tiền gấp đôi, đối chiếu với kết quả chính xác.
*Gợi ý đáp số*: FV ≈ 398,51 triệu; Rule of 72: 8 năm; chính xác ≈ 8,04 năm.

### Bài 2 (Cơ bản – PV và lựa chọn)
Khách hàng đề nghị: (a) trả ngay 1.000 triệu, hoặc (b) 1.400 triệu sau 4 năm. Chi phí vốn của bạn là 8%/năm. Chọn phương án nào?
*Gợi ý*: PV(b) = 1.400 / 1,08⁴ ≈ 1.029,04 triệu > 1.000 → chọn (b), nhưng cân nhắc rủi ro khách không trả.

### Bài 3 (Trung bình – Annuity)
Mặt bằng cho thuê 12 triệu/tháng cố định mãi mãi. Nếu lợi suất đòi hỏi là 12%/năm (đổi sang 1%/tháng), giá trị hợp lý của mặt bằng là bao nhiêu? Nếu tiền thuê tăng 4%/năm thì sao (r = 14%/năm)?
*Gợi ý*: Perpetuity: 144 / 0,12 = 1.200 triệu; Gordon (CF₁ = 60, g = 4%, r = 14%) = 600 triệu.

### Bài 4 (Trung bình – NPV và IRR)
Dự án: vốn 300 triệu, dòng tiền năm 1–4 lần lượt 100, 120, 140, 160; r = 12%. Tính NPV, IRR và cho biết quyết định.
*Gợi ý đáp số*: NPV ≈ +23,54 triệu; IRR ≈ 23,96% → NPV > 0 và IRR > 12% → chấp nhận.

### Bài 5 (Trung bình – Vay)
Vay 500 triệu, lãi 12%/năm ghép tháng, 24 tháng. Tính PMT và EAR.
*Gợi ý đáp số*: PMT ≈ 23,54 triệu; EAR ≈ 12,68%.

### Bài 6 (Nâng cao – Mini Case: Quyết định mở rộng xưởng)
Dự án A: vốn 600 triệu, dòng tiền 200, 250, 300, 350 (năm 1–4), r = 10%. (a) Tính NPV, IRR. (b) Dòng tiền thực tế thấp hơn 15% — dự án có còn đáng làm không? (c) Nếu nhà cung cấp cho trả góp 4 năm × 170 triệu thay vì trả ngay 540 triệu, có nên chọn trả góp?
*Gợi ý đáp số (a)*: NPV ≈ +252,88 triệu; IRR ≈ 26,43%. (b) Với dòng tiền bằng 85% dự báo: NPV ≈ +124,95 triệu (vẫn dương). (c) PV của 4 × 170 triệu ở 10% ≈ 538,9 triệu ≈ 540 triệu: hai phương án gần như ngang nhau, lãi ẩn của trả góp xấp xỉ 10,1% – tự dùng `=RATE(4,-170,540)` để xác nhận.

### Bài 7 (Nâng cao – Tự thực hành với doanh nghiệp của bạn)
Chọn một quyết định thực tế (mua máy, mở điểm bán, vay vốn). Lập timeline, chọn tỷ lệ chiết khấu theo mục IV.3, tính NPV/IRR/Payback bằng Excel, lập bảng độ nhạy 3×3 và đưa ra khuyến nghị bằng văn bản một trang.

---

## PHỤ LỤC: CHECKLIST TIME VALUE OF MONEY TỔNG HỢP

### Công thức tổng hợp

| Công thức | Ý nghĩa |
|-----------|---------|
| $FV = PV(1+r)^n$ | Giá trị tương lai |
| $FV = PV(1+r/m)^{mn}$ | FV khi ghép lãi $m$ lần/năm |
| $FV = PV \cdot e^{rn}$ | Ghép lãi liên tục |
| $PV = FV/(1+r)^n$ | Giá trị hiện tại |
| $NPV = -C_0 + \sum CF_t/(1+r)^t$ | Giá trị hiện tại ròng |
| $0 = -C_0 + \sum CF_t/(1+IRR)^t$ | IRR – NPV = 0 |
| $MIRR = (FV_{+}/PV_{-})^{1/n} - 1$ | IRR điều chỉnh tái đầu tư |
| $PV_{annuity} = PMT \times [1-(1+r)^{-n}]/r$ | PV dòng tiền đều |
| $FV_{annuity} = PMT \times [(1+r)^n-1]/r$ | FV dòng tiền đều |
| $PV_{perpetuity} = PMT/r$ | PV dòng tiền vĩnh viễn |
| $PV_{growing} = CF_1/(r-g)$ | Gordon Growth Model |
| $PMT = L \times i/[1-(1+i)^{-n}]$ | Khoản trả đều của khoản vay |
| $EAR = (1+APR/m)^m - 1$ | Lãi suất hiệu dụng |
| $r_{real} = (1+r_{nom})/(1+\pi) - 1$ | Fisher Equation |
| Rule of 72: $n \approx 72/r\%$ | Thời gian gấp đôi |

### Checklist trước khi ra quyết định

**A. Chuẩn bị dữ liệu**
- □ Đã vẽ timeline với mọi dòng tiền (dấu + thời điểm đầu/cuối kỳ)
- □ Dòng tiền là dòng tiền ròng tăng thêm (incremental), không tính sunk cost
- □ Đã tính thay đổi vốn lưu động và giá trị thanh lý cuối kỳ
- □ Đơn vị thời gian của lãi suất và số kỳ đã nhất quán (tháng/năm)
- □ Danh nghĩa/thực đã nhất quán giữa dòng tiền và tỷ lệ chiết khấu

**B. Chọn tỷ lệ chiết khấu**
- □ Đã dựa vào WACC/CAPM hoặc lãi vay + phần bù rủi ro (không "cảm tính")
- □ Đã thử tỷ lệ chiết khấu cao/thấp hơn 2 điểm % để kiểm tra độ nhạy

**C. Tính toán & diễn giải**
- □ Đã tính NPV (tiêu chí chính) và IRR/MIRR (biên an toàn)
- □ Đã tính cả Payback và Discounted Payback
- □ Đã so sánh các phương án trả góp bằng PV và tính lãi ẩn, không so tổng tiền danh nghĩa
- □ Đã quy đổi lãi suất vay sang EAR, kiểm tra loại lãi suất (flat hay dư nợ giảm dần)
- □ Đã lập bảng khấu hao nợ cho khoản vay lớn

**D. Kiểm tra rủi ro**
- □ Đã làm bảng độ nhạy (CF × r) và kịch bản Best/Base/Worst
- □ Đã kiểm tra NPV trên đơn vị cơ sở (từng cửa hàng/sản phẩm) trước khi nhân bản
- □ Đã đối chiếu giả định dự báo với dữ liệu thực tế/kiểm chứng độc lập
- □ Đã xem xét giá trị chiến lược và tùy chọn mà NPV không phản ánh

**E. Sau quyết định**
- □ Đã ghi lại toàn bộ giả định để đối chiếu sau
- □ Đã đặt lịch đánh giá sau đầu tư (post-investment audit) 6–12 tháng

---

*Tài liệu tham khảo: Brealey, Myers & Allen "Principles of Corporate Finance" 14th Ed; Damodaran "Applied Corporate Finance" 4th Ed; CFA Level I – Quantitative Methods*
