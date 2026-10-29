# Capital Structure – Cơ Cấu Vốn (Modigliani-Miller)

> **Mục tiêu**: Hiểu lý thuyết cơ cấu vốn tối ưu, Modigliani-Miller, Trade-off Theory, Pecking Order Theory và ứng dụng thực tiễn trong quyết định tài trợ cho doanh nghiệp, đặc biệt là SME Việt Nam.

---

## I. KHÁI NIỆM & LÝ THUYẾT

### 1. Định nghĩa

**Capital Structure** (Cơ cấu vốn) là **tỷ lệ phối hợp giữa NỢ (Debt) và VỐN CHỦ SỞ HỮU (Equity)** mà doanh nghiệp sử dụng để tài trợ cho hoạt động và đầu tư.

> **Câu hỏi cốt lõi**: DN nên vay bao nhiêu và huy động vốn cổ đông bao nhiêu? Có tỷ lệ D/E TỐI ƯU để tối thiểu hóa WACC (chi phí sử dụng vốn bình quân) và tối đa hóa giá trị doanh nghiệp hay không?

Đây là một trong những câu hỏi lâu đời và gây tranh cãi nhất trong Tài chính doanh nghiệp (Corporate Finance). Trước năm 1958, giới thực hành tin rằng tồn tại một cơ cấu vốn "tối ưu" dựa trên trực giác đơn giản: vay nợ rẻ hơn vốn cổ phần (vì lãi vay được khấu trừ thuế và trái chủ ít rủi ro hơn cổ đông), nên cứ tăng dần tỷ lệ nợ sẽ luôn làm giảm chi phí vốn bình quân — cho đến khi hai nhà kinh tế học Franco Modigliani và Merton Miller công bố một nghiên cứu mang tính cách mạng, chứng minh bằng toán học rằng trực giác đó không hoàn toàn đúng trong một thế giới lý tưởng.

### 2. Debt vs Equity

| Tiêu chí | Debt (Nợ) | Equity (Vốn CSH) |
|----------|----------|------------------|
| **Bản chất** | Vay, bắt buộc trả gốc + lãi theo lịch đã cam kết | Góp vốn, không bắt buộc hoàn trả |
| **Chi phí** | Lãi suất cố định (hoặc thả nổi theo hợp đồng) | Cổ tức + capital gain (biến động, không cam kết) |
| **Tax** | Lãi vay khấu trừ thuế ✅ | Cổ tức KHÔNG khấu trừ thuế ❌ |
| **Rủi ro cho DN** | Cao (phá sản nếu không trả được) | Thấp (không bắt buộc trả cổ tức) |
| **Quyền kiểm soát** | Không pha loãng quyền sở hữu (ownership) | Pha loãng quyền sở hữu |
| **Chi phí vốn** | Thấp hơn (Kd < Ke, vì rủi ro thấp hơn) | Cao hơn (Ke > Kd, vì rủi ro cao hơn, nhận sau cùng) |
| **Thứ tự ưu tiên khi phá sản (Priority)** | Trả TRƯỚC khi thanh lý tài sản | Nhận phần còn lại SAU CÙNG (residual claim) |

### 3. Bối cảnh lịch sử: Vì sao định lý Modigliani-Miller (MM) lại là một cột mốc Nobel kinh tế?

Năm 1958, Franco Modigliani (nhà kinh tế học người Mỹ gốc Ý) và Merton Miller công bố bài báo "The Cost of Capital, Corporation Finance and the Theory of Investment" trên American Economic Review. Đây là giai đoạn mà lý thuyết tài chính doanh nghiệp còn rất sơ khai, chủ yếu dựa trên kinh nghiệm thực hành (rule of thumb) hơn là mô hình toán học chặt chẽ.

Điều khiến công trình của MM mang tính đột phá là cách tiếp cận: thay vì hỏi "cơ cấu vốn nào tốt nhất?", họ đặt câu hỏi ngược lại — "trong điều kiện nào thì cơ cấu vốn KHÔNG quan trọng?" — rồi chứng minh bằng lập luận arbitrage (kinh doanh chênh lệch giá): nếu hai doanh nghiệp giống hệt nhau về tài sản và dòng tiền nhưng có cơ cấu vốn khác nhau lại có giá trị thị trường khác nhau, nhà đầu tư có thể vay cá nhân để tự tạo đòn bẩy (homemade leverage) và kiếm lợi nhuận phi rủi ro từ chênh lệch giá đó — cho đến khi giá trị hai doanh nghiệp bị kéo về bằng nhau. Đây chính là nền móng cho toàn bộ trường phái "định giá không có arbitrage" (no-arbitrage pricing) sau này, ảnh hưởng tới cả định giá quyền chọn (Black-Scholes) và nhiều lĩnh vực tài chính hiện đại khác.

Merton Miller nhận giải Nobel Kinh tế năm 1990 (cùng Harry Markowitz và William Sharpe) một phần lớn nhờ công trình này; Franco Modigliani nhận giải Nobel Kinh tế năm 1985 (chủ yếu cho lý thuyết vòng đời thu nhập — Life-Cycle Hypothesis — nhưng định lý MM cũng là một trong các đóng góp được ghi nhận). Việc một lý thuyết tưởng chừng "phi thực tế" (vì giả định thị trường hoàn hảo) lại trở thành nền tảng của toàn bộ môn Tài chính doanh nghiệp hiện đại cho thấy giá trị thực sự của MM không nằm ở kết luận "cơ cấu vốn không quan trọng", mà nằm ở việc nó chỉ rõ **chính xác những yếu tố nào** (thuế, chi phí phá sản, bất cân xứng thông tin, chi phí đại diện) khiến cơ cấu vốn trở nên quan trọng trong thế giới thực — và đó chính là nội dung của 4 lý thuyết còn lại.

### 4. Các lý thuyết chính

```
┌──────────────────────────────────────────────────────────────┐
│              CÁC LÝ THUYẾT CƠ CẤU VỐN                        │
├──────────────────────────────────────────────────────────────┤
│                                                                │
│  1. MODIGLIANI-MILLER (1958, 1963)                            │
│     → Capital structure irrelevance (no tax)                  │
│     → Tax shield makes debt valuable (with tax)               │
│                                                                │
│  2. TRADE-OFF THEORY                                          │
│     → Optimal D/E = Balance tax shield vs distress costs      │
│                                                                │
│  3. PECKING ORDER THEORY (Myers & Majluf, 1984)               │
│     → Internal funds > Debt > Equity (info asymmetry)         │
│                                                                │
│  4. MARKET TIMING THEORY (Baker & Wurgler, 2002)              │
│     → Issue equity when overvalued, debt when undervalued     │
│                                                                │
│  5. AGENCY THEORY (Jensen, 1986)                              │
│     → Debt disciplines managers (reduce free cash flow)       │
│                                                                │
└──────────────────────────────────────────────────────────────┘
```

Không có lý thuyết nào đúng tuyệt đối trong mọi hoàn cảnh — mục II sẽ đi sâu vào từng lý thuyết, giải thích **tại sao** mỗi công thức được xây dựng như vậy, và mục II.K sẽ tổng hợp lại "khi nào nên dùng lý thuyết nào".

---

## II. CHI TIẾT TỪNG THÀNH PHẦN

### A. M&M Proposition I – Without Taxes (1958)

#### Statement
> Trong thị trường hoàn hảo (no taxes, no bankruptcy costs, no asymmetric info), **giá trị doanh nghiệp KHÔNG phụ thuộc vào cơ cấu vốn**.

$$V_L = V_U$$

- $V_L$ = Value of levered firm (có nợ)
- $V_U$ = Value of unlevered firm (không nợ)

#### Tại sao công thức lại đơn giản là "bằng nhau"? — Trực giác "cái bánh pizza"

Hãy tưởng tượng giá trị doanh nghiệp giống như một chiếc bánh pizza có kích thước cố định, được quyết định hoàn toàn bởi khả năng sinh lời của **tài sản hoạt động** (operating assets) — tức là khả năng tạo ra dòng tiền từ hoạt động kinh doanh cốt lõi. Cơ cấu vốn (vay bao nhiêu, vốn chủ bao nhiêu) chỉ là cách CHIA chiếc bánh đó ra cho hai nhóm người nhận: chủ nợ (trái chủ) và cổ đông. "Cắt pizza thành 4 miếng hay 8 miếng không làm thay đổi kích thước pizza" — dù bạn vay 30% hay 70% tổng vốn, tổng dòng tiền mà tài sản tạo ra (và do đó tổng giá trị phân phối cho nhà đầu tư) KHÔNG đổi, miễn là không có ma sát thị trường (thuế, chi phí phá sản, bất cân xứng thông tin). MM chứng minh điều này bằng lập luận arbitrage: nếu một nhà đầu tư thấy công ty có đòn bẩy (levered) rẻ hơn công ty không đòn bẩy một cách bất hợp lý, họ có thể tự vay tiền cá nhân (homemade leverage) để tái tạo chính xác cấu trúc rủi ro mong muốn và kiếm lời phi rủi ro — hành vi arbitrage này sẽ kéo giá hai công ty về bằng nhau trong một thị trường hiệu quả.

#### Assumptions (Rất quan trọng!)
1. No taxes
2. No bankruptcy/distress costs
3. No transaction costs
4. Symmetric information
5. Individuals can borrow at same rate as firms
6. No agency costs

→ **Trong thực tế**: KHÔNG có giả định nào đúng 100% → M&M I là benchmark lý thuyết, không phải lời khuyên thực hành. Giá trị của nó nằm ở việc nó là "đường cơ sở" (baseline) để từ đó ta đo lường tác động của từng yếu tố thực tế (thuế, chi phí phá sản...) khi lần lượt gỡ bỏ các giả định — chính là cách tiếp cận của các mục B, C, D dưới đây.

---

### B. M&M Proposition II – Without Taxes

$$K_e = K_0 + (K_0 - K_d) \times \frac{D}{E}$$

- $K_0$ = Cost of capital of all-equity firm (unlevered)
- $K_e$ tăng tuyến tính (linear) theo tỷ lệ D/E

#### Tại sao Ke lại tăng TUYẾN TÍNH theo D/E? — Giải thích trực giác bằng rủi ro tài chính

Nếu M&M I nói rằng WACC (chi phí vốn bình quân, ký hiệu $K_0$ khi chưa có nợ) không đổi khi thay đổi cơ cấu vốn, thì câu hỏi tự nhiên là: tại sao Kd không đổi (lãi vay ngân hàng cố định theo hợp đồng) nhưng WACC vẫn giữ nguyên dù tỷ trọng nợ rẻ tăng lên? Câu trả lời: vì Ke (chi phí vốn chủ) phải tăng lên để "bù lại" đúng phần lợi ích từ vay rẻ.

Cơ chế đằng sau: khi doanh nghiệp vay nợ, cổ đông gánh thêm một loại rủi ro mới gọi là **rủi ro tài chính (financial risk)** — rủi ro này cộng thêm vào rủi ro kinh doanh sẵn có (business risk) của tài sản. Cụ thể, chủ nợ luôn được trả lãi và gốc TRƯỚC, nên dòng tiền còn lại cho cổ đông trở nên biến động mạnh hơn (giống hệt cơ chế khuếch đại ở mục II.I - EBIT-EPS Analysis bên dưới). Nhà đầu tư, theo nguyên lý CAPM (mục II.F), luôn đòi hỏi lợi nhuận kỳ vọng cao hơn khi rủi ro cao hơn — vì vậy Ke phải tăng đúng bằng phần bù rủi ro tài chính tăng thêm, và phần bù này tỷ lệ thuận với D/E (vay càng nhiều so với vốn chủ, rủi ro tài chính dồn lên phần vốn chủ còn lại càng lớn). Về mặt toán học, đây chính xác là phần bù $(K_0 - K_d) \times D/E$ trong công thức — khoảng cách giữa chi phí vốn tài sản và chi phí nợ, nhân với đòn bẩy D/E.

#### Biểu đồ

```
Cost of Capital
  │
  │         Ke ↗ (tăng linear với D/E)
  │       ╱
  │     ╱
  │   ╱
  │─╱──────────── K₀ (WACC = constant!)
  │╱
  │─────────────── Kd (constant)
  │
  └──────────────────────→ D/E ratio

WACC = KHÔNG ĐỔI (vì Ke tăng exactly offset lợi ích debt rẻ hơn)
→ Leverage tăng Ke đủ để offset Kd thấp → WACC flat
```

---

### C. M&M Proposition I – With Taxes (1963) + Tax Shield

$$V_L = V_U + T \times D$$

- **Tax Shield** = $T \times D$ = Giá trị hiện tại của lá chắn thuế từ nợ vay
- Debt TẠO GIÁ TRỊ vì lãi vay được khấu trừ thuế!

#### Tại sao gỡ bỏ giả định "no taxes" lại thay đổi hoàn toàn kết luận?

Năm 1963, chính MM tự sửa lại công trình năm 1958 của mình sau khi nhận ra: khi đưa thuế thu nhập doanh nghiệp vào mô hình, kết luận "cơ cấu vốn không quan trọng" sụp đổ. Lý do rất đơn giản — cơ quan thuế đối xử không công bằng giữa hai hình thức chi trả cho nhà đầu tư: lãi vay trả cho trái chủ được tính là CHI PHÍ (khấu trừ trước thuế), còn cổ tức trả cho cổ đông được tính SAU thuế. Nói cách khác, chính phủ đang "trợ cấp" một phần cho doanh nghiệp đi vay nợ, dưới dạng giảm thuế phải nộp. Khoản trợ cấp này, tính theo giá trị hiện tại, chính xác bằng $T \times D$ (thuế suất nhân với số nợ) — vì nếu nợ duy trì vĩnh viễn, tiết kiệm thuế hàng năm là $T \times K_d \times D$, chiết khấu về hiện tại với lãi suất $K_d$ sẽ triệt tiêu $K_d$ ở tử và mẫu, còn lại đúng $T \times D$.

#### Ví dụ

DN có EBIT = 100 tỷ, T = 20%:

| | All-Equity (VU) | 50% Debt (VL) |
|-|-----------------|---------------|
| EBIT | 100 | 100 |
| Interest (D=500, Kd=8%) | 0 | -40 |
| EBT | 100 | 60 |
| Tax (20%) | -20 | -12 |
| Net Income | 80 | 48 |
| + Interest to debtholders | 0 | +40 |
| **Total to all investors** | **80** | **88** |

→ Total CF tăng 8 tỷ = Tax Shield = 40 × 20% = 8 tỷ/năm

$$PV(Tax Shield) = \frac{T \times K_d \times D}{K_d} = T \times D = 20\% \times 500 = 100 \text{ tỷ}$$

#### Implication
**Theo M&M with taxes**: nếu chỉ nhìn thuần công thức này, 100% nợ sẽ maximize giá trị doanh nghiệp!

→ Nhưng thực tế KHÔNG doanh nghiệp nào dùng 100% nợ, vì MM (1963) vẫn giả định KHÔNG có chi phí phá sản — và đây chính là giả định sẽ bị gỡ bỏ tiếp theo ở Trade-Off Theory.

---

### D. Trade-Off Theory

$$V_L = V_U + PV(Tax\ Shield) - PV(Financial\ Distress\ Costs)$$

#### Tại sao cần "đánh đổi" (trade-off)? — Gỡ bỏ giả định cuối cùng của MM

Trade-Off Theory ra đời như một câu trả lời trực tiếp cho nghịch lý "100% nợ là tối ưu" ở mục C. Trong thực tế, nợ càng cao, xác suất doanh nghiệp không trả được nợ (default) càng lớn, và khi xác suất này đủ lớn, doanh nghiệp phải gánh thêm **chi phí kiệt quệ tài chính (financial distress costs)** — không chỉ là chi phí pháp lý khi phá sản, mà còn là thiệt hại gián tiếp còn lớn hơn: khách hàng rời bỏ (vì sợ công ty không còn bảo hành/giao hàng được), nhà cung cấp đòi thanh toán ngay/ siết công nợ, nhân tài giỏi bỏ đi tìm nơi ổn định hơn. Trade-Off Theory đưa ra một công thức cân bằng hai lực đối nghịch: lợi ích thuế (tăng theo D) và chi phí kiệt quệ (tăng nhanh hơn theo D khi D vượt một ngưỡng nào đó) — điểm mà tại đó lợi ích biên của tax shield bằng đúng chi phí biên của distress cost chính là cơ cấu vốn tối ưu D/E*.

#### Biểu đồ Trade-Off

```
Firm Value (V)
  │
  │           VL = VU + Tax Shield (M&M with tax)
  │          ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
  │        ╱     ╭─── Optimal!
  │      ╱     ╱│ ╲
  │    ╱     ╱  │   ╲   ← PV(Distress) tăng
  │  ╱    ╱    │     ╲
  │╱───────────│───────╲──── VU (no debt)
  │            │         ╲
  │       Optimal         ╲
  │        D/E*              ╲
  └────────────┼──────────────╲──→ D/E ratio
               │
          Tax Shield = Distress Cost at margin
```

#### Financial Distress Costs

| Loại | Ví dụ | Estimate |
|------|-------|----------|
| **Direct** | Legal fees, court costs, accountants | 3-5% firm value |
| **Indirect** | Customer loss, supplier tightening, talent flight | 10-20% firm value |
| **Agency** | Risk shifting, underinvestment, asset stripping | 5-10% firm value |

#### Optimal Capital Structure

$$Optimal\ D/E:\ nơi\ marginal\ tax\ shield = marginal\ distress\ cost$$

Typical optimal ranges by industry:

| Industry | Optimal D/E | Lý do |
|----------|------------|-------|
| Utilities | 60-70% debt | Stable CF, tangible assets |
| Real Estate | 50-60% debt | Asset-backed, predictable income |
| Manufacturing | 30-50% debt | Moderately stable, tangible |
| Technology | 0-20% debt | Volatile, intangible assets |
| Biotech/Startup | 0-5% debt | No revenue, burning cash |

Lưu ý quan trọng: để biết D/E hiện tại đang ở phía bên trái hay bên phải điểm tối ưu, doanh nghiệp cần công cụ TÍNH TOÁN cụ thể — đó chính là hai công cụ WACC và CAPM ở mục E và F dưới đây. Hai công cụ này không chỉ phục vụ riêng Trade-Off Theory mà là nền tảng tính toán dùng chung cho MỌI lý thuyết cơ cấu vốn đã nêu ở trên.

---

### E. Cách tính WACC (Weighted Average Cost of Capital – Chi phí sử dụng vốn bình quân gia quyền)

Chi phí sử dụng vốn bình quân gia quyền (WACC) là tỷ suất sinh lời tối thiểu mà một doanh nghiệp phải đạt được để làm hài lòng tất cả các nhà cung cấp vốn, bao gồm cả chủ nợ và cổ đông.

Hiểu đơn giản, nếu WACC của doanh nghiệp là 10%, nghĩa là cứ huy động được 100 đồng vốn (gồm cả vay lẫn góp), doanh nghiệp phải làm ra khoản lợi nhuận ít nhất là 10 đồng để trả chi phí cho các nguồn vốn đó. Nếu làm ra ít hơn 10%, doanh nghiệp đang lỗ về mặt kinh tế dù trên sổ sách có thể vẫn có lãi kế toán.

#### Công thức tính WACC tổng quát

Để tính WACC, ta tính chi phí của từng nguồn vốn riêng lẻ, sau đó nhân với tỷ trọng của nó trong tổng cơ cấu vốn:

$$\text{WACC}=\left(\frac{D}{V}\times r_{d}\times (1-T)\right)+\left(\frac{E}{V}\times r_{e}\right)$$

Trong đó:
- $E$ (Equity): Giá trị thị trường của Vốn chủ sở hữu.
- $D$ (Debt): Giá trị thị trường của Vốn vay.
- $V$ (Total Value): Tổng vốn của doanh nghiệp ($V = E + D$).
- $\frac{E}{V}$ và $\frac{D}{V}$: Tỷ trọng của vốn chủ sở hữu và vốn vay trong cơ cấu vốn.
- $r_{d}$ (Cost of Debt): Chi phí sử dụng vốn vay (Lãi suất vay ngân hàng hoặc trái phiếu).
- $T$ (Tax rate): Thuế suất thuế thu nhập doanh nghiệp. (Lưu ý: Đoạn $(1 - T)$ chính là việc tính toán Lá chắn thuế vì lãi vay giúp giảm thuế, làm chi phí vay thực tế rẻ hơn — xem lại mục II.C).
- $r_{e}$ (Cost of Equity): Chi phí sử dụng vốn chủ sở hữu (Mức sinh lời kỳ vọng của cổ đông).

#### Ví dụ thực tế: Tính WACC cho quán cà phê

Quán cà phê có tổng vốn đầu tư là 1 tỷ đồng. Chủ quán thiết lập cơ cấu vốn như sau:
- Vốn vay ($D$): Vay ngân hàng 400 triệu với lãi suất ($r_{d}$) là 10%/năm.
- Vốn chủ sở hữu ($E$): Tự bỏ ra 600 triệu. Cổ đông kỳ vọng mức sinh lời ($r_{e}$) là 15%/năm (vì tự bỏ tiền ra kinh doanh rủi ro hơn gửi ngân hàng nên đòi hỏi lời nhiều hơn).
- Thuế thu nhập doanh nghiệp ($T$): 20%.

**Bước 1: Tính tỷ trọng nguồn vốn**
- Tỷ trọng Vốn vay ($\frac{D}{V}$) = 400 triệu / 1 tỷ = 40% (0,4)
- Tỷ trọng Vốn chủ ($\frac{E}{V}$) = 600 triệu / 1 tỷ = 60% (0,6)

**Bước 2: Tính chi phí vay sau thuế**
- Chi phí vay thực tế = $10\% \times (1 - 0,2) = \mathbf{8\%}$ (Nhờ giảm thuế 20%, chi phí vay thực tế giảm từ 10% xuống 8%)

**Bước 3: Ráp vào công thức WACC**
- $\text{WACC} = (0,4 \times 8\%) + (0,6 \times 15\%)$
- $\text{WACC} = 3,2\% + 9\% = \mathbf{12,2\%}$

Kết luận: Quán cà phê này có WACC là 12,2%. Khi chọn dự án đầu tư hoặc tính toán hiệu quả kinh doanh, quán phải tạo ra tỷ suất lợi nhuận trên tổng vốn (ROIC) lớn hơn 12,2% thì mới được coi là có lãi và gia tăng giá trị.

#### Ý nghĩa của WACC đối với Giám đốc tài chính (CFO)

Nhiệm vụ trọng tâm của CFO là tìm ra cơ cấu vốn tối ưu (theo Trade-Off Theory ở mục D) để kéo WACC xuống mức thấp nhất có thể. WACC chính là "mẫu số" dùng để so sánh với PV(Tax Shield) và PV(Distress Cost): mỗi lần tăng D/E, WACC giảm nhờ Kd rẻ hơn Ke, nhưng đồng thời rủi ro phá sản tăng dần làm cả Kd và Ke bị đẩy lên (premium rủi ro) — điểm WACC đạt đáy nhỏ nhất chính là điểm D/E tối ưu theo Trade-Off Theory. WACC càng thấp, giá trị doanh nghiệp càng cao và các dự án đầu tư càng dễ mang lại lợi nhuận ròng lớn hơn cho chủ sở hữu.

---

### F. Cách xác định Chi phí vốn chủ sở hữu theo mô hình CAPM

Việc tính Chi phí vốn chủ sở hữu ($r_{e}$) là phần đau đầu nhất đối với các chuyên gia tài chính. Ngân hàng cho vay luôn ghi rõ lãi suất trên hợp đồng, nhưng cổ đông góp vốn thì không làm vậy. Họ chỉ âm thầm đòi hỏi: "Dự án rủi ro càng cao, lợi nhuận tôi thu về phải càng lớn". Để cụ thể hóa mong muốn này thành một con số chính xác, mô hình CAPM (Capital Asset Pricing Model – Mô hình định giá tài sản vốn, do William Sharpe phát triển năm 1964, cũng là công trình đoạt giải Nobel 1990 cùng đợt với Merton Miller) đã ra đời.

#### Công thức tính CAPM

Mô hình CAPM xác định chi phí vốn chủ sở hữu dựa trên nguyên lý: Lợi nhuận kỳ vọng = Phần thưởng cho việc chờ đợi + Phần thưởng cho việc gánh chịu rủi ro.

$$r_{e}=r_{f}+\beta \times (r_{m}-r_{f})$$

Trong đó:
- $r_{f}$ (Risk-free rate): Lãi suất phi rủi ro. Thường lấy theo lãi suất trái phiếu chính phủ kỳ hạn 10 năm. Đây là mức sinh lời bạn chắc chắn nhận được mà không gặp rủi ro nào.
- $r_{m}$ (Market return): Tỷ suất sinh lời kỳ vọng của thị trường. Ví dụ như mức tăng trưởng trung bình năm của chỉ số VN-Index.
- $(r_m - r_f)$: Phần bù rủi ro thị trường (Market Risk Premium). Là khoản lời cộng thêm mà nhà đầu tư yêu cầu khi chuyển từ kênh an toàn (trái phiếu) sang kênh rủi ro (cổ phiếu).
- $\beta$ (Beta): Hệ số đo lường rủi ro hệ thống của doanh nghiệp so với thị trường.
  - $\beta = 1$: Cổ phiếu biến động y hệt thị trường.
  - $\beta > 1$: Cổ phiếu rủi ro hơn thị trường (ví dụ ngành Bất động sản, Công nghệ). Thị trường tăng 10% nó tăng 15%, thị trường giảm 10% nó giảm 15%.
  - $\beta < 1$: Cổ phiếu an toàn hơn thị trường (ví dụ ngành Điện, Nước, Y tế).

#### Ví dụ thực tế: Tính Chi phí vốn chủ sở hữu ($r_{e}$) cho Quán cà phê

Giả sử bạn đang muốn tính $r_{e}$ cho quán cà phê của mình tại thị trường Việt Nam với các thông số thực tế giả định như sau:
- Lãi suất trái phiếu chính phủ ($r_{f}$): 4%/năm
- Tỷ suất sinh lời trung bình của thị trường chứng khoán ($r_{m}$): 12%/năm
- Hệ số rủi ro ($\beta$) của ngành F&B (Nhà hàng/Cà phê): 1,2 (ngành này rủi ro hơn thị trường chung một chút do cạnh tranh gay gắt).

Ráp số vào công thức CAPM:
- $r_e = 4\% + 1.2 \times (12\% - 4\%)$
- $r_e = 4\% + 1.2 \times 8\%$
- $r_e = 4\% + 9.6\% = \mathbf{13.6\%}$

Ý nghĩa con số 13,6%: Nếu bạn muốn kêu gọi các cổ đông góp vốn mở quán cà phê, bạn phải chứng minh được dự án này có khả năng sinh lời ít nhất 13,6%/năm. Nếu tính toán phương án kinh doanh chỉ lãi được 8-10%, cổ đông sẽ từ chối ngay lập tức vì thà họ đem tiền đi mua cổ phiếu trên thị trường chứng khoán còn khỏe và lời nhiều hơn.

#### Trực quan hóa: Mối quan hệ giữa Rủi ro (β) và Chi phí vốn (re)

Mô hình CAPM được thể hiện trên đồ thị bằng một đường thẳng gọi là Đường thị trường chứng khoán (SML - Security Market Line). Doanh nghiệp càng thuộc ngành rủi ro (Beta càng dịch về bên phải), đường SML càng đẩy mức lợi nhuận kỳ vọng của cổ đông ($r_{e}$) lên cao. Đây chính là cách con số $r_e$ đi vào công thức WACC ở mục E — và cách chi phí vốn chủ tăng theo đòn bẩy tài chính đã được giải thích bằng trực giác rủi ro ở mục B (M&M Proposition II) cũng chính là Beta bị "khuếch đại" khi D/E tăng (Hamada equation, xem Key Formulas ở mục K).

---

### G. Pecking Order Theory (Myers & Majluf, 1984)

#### Core Idea

Do **bất cân xứng thông tin (information asymmetry)** — nhà quản lý luôn biết nhiều hơn thị trường về triển vọng thực sự của doanh nghiệp — doanh nghiệp có xu hướng tuân theo một thứ tự ưu tiên tài trợ (pecking order) thay vì nhắm tới một tỷ lệ D/E mục tiêu cố định như Trade-Off Theory giả định:

```
1️⃣ INTERNAL FUNDS (Retained Earnings) ← Preferred
   │ Không cần approval, no dilution, no issuance cost
   ▼
2️⃣ DEBT
   │ Less info-sensitive, fixed claim, tax shield
   │ Market "underreacts" to debt issue
   ▼
3️⃣ EQUITY (Last resort) ← Least preferred
   Market interprets equity issue as "stock overvalued"
   → Stock price drops 2-3% on announcement
```

#### Tại sao phát hành cổ phần lại bị thị trường hiểu là tín hiệu xấu? (Adverse Selection)

Đây là phần cốt lõi, hay bị bỏ qua khi chỉ học thuộc thứ tự 1-2-3. Myers và Majluf lập luận: giả sử ban lãnh đạo biết công ty đang được định giá ĐÚNG hoặc bị định giá THẤP (undervalued) so với giá trị thực — trong trường hợp này, họ sẽ không muốn bán cổ phần mới cho nhà đầu tư bên ngoài, vì làm vậy đồng nghĩa với việc "bán rẻ" một phần công ty cho người khác ở mức giá không công bằng với cổ đông hiện hữu. Ngược lại, nếu ban lãnh đạo biết công ty đang bị định giá CAO (overvalued), họ sẽ rất muốn tranh thủ phát hành cổ phần ngay lập tức để tận dụng mức giá tốt. Nhà đầu tư bên ngoài, dù không biết chính xác công ty đang ở trường hợp nào, lại đủ thông minh để suy luận ngược: "Nếu ban lãnh đạo chọn phát hành cổ phần ngay lúc này, nhiều khả năng họ biết cổ phiếu đang overvalued" — đây chính là hiện tượng lựa chọn bất lợi (adverse selection). Kết quả: bất kể lý do thực sự là gì, thông báo phát hành cổ phần mới hầu như luôn khiến giá cổ phiếu giảm 2-3% ngay lập tức, vì thị trường "trừng phạt" trước cho khả năng xấu nhất. Nợ vay ít bị vấn đề này hơn vì giá trị khoản nợ (số tiền phải trả cố định) ít nhạy cảm với thông tin nội bộ về triển vọng công ty hơn nhiều so với giá trị cổ phần (vốn phụ thuộc hoàn toàn vào lợi nhuận tương lai không chắc chắn).

#### Empirical Evidence
- Các doanh nghiệp có lợi nhuận cao THƯỜNG có ít nợ hơn (vì ưu tiên dùng lợi nhuận giữ lại) → Ngược lại hoàn toàn với dự đoán của Trade-Off Theory (DN lãi cao, ổn định thì nên vay nhiều hơn để tận dụng tax shield)!
- Phát hành cổ phần → Giá cổ phiếu giảm 2-3% (khớp với lý thuyết lựa chọn bất lợi)
- Đòn bẩy tài chính tăng lên khi doanh nghiệp có "funding deficit" (nhu cầu vốn vượt quá dòng tiền nội bộ)

#### Ví dụ thực tế minh họa thứ tự ưu tiên tài trợ của một DN Việt Nam điển hình

Một công ty khởi nghiệp công nghệ (startup SaaS) tại Việt Nam cần 500 triệu đồng để phát triển sản phẩm mới. Thứ tự huy động vốn thực tế thường diễn ra như sau:

1. **Lợi nhuận giữ lại / tiền tích lũy cá nhân của founder** — ưu tiên số 1, vì không mất quyền kiểm soát, không phải giải trình với ai, không tốn chi phí phát hành.
2. **Vay mượn người thân, bạn bè (friends & family loan)** — khi quỹ tích lũy không đủ, đây vẫn là một dạng "nợ" nhưng ít thủ tục, lãi suất thường thấp hơn ngân hàng hoặc bằng 0, và không đòi hỏi tài sản thế chấp.
3. **Vay ngân hàng** — khi cần số vốn lớn hơn, startup thường gặp khó (ngân hàng Việt Nam thường yêu cầu tài sản thế chấp hữu hình, trong khi startup công nghệ chủ yếu có tài sản vô hình như code, bằng sáng chế), nhưng đây vẫn được ưu tiên hơn gọi vốn cổ phần nếu có thể tiếp cận được (ví dụ vay tín chấp qua các gói cho vay SME, hoặc thế chấp bất động sản cá nhân của founder).
4. **Gọi vốn cổ phần (đầu tư thiên thần – Angel Investment, hoặc Quỹ đầu tư mạo hiểm – Venture Capital)** — CHỈ khi không còn lựa chọn nào khác, vì gọi vốn cổ phần đồng nghĩa với việc pha loãng quyền sở hữu, phải chia sẻ quyền quyết định chiến lược, và đúng như lý thuyết adverse selection ở trên: nhà đầu tư luôn định giá công ty "thận trọng" hơn mức founder kỳ vọng, vì lo ngại chính founder biết nhiều hơn về rủi ro thực sự của dự án.

Đây chính là lý do thực tế tại Việt Nam, rất nhiều startup giai đoạn đầu "bootstrapping" (tự lực) càng lâu càng tốt trước khi buộc phải gọi vốn ngoài, đúng như dự đoán của Pecking Order Theory.

---

### H. Agency Theory & Free Cash Flow

#### Jensen's Free Cash Flow Theory (1986)

- **Debt = Discipline device (công cụ kỷ luật)**: Buộc managers trả lãi định kỳ → Ít tiền nhàn rỗi để đầu tư lãng phí
- Doanh nghiệp có dòng tiền tự do (free cash flow) cao nhưng cơ hội tăng trưởng thấp → Nên dùng NHIỀU nợ hơn
- LBO (Leveraged Buyout – Mua lại bằng đòn bẩy) = hình thức cực đoan: chủ động "nhồi" nợ vào công ty để kỷ luật ban quản lý

#### Tại sao nợ lại có vai trò "kỷ luật" nhà quản lý? — Cơ chế tâm lý/động lực đằng sau

Michael Jensen quan sát thấy một vấn đề cố hữu trong các doanh nghiệp đã trưởng thành, tạo ra nhiều tiền mặt nhưng thiếu cơ hội đầu tư sinh lời tốt: ban lãnh đạo (những người điều hành nhưng không sở hữu 100% công ty) có xu hướng giữ lại tiền mặt dư thừa và đem đi đầu tư vào các dự án có NPV âm hoặc thấp — không phải vì thiếu năng lực, mà vì động lực cá nhân: quản lý một công ty lớn hơn (dù kém hiệu quả hơn) thường mang lại nhiều quyền lực, danh tiếng, lương thưởng cao hơn cho CEO so với việc trả lại tiền thừa cho cổ đông dưới dạng cổ tức hoặc mua lại cổ phiếu — hiện tượng này gọi là "xây dựng đế chế" (empire building). Đây chính là một dạng chi phí đại diện (agency cost) giữa cổ đông (principal) và nhà quản lý (agent).

Giải pháp của Jensen: ép doanh nghiệp vay nợ nhiều hơn mức cần thiết về mặt thuần túy tài chính. Khi có khoản lãi vay phải trả định kỳ và bắt buộc (không giống cổ tức, vốn có thể cắt giảm mà không gây hậu quả pháp lý ngay lập tức), ban lãnh đạo buộc phải tạo đủ tiền mặt để trả nợ trước, không còn "tiền nhàn rỗi" để tùy ý rót vào các dự án empire-building kém hiệu quả. Nói cách khác, nợ vay đóng vai trò như một "cam kết đáng tin cậy" (credible commitment) tự ràng buộc chính ban lãnh đạo — tương tự như việc một người tự đặt báo thức và khóa cửa để ép mình phải dậy sớm tập thể dục, thay vì chỉ "có ý định" dậy sớm.

#### Agency Costs of Equity vs Debt

| | Equity Agency Cost | Debt Agency Cost |
|-|-------------------|-----------------|
| Vấn đề | Managers lãng phí FCF (empire building) | Risk shifting (đánh bạc với tiền chủ nợ), underinvestment |
| Giải pháp | Vay thêm nợ, mua lại cổ phiếu | Covenants (điều khoản ràng buộc), giám sát của ngân hàng |
| Ví dụ | Conglomerate discount (tập đoàn đa ngành bị định giá thấp hơn tổng các mảnh) | Dự án rủi ro cao kiểu "được ăn cả, ngã về không" khi gần phá sản |

---

### I. EBIT-EPS Analysis – Tác động của Đòn bẩy tài chính lên EPS và ROE

#### Tại sao cần phân tích EBIT-EPS?

Các mục A-H ở trên trả lời câu hỏi "cơ cấu vốn ảnh hưởng thế nào tới GIÁ TRỊ doanh nghiệp (V)". Nhưng với một chủ doanh nghiệp hoặc cổ đông hiện hữu, câu hỏi thiết thực hơn thường là: "Nếu tôi cần huy động thêm vốn, vay nợ hay phát hành thêm cổ phần sẽ cho EPS (lợi nhuận trên mỗi cổ phần) và ROE (tỷ suất sinh lời trên vốn chủ) cao hơn?" — EBIT-EPS Analysis chính là công cụ trả lời câu hỏi này bằng cách tìm điểm EBIT "hòa vốn" (indifference point) giữa hai phương án tài trợ.

$$EPS_{Debt} = \frac{(EBIT - Interest) \times (1-T)}{Shares_{existing}}$$

$$EPS_{Equity} = \frac{EBIT \times (1-T)}{Shares_{existing} + Shares_{new}}$$

Đặt hai phương trình bằng nhau → giải ra EBIT* (điểm hòa vốn). Ý nghĩa: nếu EBIT thực tế/dự kiến LỚN HƠN EBIT*, phương án vay nợ cho EPS cao hơn; nếu EBIT thực tế NHỎ HƠN EBIT*, phương án phát hành cổ phần lại cho EPS cao hơn (an toàn hơn).

#### Tại sao đòn bẩy tài chính lại khuếch đại ROE khi ROIC > Kd, và phá hủy khi ROIC < Kd?

Đây là cơ chế toán học đơn giản nhưng cực kỳ quan trọng, thường gọi là "đòn bẩy tài chính dương/âm" (positive/negative financial leverage). Trực giác: khi doanh nghiệp vay nợ với lãi suất $K_d$ và đem số tiền đó đầu tư vào tài sản sinh lời với tỷ suất $ROIC$ (Return on Invested Capital):

- Nếu $ROIC > K_d$: phần chênh lệch $(ROIC - K_d)$ nhân với số nợ vay chính là "lợi nhuận dôi dư" thuộc về cổ đông (vì chủ nợ chỉ nhận đúng $K_d$ đã thỏa thuận, phần còn lại thuộc cổ đông) → ROE của cổ đông được khuếch đại lên CAO HƠN ROIC.
- Nếu $ROIC < K_d$: doanh nghiệp kiếm được từ tài sản ÍT HƠN số phải trả lãi vay → cổ đông phải "bù lỗ" phần chênh lệch âm đó bằng chính vốn của mình → ROE bị kéo xuống THẤP HƠN ROIC, thậm chí âm nếu ROIC quá thấp.

**Ví dụ số từng bước**: Một công ty có tổng vốn đầu tư 1.000 (đơn vị tùy ý), ROIC = 10%, thuế suất T = 20%.

*Trường hợp toàn bộ vốn chủ (D/E = 0)*: Lợi nhuận sau thuế = 1.000 × 10% × (1-20%) = 80. Vốn chủ = 1.000 → ROE = 80/1.000 = 8%.

*Trường hợp D/E = 1 (nợ 500, vốn chủ 500), Kd = 6%*: EBIT = 1.000 × 10% = 100 (giả định ROIC tính trên EBIT/Invested Capital trước lãi vay). Lãi vay = 500 × 6% = 30. EBT = 100 - 30 = 70. Lợi nhuận sau thuế = 70 × (1-20%) = 56. ROE = 56/500 (vốn chủ) = 11,2% — CAO HƠN 8% ở trường hợp không vay, vì ROIC(10%) > Kd(6%).

Ngược lại, nếu ROIC chỉ là 3% (thấp hơn Kd = 6%): EBIT = 30, lãi vay vẫn 30 → EBT = 0 → lợi nhuận sau thuế = 0 → ROE = 0%, trong khi trường hợp không vay ROE vẫn dương (3% × 0,8 = 2,4%) — đòn bẩy đã biến một khoản lãi nhỏ thành hòa vốn, và nếu ROIC tiếp tục giảm, ROE sẽ ÂM nhanh hơn nhiều so với trường hợp không vay nợ.

#### Bảng minh họa: Financial Leverage Effect on ROE

| ROIC | All-Equity ROE | D/E = 1.0, Kd = 6% | D/E = 2.0, Kd = 7% |
|------|---------------|--------------------|--------------------|
| 15% | 15% | 24% ✅ Khuếch đại! | 31% ✅✅ |
| 10% | 10% | 14% ✅ Vẫn tốt | 16% ✅ |
| 6% | 6% | 6% ⚠️ Không còn lợi | 5% ⚠️ |
| 3% | 3% | 0% ❌ Mất trắng lợi ích | -5% ❌❌ Phá hủy! |

→ Đây chính là lý do Trade-Off Theory cảnh báo: đòn bẩy là "con dao hai lưỡi" — khuếch đại cả lợi nhuận lẫn rủi ro, và mức độ khuếch đại càng mạnh khi D/E càng cao.

---

### J. Ưu điểm & Nhược điểm sử dụng Debt

#### ✅ Ưu điểm sử dụng Debt:
1. **Tax shield** – Lãi vay khấu trừ thuế → giảm WACC
2. **Discipline** – Buộc management cẩn trọng (Jensen FCF theory)
3. **No dilution** – Không pha loãng ownership/control
4. **Lower cost** – Kd < Ke (luôn luôn đúng, vì rủi ro thấp hơn)
5. **Leverage amplifies ROE** – Khi ROIC > Kd → ROE tăng

#### ❌ Nhược điểm sử dụng Debt:
1. **Bankruptcy risk** – Không trả được → phá sản, mất toàn bộ
2. **Financial distress costs** – Chi phí trực tiếp + gián tiếp rất lớn
3. **Reduced flexibility** – Nghĩa vụ trả nợ cố định làm giảm lựa chọn chiến lược
4. **Covenants** – Ràng buộc hoạt động (D/E < 2x, DSCR > 1.5x)
5. **Amplifies losses** – Khi ROIC < Kd → ROE giảm nhanh, vốn chủ có thể bị "thổi bay"

---

### K. So sánh các lý thuyết – khi nào đúng? + Key Formulas tổng hợp

| Lý thuyết | Dự đoán | Bằng chứng thực nghiệm | Phù hợp nhất với |
|-----------|---------|------------------|----------|
| M&M (no tax) | D/E không quan trọng | ❌ Thực tế có quan trọng | Benchmark/giảng dạy |
| M&M (có thuế) | 100% nợ là tối ưu | ❌ Không DN nào làm vậy | Minh họa giá trị tax shield |
| Trade-Off | Tồn tại D/E tối ưu | ✅ Dữ liệu chéo (cross-sectional) ủng hộ | DN trưởng thành, có lãi ổn định |
| Pecking Order | DN lãi cao = ít nợ hơn | ✅ Dữ liệu theo thời gian ủng hộ | DN tăng trưởng, công nghệ, startup |
| Market Timing | Cơ cấu vốn = tích lũy các lần "timing" thị trường | ⚠️ Một số bằng chứng | Quyết định IPO, thời điểm phát hành |
| Agency | Nợ kỷ luật hóa dòng tiền tự do | ✅ LBO, công ty dầu khí | DN có FCF cao, tăng trưởng thấp |

#### Key Formulas

| Công thức | Ứng dụng |
|---------|-----|
| $V_L = V_U + T \times D$ | M&M có thuế |
| $K_e = K_0 + (K_0 - K_d)(1-T)(D/E)$ | M&M Ke có thuế |
| $WACC = (E/V)K_e + (D/V)K_d(1-T)$ | Chi phí vốn bình quân gia quyền |
| $\beta_L = \beta_U[1 + (1-T)(D/E)]$ | Phương trình Hamada (Beta có đòn bẩy) |
| $Degree\ of\ Financial\ Leverage = \%\Delta EPS / \%\Delta EBIT$ | Độ lớn đòn bẩy tài chính (DFL) |

---

## III. CASE STUDIES THỰC TẾ

### 1. Case Study Thành công: Microsoft – Thay đổi Capital Structure chiến lược

#### Bối cảnh
- Trước 2009: Microsoft gần như ZERO debt (tài trợ hoàn toàn bằng vốn chủ sở hữu)
- Từ 2009: Bắt đầu phát hành trái phiếu doanh nghiệp, tăng dần đòn bẩy
- 2024: ~$80 tỷ USD nợ, D/E ≈ 0,35

#### Tại sao Microsoft thêm Debt?

| Lý do | Chi tiết |
|-------|---------|
| **Tax shield** | $80B × Kd(3%) × T(21%) = ~$500 triệu USD tiết kiệm thuế/năm |
| **Lãi suất thấp lịch sử** | 2010-2021: vay được với lãi suất 2-3% (rẻ hiếm có trong lịch sử) |
| **Tiền mặt dư thừa ở nước ngoài** | Trước cải cách thuế 2017: hồi hương tiền tốn kém → vay trong nước thay vì chuyển tiền về |
| **Tài trợ M&A** | Thương vụ Activision $69B một phần được tài trợ bằng nợ |
| **Trả lại cổ đông** | Tài trợ chương trình mua lại cổ phiếu $20B+/năm mà không cần bán tài sản |
| **Vẫn rất thận trọng** | D/E = 0,35 thấp hơn nhiều so với mức trung bình ngành → vẫn giữ xếp hạng tín nhiệm AAA |

#### Tác động lên WACC

| Giai đoạn | D/E | Ke | Kd (sau thuế) | WACC |
|--------|-----|-----|--------------|------|
| Trước 2009 | 0% | 10% | - | 10,0% |
| 2015 | 20% | 9,5% | 2,0% | 8,25% |
| 2024 | 35% | 9,5% | 2,5% | 7,69% |

→ WACC giảm khoảng 2,3 điểm phần trăm (10,0% → 7,69%) → **Giá trị doanh nghiệp tăng thêm ước tính 30-40%** chỉ nhờ tối ưu hóa cơ cấu vốn, hoàn toàn không cần cải thiện hoạt động kinh doanh cốt lõi.

#### Bài học
1. Zero debt KHÔNG đồng nghĩa với tối ưu (bỏ lỡ giá trị tax shield đáng kể)
2. Chất lượng tín dụng cao → tiếp cận được nguồn vốn vay cực rẻ
3. Tăng dần đòn bẩy một cách có kiểm soát = chiến lược tối ưu hóa an toàn
4. Tài trợ tăng trưởng (M&A) mà không pha loãng cổ đông hiện hữu

Ý nghĩa kinh doanh sâu xa hơn: trường hợp Microsoft cho thấy ngay cả doanh nghiệp "hoàn hảo" về dòng tiền và lợi nhuận cũng không nên bỏ qua đòn bẩy tài chính một cách cực đoan — vì làm vậy đồng nghĩa với việc từ chối một nguồn vốn rẻ mà cổ đông hiện hữu lẽ ra được hưởng lợi (thông qua tax shield), miễn là mức đòn bẩy đó vẫn nằm rất xa vùng nguy hiểm của chi phí kiệt quệ tài chính.

---

### 2. Case Study Thất bại: Evergrande – Debt-fueled Growth → Catastrophic Collapse

#### Bối cảnh
China Evergrande Group, từng là nhà phát triển bất động sản lớn thứ hai Trung Quốc, đã sụp đổ sau nhiều năm theo đuổi chiến lược: vay nợ ồ ạt → mua quỹ đất → xây dựng → bán → vay thêm. Đỉnh điểm, tổng nợ của tập đoàn vượt **300 tỷ USD**, với tỷ lệ D/E ước tính 6-8 lần — vượt xa mọi khuyến nghị của Trade-Off Theory. Đây là một trong những case study kinh điển nhất mọi thời đại về sai lầm trong quản trị cơ cấu vốn, vi phạm nghiêm trọng cả Trade-Off Theory lẫn Pecking Order Theory.

#### Dòng thời gian nợ vay (Capital Structure Timeline)

| Năm | Tổng nợ | Tỷ lệ D/E | Chiến lược |
|------|-----------|-----------|-----------|
| 2010 | $30B | 2,0x | Tăng trưởng nhanh |
| 2015 | $95B | 3,5x | Mở rộng quyết liệt |
| 2018 | $180B | 5,0x | Đa dạng hóa (xe điện, bóng đá, nước đóng chai) |
| 2020 | $300B | 6-8x | Chính sách "**Ba vạch đỏ**" (Three Red Lines) ập tới |
| 2021 | $300B+ | Vốn chủ âm | **VỠ NỢ → Sụp đổ** |

#### 1. Vi phạm Lý thuyết đánh đổi: Đòn bẩy quá đà và "Điểm chết" tài chính

Như đã thảo luận ở mục II.D, Trade-Off Theory khuyên doanh nghiệp tìm một "điểm ngọt" để cân bằng giữa lợi ích thuế (tax shield) và chi phí kiệt quệ tài chính (financial distress costs). Evergrande đã hoàn toàn bỏ qua nguyên tắc này. Thay vì giữ tỷ lệ nợ ở mức an toàn, tập đoàn liên tục vay nợ để thâu tóm quỹ đất và mở rộng đa ngành sang cả xe điện, bóng đá, nước đóng chai — tỷ lệ nợ trên tổng tài sản có những thời điểm vượt mức 80-90%. Ban lãnh đạo Evergrande lao vào nợ nần vì tin rằng "bất động sản Trung Quốc không bao giờ giảm giá" — một giả định chưa từng được kiểm chứng qua một chu kỳ suy thoái thực sự. Khi nợ vượt quá xa điểm tối ưu D/E*, chi phí kiệt quệ tài chính không tăng tuyến tính mà tăng theo cấp số nhân (xem lại đường cong ở biểu đồ Trade-Off mục II.D): chỉ cần một biến động nhỏ từ thị trường, chi phí lãi vay khổng lồ đã tự tay "bóp nghẹt" dòng tiền của tập đoàn.

#### 2. Sự "lệch pha" chết người về kỳ hạn (Maturity Mismatch)

Trong quản trị cơ cấu vốn, nguyên tắc vàng là: dùng vốn dài hạn tài trợ tài sản dài hạn, dùng vốn ngắn hạn tài trợ tài sản ngắn hạn. Evergrande đã làm ngược lại hoàn toàn: họ gom đất, xây các siêu dự án đại đô thị (cần 5-10 năm mới thu hồi vốn đầy đủ) nhưng lại tài trợ phần lớn bằng các khoản vay ngắn hạn, phát hành thương phiếu ngắn hạn (kỳ hạn chỉ từ vài tháng đến 1 năm), và huy động tiền từ người dân qua các sản phẩm quản lý tài sản (Wealth Management Products – WMP) vốn cũng có kỳ hạn ngắn. Hậu quả: Evergrande liên tục phải rơi vào vòng xoáy "vay mới trả cũ" (đảo nợ – debt rollover). Khi dòng tiền bán nhà chậm lại (do thị trường bất động sản Trung Quốc hạ nhiệt), họ không có đủ tiền mặt để trả các khoản nợ ngắn hạn đến hạn, dẫn đến hiệu ứng domino sụp đổ toàn bộ hệ thống tài chính của tập đoàn.

#### 3. "Cú đấm thép" từ chính sách Ba vạch đỏ (The Three Red Lines)

Lý thuyết cơ cấu vốn chỉ ra rằng năng lực vay nợ của doanh nghiệp phụ thuộc rất lớn vào môi trường pháp lý — một yếu tố thường bị bỏ qua khi áp dụng Trade-Off Theory một cách máy móc. Năm 2020, Bắc Kinh ban hành chính sách "Ba vạch đỏ" để siết chặt dòng vốn vào bất động sản, nhắm thẳng vào cấu trúc vốn của các doanh nghiệp trong ngành với 3 ngưỡng:
1. Nợ phải trả trên tổng tài sản (không tính tiền người mua trả trước) phải dưới 70%.
2. Nợ ròng trên vốn chủ sở hữu phải dưới 100%.
3. Tiền mặt và các khoản tương đương tiền phải lớn hơn hoặc bằng nợ ngắn hạn.

Evergrande vi phạm CẢ 3 vạch đỏ cùng lúc. Ngay lập tức, các ngân hàng khóa van tín dụng, tập đoàn không thể vay thêm tiền để đảo nợ. Nguồn cung vốn vay (Debt) bị cắt đứt hoàn toàn trong khi vốn chủ sở hữu (Equity) đã cạn kiệt từ trước — đúng thời điểm tập đoàn cần thanh khoản nhất.

#### Góc nhìn từ Pecking Order Theory

Evergrande không chỉ vi phạm Trade-Off Theory mà còn đi ngược hoàn toàn trật tự ưu tiên tài trợ hợp lý theo Pecking Order Theory:
- Không tích lũy nội lực (internal funds): vẫn chia cổ tức khổng lồ cho cổ đông (bao gồm cả gia đình nhà sáng lập) ngay cả khi nợ đã ở mức báo động — đi ngược hoàn toàn nguyên tắc ưu tiên số 1 là giữ lại lợi nhuận.
- Không coi nợ là "bước 2 thận trọng": thay vì dùng nợ như một công cụ tài trợ có kiểm soát, Evergrande dùng nợ như công cụ tăng trưởng vô hạn, không giới hạn.
- Thao túng thời điểm phát hành vốn cổ phần (market timing) có lợi cho nội bộ: phát hành cổ phần ở các thời điểm đỉnh giá để trục lợi cho nhóm cổ đông sáng lập, thay vì vì lợi ích dài hạn của công ty.

#### Kết quả
- 2021: Vỡ nợ với tổng dư nợ hơn 300 tỷ USD
- 2024: Bị tòa án ra lệnh thanh lý (liquidation)
- Tài sản của nhà sáng lập: từ $42 tỷ USD về $0
- Hiệu ứng lan truyền (contagion): Kéo theo khủng hoảng bất động sản toàn Trung Quốc, ảnh hưởng tới Country Garden, Sunac và nhiều tập đoàn khác
- 1,6 triệu căn hộ đã bán nhưng chưa bàn giao cho người mua nhà

#### Bài học xương máu về Cơ cấu vốn từ Evergrande

1. **Tồn tại một mức đòn bẩy tối ưu** – Trade-Off Theory là đúng. Vượt quá điểm đó, đòn bẩy không còn tạo giá trị mà trở thành công cụ hủy diệt.
2. **Đòn bẩy là con dao hai lưỡi** – Khi thị trường đi lên, nợ vay giúp khuếch đại lợi nhuận (ROE, như đã chứng minh bằng số liệu ở mục II.I). Nhưng khi thị trường đi xuống, chính đòn bẩy đó là chiếc máy nghiền nát doanh nghiệp nhanh nhất.
3. **Tăng trưởng chỉ dựa vào nợ vay = lâu đài trên cát** – Doanh nghiệp vẫn cần tạo ra dòng tiền nội sinh (internal cash generation) thực sự, không thể dựa mãi vào vay mới trả cũ.
4. **Dòng tiền mặt mới là "dòng máu" của doanh nghiệp** – Giá trị tài sản trên sổ sách (quỹ đất của Evergrande rất lớn) không có ý nghĩa nếu không thể quy đổi ra tiền mặt để trả nợ đúng hạn.
5. **Rủi ro chính sách (regulatory risk)** – Cơ cấu vốn phải tính đến khả năng thay đổi chính sách của nhà nước, đặc biệt trong các ngành nhạy cảm như bất động sản.
6. **D/E > 3 lần đối với DN phi tài chính = vùng nguy hiểm** – Đặc biệt nguy hiểm khi phần lớn là nợ ngắn hạn tài trợ cho tài sản dài hạn (maturity mismatch).
7. **Trí tuệ của Pecking Order** – Tài trợ thận trọng theo đúng thứ tự ưu tiên (nội lực → nợ có kiểm soát → vốn cổ phần) giúp doanh nghiệp sống sót qua các giai đoạn suy thoái.

---

### 3. Case Study SME: Quyết định Cơ cấu vốn cho Công ty Cơ khí "Thành Phát" mở rộng nhà xưởng

#### Bối cảnh doanh nghiệp

Công ty TNHH Cơ khí Thành Phát là một SME sản xuất linh kiện cơ khí tại Bình Dương, hoạt động ổn định 8 năm. Ban giám đốc quyết định đầu tư mở rộng nhà xưởng và mua thêm dây chuyền máy CNC mới để đáp ứng đơn hàng xuất khẩu tăng vọt. Tổng vốn cần huy động thêm: **3.000 triệu đồng (3 tỷ VNĐ)**.

**Số liệu hiện tại của công ty** (trước khi huy động vốn mở rộng):
- Vốn chủ sở hữu hiện có (giá trị sổ sách): 4.000 triệu đồng
- Số cổ phần đang lưu hành: 400.000 cổ phần (mệnh giá 10.000đ/cổ phần)
- Giá trị thị trường ước tính mỗi cổ phần (dựa trên định giá gần nhất khi có nhà đầu tư ngỏ ý): 15.000đ/cổ phần → Giá trị thị trường vốn chủ hiện có = 400.000 × 15.000 = 6.000 triệu đồng
- Công ty hiện KHÔNG có nợ vay dài hạn (D = 0)
- EBIT dự kiến năm đầu sau khi mở rộng: **1.200 triệu đồng**
- Thuế suất thuế TNDN (T): 20%

**Ba phương án tài trợ cho khoản 3.000 triệu đồng cần thiết:**
- **Phương án A**: Vay ngân hàng 100% (3.000 triệu), lãi suất vay $K_d$ = 11%/năm
- **Phương án B**: Phát hành cổ phần riêng lẻ 100%, giá phát hành 15.000đ/cổ phần
- **Phương án C**: Kết hợp 50/50 — vay 1.500 triệu + phát hành cổ phần trị giá 1.500 triệu

Chi phí vốn chủ sở hữu yêu cầu bởi nhà đầu tư mới/hiện hữu ($K_e$), áp dụng CAPM có cộng thêm phần bù thanh khoản (illiquidity premium) vì cổ phần SME chưa niêm yết, được xác định là **15%/năm** (giữ không đổi giữa các phương án vì đây là công ty chưa niêm yết, nhà đầu tư luôn đòi mức sinh lời tối thiểu này bất kể cơ cấu vốn, do rủi ro kinh doanh — business risk — không đổi).

#### Bước 1: Tính số cổ phần phát hành mới và chi phí lãi vay từng phương án

| | Phương án A (100% Vay) | Phương án B (100% Cổ phần) | Phương án C (50/50) |
|---|---|---|---|
| Nợ vay mới | 3.000 triệu | 0 | 1.500 triệu |
| Lãi vay năm = Nợ × 11% | 330 triệu | 0 | 165 triệu |
| Cổ phần phát hành mới = Số tiền / 15.000đ | 0 cổ phần | 200.000 cổ phần | 100.000 cổ phần |
| Tổng số cổ phần sau phát hành | 400.000 | 600.000 | 500.000 |

#### Bước 2: Tính EPS (lợi nhuận trên mỗi cổ phần) cho từng phương án tại EBIT dự kiến = 1.200 triệu

$$EPS = \frac{(EBIT - Interest) \times (1-T)}{Số\ cổ\ phần}$$

| | Phương án A | Phương án B | Phương án C |
|---|---|---|---|
| EBIT | 1.200 | 1.200 | 1.200 |
| (-) Lãi vay | 330 | 0 | 165 |
| = EBT | 870 | 1.200 | 1.035 |
| (-) Thuế 20% | 174 | 240 | 207 |
| = Lợi nhuận sau thuế (NI) | 696 | 960 | 828 |
| Số cổ phần | 400.000 | 600.000 | 500.000 |
| **EPS (đồng/cổ phần)** | **1.740** | **1.600** | **1.656** |

→ Tại mức EBIT dự kiến 1.200 triệu, Phương án A (100% vay) cho EPS CAO NHẤT (1.740đ), vì EBIT dự kiến đủ lớn để chủ nợ chỉ nhận một phần cố định (lãi vay), phần dôi dư còn lại (nhờ ROIC > Kd sau thuế) dồn hết vào tay số cổ phần ÍT HƠN — đúng cơ chế khuếch đại đã giải thích ở mục II.I.

#### Bước 3: Tìm điểm EBIT hòa vốn (Indifference Point) giữa Phương án A và Phương án B

Đặt $EPS_A = EPS_B$:

$$\frac{(EBIT - 330)(1-0,2)}{400.000} = \frac{EBIT \times (1-0,2)}{600.000}$$

Giải phương trình (đã kiểm chứng bằng Python — xem ghi chú verify bên dưới):

$$EBIT^{*} = 990\ \text{triệu đồng}$$

Kiểm tra lại: tại EBIT = 990 triệu, $EPS_A = (990-330) \times 0,8 / 400.000 \times 1.000.000 = 1.320đ$ và $EPS_B = 990 \times 0,8/600.000 \times 1.000.000 = 1.320đ$ — bằng nhau, xác nhận điểm hòa vốn chính xác.

**Ý nghĩa**: Vì EBIT dự kiến (1.200 triệu) lớn hơn điểm hòa vốn (990 triệu) với biên an toàn khoảng 21%, Phương án vay nợ (A) về mặt EPS thuần túy là lựa chọn tốt hơn — NHƯNG đây mới chỉ là một nửa câu chuyện, cần xem xét thêm WACC và khả năng chịu đựng rủi ro ở các bước sau.

#### Bước 4: Tính WACC cho từng phương án

Sử dụng giá trị thị trường vốn chủ hiện có (6.000 triệu) cộng thêm phần vốn mới huy động:

| | Phương án A | Phương án B | Phương án C |
|---|---|---|---|
| Nợ (D) | 3.000 | 0 | 1.500 |
| Vốn chủ thị trường (E) | 6.000 | 9.000 | 7.500 |
| Tổng vốn (V = D+E) | 9.000 | 9.000 | 9.000 |
| D/V | 33,3% | 0% | 16,7% |
| Kd sau thuế = 11% × (1-0,2) | 8,8% | - | 8,8% |
| **WACC = (D/V)×Kd×(1-T) + (E/V)×Ke** | **12,93%** | **15,00%** | **13,97%** |

→ Phương án A có WACC thấp nhất (12,93%), đúng như dự đoán của lý thuyết: tận dụng tối đa lá chắn thuế (tax shield) từ nợ vay rẻ hơn vốn chủ.

#### Bước 5: Tính ROE (trên giá trị sổ sách vốn chủ) để đối chiếu góc nhìn cổ đông hiện hữu

| | Phương án A | Phương án B | Phương án C |
|---|---|---|---|
| Lợi nhuận sau thuế (NI) | 696 | 960 | 828 |
| Vốn chủ sổ sách (4.000 + vốn góp mới) | 4.000 | 7.000 | 5.500 |
| **ROE** | **17,40%** | **13,71%** | **15,05%** |

→ Một lần nữa, Phương án A cho ROE cao nhất cho cổ đông hiện hữu, vì ROIC của dự án mở rộng (ước tính từ lợi nhuận sau thuế/tổng vốn đầu tư ≈ 13,7%) lớn hơn chi phí vay sau thuế (8,8%) — đòn bẩy đang khuếch đại lợi nhuận một cách tích cực.

#### Bước 6: Kiểm tra khả năng chịu đựng rủi ro (Stress Test) — vì sao không nên chọn 100% nợ cho một SME

Đây là bước QUAN TRỌNG NHẤT mà nhiều chủ SME bỏ qua khi chỉ nhìn vào EPS/ROE ở kịch bản lạc quan. Giả định một kịch bản bất lợi: đơn hàng xuất khẩu giảm, EBIT giảm 30% so với dự kiến (từ 1.200 xuống còn 840 triệu đồng) — một tình huống hoàn toàn có thể xảy ra với SME phụ thuộc vào một vài khách hàng xuất khẩu lớn:

| | Phương án A | Phương án B | Phương án C |
|---|---|---|---|
| EBIT (kịch bản giảm 30%) | 840 | 840 | 840 |
| Lãi vay | 330 | 0 | 165 |
| **Hệ số bao phủ lãi vay (Interest Coverage = EBIT/Lãi vay)** | **2,55 lần** ⚠️ | ∞ | **5,09 lần** ✅ |
| EPS trong kịch bản xấu | 1.020đ | 1.120đ | 1.080đ |

→ Đây chính là điểm mấu chốt: các ngân hàng thương mại tại Việt Nam thường yêu cầu hệ số bao phủ lãi vay (Interest Coverage Ratio) tối thiểu **3 lần** để duy trì xếp hạng tín dụng an toàn và tránh vi phạm điều khoản vay (covenant). Trong kịch bản xấu, Phương án A (100% vay) có hệ số bao phủ lãi vay chỉ còn **2,55 lần — RƠI XUỐNG DƯỚI ngưỡng an toàn 3 lần**, đặt công ty vào nguy cơ vi phạm covenant hoặc bị ngân hàng siết chặt điều khoản. Ngược lại, Phương án C (kết hợp) vẫn duy trì hệ số bao phủ 5,09 lần — an toàn rất xa ngưỡng báo động, dù EPS kịch bản xấu vẫn gần tương đương (1.080đ so với 1.020đ của Phương án A).

#### Kết luận và Khuyến nghị

**Khuyến nghị: Công ty Thành Phát nên chọn Phương án C (kết hợp vay 1.500 triệu + phát hành cổ phần 1.500 triệu)**, KHÔNG chọn Phương án A dù Phương án A cho EPS/ROE cao hơn ở kịch bản cơ sở (base case). Lý do, liên hệ trực tiếp với Trade-Off Theory ở mục II.D:

1. **Lợi ích tax shield của Phương án C vẫn đáng kể**: WACC giảm từ 15% (toàn vốn chủ) xuống còn 13,97% — tiết kiệm hơn 1 điểm phần trăm chi phí vốn mà không phải đánh đổi quá nhiều rủi ro.
2. **SME có "sức chịu đòn bẩy" (debt capacity) thấp hơn nhiều so với công ty lớn như Microsoft** (case 1): Thành Phát phụ thuộc vào một số khách hàng xuất khẩu tập trung, dòng tiền kém đa dạng hóa hơn, không có xếp hạng tín nhiệm công khai, và không dễ dàng tiếp cận vốn cổ phần khẩn cấp nếu gặp khó khăn thanh khoản (khác với công ty niêm yết). Vì vậy, điểm tối ưu D/E* của một SME luôn nằm GẦN bên trái hơn (ít nợ hơn) so với một tập đoàn lớn, ổn định như Microsoft — đúng như bảng "Optimal ranges by industry" đã nêu ở mục II.D, SME sản xuất nên nằm ở vùng thận trọng của dải 30-50% nợ, không nên áp sát hoặc vượt ngưỡng trên.
3. **Biên an toàn (margin of safety) của Phương án C lớn hơn nhiều**: hệ số bao phủ lãi vay 5,09 lần ngay cả trong kịch bản xấu, trong khi Phương án A chỉ còn 2,55 lần — dưới ngưỡng ngân hàng yêu cầu, có thể dẫn đến việc ngân hàng từ chối giải ngân tiếp hoặc đòi bổ sung tài sản thế chấp giữa chừng.
4. **Chi phí pha loãng của Phương án C vừa phải**: chỉ phát hành thêm 100.000 cổ phần (giảm tỷ lệ sở hữu của cổ đông sáng lập ít hơn so với Phương án B), trong khi vẫn giữ được một phần kỷ luật tài chính từ nợ vay (theo Agency Theory, mục II.H) mà không đẩy công ty vào vùng rủi ro tài chính quá cao.

Đây chính là bản chất thực tiễn của Trade-Off Theory: không phải "nợ càng nhiều càng tốt" (dù công thức EPS/WACC base case gợi ý vậy), mà là **cân bằng giữa lợi ích tax shield biên và chi phí kiệt quệ tài chính biên** — và với một SME có dòng tiền kém ổn định hơn, điểm cân bằng đó nghiêng về phía ít đòn bẩy hơn so với một tập đoàn lớn như Microsoft.

> **Ghi chú phương pháp**: Toàn bộ số liệu trong case study này (EPS, WACC, ROE, điểm hòa vốn EBIT, hệ số bao phủ lãi vay) đã được kiểm tra chéo bằng Python để đảm bảo tính nhất quán số học trước khi đưa vào tài liệu — xem phần báo cáo verify ở cuối quy trình biên soạn.

---

## IV. ỨNG DỤNG CHO SME

### 1. Đặc thù quyết định cơ cấu vốn của SME Việt Nam so với công ty lớn

SME Việt Nam đối mặt với một bối cảnh huy động vốn khác biệt rất nhiều so với các tập đoàn niêm yết lớn như Microsoft (case study mục III.1):

| Yếu tố | Công ty lớn/niêm yết | SME Việt Nam |
|--------|----------------------|--------------|
| Tiếp cận vốn cổ phần | Dễ dàng (IPO, phát hành thêm trên sàn, quỹ đầu tư tổ chức) | Rất khó — gần như chỉ trông chờ vào vốn tự có, bạn bè/người thân, hoặc đàm phán riêng lẻ với nhà đầu tư thiên thần/quỹ PE nhỏ |
| Tiếp cận vốn vay | Phát hành trái phiếu doanh nghiệp, vay tín chấp theo xếp hạng tín nhiệm | Chủ yếu vay ngân hàng CÓ TÀI SẢN THẾ CHẤP, lãi suất cao hơn đáng kể |
| Chi phí vốn vay | Thấp (2-5%/năm với công ty lớn, tín nhiệm cao) | Cao hơn nhiều (9-14%/năm tùy ngân hàng, kỳ hạn, tài sản bảo đảm) |
| Khả năng chịu đòn bẩy (debt capacity) | Cao (dòng tiền đa dạng hóa, ổn định, nhiều tài sản) | Thấp (phụ thuộc ít khách hàng/đơn hàng, dòng tiền biến động theo mùa vụ) |
| Thông tin minh bạch | Báo cáo tài chính kiểm toán, công bố công khai | Thường chưa kiểm toán đầy đủ, ngân hàng khó thẩm định chính xác |

→ Chính vì những khác biệt này, **Pecking Order Theory (mục II.G) đặc biệt đúng và quan trọng với SME Việt Nam hơn bất kỳ nhóm doanh nghiệp nào khác**: do kênh vốn cổ phần gần như đóng với đa số SME (trừ khi đã có quỹ đầu tư quan tâm), con đường tài trợ thực tế gần như luôn đi theo đúng thứ tự: lợi nhuận giữ lại → vay người quen → vay ngân hàng có thế chấp → (hiếm khi) gọi vốn cổ phần. Khi tư vấn cho chủ SME, cần đặt trọng tâm vào việc tối ưu hóa khả năng tiếp cận TÍN DỤNG NGÂN HÀNG trước, thay vì áp dụng máy móc các mô hình D/E tối ưu của công ty niêm yết.

### 2. Checklist/hướng dẫn thực tế cho chủ SME khi đàm phán vay ngân hàng

Khi chuẩn bị hồ sơ vay vốn mở rộng sản xuất kinh doanh tại các ngân hàng thương mại Việt Nam, chủ SME nên chuẩn bị và lưu ý các yếu tố sau:

```
TRƯỚC KHI NỘP HỒ SƠ VAY:
□ Chuẩn bị BCTC tối thiểu 2-3 năm gần nhất (tốt nhất có kiểm toán hoặc soát xét)
□ Tính trước Hệ số bao phủ lãi vay (Interest Coverage) dự kiến — ngân hàng thường yêu cầu > 2-3 lần
□ Tính trước DSCR (Debt Service Coverage Ratio = Dòng tiền hoạt động / (Gốc + Lãi phải trả))
   → Hầu hết ngân hàng Việt Nam yêu cầu DSCR tối thiểu 1,2 - 1,5 lần
□ Chuẩn bị đầy đủ hồ sơ tài sản thế chấp (sổ đỏ, giấy tờ máy móc, định giá độc lập nếu cần)
□ Dự phóng dòng tiền 3-5 năm cho thấy khả năng trả nợ ngay cả trong kịch bản xấu (stress test)

VỀ LÃI SUẤT THỰC TẾ TẠI VIỆT NAM (tham khảo, biến động theo thời điểm và chính sách NHNN):
□ Vay thế chấp bất động sản, trung dài hạn: thường 8-11%/năm
□ Vay tín chấp/vay lưu động ngắn hạn: thường 7-10%/năm (DN tốt) đến 12-15%/năm (DN rủi ro cao hơn)
□ Vay ưu đãi theo gói hỗ trợ SME/ngành ưu tiên (xuất khẩu, công nghệ, nông nghiệp): có thể thấp hơn 1-3%
□ Luôn hỏi rõ: lãi suất cố định hay thả nổi, phí trả nợ trước hạn, phí quản lý khoản vay

ĐÀM PHÁN:
□ So sánh ít nhất 3 ngân hàng trước khi quyết định (lãi suất, điều kiện tài sản đảm bảo, thời gian giải ngân)
□ Thương lượng kỳ hạn vay KHỚP với vòng đời tài sản đầu tư (máy móc 7-10 năm → vay trung dài hạn tương ứng, tránh lặp lại sai lầm "maturity mismatch" của Evergrande ở mục III.2)
□ Hỏi rõ các điều khoản covenant (cam kết duy trì tỷ lệ D/E, DSCR tối thiểu trong suốt thời gian vay)
□ Luôn giữ lại một phần "dư địa vay" (debt capacity reserve) cho các nhu cầu vốn lưu động bất ngờ
```

### 3. Bảng benchmark D/E phù hợp cho các loại hình SME phổ biến tại Việt Nam

| Loại hình SME | D/E khuyến nghị | Lý do |
|---------------|-----------------|-------|
| **Thương mại** (bán buôn/lẻ, phân phối) | 0,3 - 0,8 lần | Vòng quay hàng tồn kho nhanh, cần vốn lưu động nhiều hơn tài sản cố định, dòng tiền tương đối đều nhưng nhạy cảm với tồn kho ế |
| **Sản xuất** (cơ khí, chế biến, may mặc) | 0,5 - 1,2 lần | Tài sản cố định (nhà xưởng, máy móc) hữu hình, dễ thế chấp → vay được nhiều hơn, nhưng cần thận trọng vì đơn hàng có thể biến động theo chu kỳ kinh tế/xuất khẩu |
| **Dịch vụ** (tư vấn, giáo dục, F&B nhỏ) | 0,1 - 0,5 lần | Ít tài sản hữu hình để thế chấp, dòng tiền phụ thuộc nhiều vào con người và thương hiệu, nên giữ đòn bẩy thấp |
| **Xây dựng** (nhà thầu, bất động sản nhỏ) | 0,8 - 1,5 lần | Cần vốn lớn cho dự án nhưng dòng tiền rất KHÔNG đều (phụ thuộc tiến độ thanh toán của chủ đầu tư) → rủi ro maturity mismatch cao nếu không cẩn trọng, nên giữ D/E ở mức vừa phải dù có tài sản thế chấp tốt |

→ Đây chỉ là benchmark tham khảo ban đầu; quyết định cuối cùng vẫn cần dựa trên stress test dòng tiền thực tế của từng doanh nghiệp cụ thể (như minh họa ở Bước 6, case study mục III.3).

---

## V. TOOLS & TEMPLATES

### 1. Công cụ/nguồn tra cứu hỗ trợ tính WACC và CAPM

| Công cụ/Nguồn | Công dụng | Ghi chú |
|----------------|-----------|---------|
| **Lãi suất trái phiếu Chính phủ VN (rf)** | Tra cứu tại website Sở Giao dịch Chứng khoán Hà Nội (HNX) hoặc Bộ Tài chính, kỳ hạn 10 năm | Cập nhật theo phiên đấu thầu, dùng làm risk-free rate trong CAPM |
| **Beta ngành (Damodaran Online)** | Trang web của GS. Aswath Damodaran (NYU Stern) công bố Beta trung bình theo ngành, cập nhật hàng năm, miễn phí | Dùng Beta thị trường mới nổi (Emerging Markets) hoặc điều chỉnh thủ công cho phù hợp bối cảnh Việt Nam |
| **VN-Index lịch sử (rm)** | Dữ liệu từ HOSE, các công ty chứng khoán (SSI, VNDirect, VCBS...) | Tính tỷ suất sinh lời trung bình dài hạn (10-20 năm) để ước lượng rm ổn định hơn, tránh dùng dữ liệu ngắn hạn biến động mạnh |
| **Excel/Google Sheets** | Tự xây công thức WACC, CAPM, EBIT-EPS indifference point | Xem cấu trúc gợi ý ở mục 2 bên dưới |
| **Công cụ tính Beta không đòn bẩy/có đòn bẩy (Hamada)** | Áp dụng công thức $\beta_L = \beta_U[1+(1-T)(D/E)]$ thủ công trong Excel | Dùng khi SME không có beta riêng (chưa niêm yết) — mượn Beta ngành rồi "re-lever" theo D/E của chính mình |

### 2. Cấu trúc Excel/Google Sheet đơn giản để SME tự mô phỏng kịch bản D/E

Gợi ý cấu trúc 1 file Google Sheet/Excel gồm 4 tab, để chủ SME tự chạy các kịch bản cơ cấu vốn khác nhau trước khi quyết định vay/gọi vốn:

```
TAB 1 — INPUTS (vùng duy nhất được phép nhập liệu thủ công):
  - EBIT dự kiến (kịch bản cơ sở + kịch bản xấu -X%)
  - Thuế suất TNDN (T)
  - Lãi suất vay ngân hàng dự kiến (Kd)
  - Số vốn chủ hiện có + số cổ phần hiện có + giá trị/cổ phần
  - Chi phí vốn chủ yêu cầu (Ke, có thể tính bằng CAPM ở Tab 2)
  - Số vốn cần huy động thêm

TAB 2 — CAPM CALCULATOR:
  - rf (nhập từ lãi suất TPCP 10 năm)
  - Beta ngành (tra Damodaran, nhập thủ công)
  - rm (nhập từ lịch sử VN-Index dài hạn)
  - Output: Ke = rf + Beta × (rm - rf)

TAB 3 — KỊCH BẢN SO SÁNH (3-5 cột, mỗi cột 1 phương án D/E khác nhau):
  - % vay / % vốn chủ của từng phương án
  - Tính tự động: Lãi vay, EBT, Thuế, NI, EPS, ROE, WACC, Interest Coverage
  - Conditional formatting: tô đỏ nếu Interest Coverage < 3 lần (cảnh báo rủi ro)

TAB 4 — DASHBOARD:
  - Biểu đồ cột so sánh WACC giữa các phương án
  - Biểu đồ cột so sánh EPS/ROE giữa các phương án (kịch bản cơ sở vs kịch bản xấu)
  - Khuyến nghị tự động (ví dụ công thức IF: nếu Interest Coverage kịch bản xấu < 3 → cảnh báo "Không nên chọn phương án này")
```

---

## VI. BÀI TẬP THỰC HÀNH

### Bài 1 (Cơ bản — Tính WACC)
Một doanh nghiệp có giá trị thị trường Nợ = 5.000 triệu đồng, Vốn chủ = 7.000 triệu đồng. Chi phí vay $K_d$ = 9,5%/năm, chi phí vốn chủ $K_e$ = 16%/năm, thuế suất T = 20%. Tính WACC.

*(Đáp số đã verify bằng Python: D/V = 41,7%, E/V = 58,3%, WACC = 12,50%)*

### Bài 2 (Cơ bản — Hiểu bản chất công thức CAPM)
Lãi suất trái phiếu chính phủ $r_f$ = 4,5%/năm, tỷ suất sinh lời thị trường $r_m$ = 13%/năm, Beta của doanh nghiệp = 1,3. Tính chi phí vốn chủ sở hữu theo CAPM. Giải thích bằng lời: tại sao Beta > 1 lại khiến $r_e$ cao hơn mức trung bình thị trường?

*(Đáp số đã verify bằng Python: $r_e$ = 15,55%)*

### Bài 3 (Trung bình — Tính giá trị Tax Shield)
Một doanh nghiệp vay 10.000 triệu đồng nợ dài hạn vĩnh viễn, thuế suất TNDN 20%. Tính PV(Tax Shield) theo công thức M&M (1963). Giải thích tại sao công thức PV(Tax Shield) lại không phụ thuộc vào lãi suất vay $K_d$ dù trực giác ban đầu có vẻ nó phải phụ thuộc.

*(Đáp số đã verify bằng Python: PV(Tax Shield) = 2.000 triệu đồng)*

### Bài 4 (Trung bình — Tìm điểm hòa vốn EBIT-EPS)
Một công ty bán lẻ có 300.000 cổ phần đang lưu hành, đang cân nhắc vay 2.000 triệu đồng (lãi suất 10%/năm) hoặc phát hành thêm cổ phần mới với giá 20.000đ/cổ phần để huy động cùng số tiền đó. Thuế suất T = 20%. Tìm EBIT hòa vốn giữa hai phương án.

*(Đáp số đã verify bằng Python: EBIT* = 800 triệu đồng — tại đó cả hai phương án đều cho EPS = 1.600đ)*

### Bài 5 (Nâng cao — Mini Case: Xưởng May mặc "Việt Tiến Nhỏ")
Một xưởng may mặc SME có vốn chủ hiện tại 3.000 triệu đồng, 250.000 cổ phần đang lưu hành, giá trị mỗi cổ phần ước tính 12.000đ. Xưởng cần huy động thêm 2.000 triệu đồng để mua máy may công nghiệp mới. Lãi suất vay ngân hàng là 12%/năm, thuế suất TNDN 20%, EBIT dự kiến năm đầu sau đầu tư là 800 triệu đồng.

Yêu cầu:
a) Tính EPS nếu vay 100% ngân hàng, so với EPS nếu phát hành 100% cổ phần mới.
b) Tìm điểm EBIT hòa vốn giữa hai phương án.
c) Nếu EBIT thực tế chỉ đạt 500 triệu đồng (thấp hơn điểm hòa vốn), phương án nào nên được chọn? Giải thích bằng lý thuyết Trade-Off.

*(Đáp số đã verify bằng Python: EPS phương án vay = 1.792đ, EPS phương án cổ phần = 1.536đ tại EBIT = 800 triệu; điểm hòa vốn EBIT* = 600 triệu đồng. Vì EBIT dự kiến 800 triệu > điểm hòa vốn 600 triệu, phương án vay có lợi hơn về EPS — nhưng học viên cần tự đánh giá thêm hệ số bao phủ lãi vay trong kịch bản xấu trước khi kết luận cuối cùng, theo đúng cách tiếp cận ở case study mục III.3, Bước 6.)*

### Bài 6 (Nâng cao — Tự thực hành với doanh nghiệp của chính bạn)
Áp dụng toàn bộ quy trình 6 bước ở case study mục III.3 (Thành Phát) cho chính doanh nghiệp/ý tưởng kinh doanh của bạn: xác định số vốn cần huy động thêm, so sánh tối thiểu 2 phương án tài trợ (vay/vốn chủ/kết hợp), tính WACC, EPS, ROE cho từng phương án, và bắt buộc thực hiện stress test (giảm EBIT 20-30%) trước khi đưa ra khuyến nghị cuối cùng.

---

## PHỤ LỤC: CHECKLIST CAPITAL STRUCTURE TỔNG HỢP

```
PHÂN TÍCH:
□ D/E ratio hiện tại vs peers/industry?
□ WACC tối ưu tại D/E nào?
□ Tax shield value bao nhiêu?
□ Distress probability & costs estimated?
□ Debt capacity (max debt before distress)?

QUYẾT ĐỊNH:
□ Business stability → chịu được leverage?
□ Asset tangibility → collateral available?
□ Growth needs → need flexibility?
□ Tax rate → tax shield meaningful?
□ Management discipline needed → more debt?
□ Pecking Order: Internal funds available first?

RISK CHECKS:
□ Interest Coverage Ratio > 3x?
□ Debt/EBITDA < 3-4x?
□ Debt maturity schedule → no cliff?
□ Covenant compliance comfortable?
□ Stress test: Can survive revenue -30%?
□ Financial flexibility reserve maintained?
```

---

*Tài liệu tham khảo: Modigliani & Miller (1958, 1963); Myers & Majluf "Pecking Order" (1984); Jensen "Agency Costs of FCF" (1986); Sharpe "Capital Asset Prices: A Theory of Market Equilibrium" (1964); Brealey, Myers & Allen 14th Ed; Damodaran "Applied Corporate Finance"*
