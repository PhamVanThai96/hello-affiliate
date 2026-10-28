# Mergers & Acquisitions – M&A (Sáp Nhập & Mua Lại)

> **Mục tiêu**: Hiểu bản chất M&A (vì sao mua, mua với giá nào là hợp lý), cách định giá thương vụ, đo lường synergies, chọn cấu trúc thanh toán (tiền mặt, cổ phiếu, vay – LBO), quy trình thực hiện, và tại sao phần lớn thương vụ M&A thất bại. Có 3 case study chi tiết (2 case quốc tế + 1 case SME Việt Nam tính toán từng bước) để người mới có thể tự ra quyết định "mua hay không mua, trả tối đa bao nhiêu".

---

## I. KHÁI NIỆM & LÝ THUYẾT

### 1. Định nghĩa

**Merger** (Sáp nhập): Hai công ty HỢP NHẤT thành một thực thể mới (A + B = C). Cả hai pháp nhân cũ chấm dứt tồn tại.

**Acquisition** (Mua lại): Một công ty MUA và kiểm soát công ty khác (A mua B → A sở hữu B, B có thể vẫn tồn tại như công ty con).

> Trong thực tế, "merger" thường vẫn là acquisition được "rebrand" để cả hai bên đều dễ chấp nhận (gọi là *merger of equals*). Bài học từ AOL – Time Warner (xem Case 2) cho thấy: luôn có một bên thực sự nắm quyền, giả vờ ngược lại chỉ gây hỗn loạn.

**Hai câu hỏi cốt lõi của mọi thương vụ M&A:**

1. **Mua cái gì và vì sao?** (Chiến lược – synergies có thật không?)
2. **Trả bao nhiêu và trả bằng gì?** (Định giá, premium, cấu trúc thanh toán)

Toàn bộ tài liệu này xoay quanh hai câu hỏi đó. Về mặt tài chính, M&A chỉ là một dạng **quyết định đầu tư vốn (Capital Budgeting)** đặc biệt: "dự án" ở đây là cả một doanh nghiệp, và quy tắc vàng vẫn là *chỉ làm khi NPV > 0*, tức giá trị nhận được lớn hơn số tiền phải bỏ ra.

### 2. Phân loại M&A

```
┌────────────────────────────────────────────────────────────┐
│                    CÁC LOẠI M&A                            │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  THEO QUAN HỆ KINH DOANH:                                  │
│  1. HORIZONTAL (Theo chiều ngang): Cùng ngành, cùng chuỗi  │
│     giá trị. VD: Facebook mua Instagram, Disney mua Fox    │
│                                                            │
│  2. VERTICAL (Theo chiều dọc): Khác vị trí trong chuỗi     │
│     giá trị. VD: Apple mua nhà cung cấp chip,              │
│     Amazon mua Whole Foods                                 │
│                                                            │
│  3. CONGLOMERATE (Tập đoàn đa ngành): Khác ngành hoàn toàn │
│     VD: Berkshire mua See's Candies, GEICO, BNSF Railroad  │
│                                                            │
│  THEO THÁI ĐỘ:                                             │
│  • FRIENDLY (Thân thiện): Board đồng ý, hai bên đàm phán   │
│  • HOSTILE (Thù địch): Target board TỪ CHỐI → Bidder đi    │
│    thẳng đến cổ đông (tender offer / proxy fight)          │
│                                                            │
│  THEO CẤU TRÚC THANH TOÁN:                                 │
│  • Stock deal: Thanh toán bằng cổ phiếu của acquirer       │
│  • Cash deal: Thanh toán bằng tiền mặt                     │
│  • Mixed: Kết hợp cash + stock                             │
│  • LBO: Leveraged Buyout (vay nợ để mua, dùng chính        │
│    dòng tiền/tài sản của target để trả nợ)                 │
│                                                            │
│  THEO ĐỐI TƯỢNG MUA:                                       │
│  • Share deal (mua cổ phần/phần vốn góp): mua cả pháp nhân │
│    kèm mọi quyền lợi & nghĩa vụ ẩn                         │
│  • Asset deal (mua tài sản): chọn lọc tài sản cần mua,     │
│    tránh rủi ro nợ ẩn nhưng phức tạp thủ tục chuyển nhượng │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### 3. Động lực M&A – Tại sao mua?

| Động lực | Giải thích | Ví dụ |
|----------|-----------|-------|
| **Synergies** (Hiệp lực) | 1 + 1 = 3 (tiết kiệm chi phí, tăng doanh thu) | Disney + Pixar: kho nội dung |
| **Growth** (Tăng trưởng) | Mua tăng trưởng nhanh hơn tự xây (organic) | Facebook mua WhatsApp (hàng tỷ user) |
| **Market power** | Giảm cạnh tranh, tăng sức mạnh định giá | T-Mobile + Sprint |
| **Diversification** | Giảm rủi ro nhờ đa ngành | Amazon mua Whole Foods |
| **Technology/IP** | Mua công nghệ/bằng sáng chế | Google mua DeepMind (AI) |
| **Talent** | Acqui-hire (mua cả đội ngũ) | Big Tech mua startup AI |
| **Tax benefit** | Khoản lỗ chuyển sang (NOL), cấu trúc thuế tối ưu | Corporate inversions |
| **Empire building** | Cái tôi CEO, thù lao gắn với quy mô công ty | Nhiều tập đoàn đa ngành thất bại |
| **Undervaluation** | Target bị định giá thấp → mua rẻ | Activist investors |

**Lưu ý quan trọng – chỉ một số động lực tạo giá trị thật cho cổ đông.** Synergies, công nghệ, và mua target bị định giá thấp là những lý do *có thể* tạo giá trị. Đa dạng hóa (cổ đông tự đa dạng hóa danh mục rẻ hơn nhiều bằng cách mua cổ phiếu khác) và "empire building" gần như chỉ phục vụ lợi ích của ban lãnh đạo, thường *phá hủy* giá trị cho cổ đông.

### 4. Bối cảnh lịch sử: Các làn sóng M&A và vì sao nó lặp đi lặp lại

M&A không diễn ra đều đặn mà đến theo **các làn sóng (merger waves)**, mỗi làn sóng gắn với một biến động kinh tế/công nghệ/pháp lý:

| Làn sóng | Thời kỳ | Đặc điểm | Hệ quả |
|----------|---------|----------|--------|
| 1 | 1890s–1904 | Sáp nhập ngang để tạo độc quyền (Standard Oil, US Steel) | Đạo luật Sherman (1890) và Clayton (1914) ra đời để chống độc quyền |
| 2 | 1916–1929 | Sáp nhập dọc, tạo "oligopoly" | Chấm dứt bởi khủng hoảng 1929 |
| 3 | 1960s | Tập đoàn đa ngành (conglomerate) | Phần lớn tan rã trong thập niên 1970–80 vì quản lý kém |
| 4 | 1980s | Thâu tóm thù địch, LBO, "junk bond" (trái phiếu rủi ro cao) | Thương vụ RJR Nabisco (1988, ~25 tỷ USD) do KKR dẫn dắt là biểu tượng |
| 5 | 1990s–2000 | Sáp nhập xuyên biên giới, công nghệ – viễn thông, dùng cổ phiếu "định giá bong bóng" | Kết thúc với bong bóng dot-com (AOL – Time Warner là đỉnh điểm) |
| 6–7 | 2003–nay | Private equity, mua lại xuyên quốc gia, thương vụ công nghệ/AI | Làn sóng tăng khi lãi suất thấp, co lại khi lãi suất tăng |

**Vì sao cần biết lịch sử này?** Vì có hai quy luật nhận thấy lặp đi lặp lại:

1. **Làn sóng M&A thường đi cùng thị trường chứng khoán nóng và tín dụng rẻ.** Khi cổ phiếu đắt (đồng tiền "rẻ"), các công ty dùng cổ phiếu để mua. Khi bong bóng vỡ, nhiều thương vụ lộ ra là trả giá quá cao.
2. **Cùng một lỗi lặp lại**: Giả thuyết kiêu ngạo của **Richard Roll (1986) – "hubris hypothesis"** cho rằng nhà quản lý tin mình định giá chính xác hơn thị trường và hay trả quá cao; còn hiện tượng **"lời nguyền người thắng thầu" (winner's curse)** (Capen, Clapp và Campbell, 1971 – nghiên cứu đấu giá dầu khí) cho thấy bên thắng đấu giá thường chính là bên đã ước lượng giá trị quá lạc quan nhất.

### 5. Tỷ lệ thành công của M&A – "Hôn nhân lần hai"

```
CÁC NGHIÊN CỨU THƯỜNG CHO THẤY (số liệu tổng hợp, thay đổi theo mẫu & giai đoạn):
• Khoảng 60-70% thương vụ M&A KHÔNG tạo giá trị (hoặc phá hủy giá trị) cho cổ đông acquirer
• Giá cổ phiếu acquirer trung bình giảm nhẹ khi công bố (khoảng 1-3%)
• Cổ đông target hưởng lợi lớn (premium trung bình 20-30%+)
• Synergies thực hiện được thường chỉ khoảng 50-70% so với dự kiến
• Quá trình tích hợp thường kéo dài gấp 2-3 lần kế hoạch

"M&A giống cuộc hôn nhân lần hai – chiến thắng của niềm hy vọng trước kinh nghiệm"
```

> **Cách hiểu đúng**: Con số trên không có nghĩa "đừng bao giờ làm M&A". Nó có nghĩa: *giá trị thường chảy về phía người bán (target)*, còn bên mua chỉ hưởng lợi nếu **synergies thực sự lớn hơn premium đã trả** (xem mục II.B). Đây là lý do toàn bộ tài liệu này nhấn mạnh việc tính "giá tối đa chấp nhận được" (walk-away price) trước khi đàm phán.

---

## II. CHI TIẾT TỪNG THÀNH PHẦN

### A. Định giá trong M&A (Valuation)

#### 1. Vì sao cần nhiều phương pháp định giá cùng lúc?

Không có "một con số giá trị đúng" của một doanh nghiệp. Mỗi phương pháp trả lời một câu hỏi khác nhau và mắc những sai số khác nhau:

- **DCF** (Discounted Cash Flow) hỏi: *"Doanh nghiệp này kiếm được bao nhiêu tiền trong tương lai, quy về hôm nay?"* → mạnh về nền tảng nhưng cực nhạy với giả định (tốc độ tăng trưởng g, chi phí vốn WACC).
- **Comparable Companies** (Công ty tương đương) hỏi: *"Thị trường đang trả bao nhiêu cho những công ty giống thế này?"* → phản ánh tâm lý thị trường hiện tại, nhưng thị trường có thể đang quá lạc quan hoặc bi quan.
- **Precedent Transactions** (Giao dịch tiền lệ) hỏi: *"Trong các thương vụ M&A tương tự, người ta đã trả bao nhiêu?"* → đã **bao gồm premium kiểm soát** (control premium) nên thường cao hơn Comps.

Dùng cả ba rồi **kết hợp thành một khoảng giá trị** (range) giúp giảm rủi ro dựa dẫm vào một giả định duy nhất. Công cụ trình bày khoảng này gọi là **Football Field** (nhìn như sân bóng với các thanh ngang chồng lên nhau).

| Method | Cách tiếp cận | Phù hợp nhất cho |
|--------|---------------|-------------------|
| **DCF** | Nội tại: PV của dòng tiền tự do (FCF) tương lai | Giá trị cơ bản (fundamental value) |
| **Comparable Companies** | Tương đối: bội số của công ty cùng ngành đang niêm yết | Đối chiếu thị trường |
| **Precedent Transactions** | Tương đối: bội số của các thương vụ M&A đã diễn ra | Ước lượng control premium |

#### 2. Bội số EV/EBITDA – công thức & lý do

$$EV = Vốn\,hóa\,thị\,trường + Nợ\,vay - Tiền\,mặt$$

$$EV/EBITDA = \frac{Enterprise\,Value}{EBITDA}$$

**Tại sao dùng EV (Enterprise Value) chứ không dùng giá cổ phiếu?** Khi mua cả công ty, người mua không chỉ trả cho cổ đông mà còn **gánh khoản nợ** và **được hưởng khoản tiền mặt** của target. EV là "giá thật sự phải trả để sở hữu toàn bộ hoạt động kinh doanh", không phụ thuộc vào cách công ty tài trợ (nhiều nợ hay ít nợ). Nhờ vậy so sánh được giữa các công ty có cơ cấu vốn khác nhau.

**Tại sao dùng EBITDA?** EBITDA (lợi nhuận trước lãi vay, thuế, khấu hao) loại bỏ ảnh hưởng của cơ cấu vốn (lãi vay), chính sách thuế và chính sách khấu hao – những yếu tố thay đổi theo từng công ty – nên bội số EV/EBITDA là thước đo "ngang tầm" được giữa các công ty. Nhược điểm: bỏ qua nhu cầu đầu tư (capex), nên với ngành nặng tài sản cần kiểm tra thêm EV/EBIT hoặc FCF.

**Từ EV sang giá trị vốn chủ (Equity Value) – bước hay bị quên:**

$$Equity\,Value = EV - Nợ\,ròng \quad (Nợ\,ròng = Nợ\,vay - Tiền\,mặt)$$

#### 3. Football Field – minh họa

```
                    Khoảng giá trị (tỷ USD)
Phương pháp         │ Low    │ Mid    │ High   │
────────────────────┼────────┼────────┼────────┤
52-Week Trading     │   8    │  10    │   12   │
                    │████████│████████│████████│
DCF                 │   9    │  12    │   15   │
                    │████████│████████│████████│████
Comparable Cos      │   10   │  11    │   13   │
                    │████████│████████│████████│
Precedent Txns      │   11   │  13    │   16   │
                    │████████│████████│████████│████
                    └────────┴────────┴────────┘
                         ◄── Offer range ──►
                         ($11-14B điển hình)
```

**Cách đọc**: Vùng nằm *chồng lên nhau* ở nhiều phương pháp (ở đây khoảng 11-13) là vùng giá "an toàn" nhất. Khoảng chào giá (offer range) thường nằm giữa giá trị nội tại và mức premium thị trường chấp nhận.

#### 4. Control premium – vì sao người mua trả cao hơn giá thị trường?

Giá cổ phiếu trên sàn là giá của **cổ đông thiểu số** (không có quyền quyết định). Khi mua kiểm soát, người mua có quyền thay ban lãnh đạo, cắt chi phí, đổi chiến lược – đó là giá trị thêm, và họ buộc phải chia sẻ một phần cho cổ đông cũ để họ chịu bán. Premium điển hình **20–50%** so với giá cổ phiếu "chưa bị ảnh hưởng" (unaffected price – giá trước khi tin đồn thâu tóm xuất hiện).

---

### B. Định giá Synergies – "Điều kiện sống còn" để thương vụ tạo giá trị

#### 1. Vì sao synergies quyết định mọi thứ?

Hãy đặt câu hỏi ngây thơ: *"Nếu target đáng giá 10 tỷ trên thị trường, vì sao tôi trả 13 tỷ?"* Câu trả lời duy nhất hợp lý: vì sau khi sáp nhập, **tổng giá trị của hai công ty cộng lại lớn hơn tổng riêng lẻ**. Phần "dư ra" này gọi là synergies.

$$\text{Value of Synergies} = V_{Combined} - (V_A + V_B)$$

Nếu bạn trả premium cho cổ đông target, thì phần synergies phải đủ lớn để *bù* premium đó, nếu không thì bạn chỉ đang chuyển tiền của cổ đông mình sang cổ đông bên kia.

$$\text{Acquisition Premium} = \frac{Giá\,chào - Giá\,thị\,trường}{Giá\,thị\,trường}$$

$$\boxed{\text{Value created for acquirer} = Synergies\,(NPV) - Premium\,Paid}$$

- Nếu **Synergies > Premium** → Acquirer tạo giá trị ✅
- Nếu **Synergies < Premium** → Giá trị bị PHÁ HỦY với cổ đông acquirer ❌

**Ví dụ nhanh**: Target vốn hóa 10 tỷ USD, premium 30% → giá chào 13 tỷ → premium trả = 3 tỷ. Nếu NPV synergies = 5 tỷ → tạo ra 5 − 3 = **2 tỷ giá trị** cho acquirer. Nếu synergies chỉ 2 tỷ → phá hủy 1 tỷ.

#### 2. Bốn loại synergies và độ tin cậy

| Loại synergy | Nguồn gốc | Độ tin cậy | Xác suất thực hiện |
|-------------|-----------|------------|--------------------|
| **Cost synergies** (Tiết kiệm chi phí) | Loại bỏ chức năng trùng lặp (HR, IT, trụ sở), gộp mua hàng, gộp kho vận | Cao – nằm trong tầm kiểm soát của acquirer | 70-80% |
| **Revenue synergies** (Tăng doanh thu) | Bán chéo (cross-sell), thị trường mới, sức mạnh định giá | Thấp – phụ thuộc hành vi khách hàng & đối thủ | 30-50% |
| **Financial synergies** (Tài chính) | Chi phí vay thấp hơn, tận dụng thuế | Trung bình | 60-70% |
| **Operational synergies** (Vận hành) | Quy mô, best practices | Trung bình | 50-60% |

**Quy tắc thực hành**: Với revenue synergies, hãy **chiết khấu ít nhất 50%** (tức chỉ tính 1/2 giá trị kỳ vọng) vì nó phụ thuộc vào khách hàng và đối thủ – không phải thứ mình quyết định một mình. Với cost synergies, vẫn phải trừ **chi phí tích hợp một lần** (integration cost: sa thải, di dời, hợp nhất hệ thống – thường 1-1.5 lần cost synergies hàng năm).

#### 3. Giá tối đa (Walk-away price)

Từ công thức trên, giá tối đa mà acquirer có thể trả mà *không phá hủy giá trị* là:

$$\text{Walk-away price} = V_{standalone} + NPV(Synergies) - Chi\,phí\,tích\,hợp$$

Nếu đối phương đòi giá cao hơn mức này → **bỏ đi** (walk away). Mức giá này nên được xác định *trước* khi bước vào bàn đàm phán, để tránh bị "cuốn" vào cuộc đấu giá (winner's curse). Case 3 (SME) bên dưới tính chi tiết quy trình này.

---

### C. Cấu trúc thương vụ & nguồn tài trợ (Deal Structure & Financing)

#### 1. Tiền mặt hay cổ phiếu?

| | Cash Deal (trả tiền mặt) | Stock Deal (trả bằng cổ phiếu) |
|-|-----------|-----------|
| **Thuế cho bên bán** | Phát sinh thuế ngay (taxable event) | Có thể hoãn thuế (hoán đổi cổ phiếu) |
| **Chia sẻ rủi ro** | Acquirer gánh TOÀN BỘ rủi ro | Chia sẻ (nếu trả quá cao, cả hai cùng chịu qua pha loãng) |
| **Tín hiệu thị trường** | "Cổ phiếu mình đang bị định giá THẤP nên dùng tiền" | "Cổ phiếu mình đang bị định giá CAO nên dùng cổ phiếu làm tiền" |
| **Độ tự tin** | CAO – bỏ tiền thật ra | Thấp hơn – chia sẻ rủi ro |
| **Tác động EPS** | Không pha loãng cổ phần | Pha loãng (thêm cổ phiếu) |
| **Nguồn tài trợ** | Cần tiền mặt/nợ | Không cần tiền |

**Vì sao "tín hiệu" quan trọng?** Đây là hệ quả trực tiếp của thông tin bất cân xứng (xem *Pecking Order Theory* của Myers & Majluf trong file cơ cấu vốn): ban lãnh đạo biết rõ hơn thị trường về giá trị thật của công ty mình. Khi họ chọn phát hành cổ phiếu để mua, thị trường hiểu ngầm là họ nghĩ cổ phiếu mình đang đắt → giá thường giảm khi công bố. Ngược lại, trả tiền mặt là tín hiệu tự tin. Với target, nhận cổ phiếu còn có nghĩa là *cùng gánh rủi ro tích hợp* – nên thường được dùng khi giá trị synergies chưa chắc chắn.

#### 2. Leveraged Buyout (LBO) – Mua lại bằng đòn bẩy

**Nguồn gốc**: LBO được phát triển mạnh từ thập niên 1960–70 và bùng nổ ở thập niên 1980 với các quỹ như **KKR (Kohlberg Kravis Roberts, thành lập 1976)**. Ý tưởng ban đầu gọi là "bootstrap acquisition": dùng chính tài sản và dòng tiền của công ty bị mua làm bảo đảm để vay tiền mua lại nó.

**Vấn đề LBO giải quyết**: Quỹ đầu tư muốn mua doanh nghiệp tốt nhưng không đủ vốn tự có. Nếu mua toàn bằng vốn tự có, lợi suất trên vốn bị "pha loãng". Nếu vay nhiều, mỗi đồng vốn tự có kiểm soát được nhiều tài sản hơn, nhưng đồng thời dòng tiền của target phải đủ trả nợ.

```
Cấu trúc LBO điển hình:
┌──────────────────────────────────────────────┐
│       MUA CÔNG TY TARGET (100 triệu USD)     │
├──────────────────────────────────────────────┤
│                                              │
│  NGUỒN TÀI TRỢ:                              │
│  • Vốn chủ (quỹ PE): 30M (30%)               │
│  • Nợ ưu tiên (Senior Debt): 50M (50%)       │
│  • Mezzanine (nợ thứ cấp):   20M (20%)       │
│                             ─────────        │
│  Tổng:                      100M             │
│                                              │
│  CƠ CHẾ SINH LỢI:                            │
│  1. Dùng dòng tiền target để trả nợ          │
│  2. Cải thiện vận hành → tăng EBITDA         │
│  3. Thoái vốn sau 3-7 năm (IPO hoặc bán)     │
│  4. Vốn chủ tăng từ 30M → 90M+ (gấp 3 lần!)  │
│                                              │
│  MẤU CHỐT: Quỹ PE dùng TIỀN CỦA NGƯỜI KHÁC   │
│  (nợ) để khuếch đại lợi suất vốn chủ         │
│                                              │
└──────────────────────────────────────────────┘
```

**Các động lực sinh lợi của LBO:**

$$IRR_{LBO} = f(Entry\,Multiple,\; Exit\,Multiple,\; Leverage,\; EBITDA\,Growth,\; FCF\,Paydown)$$

| Động lực | Đóng góp điển hình vào lợi suất |
|----------|----------------------|
| Tăng EBITDA (cải thiện vận hành) | 30-40% |
| Trả bớt nợ (giảm đòn bẩy – de-leveraging) | 30-40% |
| Tăng bội số (bán với EV/EBITDA cao hơn) | 20-30% |
| **IRR mục tiêu của quỹ PE** | **20-25%+** |

**Ví dụ số minh họa từng bước** (đơn vị triệu USD):

- Mua vào: EV = 100 = 8 × EBITDA 12,5. Vốn chủ 30, nợ 70.
- Sau 5 năm: EBITDA tăng lên 17,5; giữ nguyên bội số 8× → EV thoái vốn = 8 × 17,5 = **140**.
- Dòng tiền trả nợ giảm nợ từ 70 xuống 35.
- Vốn chủ thu về = 140 − 35 = **105** → bội số vốn (MoM) = 105 / 30 = **3,5 lần**.

$$IRR = \left(\frac{105}{30}\right)^{1/5} - 1 = 28{,}5\%/năm$$

**Phân rã giá trị tạo ra (105 − 30 = 75):** EBITDA tăng (17,5 − 12,5) × 8 = **40**; trả nợ 70 − 35 = **35**; mở rộng bội số = **0**. Tức là ở ví dụ này lợi nhuận đến từ *cải thiện vận hành và dòng tiền trả nợ*, không dựa vào may mắn thị trường – đó là LBO "lành mạnh". Cảnh báo: nếu EBITDA giảm 30% thay vì tăng, đòn bẩy 70% sẽ nhanh chóng xóa sạch vốn chủ – đòn bẩy khuếch đại cả lãi lẫn lỗ.

---

### D. Phân tích Accretion/Dilution (Tăng/Pha loãng EPS)

#### 1. Vì sao cần phân tích này?

Thị trường chứng khoán và ban lãnh đạo thường "ám ảnh" với EPS (lợi nhuận trên mỗi cổ phiếu). Một thương vụ làm EPS giảm (dilutive) thường bị cổ đông phản đối, dù có thể vẫn tạo giá trị dài hạn. Vì vậy cần đo trước tác động lên EPS.

$$\text{Accretive nếu: } EPS_{pro\,forma} > EPS_{standalone}$$

$$\text{Dilutive nếu: } EPS_{pro\,forma} < EPS_{standalone}$$

$$EPS_{pro\,forma} = \frac{NI_{A} + NI_{B} + Synergies_{sau\,thuế} - Chi\,phí\,tài\,trợ_{sau\,thuế}}{Số\,CP_{A} + Số\,CP\,mới\,phát\,hành}$$

#### 2. Quy tắc nhanh (Quick Test) và lý do

> Nếu **Earnings Yield của target (E/P)** > **Chi phí tài trợ sau thuế của acquirer** → Accretive.

**Lý do**: Earnings yield (E/P = nghịch đảo của P/E) cho biết "mỗi đồng bỏ ra mua target thu lại bao nhiêu % lợi nhuận". Nếu tỷ lệ đó cao hơn chi phí của đồng tiền dùng để mua (lãi vay sau thuế, hoặc E/P của chính acquirer nếu trả bằng cổ phiếu), thì mỗi đồng mua vào "lãi" nhiều hơn "chi phí" → EPS tăng. Với thương vụ trả bằng cổ phiếu: acquirer có P/E **cao hơn** P/E của target → accretive (vì dùng "tiền đắt" mua tài sản "rẻ" theo P/E).

**Cảnh báo quan trọng**: Accretion *không* đồng nghĩa với tạo giá trị. Một thương vụ có thể làm EPS tăng chỉ vì dùng nợ rẻ hoặc P/E của acquirer cao – trong khi giá trả vẫn vượt quá giá trị thực. Hãy luôn đối chiếu bằng NPV (Value created = Synergies − Premium). Case 3 minh họa chính điều này.

---

### E. Goodwill và kế toán M&A (tại sao "lợi thế thương mại" là rủi ro)

Khi giá mua vượt giá trị hợp lý (fair value) của tài sản ròng có thể xác định, phần chênh lệch ghi nhận là **Goodwill** (Lợi thế thương mại):

$$Goodwill = Giá\,mua - (Giá\,trị\,hợp\,lý\,tài\,sản\,ròng\,xác\,định\,được)$$

**Vì sao cần hiểu?** Goodwill không phải tiền mặt, không khấu hao theo chuẩn IFRS/US GAAP (chỉ kiểm tra **suy giảm giá trị – impairment** hàng năm); nó là "dấu vết kế toán" của premium đã trả. Khi thương vụ không đạt kỳ vọng, goodwill bị **ghi giảm (write-down)** – làm lợi nhuận kỳ đó sụt mạnh, như khoản 99 tỷ USD của AOL Time Warner. Goodwill chiếm tỷ trọng càng lớn trong tổng giá mua thì rủi ro ghi giảm càng cao, và đó cũng là chỉ báo mức độ phụ thuộc vào synergies tương lai. (Theo VAS Việt Nam, lợi thế thương mại thường được phân bổ dần theo thời gian – nên kiểm tra quy định kế toán hiện hành khi áp dụng.)

---

### F. Quy trình M&A (Process)

```
QUY TRÌNH BÁN (SELL-SIDE) ĐIỂN HÌNH (3-6 tháng):

Giai đoạn 1: CHUẨN BỊ (4-6 tuần)
  │ • Thuê ngân hàng đầu tư/tư vấn (advisor)
  │ • Chuẩn bị Information Memo (IM)
  │ • Xác định người mua tiềm năng (50-100)
  │ • Lập data room
  ▼
Giai đoạn 2: TIẾP THỊ (4-6 tuần)
  │ • Liên hệ người mua (teaser → NDA → IM)
  │ • Thuyết trình của ban quản lý
  │ • Nhận Indications of Interest (IOI – thư bày tỏ quan tâm)
  │ • Chọn danh sách rút gọn (5-10 người mua)
  ▼
Giai đoạn 3: THẨM ĐỊNH (Due Diligence) (4-8 tuần)
  │ • Mở data room cho người mua đã chọn
  │ • Gặp ban quản lý, thăm cơ sở
  │ • Người mua thẩm định tài chính, pháp lý, thương mại
  │ • Nhận giá chào cuối cùng có ràng buộc (binding bids)
  ▼
Giai đoạn 4: ĐÀM PHÁN & KÝ KẾT (2-4 tuần)
  │ • Chọn người mua ưu tiên
  │ • Đàm phán SPA (Sale and Purchase Agreement)
  │ • Hội đồng quản trị duyệt, ý kiến độc lập (fairness opinion)
  │ • Ký thỏa thuận chính thức
  ▼
Giai đoạn 5: HOÀN TẤT (CLOSING) (4-12 tuần)
  │ • Cơ quan quản lý duyệt (chống độc quyền)
  │ • Cổ đông biểu quyết (nếu cần)
  │ • Thỏa mãn điều kiện tiên quyết
  │ • Đóng giao dịch → Chuyển tiền → Chuyển quyền sở hữu
  ▼
Giai đoạn 6: TÍCH HỢP (6-24 tháng)
  │ • PMI (Post-Merger Integration)
  │ • Hiện thực hóa synergies
  │ • Giữ chân nhân tài chủ chốt
  │ • Hợp nhất hệ thống, văn hóa
  └→ THÀNH CÔNG hay THẤT BẠI được quyết định ở đây!
```

#### Due Diligence – Danh mục thẩm định

**Vì sao cần thẩm định?** Người bán luôn biết về doanh nghiệp của họ nhiều hơn người mua (bất cân xứng thông tin). Due diligence là quá trình để người mua *thu hẹp khoảng cách thông tin* trước khi trả tiền, và tìm ra những "quả mìn" (nợ ẩn, kiện tụng, khách hàng sắp rời bỏ) để điều chỉnh giá hoặc từ bỏ.

| Lĩnh vực | Hạng mục chính |
|----------|----------|
| **Financial** (Tài chính) | Chất lượng doanh thu, định kỳ vs một lần, vốn lưu động, nợ, nợ ngoài bảng |
| **Legal** (Pháp lý) | Kiện tụng, quyền sở hữu trí tuệ, hợp đồng, tuân thủ |
| **Commercial** (Thương mại) | Vị thế thị trường, tập trung khách hàng, lợi thế cạnh tranh |
| **Operational** (Vận hành) | Công suất, công nghệ, chuỗi cung ứng, hợp đồng lao động |
| **Tax** (Thuế) | Lỗ chuyển sang (NOL), chuyển giá, rủi ro truy thu |
| **HR** (Nhân sự) | Rủi ro mất nhân tài, đánh giá văn hóa, hợp đồng lao động |
| **IT** | Tương thích hệ thống, nợ kỹ thuật, an ninh mạng |
| **Environmental** (Môi trường) | Trách nhiệm ô nhiễm, chi phí tuân thủ |

---

### G. Chiến thuật phòng thủ (Defensive Tactics) & thâu tóm thù địch

**Vấn đề**: Khi board của target không muốn bán, bên mua có thể đi thẳng đến cổ đông qua **tender offer** (chào mua công khai) hoặc **proxy fight** (giành phiếu bầu thay board). Các chiến thuật phòng thủ ra đời để *tăng chi phí hoặc kéo dài thời gian* của kẻ thâu tóm, giúp board có thêm thời gian tìm giá tốt hơn – nhưng cũng có thể bị lạm dụng để bảo vệ ghế của ban lãnh đạo (xung đột đại diện).

| Chiến thuật | Mô tả |
|------|-------|
| **Poison Pill** (Viên thuốc độc) | Kế hoạch quyền mua: cổ đông hiện hữu được mua cổ phiếu với giá chiết khấu 50% nếu bên thâu tóm nắm >15% → pha loãng mạnh kẻ thâu tóm |
| **Staggered Board** (Hội đồng quản trị phân kỳ) | Mỗi năm chỉ 1/3 board được bầu lại → không thể thay cả board trong một lần |
| **White Knight** (Hiệp sĩ trắng) | Tìm bên mua thân thiện để trả giá cao hơn kẻ thù địch |
| **Crown Jewel Defense** | Bán tài sản giá trị nhất → target kém hấp dẫn |
| **Pac-Man Defense** | Phản công: mua ngược lại kẻ thâu tóm |
| **Golden Parachute** (Dù vàng) | Khoản bồi thường lớn cho lãnh đạo nếu công ty bị mua → tăng chi phí thương vụ |
| **Shark Repellent** | Yêu cầu tỷ lệ phiếu siêu đa số (80%+) để phê duyệt sáp nhập |

---

### H. Ưu điểm & Nhược điểm của M&A

#### ✅ Ưu điểm
1. **Speed** (Tốc độ) – Mua nhanh hơn tự xây (organic mất nhiều năm)
2. **Market position** – Có ngay thị phần, tập khách hàng
3. **Synergies** – Tiết kiệm chi phí, tăng doanh thu
4. **Technology/IP** – Sở hữu đổi mới tức thì
5. **Talent** – Có cả đội ngũ chuyên môn
6. **Diversification** – Giảm rủi ro tập trung kinh doanh
7. **Tax benefits** – Tận dụng lỗ chuyển sang (NOL), khấu hao

#### ❌ Nhược điểm / Rủi ro
1. **Overpayment** – Lý do số 1 khiến M&A phá hủy giá trị (winner's curse)
2. **Integration failure** – Xung đột văn hóa, hệ thống không tương thích
3. **Synergy overestimation** – "Revenue synergies" hiếm khi đạt đủ
4. **Management distraction** – 12-18 tháng tập trung tích hợp thay vì vận hành
5. **Talent flight** – Nhân sự chủ chốt rời đi sau mua lại
6. **Debt burden** – LBO có thể quá đòn bẩy → khó khăn tài chính
7. **Regulatory risk** – Bị chống độc quyền chặn sau khi đã chi hàng triệu USD
8. **Cultural destruction** – Mua sự sáng tạo rồi vô tình giết chết nó

### I. Sai lầm phổ biến & cách phòng tránh

| Sai lầm | Phòng tránh |
|---------|-----------|
| Trả quá cao (winner's curse) | Kỷ luật: rời đi nếu giá vượt mức tối đa (walk-away price) |
| Kiêu ngạo/xây đế chế (Hubris) | Hội đồng quản trị độc lập giám sát, lấy ý kiến cổ đông |
| Phóng đại synergies | Chiết khấu revenue synergies ≥50%, lộ trình thận trọng |
| Bỏ qua xung đột văn hóa | Đánh giá văn hóa trước thương vụ, có kế hoạch tích hợp |
| Không giữ được nhân tài | "Còng tay vàng" (golden handcuffs), làm rõ vai trò TRƯỚC khi đóng deal |
| Tích hợp quá chậm | Kế hoạch 100 ngày, đội PMI chuyên trách |
| Không đánh giá lại sau mua | Theo dõi mức thực hiện synergies hàng quý |

---

## III. CASE STUDIES THỰC TẾ

> **Lưu ý về số liệu**: Hai case quốc tế dưới đây dựa trên các thông tin công khai và được làm tròn/ước lượng để phục vụ học tập; một số chỉ số (đặc biệt về giá trị tạo ra) là ước tính chứ không phải số liệu kiểm toán. Case 3 là tình huống giả định do biên soạn, số liệu đã được kiểm tra tính nhất quán.

### 1. Case Study Thành công: Disney + Pixar (7,4 tỷ USD, 2006)

#### Bối cảnh
- 2005: Disney Animation sa sút (thất bại với *Treasure Planet*, *Home on the Range*); mảng hoạt hình truyền thống đang "chết dần".
- Pixar là chuẩn mực vàng: *Toy Story, Finding Nemo, The Incredibles* – hầu hết phim đều thành công cả về nghệ thuật lẫn doanh thu.
- Hợp đồng phân phối giữa Disney và Pixar sắp hết hạn → Disney đứng trước lựa chọn: mất đối tác sáng tạo nhất (và có thể để Pixar thành đối thủ) HOẶC mua.
- CEO mới của Disney là **Bob Iger** (nhậm chức 2005), người chủ trương hàn gắn quan hệ với Pixar mà CEO tiền nhiệm đã làm rạn nứt.

#### Tóm tắt thương vụ

| Hạng mục | Chi tiết |
|------|--------|
| Giá | Khoảng 7,4 tỷ USD (toàn bộ bằng cổ phiếu Disney) |
| Premium | Rất thấp so với mức premium điển hình của M&A (gần như mua ở mức giá thị trường) |
| Định giá | Đắt theo chỉ số truyền thống (nhiều chục lần lợi nhuận) – Disney mua *giá trị chiến lược*, không mua dòng tiền hiện tại |
| Cấu trúc | Stock deal (cổ phiếu Disney trả cho cổ đông Pixar) |
| Điều khoản chính | Steve Jobs (cổ đông lớn nhất của Pixar) trở thành cổ đông cá nhân lớn nhất của Disney và vào board |
| Điều khoản chính | Pixar giữ **độc lập sáng tạo**; lãnh đạo Pixar (Ed Catmull, John Lasseter) được giao điều hành cả Disney Animation |

#### Diễn giải bước 1 – Vì sao chấp nhận định giá "đắt"?

Phân tích theo công thức *Value created = Synergies − Premium*: premium trả cho cổ đông Pixar rất nhỏ, nên chỉ cần synergies dương bất kỳ là có lời. Disney không cần bài toán tiết kiệm chi phí: giá trị nằm ở **doanh thu tăng thêm** (một loại synergy thường được xem là rủi ro cao) – nhưng ở đây nguồn gốc doanh thu rất rõ ràng và có thể kiểm chứng: (i) Disney có sức mạnh phân phối, công viên giải trí, hàng hóa mà Pixar thiếu; (ii) Pixar có năng lực sáng tạo mà Disney đã đánh mất. Đây là loại **revenue synergy có logic cụ thể** chứ không phải "sẽ bán chéo được".

#### Diễn giải bước 2 – Các nguồn giá trị (ước tính)

| Nguồn giá trị | Giá trị ước tính (doanh thu gộp, không phải lợi nhuận) |
|---------|-------------------|
| Phim tiếp theo của thương hiệu Pixar (*Toy Story 3, 4; Incredibles 2; Finding Dory*) | Hơn 10 tỷ USD doanh thu phòng vé |
| Nội dung công viên giải trí (khu Pixar, trò chơi) | Vài tỷ USD doanh thu |
| Disney Animation hồi sinh (*Frozen, Moana, Encanto*) | Hơn 8 tỷ USD doanh thu phòng vé |
| Hàng hóa & streaming (Disney+, ra mắt 2019) | Hàng tỷ USD mỗi năm |

> **Lưu ý khi đọc**: Doanh thu phòng vé *không phải* giá trị tạo ra. Sau khi trừ chi phí sản xuất, tiếp thị, chia sẻ với rạp, lợi nhuận thực chỉ là một phần nhỏ. Vì vậy ROI bên dưới chỉ là **chỉ báo định tính** cho thấy mức độ thành công, không phải số liệu tài chính chính xác.

#### Diễn giải bước 3 – Tính ROI chỉ báo

Giả sử (ước tính thận trọng) tổng giá trị kinh tế gia tăng quy về hiện tại đạt 50 tỷ USD – thấp hơn nhiều so với tổng doanh thu gộp kể trên:

$$ROI = \frac{Value\,Created - Price\,Paid}{Price\,Paid} = \frac{50 - 7{,}4}{7{,}4} = 5{,}76 \Rightarrow \approx 576\%$$

Kể cả khi giá trị thật chỉ bằng 1/5 con số này (≈10 tỷ USD), thương vụ vẫn tạo lợi nhuận dương nhờ giá mua thấp so với giá trị chiến lược.

#### Vì sao thành công? (Bài học)

| Yếu tố | Chi tiết |
|-------|--------|
| **Bảo tồn văn hóa** | Pixar giữ văn hóa, quy trình sáng tạo và lãnh đạo riêng |
| **Không ép tích hợp** | Giữ studio riêng, bản sắc riêng; thay vào đó đưa người Pixar vào dẫn dắt Disney Animation |
| **Lãnh đạo tầm nhìn** | Steve Jobs + Bob Iger tôn trọng lẫn nhau |
| **Điểm mạnh bổ sung** | Disney = phân phối/thương hiệu; Pixar = sáng tạo/công nghệ |
| **Giữ chân nhân tài** | Ed Catmull và John Lasseter ở lại, được trao nhiều quyền hơn |
| **Giá hợp lý so với giá trị chiến lược** | Premium thấp, giá trị tạo ra lớn |
| **Luận điểm chiến lược rõ ràng** | "Thắng trong mảng hoạt hình" – đo được, cụ thể |

> **Bài học cốt lõi**: Với doanh nghiệp *sáng tạo/con người là tài sản chính*, tích hợp mạnh tay thường phá hủy chính thứ mình mua. Mô hình "mua và để độc lập có kiểm soát" là cách bảo toàn giá trị.

---

### 2. Case Study Thất bại: AOL + Time Warner (182 tỷ USD, 2000)

#### Bối cảnh
- Tháng 1/2000: "Sáp nhập của thế kỷ" – AOL (internet) mua Time Warner (truyền thông/nội dung); lớn nhất lịch sử vào thời điểm đó: khoảng **182 tỷ USD**.
- Luận điểm: "Hội tụ giữa nội dung và phân phối internet" – mỗi bên bổ sung cho bên kia.
- Thời điểm: gần đỉnh bong bóng dot-com – định giá cổ phiếu internet cực kỳ phi thực tế.

#### Tóm tắt thương vụ

| Hạng mục | Chi tiết |
|------|--------|
| Giá | Khoảng 182 tỷ USD (toàn bộ bằng cổ phiếu) |
| Doanh thu kết hợp | Khoảng 33 tỷ USD |
| Vốn hóa AOL | Khoảng 163 tỷ USD (!!!) – đúng đỉnh dot-com |
| Vốn hóa Time Warner | Khoảng 83 tỷ USD |
| Premium | Khoảng 71% so với giá thị trường của cổ đông Time Warner |
| Thế đứng | AOL là bên mua, nhưng được gọi là "merger of equals" |
| Luận điểm | Internet + Nội dung = đế chế truyền thông bất khả chiến bại |

#### Phân tích bước 1 – Công thức "Synergies − Premium" áp vào AOL–TW

Premium 71% trên vốn hóa ~83 tỷ USD tương ứng khoảng **59 tỷ USD** tiền thưởng cho cổ đông Time Warner (83 × 0,71 ≈ 59). Điều này nghĩa là AOL phải chứng minh được **NPV synergies > 59 tỷ USD** mới tạo được giá trị. Hỏi ngược lại: synergy cụ thể nào đáng 59 tỷ? Không ai trả lời được bằng con số cụ thể – "cross-sell" khách hàng AOL sang tạp chí và cáp là khẩu hiệu, không phải kế hoạch.

#### Phân tích bước 2 – Điều gì đã sai

| Yếu tố | Chi tiết |
|--------|--------|
| **Dot-com sụp đổ** | Vốn hóa AOL giảm từ khoảng 163 tỷ → còn khoảng 20 tỷ USD trong vòng ~2 năm |
| **Dùng "tiền giả" mua tài sản thật** | Cổ phiếu AOL bị định giá quá cao → dùng làm đồng tiền mua tài sản truyền thống có giá trị thật |
| **Không có synergies thực** | Internet + cáp + tạp chí → gần như không có synergies đáng kể |
| **Chiến tranh văn hóa** | AOL (trẻ, công nghệ, thoải mái) vs TW (truyền thông cũ, phân cấp, doanh nghiệp truyền thống) |
| **Revenue synergies là ảo tưởng** | "Bán chéo" không thành: khách hàng khác nhau, nhu cầu khác nhau |
| **Xung đột lãnh đạo** | Lãnh đạo AOL và TW liên tục tranh giành quyền lực |
| **Thay đổi công nghệ** | Băng thông rộng (broadband) giết chết mô hình quay số (dial-up) của AOL chỉ sau vài năm |
| **Ghi giảm tài sản** | Khoản ghi giảm goodwill khoảng **99 tỷ USD** (2002) – lớn nhất lịch sử vào thời điểm đó |

#### Phân tích bước 3 – Thiệt hại tài chính (ước tính làm tròn)

| Chỉ số | Khi sáp nhập (2000) | ~3 năm sau (2003) |
|--------|-----------------|---------------------|
| Vốn hóa kết hợp | Khoảng 280 tỷ USD | Khoảng 72 tỷ USD |
| Giá trị bốc hơi | | Khoảng **208 tỷ USD** |
| Ghi giảm goodwill | 0 | Khoảng 99 tỷ USD |
| Thuê bao AOL | Tăng nhanh đến đỉnh, rồi suy giảm | Suy giảm liên tục |

Phép tính cơ bản của khoản bốc hơi: 280 − 72 = **208** tỷ USD. Phần lớn đây là sự sụp đổ của chính bong bóng định giá, không chỉ do M&A, nhưng thương vụ khiến cổ đông Time Warner (vốn đang sở hữu tài sản thực) phải gánh luôn rủi ro bong bóng.

#### Bài học M&A thất bại

```
1. ĐỊNH GIÁ QUYẾT ĐỊNH TẤT CẢ:
   AOL dùng cổ phiếu ĐƯỢC PHÓNG ĐẠI giá để "mua" tài sản thật
   → Khi cổ phiếu về giá thật, việc trả quá cao lộ ra
   → BÀI HỌC: Stock deal ở đỉnh thị trường = nguy hiểm

2. "SYNERGIES" CẦN CÓ LOGIC:
   "Internet + Cáp + Tạp chí" = synergy gì chính xác?
   → Nếu không diễn đạt được synergy CỤ THỂ bằng tiền, đừng làm

3. SỰ PHÙ HỢP VĂN HÓA LÀ BẮT BUỘC:
   AOL = văn hóa startup. TW = doanh nghiệp truyền thống.
   Trộn dầu với nước → hai bên khổ sở, nhân tài ra đi

4. PHẢI CÓ KẾ HOẠCH TÍCH HỢP TRƯỚC KHI KÝ:
   Không có kế hoạch rõ → 2 năm hỗn loạn
   → Lên kế hoạch tích hợp TRƯỚC khi ký, không phải sau

5. RỦI RO CÔNG NGHỆ:
   Mảng cốt lõi của AOL (dial-up) đang HẤP HỐI
   → Mua KHÔNG sửa được một mô hình kinh doanh đã hỏng

6. KIÊU NGẠO (HUBRIS):
   "Sáp nhập của thế kỷ" → thất bại lớn của thế kỷ
   → Càng khoa trương, càng ngã đau

7. "MERGER OF EQUALS" LÀ NÓI DỐI:
   Luôn có một bên là acquirer. Giả vờ khác đi → hỗn loạn
```

---

### 3. Case Study SME Việt Nam: "Bánh Quê Xưa" mua lại "Hạnh Phúc Bakery"

#### Bối cảnh doanh nghiệp

**Bánh Quê Xưa (Acquirer – Bên mua)**: công ty sản xuất bánh truyền thống tại Đồng Nai, bán qua hệ thống đại lý và siêu thị khu vực Đông Nam Bộ. Không vay nợ, đang có 10.000 triệu đồng tiền mặt dư. Giá cổ phiếu nội bộ giao dịch quanh P/E = 8.

| Chỉ tiêu (triệu đồng) | Bánh Quê Xưa |
|---------|-------------|
| EBITDA | 5.500 |
| Khấu hao | 1.750 |
| EBIT | 3.750 |
| Lợi nhuận sau thuế (thuế TNDN 20%) | 3.000 |
| Số cổ phần | 1.000 nghìn cổ phần |
| EPS | 3.000 đồng/cổ phần |
| Giá/cổ phần (P/E = 8) | 24.000 đồng |

**Hạnh Phúc Bakery (Target – Bên bị mua)**: chuỗi tiệm bánh tại TP.HCM và Bình Dương, chủ sở hữu muốn nghỉ hưu và bán. Có sản phẩm bổ sung (bánh tươi), kênh bán lẻ trực tiếp.

| Chỉ tiêu (triệu đồng) | Hạnh Phúc Bakery |
|---------|-------------|
| Doanh thu | 20.000 |
| EBITDA | 4.000 |
| Khấu hao | 600 |
| EBIT | 3.400 |
| Nợ vay (lãi 10%/năm) | 2.000 |
| Tiền mặt | 500 |
| Lãi vay | 200 |
| Lợi nhuận trước thuế | 3.200 |
| Lợi nhuận sau thuế (20%) | 2.560 |
| Vốn chủ sổ sách (book value) | 9.000 |

Chủ Hạnh Phúc đòi **22.000 triệu** cho 100% vốn chủ. Câu hỏi của Hội đồng Bánh Quê Xưa: *Định giá độc lập của Hạnh Phúc là bao nhiêu? Synergies đáng giá bao nhiêu? Trả tối đa bao nhiêu? Trả bằng gì? Thương vụ có làm EPS tăng không? Rủi ro nào lớn nhất?*

#### Bước 1: Định giá độc lập (Stand-alone) của Hạnh Phúc Bakery

**Phương pháp 1 – Bội số EV/EBITDA của công ty cùng ngành quy mô nhỏ (5×)**:

$$EV = 5 \times 4.000 = 20.000 \quad;\quad Nợ\,ròng = 2.000 - 500 = 1.500$$

$$Equity = 20.000 - 1.500 = 18.500$$

**Phương pháp 2 – Giao dịch tiền lệ (5,5×, đã gồm premium kiểm soát)**:

$$EV = 5{,}5 \times 4.000 = 22.000 \;\Rightarrow\; Equity = 22.000 - 1.500 = 20.500$$

**Phương pháp 3 – DCF**. Trước hết tính dòng tiền tự do (FCF):

$$NOPAT = EBIT \times (1 - t) = 3.400 \times 0{,}8 = 2.720$$

$$FCF = NOPAT + Khấu\,hao - Capex - \Delta Vốn\,lưu\,động = 2.720 + 600 - 500 - 20 = 2.800$$

Giả định tăng trưởng vĩnh viễn g = 4%, WACC = 18% (cao hơn doanh nghiệp lớn vì SME, thiếu thanh khoản, rủi ro chủ sở hữu). Dùng công thức giá trị vĩnh viễn tăng trưởng đều (Gordon):

$$EV = \frac{FCF \times (1+g)}{WACC - g} = \frac{2.800 \times 1{,}04}{0{,}18 - 0{,}04} = \frac{2.912}{0{,}14} = 20.800$$

$$Equity = 20.800 - 1.500 = 19.300$$

**Tổng hợp (Football Field của case)**:

| Phương pháp | EV | Equity |
|--------|----|--------|
| EV/EBITDA 5× (Comps) | 20.000 | 18.500 |
| DCF | 20.800 | **19.300** |
| Giao dịch tiền lệ 5,5× | 22.000 | 20.500 |

**Quyết định**: Dùng DCF **19.300** làm giá trị độc lập (stand-alone) "neo" vì nó nằm giữa khoảng 18.500–20.500. Chủ Hạnh Phúc đòi 22.000 – cao hơn cả mức cao nhất của tiền lệ (20.500) tới 1.500 triệu.

#### Bước 2: Định giá Synergies

Đội M&A của Bánh Quê Xưa xác định 2 nguồn synergies:

- **Cost synergies**: Gộp mua nguyên liệu (bột, đường, bơ), dùng chung kho và vận chuyển → tiết kiệm trước thuế **300 triệu năm 1, 600 triệu/năm từ năm 2 trở đi** (duy trì vĩnh viễn, không tăng trưởng).
- **Revenue synergies**: Đưa bánh Hạnh Phúc vào hệ thống đại lý/siêu thị của Bánh Quê Xưa → EBITDA tăng thêm 500 triệu/năm từ năm 2 đến năm 5. **Chiết khấu 50% xác suất** (theo quy tắc ở mục II.B) → chỉ tính 250 triệu/năm.
- **Chi phí tích hợp một lần**: 1.200 triệu (đổi bao bì, hợp nhất phần mềm, hỗ trợ nhân viên nghỉ việc) – ghi nhận tại thời điểm 0.

Chiết khấu ở r = 18%, thuế t = 20%.

**Cost synergies, 5 năm đầu** (sau thuế = trước thuế × 0,8):

$$PV_{5\,năm} = \frac{300 \times 0{,}8}{1{,}18} + \frac{600 \times 0{,}8}{1{,}18^2} + \frac{600 \times 0{,}8}{1{,}18^3} + \frac{600 \times 0{,}8}{1{,}18^4} + \frac{600 \times 0{,}8}{1{,}18^5} \approx 1.297{,}7$$

**Cost synergies, giá trị vĩnh viễn từ năm 6** (tính ở cuối năm 5 rồi chiết khấu về hiện tại):

$$TV = \frac{600 \times 0{,}8}{0{,}18} = 2.666{,}7 \;\Rightarrow\; PV = \frac{2.666{,}7}{1{,}18^5} \approx 1.165{,}6$$

$$PV(Cost\,synergies) \approx 1.297{,}7 + 1.165{,}6 = 2.463{,}3$$

**Revenue synergies** (250 triệu đã chiết khấu xác suất, sau thuế = 200, năm 2–5):

$$PV = \sum_{k=2}^{5} \frac{500 \times 0{,}5 \times 0{,}8}{1{,}18^k} \approx 455{,}9$$

**NPV synergies ròng**:

$$NPV_{syn} = 2.463{,}3 + 455{,}9 - 1.200 = \boxed{1.719{,}2 \text{ triệu}}$$

**Diễn giải**: Chỉ riêng cost synergies đã chiếm phần lớn (2.463 trong tổng 2.919 trước chi phí tích hợp); revenue synergies đóng góp nhỏ, đúng với nguyên tắc "không dựa vào doanh thu tăng thêm làm trụ cột của giá".

#### Bước 3: Giá tối đa (Walk-away price) và premium

$$\text{Walk-away}_{tổng\,synergies} = 19.300 + 1.719{,}2 = 21.019$$

$$\text{Walk-away}_{chỉ\,cost\,synergies} = 19.300 + (2.463{,}3 - 1.200) = 20.563$$

Giá đòi của chủ **22.000 > 21.019** → vượt walk-away price. Nếu trả đúng 22.000, Bánh Quê Xưa phá hủy khoảng 22.000 − 21.019 ≈ **981 triệu** giá trị ngay cả khi mọi synergies thành công (kể cả revenue synergies chiết khấu).

Hội đồng đề xuất phương án đàm phán **"giá tối đa kịch bản mở" 20.500 triệu** (bao gồm giá cơ sở 19.800 + earn-out tối đa 700 triệu gắn với việc giữ chân khách hàng lớn và thợ bánh trưởng 24 tháng), tức bằng mức tiền lệ cao nhất và dưới walk-away chỉ-cost-synergies (20.563):

$$Premium = 20.500 - 19.300 = 1.200 \;(6{,}2\%\,so\,với\,DCF;\;10{,}8\%\,so\,với\,Comps\,18.500)$$

$$Value\,created = NPV_{syn} - Premium = 1.719{,}2 - 1.200 = \boxed{519{,}2 \text{ triệu}}$$

(Nếu chỉ chốt ở giá cơ sở 19.800: premium = 500, Value created = 1.719,2 − 500 = **1.219,2** triệu.)

#### Bước 4: Kiểm tra độ nhạy – "Điều gì xảy ra nếu synergies kém hơn dự tính?" (Stress test giá trị)

Giữ giá 20.500 (premium 1.200), thay đổi mức thực hiện synergies:

| Kịch bản | NPV synergies ròng | Value created = NPV − 1.200 |
|--------|-----------------|------------------|
| Cơ sở (100% cost + 50% xác suất revenue) | 1.719,2 | **+519,2** |
| Chỉ cost synergies (revenue = 0) | 1.263,3 | **+63,3** |
| Cost synergies chỉ đạt 50%, revenue = 0 | 2.463,3 × 0,5 − 1.200 = 31,6 | **−1.168,4** |
| Cost synergies 100%, revenue = 0, chi phí tích hợp 1.800 (vượt 50%) | 2.463,3 − 1.800 = 663,3 | **−536,7** |

Phép tính điểm hòa vốn: nếu revenue synergies = 0 và chi phí tích hợp đúng 1.200, cost synergies phải đạt tối thiểu $(1.200 + 1.200)/2.463{,}3 \approx 97{,}4\%$ kế hoạch thì mới hòa vốn → **biên an toàn rất mỏng ở mức giá 20.500**.

> **Bài học**: Mức giá 20.500 chỉ tạo giá trị khi gần như mọi thứ đều đúng kế hoạch. Đó là lý do cấu trúc **earn-out** (trả sau, gắn với kết quả) là công cụ rất phù hợp: phần giá cơ sở 19.800 có biên an toàn tốt hơn (Value created dương cả khi chỉ cost synergies: 1.263,3 − 500 = 763,3), còn 700 triệu còn lại chỉ phải trả nếu rủi ro đã được giải tỏa.

#### Bước 5: Cấu trúc thanh toán và tác động EPS (kịch bản giá tối đa 20.500)

Ba phương án tài trợ (giả định lãi vay mới 11%/năm, lãi tiền gửi mất đi 5%/năm, thuế 20%, cổ phiếu Bánh Quê Xưa định giá 24.000 đồng):

**Chi phí sau thuế**: lãi vay = 11% × 0,8 = **8,8%**; tiền mặt sử dụng = 5% × 0,8 = **4,0%**.

**Phương án A – Hỗn hợp**: 8.000 tiền mặt + 6.500 vay + 6.000 cổ phiếu mới (tổng = 20.500).

- Cổ phần mới = 6.000 triệu / 24.000 đồng = **250 nghìn cổ phần** → tổng 1.250 nghìn.
- Chi phí tài trợ sau thuế = (6.500 × 11% + 8.000 × 5%) × 0,8 = (715 + 400) × 0,8 = **892 triệu**.
- LNST kết hợp năm 1 (chưa có synergies) = 3.000 + 2.560 − 892 = **4.668** triệu.

$$EPS_{pro\,forma,\,Y1} = \frac{4.668}{1.250} = 3{,}7344 \text{ triệu/nghìn CP} \approx 3.734\,đ \;\Rightarrow\; +24{,}5\%$$

- Năm 3, đã có cost synergies sau thuế 600 × 0,8 = 480: LNST = 5.148 → EPS = 5.148/1.250 = 4,118 (≈ **+37,3%**).

**Phương án B – 100% cổ phiếu**: cổ phần mới = 20.500 / 24 = 854,2 nghìn → tổng 1.854,2 nghìn.

$$EPS_{Y1} = \frac{3.000 + 2.560}{1.854{,}2} = 2{,}9987 \approx 2.999\,đ \Rightarrow \approx 0\%\;\text{(trung lập)}$$

$$EPS_{Y3} = \frac{5.560 + 480}{1.854{,}2} = 3{,}2575 \Rightarrow +8{,}6\%$$

Lý do EPS Y1 gần như không đổi: **E/P của target = 2.560/20.500 = 12,49%**, gần bằng **E/P của chính Bánh Quê Xưa = 1/8 = 12,5%** → đúng như Quick Test dự báo (bằng nhau → không tăng, không giảm).

**Phương án C – Tiền mặt + vay**: 8.000 tiền mặt + 12.500 vay, không phát hành cổ phiếu.

- Chi phí tài trợ sau thuế = (12.500 × 11% + 8.000 × 5%) × 0,8 = (1.375 + 400) × 0,8 = **1.420**.
- LNST năm 1 = 5.560 − 1.420 = 4.140 → EPS = 4,14 (**+38,0%**); năm 3: 4.620 → EPS 4,62 (**+54,0%**).

| Phương án | EPS Y1 | Tăng/Giảm Y1 | EPS Y3 | Tăng/Giảm Y3 |
|----------|-------|---------|-------|---------|
| Hiện tại (stand-alone) | 3.000 đ | – | – | – |
| A – Hỗn hợp | 3.734 đ | +24,5% | 4.118 đ | +37,3% |
| B – 100% cổ phiếu | 2.999 đ | ≈ 0% | 3.258 đ | +8,6% |
| C – Tiền + vay | 4.140 đ | +38,0% | 4.620 đ | +54,0% |

**Chi phí tích hợp 1.200 một lần**: nếu ghi nhận vào năm 1 của phương án A thì EPS năm 1 = (4.668 − 1.200)/1.250 = 2,774 → **−7,5%** (dilutive tạm thời). Cho thấy cần phân biệt EPS "điều chỉnh" (bỏ khoản một lần) và EPS "báo cáo".

**Phản trực giác cần nhớ**: Phương án C có EPS đẹp nhất nhưng KHÔNG tạo nhiều giá trị hơn A hay B – cả ba cùng trả 20.500 và nhận cùng NPV synergies. EPS khác nhau chỉ vì *chi phí vốn đang bị so sánh sai*: nợ trông "rẻ" (8,8%) nhưng đẩy rủi ro tài chính lên – bước 6 kiểm tra điều đó.

#### Bước 6: Kiểm tra khả năng chịu đựng của cấu trúc nợ (Phương án A)

- Nợ sau thương vụ = nợ cũ của Hạnh Phúc 2.000 + vay mới 6.500 = **8.500**.
- EBITDA kết hợp = 5.500 + 4.000 = **9.500** → $Nợ/EBITDA = 8.500/9.500 = 0{,}89\times$ (rất an toàn, thấp hơn ngưỡng 3-4×).
- Lãi vay kết hợp = 200 + 6.500 × 11% = **915**. EBIT kết hợp = 3.750 + 3.400 = 7.150 → Hệ số bảo vệ lãi vay (ICR) = 7.150 / 915 = **7,8×**.

**Stress test – EBITDA kết hợp sụt giảm (chưa tính synergies)**:

| EBITDA giảm | EBIT | ICR | Nợ/EBITDA |
|---------|------|-----|-----------|
| 0% | 7.150 | 7,8× | 0,89× |
| 20% | 5.250 | 5,7× | 1,12× |
| 30% | 4.300 | 4,7× | 1,28× |
| 40% | 3.350 | 3,7× | 1,49× |

Ngay cả khi EBITDA giảm 40%, ICR vẫn 3,7× > 3×. Nghĩa là rủi ro tài chính của cấu trúc nợ ở mức thấp – rủi ro thực sự của thương vụ **không nằm ở đòn bẩy mà ở synergies/giá** (Bước 4).

#### Bước 7: Goodwill và cơ cấu sở hữu

- Giá mua 20.500; vốn chủ sổ sách 9.000, thẩm định đánh giá lại tài sản (thương hiệu, thiết bị) tăng 1.500 → giá trị hợp lý tài sản ròng = 10.500.

$$Goodwill = 20.500 - 10.500 = 10.000 \;(\approx 48{,}8\%\text{ giá mua})$$

Gần một nửa giá mua nằm ở goodwill → thương vụ phụ thuộc rất lớn vào việc synergies và khách hàng thực sự được giữ lại; nếu thất bại sẽ phải ghi giảm lớn.

- Ở phương án A, chủ Hạnh Phúc nhận 250 nghìn cổ phần mới = 250/1.250 = **20%** vốn của Bánh Quê Xưa → cần thỏa thuận cổ đông (quyền biểu quyết, thoái vốn).

#### Kết luận và Khuyến nghị

1. **Không chấp nhận giá 22.000** (vượt walk-away 21.019).
2. **Đề nghị**: giá cơ sở **19.800** + earn-out tối đa 700 (tổng tối đa 20.500) gắn với 2 điều kiện: giữ ≥ 90% doanh thu 3 khách hàng lớn nhất và thợ bánh trưởng ở lại 24 tháng.
3. **Cấu trúc**: Phương án A (hỗn hợp) – cân bằng giữa EPS tăng, sử dụng tiền dư và giữ chủ cũ gắn bó thông qua 20% cổ phần. Không cần 100% nợ vì EPS tăng thêm không đổi lấy được giá trị thật.
4. **Hai bài học chính**: (i) *Giá trị nằm ở cost synergies, không ở EPS*. (ii) *Biên an toàn giữa giá trả và walk-away quyết định thương vụ có xứng đáng không*, không phải chuyện EPS có "đẹp" hay không.

---

## IV. ỨNG DỤNG CHO SME

### 1. M&A trong bối cảnh SME Việt Nam

SME Việt Nam gặp M&A ở **ba vị trí khác nhau**, mỗi vị trí cần mindset khác:

| Vai trò | Tình huống điển hình | Điều cần tập trung |
|--------|------------------|---------------|
| **Bên mua (Buyer)** | Mua lại đối thủ nhỏ, mua chuỗi cung ứng, mua cơ sở có sẵn thay vì tự xây | Walk-away price, synergies, thẩm định |
| **Bên bán (Seller)** | Chủ doanh nghiệp muốn nghỉ hưu, cần vốn, hoặc nhận đầu tư chiến lược | Chuẩn hóa sổ sách, làm "đẹp" báo cáo trước 12-24 tháng, đàm phán earn-out |
| **Nhà đầu tư thiểu số/nhận vốn** | Bán 10-30% cho quỹ đầu tư hoặc đối tác chiến lược | Định giá, quyền bảo vệ cổ đông thiểu số, lộ trình thoái vốn |

Ví dụ quy mô lớn tại Việt Nam để tham khảo xu hướng: các thương vụ như Masan tiếp quản VinCommerce (2019), Central Group mua Big C Việt Nam (2016), ThaiBev mua Sabeco (2017) cho thấy dòng vốn chiến lược nước ngoài/khu vực tìm kiếm quy mô thị trường nội địa, thường dùng cấu trúc mua cổ phần với vốn vay (số tiền chính xác cần tra cứu tin chính thống nếu trích dẫn).

### 2. Khác biệt định giá SME so với công ty niêm yết

| Yếu tố | Công ty niêm yết | SME Việt Nam |
|-------|-------------|-----------|
| Bội số EV/EBITDA điển hình | 8-12× (tùy ngành) | 3-6× (chiết khấu thanh khoản & quy mô) |
| Chất lượng báo cáo | Kiểm toán | Thường chưa chuẩn, có thể "hai sổ" |
| Phụ thuộc chủ sở hữu | Thấp | Rất cao – "key man risk" |
| Tập trung khách hàng | Thấp | Thường cao (1-3 khách hàng lớn) |
| Chiết khấu thiếu thanh khoản | Không | 20-30% (discount for lack of marketability) |

**Hệ quả**: Với SME, **thẩm định tài chính (Quality of Earnings)** quan trọng hơn mô hình định giá. EBITDA "trên giấy" thường cần điều chỉnh: chi phí cá nhân chủ qua công ty, lương quản lý dưới thị trường, doanh thu chưa xuất hóa đơn, công nợ khó đòi.

### 3. Pháp lý & thuế cần lưu ý khi M&A tại Việt Nam (tham khảo – cần xác nhận với luật sư/kế toán)

- **Hình thức**: Mua cổ phần/phần vốn góp (share deal) kế thừa mọi nghĩa vụ ẩn của công ty; Mua tài sản (asset deal) chọn lọc nhưng phức tạp thủ tục chuyển quyền và có thể phát sinh thuế/phí chuyển nhượng tài sản.
- **Kiểm soát tập trung kinh tế**: Luật Cạnh tranh 2018 yêu cầu thông báo/thẩm định khi thương vụ đạt các ngưỡng về thị phần, doanh thu, tổng tài sản hoặc giá trị giao dịch (một số ngưỡng được quy định chi tiết trong nghị định hướng dẫn) → SME nhỏ thường dưới ngưỡng nhưng cần kiểm tra nếu thị phần địa phương cao.
- **Thuế**: Thu nhập từ chuyển nhượng vốn/cổ phần chịu thuế (cá nhân và doanh nghiệp có cơ chế tính khác nhau) → cần mô hình hóa thuế bên bán, vì ảnh hưởng đến giá thực nhận.
- **Doanh nghiệp có yếu tố nước ngoài**: có thể cần thủ tục đầu tư/ngành nghề hạn chế.

### 4. Ba sai lầm đặc thù của SME khi làm M&A

1. **Mua vì "cơ hội giá rẻ" không có chiến lược** – tương tự "empire building" trên quy mô nhỏ.
2. **Không thẩm định khách hàng & nhân sự then chốt** – ở SME, giá trị gắn liền chủ cũ; chủ đi thì khách đi.
3. **Dùng hết tiền mặt và vay quá nhiều** – chủ quan về cash flow; tích hợp luôn tốn tiền hơn dự kiến (hệ số 1-1,5× synergies hàng năm).

---

## V. TOOLS & TEMPLATES

### 1. Công cụ & nguồn dữ liệu hỗ trợ

| Mục đích | Công cụ/Nguồn | Chi phí tham khảo |
|---------|-----------|----------------|
| Dữ liệu bội số ngành VN | Vietstock, CafeF, FiinPro (có phí), báo cáo công ty chứng khoán | Miễn phí – vài chục triệu đồng/năm (gói chuyên nghiệp) |
| Bội số & chi phí vốn quốc tế | Damodaran Online (NYU Stern) | Miễn phí |
| Tin giao dịch M&A | Báo cáo của các hãng tư vấn (Deloitte, PwC, KPMG, Grant Thornton VN), Vietnam M&A Forum | Miễn phí – tùy báo cáo |
| Phòng dữ liệu (Data room) | Google Drive/Dropbox có phân quyền (SME); Datasite/Intralinks (thương vụ lớn) | Miễn phí – hàng nghìn USD |
| Mô hình tài chính | Excel / Google Sheets | Miễn phí |
| Tư vấn thuế/pháp lý | Công ty luật, công ty kiểm toán | Tùy phạm vi (thương lượng) |

> Các mức phí chỉ mang tính tham khảo theo thông tin phổ biến, nên hỏi báo giá thực tế.

### 2. Cấu trúc workbook Excel để mô phỏng một thương vụ SME

| Sheet | Nội dung | Công thức/ô chính |
|-------|---------|-----------------|
| 1. Inputs | Số liệu Acquirer, Target, giả định (g, WACC, thuế) | Ô input màu xanh |
| 2. Stand-alone | Định giá Target: Comps, tiền lệ, DCF | `=FCF*(1+g)/(WACC-g)` |
| 3. Synergies | Bảng dòng tiền cost & revenue synergies theo năm, xác suất | `=NPV(r, ...)` |
| 4. Max Price | Walk-away = Stand-alone + NPV synergies | So với giá chào |
| 5. Financing | Các phương án tiền/vay/cổ phiếu | Số cổ phần mới = Giá cổ phiếu mới / Giá/CP |
| 6. EPS | Accretion/Dilution cho từng phương án Y1, Y3 | `=NI_pro_forma/Shares` |
| 7. Stress | Bảng độ nhạy synergies (0/50/100%) và EBITDA giảm | Data Table |
| 8. Goodwill | Giá mua − giá trị hợp lý tài sản ròng | Tỷ trọng goodwill |

### 3. Template: Thư bày tỏ quan tâm (IOI) – các mục cần có

```
1. Bên mua & bên bán; mục đích thương vụ
2. Khoảng giá chào (range) và cơ sở (EV/EBITDA, phương pháp)
3. Cấu trúc thanh toán (tiền/cổ phiếu/earn-out)
4. Nguồn tiền & bằng chứng khả năng thanh toán
5. Điều kiện chính: thẩm định, giữ chân nhân sự, độc quyền đàm phán (exclusivity)
6. Mốc thời gian dự kiến
7. Cam kết bảo mật (NDA)
```

---

## VI. BÀI TẬP THỰC HÀNH

### Bài 1 – Premium và giá trị tạo ra
Công ty X định mua Công ty Y có vốn hóa thị trường 500 tỷ đồng, chào mua với premium 30%. NPV synergies ước tính 120 tỷ. (a) Premium trả bao nhiêu tỷ? (b) Giá trị tạo ra/phá hủy cho cổ đông X là bao nhiêu? (c) Giá tối đa X nên trả là bao nhiêu (bỏ qua chi phí tích hợp)?

### Bài 2 – Accretion/Dilution (trả toàn bộ bằng cổ phiếu)
Acquirer: LNST 100 tỷ, 50 triệu cổ phần, P/E = 10 (giá = 20.000 đ/cổ phần). Target: LNST 30 tỷ, giá mua 400 tỷ, trả 100% bằng cổ phiếu acquirer. Tính EPS trước/sau, tăng hay giảm bao nhiêu %? Đối chiếu với Quick Test E/P.

### Bài 3 – LBO đơn giản
Quỹ mua doanh nghiệp EV = 80 tỷ (5× EBITDA 16 tỷ), vốn chủ quỹ góp 40 tỷ, nợ 40 tỷ. Sau 4 năm EBITDA = 22 tỷ, bội số 5×, nợ còn 20 tỷ. Tính vốn chủ thu về, MoM và IRR.

### Bài 4 – Walk-away price
Doanh nghiệp A cân nhắc mua B có giá trị stand-alone 200 tỷ. PV cost synergies (sau thuế) 40 tỷ; PV revenue synergies kỳ vọng 30 tỷ nhưng chỉ tin 50%; chi phí tích hợp 25 tỷ. Tính walk-away price. Nếu chủ B đòi 240 tỷ, bạn nên làm gì?

### Bài 5 – Phân tích tình huống (thảo luận)
Một chuỗi cà phê SME ở Đà Nẵng (doanh thu 30 tỷ) muốn mua lại một chuỗi 5 quán của đối thủ với lý do "mở rộng nhanh". Hãy liệt kê: (i) 3 synergies cụ thể có thể có và độ tin cậy từng loại; (ii) 5 hạng mục due diligence ưu tiên; (iii) rủi ro văn hóa/nhân sự.

### Đáp án gợi ý (đã kiểm tra tính toán)

- **Bài 1**: (a) 500 × 30% = 150 tỷ. (b) 120 − 150 = **−30 tỷ** (phá hủy giá trị). (c) Giá tối đa = 500 + 120 = 620 tỷ → premium tối đa = 120 tỷ (24%).
- **Bài 2**: Cổ phần mới = 400 tỷ / 20.000 = 20 triệu → tổng 70 triệu. EPS trước = 100 tỷ / 50 triệu = 2.000 đ. EPS sau = 130 tỷ / 70 triệu ≈ 1.857 đ → **giảm 7,1%** (dilutive). Quick Test: E/P target = 30/400 = 7,5% < E/P acquirer = 10% → khớp (dilutive).
- **Bài 3**: EV thoái vốn = 22 × 5 = 110; vốn chủ thu về = 110 − 20 = 90 → MoM = 90/40 = 2,25×; IRR = $2{,}25^{1/4} - 1 \approx 22{,}5\%$/năm.
- **Bài 4**: Walk-away = 200 + 40 + 30 × 50% − 25 = **230 tỷ**. Đòi 240 → vượt 10 tỷ → từ chối hoặc đề nghị giá cơ sở thấp hơn kèm earn-out gắn với kết quả.
- **Bài 5**: Gợi ý – cost synergies (gộp mua hạt, thuê mặt bằng, quản lý tập trung) tin cậy cao nhất; revenue synergies (thẻ thành viên chung) tin cậy thấp; due diligence ưu tiên: doanh thu từng quán, hợp đồng thuê mặt bằng, nhân sự then chốt, nhà cung cấp, thương hiệu/giấy phép.

---

## PHỤ LỤC: CHECKLIST M&A TỔNG HỢP

### Công thức tổng hợp

| Chỉ số | Công thức | Ý nghĩa |
|-------|-----------|---------|
| Enterprise Value | $EV = Vốn\,hóa + Nợ - Tiền\,mặt$ | Giá thật sự để sở hữu hoạt động kinh doanh |
| Equity Value | $Equity = EV - Nợ\,ròng$ | Giá trị phần của cổ đông |
| Bội số | $EV/EBITDA$ | So sánh định giá giữa các công ty |
| DCF (Gordon) | $EV = \dfrac{FCF(1+g)}{WACC - g}$ | Giá trị nội tại |
| Premium | $\dfrac{Giá\,chào - Giá\,TT}{Giá\,TT}$ | Mức thưởng cho cổ đông target |
| Synergies | $V_{AB} - V_A - V_B$ | Giá trị tạo thêm do kết hợp |
| Value created | $NPV_{syn} - Premium$ | Lãi/lỗ của acquirer |
| Walk-away price | $V_{standalone} + NPV_{syn} - Chi\,phí\,tích\,hợp$ | Giá tối đa không phá hủy giá trị |
| EPS pro forma | $\dfrac{NI_A + NI_B + Syn_{sau\,thuế} - Phí\,tài\,trợ_{sau\,thuế}}{Cổ\,phần\,A + Cổ\,phần\,mới}$ | Tác động lên lợi nhuận mỗi cổ phần |
| Quick Test | $E/P_{target} > Chi\,phí\,tài\,trợ\,sau\,thuế$ | Accretive nếu đúng |
| Goodwill | $Giá\,mua - FV\,tài\,sản\,ròng$ | Dấu vết kế toán của premium |
| LBO IRR | $\left(\dfrac{Vốn\,chủ\,thoái}{Vốn\,chủ\,đầu\,vào}\right)^{1/n} - 1$ | Lợi suất quỹ PE |
| ICR | $\dfrac{EBIT}{Lãi\,vay}$ | Khả năng trả lãi (mục tiêu >3×) |

### Checklist

```
TRƯỚC KHI MUA (PRE-DEAL):
□ Lý do chiến lược rõ ràng (không chỉ là "tăng trưởng")?
□ Khoảng giá trị định giá (DCF + Comps + Tiền lệ) đã lập?
□ Synergies đã xác định VÀ định lượng thận trọng (revenue chiết khấu ≥50%)?
□ Giá tối đa ("walk-away price") đã chốt trước đàm phán?
□ Nguồn vốn đã chắc chắn (tiền/nợ/cổ phiếu)?
□ Kế hoạch tích hợp đã phác thảo TRƯỚC khi ký?

THẨM ĐỊNH (DUE DILIGENCE):
□ Tài chính: chất lượng doanh thu, biên lợi nhuận, vốn lưu động, nợ ngoài bảng?
□ Pháp lý: rủi ro kiện tụng, vấn đề hợp đồng, sở hữu trí tuệ?
□ Thương mại: cạnh tranh, tập trung khách hàng?
□ Đánh giá văn hóa: tương thích hay xung đột?
□ Nhân tài then chốt đã xác định: có kế hoạch giữ chân?
□ Hệ thống IT: tương thích? Chi phí tích hợp?
□ Thuế & nợ ẩn: đã điều chỉnh giá hoặc cấu trúc earn-out?

THỰC HIỆN (EXECUTION):
□ Phân tích Accretion/Dilution dương? (và đã đối chiếu với NPV, không chỉ EPS)
□ Kịch bản stress (synergies 50%, chi phí tích hợp +50%) vẫn chấp nhận được?
□ Đường đi duyệt của cơ quan quản lý (cạnh tranh) rõ ràng?
□ Kỳ vọng ủng hộ của cổ đông?
□ Kế hoạch truyền thông (nhân viên, khách hàng) đã sẵn sàng?
□ Day 1 readiness đã lên kế hoạch?
□ Goodwill/tỷ trọng giá mua đã được đánh giá rủi ro ghi giảm?

SAU SÁP NHẬP (PMI):
□ Đã lập văn phòng tích hợp?
□ Kế hoạch 100 ngày có cột mốc?
□ Bảng theo dõi synergies hàng quý?
□ Giám sát nhân tài then chốt (thưởng giữ chân)?
□ Sáng kiến tích hợp văn hóa?
□ Đánh giá lại (post-audit) sau 1 năm và 3 năm?
□ Có "tiêu chí dừng" (kill criteria) nếu synergies không đạt?
```

---

*Tài liệu tham khảo: DePamphilis "Mergers, Acquisitions, and Other Restructuring Activities" 10th Ed; Rosenbaum & Pearl "Investment Banking" 3rd Ed; Bruner "Applied M&A"; McKinsey "Valuation" 7th Ed; CFA Level II – Corporate Issuers*
