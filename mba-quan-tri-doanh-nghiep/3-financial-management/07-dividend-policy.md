# Dividend Policy – Chính Sách Cổ Tức

> **Mục tiêu**: Hiểu bản chất bài toán "chia hay giữ lợi nhuận", các lý thuyết chính sách cổ tức (M&M Irrelevance, Bird-in-Hand, Tax Preference, Signaling, Clientele, Agency), các hình thức chi trả (tiền mặt, cổ phiếu, mua lại cổ phiếu), và biết cách thiết kế chính sách cổ tức phù hợp cho một SME Việt Nam dựa trên số liệu cụ thể (dòng tiền, cơ hội đầu tư, thuế, nhu cầu cổ đông).

---

## I. KHÁI NIỆM & LÝ THUYẾT

### 1. Định nghĩa và bài toán cốt lõi

**Chính sách cổ tức (Dividend Policy)** là bộ nguyên tắc quyết định **bao nhiêu lợi nhuận sau thuế được chia cho cổ đông** (cổ tức – dividends) và **bao nhiêu được giữ lại** (lợi nhuận giữ lại – retained earnings) để tái đầu tư vào doanh nghiệp. Đi kèm là các quyết định về **hình thức** (tiền mặt, cổ phiếu, mua lại cổ phiếu), **tần suất** (quý, nửa năm, năm) và **tính ổn định** (cố định hay thả nổi theo lợi nhuận).

> **Câu hỏi cốt lõi**: Mỗi đồng lợi nhuận, doanh nghiệp (DN) nên *trả cho cổ đông* hay *giữ lại tự đầu tư*? Và việc chia/giữ có làm thay đổi giá trị DN hay không?

$$\text{Lợi nhuận sau thuế (Net Income)} = \text{Cổ tức chi trả (Dividends)} + \text{Lợi nhuận giữ lại (Retained Earnings)}$$

#### Tại sao đây là một bài toán thực sự?

Về bản chất, lợi nhuận sau thuế **thuộc về cổ đông** (họ là chủ sở hữu phần còn lại sau khi trả hết chủ nợ, nhà cung cấp, nhân viên, Nhà nước). Vì vậy câu hỏi không phải là "lợi nhuận của ai", mà là: **ai sẽ tái đầu tư số tiền đó hiệu quả hơn – ban quản lý DN hay chính cổ đông?**

- Nếu DN có thể đầu tư số tiền giữ lại với suất sinh lời **cao hơn** mức cổ đông tự kiếm được ở nơi khác với mức rủi ro tương đương (tức dự án có NPV > 0) → nên **giữ lại**.
- Nếu DN không còn cơ hội đầu tư tốt → giữ tiền mặt nhàn rỗi là **lãng phí** (tiền nằm im, bị ban quản lý tiêu vào các dự án "xây đế chế") → nên **trả lại** cho cổ đông.

Do đó, chính sách cổ tức thực chất là **quyết định phân bổ vốn (capital allocation)** chứ không chỉ là "thủ tục chia tiền" cuối năm.

#### Các công thức nền tảng

**Tỷ lệ chi trả cổ tức (Payout Ratio)** – đo phần trăm lợi nhuận được chia:

$$\text{Payout Ratio} = \frac{\text{Cổ tức (Dividends)}}{\text{Lợi nhuận sau thuế (Net Income)}} = \frac{\text{DPS}}{\text{EPS}}$$

**Tỷ lệ giữ lại (Retention Ratio, ký hiệu $b$)** – phần lợi nhuận ở lại DN:

$$b = 1 - \text{Payout Ratio} = \frac{\text{Lợi nhuận giữ lại}}{\text{Lợi nhuận sau thuế}}$$

Trong đó DPS (Dividends Per Share) là cổ tức trên mỗi cổ phần, EPS (Earnings Per Share) là lợi nhuận trên mỗi cổ phần.

### 2. Bối cảnh lịch sử: Vì sao cổ tức là một "câu đố" của giới tài chính?

Tài chính doanh nghiệp có nhiều quyết định mà lý thuyết cho đáp án khá rõ (chọn dự án theo NPV, chọn cơ cấu vốn theo WACC...). Riêng cổ tức thì không. Nhà kinh tế **Fischer Black** (đồng tác giả công thức Black–Scholes) năm **1976** gọi đó là **"Dividend Puzzle" (câu đố cổ tức)**: *"Càng nhìn vào bức tranh cổ tức, ta càng thấy nó như một câu đố, với những mảnh ghép không khớp nhau."* Lý do: DN trả cổ tức dù cổ tức bị đánh thuế nặng hơn lãi vốn ở nhiều nước, nhưng cùng lúc cổ phiếu có cổ tức vẫn được ưa chuộng.

Dòng thời gian các mốc lý thuyết quan trọng:

| Năm | Người/Công trình | Đóng góp |
|-----|------------------|----------|
| 1956 | **John Lintner** – khảo sát 28 công ty Mỹ | Phát hiện các nhà quản lý *làm mượt* (smoothing) cổ tức, rất ngại cắt giảm → mô hình Partial Adjustment |
| 1956–1963 | **Myron Gordon, John Lintner** | Lập luận "Bird-in-Hand": nhà đầu tư thích cổ tức chắc chắn hơn lãi vốn bấp bênh |
| 1961 | **Merton Miller & Franco Modigliani** | Chứng minh trong thị trường hoàn hảo, cổ tức **không ảnh hưởng** giá trị DN (cùng logic với M&M 1958 về cơ cấu vốn) |
| 1974 | **Black & Scholes** | Kiểm định thực nghiệm: không tìm thấy bằng chứng chắc chắn rằng cổ tức cao làm giá cổ phiếu cao hơn |
| 1979–1985 | **Bhattacharya; Miller & Rock** | Mô hình **Signaling**: cổ tức là tín hiệu về triển vọng lợi nhuận khi thông tin bất cân xứng |
| 1980 | **Litzenberger & Ramaswamy** | Bằng chứng về **Tax Preference**: cổ phiếu có cổ tức cao đòi hỏi lợi suất cao hơn bù thuế |
| 1984–1986 | **Easterbrook; Jensen** | **Agency / Free Cash Flow**: cổ tức giúp "rút" tiền dư khỏi tay ban quản lý |

> **Ý nghĩa thực hành**: Không có một lý thuyết nào "thắng" tuyệt đối. Mỗi lý thuyết đúng trong một hoàn cảnh nhất định (thuế, thông tin, cổ đông, chu kỳ DN). Nhiệm vụ của chủ DN/CFO là biết **lý thuyết nào đang chi phối công ty mình**.

### 3. Cơ chế thực tế: Các hình thức chi trả và các mốc ngày quan trọng

#### 3.1. Các hình thức chi trả cổ tức

| Hình thức | Mô tả | Ví dụ |
|-----------|--------|-------|
| **Cổ tức tiền mặt (Cash Dividend)** | Chuyển tiền/tiền mặt cho cổ đông | 2.000đ/cổ phiếu |
| **Cổ tức bằng cổ phiếu (Stock Dividend)** | Phát hành thêm cổ phiếu cho cổ đông hiện hữu theo tỷ lệ | 10% → sở hữu 10 CP được thêm 1 CP |
| **Mua lại cổ phiếu (Share Buyback)** | DN dùng tiền mua cổ phiếu của chính mình | Apple mua lại hàng chục tỷ USD mỗi năm |
| **Cổ tức đặc biệt (Special Dividend)** | Khoản chia một lần từ tiền dư bất thường | Costco từng chia special dividend 15 USD/CP |
| **Cổ tức bằng tài sản (Property Dividend)** | Chia bằng tài sản/cổ phần công ty con (hiếm) | Spin-off: chia cổ phiếu công ty con |

#### 3.2. Dòng thời gian chi trả cổ tức (Dividend Timeline)

```
 Ngày công bố        Ngày giao dịch         Ngày đăng ký           Ngày thanh toán
 (Declaration)       KHÔNG hưởng quyền      cuối cùng              (Payment Date)
                     (Ex-dividend Date)     (Record Date)
      │                     │                    │                       │
──────●─────────────────────●────────────────────●───────────────────────●────────►
 HĐQT/ĐHĐCĐ ra        Mua từ ngày này          Danh sách cổ đông       Tiền/cổ phiếu
 nghị quyết           KHÔNG được nhận          được chốt               về tài khoản
                      cổ tức
```

- Ai **sở hữu cổ phiếu trước ngày giao dịch không hưởng quyền** thì được nhận cổ tức. Từ ngày này, giá tham chiếu (reference price) được điều chỉnh giảm đúng bằng cổ tức, vì người mua mới không còn được hưởng khoản đó.
- Ví dụ: cổ phiếu đóng cửa 30.000đ trước ngày không hưởng quyền, cổ tức tiền mặt 2.000đ/CP → giá tham chiếu ngày không hưởng quyền = 30.000 − 2.000 = **28.000đ**. Giá giảm không phải là "thua lỗ" mà là tiền đã chuyển từ tài sản DN sang túi cổ đông (xem giải thích M&M ở mục II.B).
- Với công ty cổ phần chưa niêm yết/SME, quy trình tương tự nhưng thực hiện qua nghị quyết ĐHĐCĐ và danh sách cổ đông của chính công ty.

### 4. Tổng quan các lý thuyết chính

```
┌────────────────────────────────────────────────────────────────┐
│                CÁC LÝ THUYẾT CỔ TỨC                           │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  1. M&M DIVIDEND IRRELEVANCE (1961)                           │
│     → Chính sách cổ tức KHÔNG ảnh hưởng giá trị DN            │
│     → "Homemade dividends" – nhà đầu tư tự tạo                │
│                                                                │
│  2. BIRD-IN-HAND (Gordon & Lintner)                           │
│     → Nhà đầu tư thích cổ tức (chắc chắn) hơn lãi vốn         │
│     → Cổ tức cao → Ke thấp → Giá cổ phiếu cao                 │
│                                                                │
│  3. TAX PREFERENCE (Litzenberger & Ramaswamy)                 │
│     → Cổ tức bị đánh thuế nặng hơn lãi vốn                    │
│     → Nhà đầu tư thích cổ tức THẤP → hiệu quả thuế            │
│                                                                │
│  4. SIGNALING / INFORMATION CONTENT                            │
│     → Tăng cổ tức = tín hiệu tích cực (quản lý TỰ TIN)        │
│     → Cắt cổ tức = tín hiệu RẤT tiêu cực                      │
│                                                                │
│  5. AGENCY THEORY / FREE CASH FLOW                             │
│     → Cổ tức làm giảm FCF dư → giảm chi phí đại diện          │
│     → Buộc ban quản lý có kỷ luật                              │
│                                                                │
│  6. CLIENTELE EFFECT                                           │
│     → Mỗi nhóm nhà đầu tư thích một chính sách khác nhau      │
│     → Người hưu trí: cổ tức cao. Nhà đầu tư tăng trưởng: thấp │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

## II. CHI TIẾT TỪNG THÀNH PHẦN

### A. Các chỉ số đo lường cổ tức cơ bản

#### Tại sao cần nhiều chỉ số, không chỉ một con số "cổ tức bao nhiêu đồng"?

Con số cổ tức tuyệt đối (ví dụ 2.000đ/CP) tự nó không nói lên điều gì: 2.000đ trên cổ phiếu giá 20.000đ là rất hào phóng, còn 2.000đ trên cổ phiếu giá 200.000đ thì rất ít. Tương tự, 2.000đ/CP có *bền vững* hay không còn phụ thuộc DN kiếm được bao nhiêu và có đủ tiền mặt để trả không. Vì vậy phải đặt cổ tức **trong tương quan** với giá (yield), với lợi nhuận (payout) và với dòng tiền (coverage).

| Chỉ số | Công thức | Trả lời câu hỏi |
|--------|-----------|-----------------|
| **Tỷ suất cổ tức (Dividend Yield)** | $\dfrac{DPS}{P_0}$ | "Giá bỏ ra mua cổ phiếu, mỗi năm nhận về bao nhiêu % bằng cổ tức?" |
| **Tỷ lệ chi trả (Payout Ratio)** | $\dfrac{DPS}{EPS}$ | "Bao nhiêu % lợi nhuận được chia?" |
| **Tỷ lệ chi trả theo dòng tiền** | $\dfrac{Dividends}{FCF}$ | "Cổ tức có được trả bằng tiền thật hay chỉ bằng lợi nhuận kế toán?" |
| **Hệ số bao phủ cổ tức bằng FCF** | $\dfrac{FCF}{Dividends}$ | "Dòng tiền gấp mấy lần cổ tức? (>1,5 lần là an toàn)" |
| **Tỷ suất mua lại (Buyback Yield)** | $\dfrac{Buybacks}{Market\ Cap}$ | "Ngoài cổ tức, DN trả lại bao nhiêu % qua mua lại cổ phiếu?" |
| **Tổng tỷ suất cho cổ đông (Total Shareholder Yield)** | Dividend Yield + Buyback Yield | "Tổng cộng DN trả lại bao nhiêu % vốn hóa mỗi năm?" |

**Vì sao phải nhìn FCF, không chỉ lợi nhuận?** Lợi nhuận là con số kế toán, có thể bao gồm khoản phải thu chưa thu được hoặc khấu hao không phải tiền mặt; còn cổ tức phải trả bằng *tiền thật*. GE (Case Study III.2) là ví dụ điển hình: trả cổ tức từ "lợi nhuận" bị thổi phồng trong khi dòng tiền thực không đủ.

**Ví dụ minh họa nhanh**: Cổ phiếu giá 40.000đ, DPS = 2.000đ, EPS = 4.000đ.
- Dividend Yield = 2.000 / 40.000 = **5,0%**
- Payout Ratio = 2.000 / 4.000 = **50%** → Retention $b$ = 50%
- Nếu mua lại cổ phiếu tương đương thêm 2,5% vốn hóa → Total Shareholder Yield = 5,0% + 2,5% = **7,5%**

### B. M&M Dividend Irrelevance Theorem (1961)

#### Phát biểu

Trong **thị trường hoàn hảo** (không thuế, không chi phí giao dịch, thông tin đối xứng):

> **Giá trị DN chỉ phụ thuộc vào khả năng sinh lời của tài sản và rủi ro kinh doanh, KHÔNG phụ thuộc vào chính sách cổ tức.**

#### Tại sao kết luận này lại "đúng" về mặt logic? – Trực giác "cái bánh pizza" và "homemade dividends"

Hãy tưởng tượng giá trị DN là một cái bánh pizza; cổ tức chỉ là việc *cắt bánh ra thành miếng ở bên trong DN hay bên ngoài DN*. Cái bánh vẫn to như cũ. Cụ thể:

- Khi DN trả cổ tức 3.000đ/CP, **tài sản DN giảm đúng 3.000đ/CP** → giá cổ phiếu giảm đúng 3.000đ (ex-dividend). Cổ đông chỉ chuyển tiền từ "túi bên trái" (cổ phiếu) sang "túi bên phải" (tiền mặt). Của cải không đổi.
- Nếu cổ đông muốn **nhiều tiền hơn** mức DN chia → tự bán bớt cổ phiếu để tạo ra "cổ tức tự chế" (**homemade dividends**).
- Nếu cổ đông muốn **ít tiền hơn** → dùng cổ tức nhận được để mua thêm cổ phiếu (tái đầu tư).
- Hệ quả: dù DN chia nhiều hay ít, nhà đầu tư luôn tự tạo được dòng tiền mình muốn → **chính sách cổ tức không tạo thêm giá trị**.

#### Ví dụ số: "Homemade dividend" từng bước

Công ty có giá trị vốn chủ 20.000 triệu đồng, 1.000.000 cổ phần → giá 20.000đ/CP. Nhà đầu tư N sở hữu 100 CP (giá trị 2.000.000đ).

| Bước | Chính sách X: DN chia 3.000đ/CP | Chính sách Y: DN không chia |
|------|-------------------------------|---------------------------|
| Giá trị cổ phiếu sau chính sách | 17.000đ (20.000 − 3.000) | 20.000đ |
| Nhà đầu tư N nhận cổ tức | 100 × 3.000 = **300.000đ** | 0đ |
| Giá trị 100 CP còn lại | 100 × 17.000 = 1.700.000đ | 100 × 20.000 = 2.000.000đ |
| **Tổng tài sản của N** | 300.000 + 1.700.000 = **2.000.000đ** | **2.000.000đ** |

- Nếu N thích có 300.000đ tiền mặt dưới chính sách Y: N bán 300.000 / 20.000 = **15 CP** → có tiền mặt 300.000đ, còn 85 CP × 20.000 = 1.700.000đ. Kết quả **giống hệt** chính sách X.
- Nếu N không cần tiền dưới chính sách X: N dùng 300.000đ mua thêm 300.000 / 17.000 ≈ **17,6 CP** → trạng thái gần giống hệt chính sách Y.

→ Cả hai chính sách cho cùng kết quả → cổ tức là **không liên quan (irrelevant)**.

#### Các giả định (Assumptions) – rất quan trọng!

1. Không có thuế (hoặc thuế cổ tức = thuế lãi vốn)
2. Không có chi phí giao dịch (bán cổ phiếu miễn phí, mua cổ phiếu miễn phí)
3. Thông tin đối xứng (cổ đông biết rõ như ban quản lý)
4. Nhà đầu tư lý trí
5. Không có chi phí đại diện (agency costs)
6. Chính sách đầu tư của DN cố định (không bị ảnh hưởng bởi cách chia)

→ **Trong thực tế**: Mọi giả định đều bị vi phạm ở các mức độ khác nhau → **cổ tức CÓ ảnh hưởng**. Giá trị của M&M không nằm ở chỗ nó "đúng", mà ở chỗ nó **chỉ ra chính xác các "ma sát" nào khiến cổ tức quan trọng**: thuế (Tax Preference), thông tin (Signaling), chi phí giao dịch/thanh khoản (Clientele, Bird-in-Hand), chi phí đại diện (Agency). Mỗi lý thuyết dưới đây chính là việc gỡ bỏ một giả định.

> **Với SME Việt Nam**: giả định số 2 (chi phí giao dịch bằng 0) bị vi phạm nặng nhất. Cổ phần công ty chưa niêm yết rất khó bán lẻ, buộc phải bán với giá chiết khấu → "homemade dividend" không thực tế → cổ tức tiền mặt thật sự quan trọng với cổ đông nhỏ (xem Case SME III.3).

### C. Bird-in-Hand Theory (Gordon & Lintner)

#### Ý tưởng

$$K_e = \frac{D_1}{P_0} + g$$

- $K_e$: chi phí vốn chủ sở hữu (suất sinh lời kỳ vọng của cổ đông)
- $D_1/P_0$: tỷ suất cổ tức kỳ vọng năm tới; $g$: tốc độ tăng trưởng kỳ vọng (phần lãi vốn)

Gordon (1959) và Lintner (1962) cho rằng nhà đầu tư coi **cổ tức là chắc chắn hơn lãi vốn** ("một con chim trong tay bằng hai con trên cây"). Lập luận: phần lãi vốn $g$ phụ thuộc tương lai xa và bấp bênh hơn cổ tức nhận ngay → nhà đầu tư gán rủi ro cao hơn cho $g$ → DN chia nhiều cổ tức hơn thì $K_e$ **thấp hơn** → giá cổ phiếu cao hơn.

#### Phản biện của M&M và thực nghiệm

M&M gọi đây là **"bird-in-hand fallacy" (ngụy biện)**: rủi ro của cổ đông nằm ở *dòng tiền hoạt động của DN*, không phụ thuộc cách chia dòng tiền đó thành cổ tức hay lãi vốn. Một đồng cổ tức và một đồng lãi vốn đều đến từ cùng một DN rủi ro như nhau. Hơn nữa, nếu DN chia thêm cổ tức, DN phải huy động thêm vốn mới (hoặc bỏ dự án) để bù – rủi ro của phần còn lại không giảm.

Thực nghiệm (Black & Scholes 1974) không tìm được bằng chứng rõ rệt rằng cổ tức cao làm giá cao hơn. Tuy vậy, trong thực tế vẫn có nhà đầu tư *thật sự cần* dòng tiền đều đặn (hưu trí, quỹ) → hiện tượng này được giải thích tốt hơn bằng **Clientele Effect** và **thanh khoản** (mục II.F).

### D. Tax Preference Theory

#### Tại sao thuế làm thay đổi kết luận của M&M?

Khi gỡ giả định "không thuế", cổ tức và lãi vốn không còn là hai cách tương đương. Cổ đông cá nhân thường phải nộp thuế **ngay** khi nhận cổ tức, còn lãi vốn chỉ bị đánh thuế khi **thực sự bán** cổ phiếu (có thể hoãn nhiều năm). Với cùng 1 đồng thu nhập, ai tìm được cách hoãn/giảm thuế sẽ giàu hơn.

| | Cổ tức tiền mặt | Lãi vốn (Capital Gains) |
|-|---------------|---------------|
| Thời điểm đánh thuế | Khi nhận | Khi **thực hiện** (bán) |
| Thuế suất (Mỹ) | Tới 20% + 3,8% NIIT | 0% / 15% / 20% (dài hạn) |
| Hoãn thuế | Không | Có (giữ càng lâu càng hoãn) |
| Step-up khi thừa kế | Không | Có (Mỹ: nhận theo giá thị trường) |
| **Việt Nam (cá nhân)** | **5%** thuế TNCN trên cổ tức | **0,1%** trên giá trị chuyển nhượng (cổ phiếu CTCP) |
| **Việt Nam (pháp nhân nhận cổ tức)** | Thường được miễn thuế TNDN với cổ tức nhận từ công ty đã nộp thuế | Tính vào thu nhập khác, chịu thuế TNDN |

> **Lưu ý**: Mức thuế VN nêu trên là kiến thức tổng quát tại thời điểm biên soạn; chủ DN nên xác nhận lại với kế toán thuế vì quy định và hướng dẫn thay đổi theo thời gian (đặc biệt phân biệt chuyển nhượng *cổ phần CTCP* và *phần vốn góp công ty TNHH*, loại thứ hai bị đánh thuế 20% trên phần chênh lệch).

#### Ví dụ định lượng: Cổ đông cần 100 triệu tiền mặt – lấy từ cổ tức hay từ bán cổ phiếu?

| Cách lấy tiền | Công thức tìm số tiền gộp (gross) cần có | Kết quả |
|---------------|------------------------------------------|---------|
| Nhận cổ tức (thuế 5%) | $100 / (1 - 0{,}05)$ | cần cổ tức gộp **105,26 triệu** (nộp 5,26 triệu) |
| Bán cổ phiếu (thuế 0,1% giá bán) | $100 / (1 - 0{,}001)$ | cần bán **100,10 triệu** (nộp 0,10 triệu) |

→ Chênh lệch thuế gần **50 lần** (5,26 vs 0,10 triệu) → nếu thị trường thanh khoản tốt, nhà đầu tư cá nhân VN có động cơ thuế thích *mua lại cổ phiếu/lãi vốn* hơn cổ tức. Nhưng kết luận này chỉ đúng khi **dễ bán cổ phiếu**; với SME chưa niêm yết, chi phí tìm người mua và chiết khấu thanh khoản lớn hơn nhiều khoản tiết kiệm thuế (xem Case III.3).

→ Ở đa số quốc gia: lãi vốn bị đánh thuế nhẹ hơn → nhà đầu tư ưa **mua lại cổ phiếu/giữ lại lợi nhuận** hơn cổ tức.

### E. Signaling Theory và Mô hình Lintner

#### Tại sao cổ tức mang tín hiệu thông tin?

M&M giả định ban quản lý và cổ đông biết thông tin như nhau. Thực tế, **ban quản lý biết rõ triển vọng hơn** (đơn hàng sắp ký, dòng tiền quý tới...). Vì cổ tức là **tiền thật rời khỏi DN** và rất khó cắt giảm sau đó (xem Lintner), chỉ những DN tự tin về dòng tiền tương lai mới dám cam kết cổ tức cao hơn. Do đó thị trường đọc cổ tức như một "lời nói có giá" – khó giả mạo vì giả mạo sẽ phải trả giá khi bị buộc cắt.

#### Phản ứng của thị trường (mức tham khảo từ nghiên cứu thực nghiệm)

| Sự kiện | Phản ứng thị trường | Thông điệp thị trường đọc được |
|---------|--------------------|--------------------|
| Bắt đầu chia cổ tức (**Initiation**) | Giá ↑ khoảng 1–3% | "Ban quản lý tự tin dòng tiền bền vững" |
| Tăng cổ tức (**Increase**) | Giá ↑ khoảng 1–2% | "Lợi nhuận sẽ tiếp tục tăng" |
| Giữ nguyên (**Maintain**) | Trung tính | Như kỳ vọng |
| Cắt giảm (**Cut**) | Giá ↓ khoảng 5–10% hoặc hơn | "Ban quản lý đang bế tắc!" |
| Ngừng hẳn (**Omission**) | Giá ↓ khoảng 10–25% hoặc hơn | "DN gặp khó khăn nghiêm trọng" |

*(Các con số mang tính khoảng tham khảo tổng hợp từ nghiên cứu dạng Asquith & Mullins 1983, Healy & Palepu 1988; mức chính xác thay đổi theo thị trường và thời kỳ.)*

Sự bất đối xứng (tăng chỉ +1–2% nhưng cắt tới −5–10%+) giải thích vì sao quản lý rất ngại cắt – dẫn tới mô hình Lintner dưới đây.

#### Mô hình Lintner (1956) – Partial Adjustment

Lintner phỏng vấn các CFO và phát hiện: họ có một **tỷ lệ chi trả mục tiêu** (target payout) nhưng **không bao giờ nhảy thẳng tới đó**, mà điều chỉnh từ từ:

$$\Delta D_t = D_t - D_{t-1} = c \times (\text{Target } D_t - D_{t-1}) + \varepsilon, \qquad \text{Target } D_t = \text{Target Payout} \times EPS_t$$

- $c$ là tốc độ điều chỉnh (speed of adjustment), thường khoảng 0,3–0,5
- Quản lý **làm mượt (smooth)** cổ tức: tăng chậm khi lợi nhuận tăng, và cực kỳ ngại giảm

**Ví dụ từng bước**: Tỷ lệ chi trả mục tiêu 50%, $c$ = 0,4, cổ tức năm trước $D_{t-1}$ = 1.200đ/CP.

| Năm | EPS | Cổ tức mục tiêu = 50% × EPS | Điều chỉnh $\Delta D = 0{,}4 \times (\text{Mục tiêu} - D_{t-1})$ | Cổ tức thực chi $D_t$ | Payout thực |
|-----|-----|-----------------------------|----------|---------------|-------------|
| 1 | 4.000 | 2.000 | 0,4 × (2.000 − 1.200) = +320 | **1.520** | 38,0% |
| 2 | 5.000 | 2.500 | 0,4 × (2.500 − 1.520) = +392 | **1.912** | 38,2% |
| 3 (EPS rơi) | 2.800 | 1.400 | 0,4 × (1.400 − 1.912) = −205 | **1.707** | 61,0% |

→ Dù EPS giảm gần 44% (5.000 → 2.800), cổ tức chỉ giảm khoảng 11% và payout thực nhảy lên 61% – đúng bản chất "cổ tức dính (sticky)": DN chấp nhận payout cao hơn mục tiêu tạm thời để tránh tín hiệu xấu.

### F. Clientele Effect và Agency Theory (Free Cash Flow)

#### F.1. Clientele Effect – "Mỗi nhóm cổ đông một khẩu vị"

Các nhóm nhà đầu tư khác nhau có nhu cầu và mức thuế khác nhau, nên tự sàng lọc vào các cổ phiếu có chính sách phù hợp:

| Nhóm nhà đầu tư | Ưa thích | Lý do |
|-----------------|----------|-------|
| Người hưu trí, quỹ hưu trí | Cổ tức cao, đều | Cần dòng tiền chi tiêu; tránh phí giao dịch khi bán cổ phiếu |
| Nhà đầu tư trẻ, thu nhập cao | Cổ tức thấp/mua lại | Nhiều thuế; muốn lãi vốn hoãn thuế |
| Quỹ/pháp nhân được miễn thuế cổ tức | Cổ tức | Không bị thuế → cổ tức "rẻ" |
| Quỹ chỉ đầu tư tăng trưởng | Giữ lại tái đầu tư | Mandate đầu tư tăng trưởng |

**Hệ quả**: Khi DN đổi chính sách đột ngột (ví dụ cắt cổ tức), nhóm khách hàng cũ bán ra, nhóm mới chưa kịp vào → giá giảm do **chi phí chuyển đổi cổ đông**. Đây là một trong những lý do vì sao DN nên *ổn định* chính sách (cũng chính là điều xảy ra với GE).

#### F.2. Agency Theory và Free Cash Flow (Jensen 1986)

**Vấn đề**: Ban quản lý không sở hữu 100% DN nên không chịu hết hậu quả của quyết định sai. Nếu DN có nhiều tiền nhàn rỗi (Free Cash Flow – FCF), họ có xu hướng dùng tiền đó để "xây đế chế": mua lại DN khác với giá cao, mở rộng quá mức, chi tiêu xa xỉ – tức là đầu tư vào dự án có **NPV < 0**.

**Giải pháp**: Chi cổ tức (hoặc mua lại cổ phiếu) **rút bớt tiền dư** khỏi tay ban quản lý → họ phải quay lại thị trường vốn mỗi khi cần tiền, nơi họ bị thị trường giám sát. Đây là lý do chia cổ tức làm *giảm chi phí đại diện*, cùng cơ chế "kỷ luật" như nợ vay trong lý thuyết cơ cấu vốn.

### G. Mua lại cổ phiếu (Share Buyback) so với Cổ tức tiền mặt

#### Tại sao Buyback ngày càng phổ biến?

Kể từ thập niên 1980, DN Mỹ chuyển dần từ cổ tức sang mua lại cổ phiếu vì: (1) **thuế** – cổ đông chọn bán hay giữ nên kiểm soát thời điểm chịu thuế; (2) **linh hoạt** – không có tín hiệu "cam kết" như cổ tức, có thể dừng bất cứ lúc nào mà không bị phạt về tín hiệu; (3) **tín hiệu** – "cổ phiếu đang bị định giá thấp".

| Tiêu chí | Cổ tức tiền mặt | Mua lại cổ phiếu |
|----------|-----------------|-------------------|
| **Thuế** | Nộp ngay | Hoãn (chịu thuế lãi vốn khi bán) |
| **Linh hoạt** | Cam kết đều đặn (dính) | Tùy chọn, có thể làm một lần |
| **Tín hiệu** | "Tự tin về lợi nhuận" | "Cổ phiếu bị định giá thấp" hoặc có tiền dư |
| **Tác động EPS** | Trung tính | EPS tăng (ít cổ phiếu hơn) |
| **Ai hưởng lợi** | Mọi cổ đông như nhau | Cổ đông còn lại (tỷ lệ sở hữu tăng) |
| **Xu hướng 1990–2024** | Giảm tương đối | Tăng mạnh (ở Mỹ đã vượt cổ tức) |

*Số liệu S&P 500 năm 2023 (tham khảo, mang tính ước lượng làm tròn từ nguồn S&P Dow Jones Indices): mua lại cổ phiếu khoảng 795 tỷ USD, cổ tức khoảng 588 tỷ USD; tổng khoảng 1.383 tỷ USD (≈ 90% lợi nhuận). Cần kiểm chứng lại với nguồn gốc khi dùng cho báo cáo chính thức.*

#### Ngụy biện "Buyback làm EPS tăng nên giá tăng" – Ví dụ số từng bước

DN có lợi nhuận sau thuế 3.000 triệu, 1.000.000 CP (EPS 3.000đ), giá thị trường 20.000đ (P/E = 6,67), vốn hóa 20.000 triệu. DN dùng 1.000 triệu để mua lại 5% cổ phiếu.

| Bước | Tính toán | Kết quả |
|------|-----------|---------|
| Số CP mua lại | 1.000 triệu / 20.000đ | 50.000 CP |
| CP còn lưu hành | 1.000.000 − 50.000 | 950.000 CP |
| **EPS mới** | 3.000 triệu / 950.000 | **3.157,9đ** (tăng 5,3%) |
| Vốn hóa sau mua lại | 20.000 − 1.000 (tiền đã rời DN) | 19.000 triệu |
| **Giá mới mỗi CP** | 19.000 triệu / 950.000 | **20.000đ (không đổi!)** |
| P/E mới | 20.000 / 3.157,9 | 6,33 (giảm từ 6,67) |

→ EPS tăng nhưng **giá cổ phiếu không đổi**, vì DN cũng mất đi đúng số tiền đã dùng mua lại. Mua lại chỉ *tạo ra giá trị* khi mua dưới giá trị nội tại, hoặc khi nó giúp tránh bị lãng phí tiền dư. Cổ đông không bán vẫn có tỷ lệ sở hữu tăng lên, còn cổ đông bán thì nhận tiền mặt – một cách chia "tùy chọn" mà cổ tức không có.

### H. Tốc độ tăng trưởng bền vững (Sustainable Growth Rate)

#### Tại sao $g = ROE \times b$? – Chứng minh trực giác

Hãy giả định DN không phát hành thêm vốn chủ và ROE không đổi. Mỗi năm, phần lợi nhuận giữ lại ($b \times NI$) được cộng vào vốn chủ sở hữu → vốn chủ tăng một tỷ lệ $\dfrac{b \times NI}{E} = b \times ROE$ → vì lợi nhuận năm sau = ROE × vốn chủ sau, nên lợi nhuận cũng tăng đúng tỷ lệ đó:

$$g = ROE \times b = ROE \times (1 - \text{Payout})$$

*Ví dụ số*: Vốn chủ 5.000, lợi nhuận 1.000 (ROE 20%), giữ lại $b$ = 60% → giữ 600 → vốn chủ 5.600 → lợi nhuận năm sau = 20% × 5.600 = **1.120** → tăng **12%** = 20% × 0,6 ✔.

| Payout Ratio | Retention $b$ | ROE | Tăng trưởng bền vững $g$ |
|--------------|--------------|-----|--------------|
| 30% | 70% | 20% | **14%** |
| 50% | 50% | 20% | **10%** |
| 80% | 20% | 20% | **4%** |
| 100% | 0% | 20% | **0%** (không tăng trưởng!) |

→ **Trade-off cốt lõi**: Chia nhiều cổ tức ⇒ giữ lại ít ⇒ tăng trưởng nội sinh thấp. Muốn tăng trưởng nhanh hơn $g$ mà không giảm cổ tức, phải **vay thêm hoặc phát hành thêm vốn**.

**Lưu ý hạn chế**: $g = ROE \times b$ dùng ROE *bình quân* của DN, nhưng dự án mới có thể có ROIC khác ROE hiện tại. Công thức cũng giả định không đổi đòn bẩy; khi vay thêm, tăng trưởng thực có thể cao hơn $g$.

**Mô hình Gordon (định giá cổ phiếu)**: $P_0 = \dfrac{D_1}{K_e - g}$ — chỉ hợp lệ khi $g < K_e$ vĩnh viễn. Nếu $g$ tính được bằng $ROE \times b$ lớn hơn $K_e$ (như DN tăng trưởng nhanh), đó chỉ là giai đoạn tạm thời, không thể dùng Gordon cho cả đời DN.

### I. Các mô hình chính sách cổ tức trong thực tế

| Mô hình | Nguyên tắc | Ưu điểm | Nhược điểm | Phù hợp với |
|---------|------------|---------|-----------|-------------|
| **Cổ tức ổn định (Stable Dividend)** | Trả DPS cố định/tăng nhẹ theo thời gian | Tín hiệu tốt, nhà đầu tư dễ lập kế hoạch | Cứng nhắc khi lợi nhuận giảm mạnh | DN trưởng thành, dòng tiền ổn định |
| **Tỷ lệ chi trả cố định (Constant Payout)** | Luôn chia X% lợi nhuận | Minh bạch, tự điều chỉnh theo lợi nhuận | Cổ tức dao động mạnh theo chu kỳ | DN ngành chu kỳ, cổ đông chấp nhận biến động |
| **Cổ tức phần dư (Residual Dividend)** | Ưu tiên đầu tư dự án NPV > 0, phần dư mới chia | Tối ưu phân bổ vốn, tối thiểu phát hành thêm vốn | Cổ tức rất bấp bênh | DN tăng trưởng, SME có kế hoạch đầu tư |
| **Thấp đều + thưởng thêm (Low Regular + Extra)** | Cổ tức nền thấp (chắc chắn) + cổ tức bổ sung khi lợi nhuận tốt | Cân bằng ổn định và linh hoạt | Phải kỷ luật khi định "nền" | DN có lợi nhuận biến động (nông sản, xây dựng) |
| **Cổ tức bằng cổ phiếu (Stock Dividend)** | Phát hành thêm cổ phiếu cho cổ đông theo tỷ lệ | Giữ tiền mặt, giữ tỷ lệ sở hữu | Làm tăng số cổ phần, loãng EPS | DN cần giữ tiền mặt, tăng vốn điều lệ |

#### Ví dụ Residual Dividend (từng bước)

Lợi nhuận sau thuế 3.000 triệu; DN muốn giữ cơ cấu vốn mục tiêu 40% nợ / 60% vốn chủ cho mọi khoản đầu tư.

| Năm | Ngân sách đầu tư | Vốn chủ cần = 60% × ngân sách | Cổ tức = 3.000 − vốn chủ cần | Payout |
|-----|------------------|-------------------------------|------------------------------|--------|
| 1 | 2.400 | 1.440 | **1.560** | 52% |
| 2 | 4.000 | 2.400 | **600** | 20% |
| 3 | 1.000 | 600 | **2.400** | 80% |

→ Payout dao động 20%–80%: đúng về mặt tối ưu vốn nhưng **cổ đông chịu rủi ro thu nhập** và thị trường đọc tín hiệu xấu mỗi khi giảm. Vì vậy thực tế thường dùng Residual để quyết định *tổng* cổ tức dài hạn, rồi áp dụng mô hình "Thấp đều + thưởng thêm" để làm mượt.

#### Cổ tức bằng cổ phiếu (Stock Dividend) – bản chất kinh tế

Ví dụ: 1.000.000 CP, giá 20.000đ, lợi nhuận 3.000 triệu; chia cổ tức cổ phiếu 10% (cổ đông sở hữu 10 CP được thêm 1 CP).

| Chỉ tiêu | Trước | Sau |
|---------|-------|-----|
| Số CP | 1.000.000 | **1.100.000** |
| EPS | 3.000đ | 3.000 triệu / 1.100.000 = **2.727đ** |
| Giá lý thuyết | 20.000đ | 20.000 triệu / 1.100.000 = **18.182đ** |
| Cổ đông giữ 600.000 CP | 600.000 × 20.000 = 12.000 triệu | 660.000 × 18.182 = **12.000 triệu** |
| Vốn điều lệ (mệnh giá 10.000đ) | 10.000 triệu | +100.000 CP × 10.000 = **+1.000 triệu** (lấy từ lợi nhuận giữ lại) |

→ Cổ đông **không giàu thêm**; chỉ là số cổ phiếu tăng, giá chia lại. Bản chất là **chuyển lợi nhuận giữ lại thành vốn điều lệ**. Ưu điểm là DN giữ nguyên tiền mặt để đầu tư; cổ đông cá nhân thường không bị thuế khi nhận (thuế phát sinh khi chuyển nhượng – cần xác nhận quy định hiện hành).

### J. Ưu điểm và nhược điểm của việc trả cổ tức

#### ✅ Ưu điểm trả cổ tức

1. **Tín hiệu tự tin (Signal confidence)** – "Chúng tôi đủ khỏe để chia tiền"
2. **Thu hút nhà đầu tư thu nhập** – quỹ hưu trí, người hưu trí CẦN dòng tiền đều
3. **Kỷ luật (Discipline)** – rút bớt FCF dư, ban quản lý khó lãng phí
4. **Chim trong tay (Bird-in-hand)** – thu nhập chắc chắn hơn lãi vốn bấp bênh
5. **Hỗ trợ giá cổ phiếu** – tỷ suất cổ tức hấp dẫn tạo "đáy giá"
6. **Miễn thuế cho một số nhóm** – VN: pháp nhân nhận cổ tức từ công ty đã nộp thuế TNDN thường được miễn thuế TNDN

#### ❌ Nhược điểm

1. **Bất lợi thuế** – cá nhân nộp thuế khi nhận (5% VN, tới 23,8% Mỹ)
2. **Giảm linh hoạt** – một khi đã trả, rất khó cắt (thị trường trừng phạt!)
3. **Chi phí cơ hội** – tiền đã chia không còn để đầu tư tăng trưởng
4. **Hạn chế tăng trưởng** – payout cao → giữ lại ít → $g$ thấp
5. **Dính (Sticky)** – phải duy trì cả năm xấu (áp lực tín hiệu)
6. **Đánh thuế hai lần (Double taxation)** – thuế DN + thuế cá nhân (ở một số nước)

### K. Khung ra quyết định: Khi nào nên trả cao, khi nào nên giữ lại

#### K.1. Khung quyết định

```
NÊN TRẢ CỔ TỨC CAO?

CÓ (Payout cao):                        KHÔNG (Payout thấp / Buyback):
• DN trưởng thành, ổn định              • Giai đoạn tăng trưởng cao
• Ít cơ hội tăng trưởng                  • Nhiều dự án có lợi nhuận (NPV > 0)
• Dòng tiền tự do (FCF) dư thừa         • Cần tiền để đầu tư
• Cổ đông = người hưu trí/quỹ            • Cổ đông thích lãi vốn
• Thông lệ ngành (điện nước, REIT)      • Thông lệ ngành (công nghệ)
• Muốn phát tín hiệu tự tin             • Thuế cổ tức cao
• Giảm chi phí đại diện (FCF)           • Muốn giữ linh hoạt tài chính

        ┌─────────────────────┐
        │ LIFE CYCLE THEORY   │
        ├─────────────────────┤
        │ Startup: 0% payout  │ ← Giữ lại tất cả, đang đốt tiền
        │ Growth:  0-20%      │ ← Cần vốn để đầu tư
        │ Mature:  30-60%     │ ← Ổn định, tăng trưởng vừa
        │ Decline: 60-100%+   │ ← Hết dự án, trả lại cổ đông
        └─────────────────────┘
```

#### K.2. Dividend Yield và tăng trưởng theo loại hình DN

| Loại DN | Dividend Yield | Payout | Tăng trưởng |
|---------|---------------|--------|--------|
| Công nghệ tăng trưởng cao | 0–1% | 0–20% | 20–40%/năm |
| Large-cap tăng trưởng | 1–2% | 20–35% | 10–15%/năm |
| Blue-chip ổn định | 2–4% | 40–60% | 5–10%/năm |
| Điện nước/REIT | 4–8% | 70–95% | 2–5%/năm |
| Khủng hoảng/Tái cấu trúc | 0% (cắt) | 0% | Âm/tái cấu trúc |

#### K.3. Hướng dẫn chọn chính sách theo yếu tố (Dividend Policy Selection Guide)

| Yếu tố | Tác động lên chính sách |
|--------|-----------------|
| Môi trường thuế | Thuế cổ tức cao → ưu tiên buyback/giữ lại |
| Cơ cấu cổ đông | Người hưu trí → cổ tức cao. Tổ chức/quỹ tăng trưởng → buyback/thấp |
| Cơ hội tăng trưởng | Tăng trưởng cao → giữ lại. Thấp → chia |
| Độ ổn định dòng tiền | Ổn định → cam kết được cổ tức. Biến động → buyback/thấp đều + thưởng thêm |
| Thông lệ ngành | Theo ngành trừ khi có lý do mạnh để khác |
| Ràng buộc pháp lý | REIT phải chia 90%+. Hợp đồng vay (covenants) có thể hạn chế chia cổ tức |
| Vòng đời DN | Startup 0% → Tăng trưởng 0–20% → Trưởng thành 30–60% → Suy giảm 60–100% |

#### K.4. Tóm tắt: khi nào lý thuyết nào đúng?

| Lý thuyết | Đúng nhất khi | Hàm ý cho DN |
|-----------|---------------|--------------|
| M&M Irrelevance | Thị trường gần hoàn hảo, nhiều nhà đầu tư lớn, thanh khoản cao | Cổ tức ít quan trọng; tập trung vào dự án đầu tư |
| Bird-in-Hand / Clientele | Cổ đông cần thu nhập, khó bán cổ phần (SME, thanh khoản thấp) | Cổ tức tiền mặt có giá trị thực |
| Tax Preference | Thuế cổ tức > thuế lãi vốn, thị trường thanh khoản | Ưu tiên giữ lại/buyback |
| Signaling | Thông tin bất cân xứng lớn | Giữ ổn định, tránh cắt; tăng khi chắc chắn |
| Agency / FCF | DN dư tiền, quản lý có xu hướng xây đế chế | Chia bớt tiền dư |

---

## III. CASE STUDIES THỰC TẾ

### 1. Case Study Thành công: Berkshire Hathaway – ZERO Dividend, Maximum Value

#### Bối cảnh

- **Warren Buffett**'s Berkshire Hathaway: **chưa từng trả cổ tức tiền mặt** kể từ khi ông nắm quyền kiểm soát (1965; ngoại lệ duy nhất được ghi nhận là khoản 0,10 USD/CP vào khoảng 1967)
- Vốn hóa thị trường: khoảng 900 tỷ USD trở lên (2024)
- Tốc độ tăng giá trị cổ phiếu bình quân khoảng **19,8%/năm** giai đoạn 1965–2023 (theo thư gửi cổ đông của Berkshire; số liệu cần đối chiếu nguồn gốc khi dùng trích dẫn chính thức)

#### Lập luận của Buffett chống lại cổ tức

| Lập luận | Chi tiết |
|----------|----------|
| **Bất lợi thuế** | 1 USD cổ tức → thuế tối đa khoảng 23,8% → cổ đông giữ 0,76 USD. 1 USD giữ lại → toàn bộ 1 USD tiếp tục sinh lời |
| **Cơ hội tái đầu tư** | ROE/suất sinh lời của Buffett >> lợi suất thị trường → tái đầu tư nội bộ tốt hơn |
| **Phân bổ lý trí** | "Tôi phân bổ 1 USD tốt hơn thị trường" – đúng trong lịch sử |
| **Homemade dividends** | "Cần thu nhập thì bán bớt cổ phiếu" – tiết kiệm thuế |
| **Linh hoạt** | Không cam kết cổ tức → triển khai vốn khi có cơ hội |

Đây chính là cách áp dụng thực tế của **M&M kết hợp Tax Preference**: nếu cổ đông có thể tự tạo "homemade dividend" bằng cách bán cổ phiếu và thuế lãi vốn thấp hơn thuế cổ tức, thì mỗi đồng cổ tức chia ra là một đồng bị "rò rỉ thuế" mà không tạo thêm giá trị.

#### Mô phỏng từng bước: Vì sao giữ lại tạo giá trị lớn hơn rất nhiều?

*Mô hình đơn giản hóa (stylized) để minh họa cơ chế; không phải số liệu lịch sử chính thức.*

**Giả định**: Đầu tư 1.000 USD vào năm 1965; 59 năm đến 2023; Berkshire tạo ROE tương đương 19,8%/năm; S&P 500 (có tái đầu tư cổ tức) 10,2%/năm; nếu Berkshire trả cổ tức, cổ tức bị đánh thuế 23,8% rồi cổ đông đem tái đầu tư vào S&P 500.

**Kịch bản 1 – Giữ lại 100% (payout 0%)**:

$$1.000 \times (1 + 0{,}198)^{59} \approx 42{,}56\ \text{triệu USD}$$

**Kịch bản 2 – S&P 500 (tham chiếu)**:

$$1.000 \times (1 + 0{,}102)^{59} \approx 308.000\ \text{USD}$$

**Kịch bản 3 – Berkshire trả cổ tức payout 30%** (mô phỏng từng năm): mỗi năm vốn chủ tăng chỉ $19{,}8\% \times 70\% = 13{,}86\%$ (do 30% lợi nhuận đã chia), còn 30% × lợi nhuận được trả ra, sau thuế 23,8% còn 76,2% đem tái đầu tư vào S&P 500 với 10,2%/năm. Kết quả sau 59 năm (chạy bằng Python):

| Thành phần | Giá trị |
|-----------|---------|
| Giá trị vốn chủ còn trong Berkshire | ≈ 2,12 triệu USD |
| Danh mục S&P 500 (tích lũy từ cổ tức sau thuế) | ≈ 2,24 triệu USD |
| **Tổng cộng** | **≈ 4,36 triệu USD** (tương đương 15,3%/năm) |

| Kịch bản | Giá trị sau 59 năm (từ 1.000 USD) | Tốc độ tăng bình quân/năm |
|----------|----------------------|--------------------|
| BRK giữ lại 100% | **≈ 42,6 triệu USD** | 19,8% |
| BRK trả 30% payout (sau thuế, tái đầu tư S&P) | ≈ 4,36 triệu USD | ≈ 15,3% |
| BRK trả 50% payout (cùng giả định) | ≈ 1,41 triệu USD | ≈ 13,1% |
| S&P 500 (đã gồm cổ tức tái đầu tư) | ≈ 0,31 triệu USD | 10,2% |

*(Lưu ý: Bản trước của file nêu "≈ 12 triệu USD" cho kịch bản 30% payout; kết quả mô phỏng trong bản này cho ≈ 4,4 triệu USD với giả định minh bạch ở trên. Số liệu BRK giữ lại 100% ban đầu ghi "37 triệu USD" ứng với 58 năm; ở 59 năm là ≈ 42,6 triệu USD. Chưa trừ thuế lãi vốn khi cuối cùng bán cổ phiếu – với cả ba kịch bản sẽ giảm tuyệt đối, nhưng không đổi thứ tự.)*

#### Diễn giải ý nghĩa kinh doanh

- **Hiệu ứng lãi kép (compounding)**: 30% lợi nhuận bị chia ra làm giảm tốc độ tăng trưởng từ 19,8% xuống còn 13,86% *trong lõi Berkshire*. Sau 59 năm, chênh lệch giữa $1{,}198^{59}$ và $1{,}1386^{59}$ lên tới hàng chục lần.
- **Lợi thế phụ thuộc vào năng lực phân bổ vốn**: Cơ chế giữ lại chỉ vượt trội vì Berkshire tái đầu tư với suất sinh lời (19,8%) cao hơn nhiều lần mức cổ đông tự kiếm (10,2%). Nếu Berkshire chỉ tái đầu tư được 8%, thì chia cổ tức mới là lựa chọn đúng.
- **Thuế**: Bất lợi thuế 23,8% làm thiệt hại thêm cho kịch bản chia cổ tức.

#### Cập nhật 2024

- Berkshire đã **mua lại cổ phiếu** (hàng tỷ USD/năm trong một số năm) – cách trả lại vốn tiết kiệm thuế khi giá thấp hơn giá trị nội tại
- Lý do: khoản tiền mặt lên tới trên 150 tỷ USD (có lúc trên 300 tỷ USD), ít cơ hội đầu tư hấp dẫn → ngay cả Buffett cũng chuyển sang buyback khi không tìm được dự án tốt
- Vẫn **không chia cổ tức tiền mặt** (dính, bất lợi thuế)

#### Bài học

1. Với nhà phân bổ vốn xuất sắc, **giữ lại >> chia cổ tức**
2. Hiệu ứng lãi kép của thuế qua nhiều thập kỷ là KHỔNG LỒ
3. Buyback > cổ tức khi cổ phiếu bị định giá thấp
4. CHỈ hiệu quả khi DN thực sự tái đầu tư tốt (đa số DN KHÔNG làm được – xem Agency Theory)
5. Khi hết cơ hội đầu tư hấp dẫn, ngay cả Berkshire cũng phải trả lại vốn qua buyback

---

### 2. Case Study Thất bại: GE – Cắt cổ tức = Phá hủy niềm tin

#### Bối cảnh

- General Electric (GE): từng là cổ phiếu "dividend aristocrat" – được các quỹ hưu trí và nhà đầu tư thu nhập yêu thích, duy trì cổ tức nhiều thập kỷ
- Dividend yield khoảng 3–4% trong giai đoạn đỉnh
- Ba lần cắt cổ tức lớn: **2009** (cắt lần đầu sau gần 70 năm, từ ~1,24 → ~0,40 USD/CP, ~−68%), **cuối 2017** (cắt ~50% cổ tức quý) và **cuối 2018** (cắt ~92%, còn 0,01 USD/quý = 0,04 USD/năm)

*(Số liệu cổ tức, giá cổ phiếu trong bảng dưới là số liệu làm tròn từ trí nhớ/nguồn công khai, cần kiểm chứng trước khi dùng trong tài liệu chính thức.)*

#### Dòng thời gian thảm họa (Timeline)

| Năm | Cổ tức hằng năm (xấp xỉ) | Giá cổ phiếu (xấp xỉ) | Yield | Tín hiệu thị trường |
|-----|----------------|------------|-------|--------|
| 2007 | 1,24 USD | 42 USD | 3,0% | Bình thường |
| 2009 | ~0,40 USD (−68%) | 15 USD | ~2,7% | Khủng hoảng! Cắt lần đầu sau gần 7 thập kỷ |
| 2017 | ~0,96 → ~0,48 USD (−50% cuối năm) | 30 USD | ~1,6% | "Tái cơ cấu nhưng ổn định" |
| 2018 | ~0,04 USD/năm quy đổi (−92%) | 8 USD | 0,5% | Tín hiệu thảm họa |
| 2021 | ~0,08 USD | 12 USD | 0,7% | Niềm tin bị phá vỡ |
| 2024 | Tách thành các công ty độc lập | - | - | Kết thúc GE như từng biết |

#### Phân tích từng bước: Vì sao cắt cổ tức lại "giết" cổ phiếu?

**Bước 1 – Tác động trực tiếp lên cổ đông thu nhập**: Ví dụ nhà đầu tư hưu trí nắm 10.000 CP GE.
- Trước cắt 2009: 10.000 × 1,24 = **12.400 USD/năm**
- Sau cắt 2009: 10.000 × 0,40 = **4.000 USD/năm**, giảm **8.400 USD (−68%)** thu nhập sinh hoạt
- → Họ phải bán cổ phiếu để bù thu nhập, tạo **áp lực bán** (đúng cơ chế Clientele Effect)

**Bước 2 – Tác động tín hiệu**: Theo Signaling Theory, DN trả đều nhiều thập kỷ → thị trường coi cổ tức là "cam kết". Cắt lần đầu sau gần 7 thập kỷ → thị trường suy luận "tình hình tệ hơn công bố". Giá giảm mạnh hơn nhiều so với giá trị dòng tiền cổ tức bị mất (vì thông tin kèm theo).

**Bước 3 – Cơ chế xoắn ốc tự củng cố**:

```
Cắt cổ tức → Quỹ có mandate thu nhập buộc bán → Giá giảm
   → Vốn hóa giảm, chi phí vốn tăng → Hạ bậc tín nhiệm
   → Tài trợ đắt hơn, khó bán tài sản → Kết quả xấu hơn
   → Lại phải cắt thêm (2017, 2018)
```

| Yếu tố | Tác động |
|--------|----------|
| **Tín hiệu (Signaling)** | Phá vỡ chuỗi nhiều thập kỷ → "Mọi thứ TỆ HƠN thông báo" |
| **Cú sốc nhóm khách hàng (Clientele)** | Người hưu trí phụ thuộc cổ tức → bị ép bán → giá giảm dây chuyền |
| **Mất uy tín** | Ban lãnh đạo nhiều lần khẳng định cổ tức "an toàn" trước khi cắt → mất niềm tin |
| **Mandate tổ chức** | Một số quỹ BUỘC phải bán khi cắt cổ tức |
| **Xoắn ốc tự củng cố** | Cắt → nhà đầu tư rời → giá giảm → hạ bậc tín nhiệm → xấu hơn |

#### Phân tích nguyên nhân gốc rễ (Root Cause Analysis)

- Tổn thất tiềm ẩn ở GE Capital (thiếu hụt dự phòng bảo hiểm trên 15 tỷ USD được công bố vào đầu 2018)
- Thương vụ mua lại phá hủy giá trị (Alstom, Baker Hughes) – ví dụ điển hình của **chi phí đại diện/FCF** (quản lý chi tiêu vào dự án NPV < 0)
- Quản lý lợi nhuận (earnings management) nhiều năm → cổ tức được trả từ **lợi nhuận KHÔNG bền vững** (payout thực theo dòng tiền vượt xa payout kế toán)
- "Cổ tức là chiếc áo cuối cùng của hoàng đế" → khi cắt, lộ ra sự thật

#### Bài học thất bại

```
1. BỀN VỮNG > MỨC CAO: Chỉ trả những gì có thể duy trì dài hạn
   → Payout nên chừa biên an toàn (FCF coverage > 1,5 lần)

2. ĐỪNG HỨA ĐIỀU KHÔNG GIỮ ĐƯỢC: Lời khẳng định "an toàn" ngay
   trước khi cắt = phá hủy uy tín vĩnh viễn

3. CỔ TỨC LÀ MỘT CAM KẾT: Một khi đã bắt đầu, thị trường KỲ VỌNG
   tiếp tục → Cân nhắc kỹ trước khi khởi xướng

4. HIỂU CƠ CẤU CỔ ĐÔNG: Nếu cổ đông phụ thuộc thu nhập,
   cắt cổ tức gây ra bán tháo dây chuyền

5. SỬA DOANH NGHIỆP TRƯỚC: Đừng dùng cổ tức để che giấu suy thoái
   → Dòng tiền → Đầu tư → RỒI MỚI cổ tức
```

#### So sánh đối chiếu Berkshire và GE

| Tiêu chí | Berkshire | GE |
|----------|-----------|-----|
| Chính sách | Không cổ tức, thông báo rõ từ đầu | Cổ tức cao đều nhiều thập kỷ |
| Kỳ vọng thị trường | Đã định vị "không cổ tức" → không có tín hiệu xấu | Kỳ vọng "cổ tức ổn định" → cắt = tín hiệu xấu |
| Tính nhất quán | Chính sách phù hợp năng lực phân bổ vốn | Chính sách che giấu vấn đề cơ bản |
| Cơ cấu cổ đông | Thu hút cổ đông dài hạn chấp nhận lãi vốn | Thu hút cổ đông thu nhập → dễ bán tháo |

→ Bài học chung: **không có chính sách tốt tuyệt đối; chỉ có chính sách phù hợp với cổ đông, năng lực tạo dòng tiền và nhất quán theo thời gian.**

---

### 3. Case Study SME: Công ty CP Thực phẩm sấy "Hương Quê" – Quyết định chia bao nhiêu cổ tức năm 2024

#### Bối cảnh doanh nghiệp

Công ty Cổ phần Thực phẩm sấy Hương Quê (Long An) chế biến trái cây, rau củ sấy xuất khẩu và bán cho chuỗi siêu thị, hoạt động 7 năm, chưa niêm yết. Cuối năm tài chính, Hội đồng quản trị (HĐQT) phải đề xuất mức chia cổ tức lên Đại hội đồng cổ đông (ĐHĐCĐ).

**Số liệu hiện tại (đơn vị: triệu đồng, trừ khi ghi khác):**

| Chỉ tiêu | Giá trị |
|----------|---------|
| Lợi nhuận sau thuế (NI) | 3.000 |
| Số cổ phần lưu hành | 1.000.000 CP (mệnh giá 10.000đ) |
| EPS | 3.000đ/CP |
| Vốn chủ sở hữu (sổ sách) | 12.000 → ROE = 25% |
| Giá trị thị trường ước tính | 20.000/CP → 20.000 triệu |
| Chi phí vốn chủ yêu cầu ($K_e$, đã cộng phần bù thanh khoản) | 15% |
| Nợ vay hiện hữu | 2.000 triệu, lãi suất 10%/năm → lãi 200 |
| Thuế suất thuế TNDN | 20% |
| Dòng tiền tự do (FCF) trước chia cổ tức | NI 3.000 + khấu hao 500 − capex duy trì 400 − tăng vốn lưu động 100 = **3.000** |

**Cổ đông:**
- Ông Hùng (sáng lập, giám đốc): 60% (600.000 CP) – không cần tiền mặt, muốn mở rộng
- Bà Lan (đã nghỉ hưu): 25% (250.000 CP) – cần khoảng **140 triệu/năm sau thuế** để chi tiêu
- Anh Minh (cá nhân đầu tư): 15% (150.000 CP) – chấp nhận cả hai

**Cơ hội đầu tư năm tới**: Xây dây chuyền kho lạnh + máy sấy mới, **vốn đầu tư 2.400 triệu**, tạo thêm lợi nhuận sau thuế **432 triệu/năm** (giả định ổn định như dòng tiền vĩnh viễn để đơn giản hóa).

**Ba phương án chính sách:**
- **P1** – Chia nhiều: payout 70%
- **P2** – Giữ lại tối đa: payout 0%
- **P3** – Cân bằng: payout 20%

#### Bước 1: Đánh giá dự án mới – có đáng giữ tiền lại không?

$$ROIC_{dự\ án} = \frac{432}{2.400} = 18\% \qquad NPV = \frac{432}{0{,}15} - 2.400 = 2.880 - 2.400 = +480\ \text{triệu}$$

→ Suất sinh lời dự án (18%) **cao hơn** chi phí vốn chủ (15%) → NPV = **+480 triệu**. Theo logic cổ tức phần dư, DN có lý do để *giữ lại tiền* cho dự án này thay vì chia hết.

#### Bước 2: Tính tiền sẵn có để chia và để đầu tư theo từng chính sách

| Chỉ tiêu | P1 (70%) | P2 (0%) | P3 (20%) |
|----------|---------|---------|---------|
| Cổ tức = NI × payout | 2.100 | 0 | 600 |
| DPS (đồng/CP) | 2.100 | 0 | 600 |
| Lợi nhuận giữ lại = NI − cổ tức | 900 | 3.000 | 2.400 |
| Tiền sẵn có đầu tư = FCF − cổ tức | 900 | 3.000 | 2.400 |
| Vốn cần cho dự án | 2.400 | 2.400 | 2.400 |
| **Thiếu hụt (phải vay thêm)** | **1.500** | 0 | 0 |
| **Tiền thừa (nằm không)** | 0 | **600** | 0 |

→ P3 là phương án **khớp tiền** nhất: giữ lại đúng 2.400 triệu cho dự án.

#### Bước 3: Tốc độ tăng trưởng bền vững $g = ROE \times b$

| | P1 | P2 | P3 |
|-|----|----|----|
| Retention $b$ | 30% | 100% | 80% |
| **g = 25% × b** | **7,5%** | 25% | 20% |

→ P1 làm tăng trưởng nội sinh tụt xuống chỉ còn 7,5% – muốn đầu tư dự án, phải vay thêm.

#### Bước 4: Phân tích P1 – "Chia rồi lại đi vay" có hợp lý không?

P1 chia 2.100 triệu nhưng thiếu 1.500 triệu cho dự án → vay ngân hàng 1.500 triệu (lãi 11%/năm).

| Khoản mục | Tính toán | Kết quả |
|-----------|-----------|---------|
| Lãi vay mới | 1.500 × 11% | 165 triệu/năm (sau thuế = 132) |
| Chi phí hồ sơ vay (giả định 1%) | 1.500 × 1% | 15 triệu |
| Thuế cổ tức tăng thêm (so với P3) | (2.100 − 600) × 5% | 75 triệu |
| **Tổng "rò rỉ" giá trị so với P3** | 75 + 15 | **≈ 90 triệu** |

- Về lý thuyết M&M, vay đúng lãi suất thị trường để trả cổ tức không tạo/hủy giá trị, nhưng khi có **thuế cổ tức 5% + phí vay**, DN vô cớ thất thoát khoảng 90 triệu mà không đạt thêm lợi ích nào về đầu tư.
- Nợ tăng từ 2.000 → 3.500 triệu. Kiểm tra mức an toàn (EBIT hiện tại: $3.000/0{,}8 + 200 = 3.950$; EBIT dự án: $432/0{,}8 = 540$):

| Chỉ tiêu | Cơ sở | Kịch bản xấu (EBIT cũ −30%) |
|----------|-------|--------------|
| Hệ số bao phủ lãi vay P1 = EBIT / (200 + 165) | (3.950 + 540) / 365 = **12,3 lần** | (2.765 + 540) / 365 = **9,05 lần** |
| Hệ số bao phủ lãi vay P3 = EBIT / 200 | 4.490 / 200 = 22,45 lần | 3.305 / 200 = 16,5 lần |

→ P1 **không rủi ro vỡ nợ** (bao phủ lãi vay vẫn > 3 lần rất xa), nhưng *vô ích* trừ khi cổ đông thật sự cần nhiều tiền mặt.

#### Bước 5: Phân tích P2 – "Giữ lại tất cả" có tối ưu không?

P2 giữ lại 3.000 triệu nhưng dự án chỉ cần 2.400 → **600 triệu nhàn rỗi**.

| | Tính toán | Kết quả |
|-|-----------|---------|
| Lãi gửi ngân hàng sau thuế (giả định 5%/năm) | 600 × 5% × (1 − 20%) | 24 triệu |
| Cổ đông đòi hỏi tối thiểu | 600 × 15% | 90 triệu |
| **Thiệt hại mỗi năm do giữ tiền nhàn rỗi** | 90 − 24 | **≈ 66 triệu/năm** |

→ Đây là bài học của Agency Theory: **tiền dư không có dự án NPV>0 nên trả lại cổ đông**. Ngoài ra P2 bỏ qua nhu cầu tiền mặt của bà Lan.

#### Bước 6: Nhu cầu cổ đông và "homemade dividend" có khả thi không?

Bà Lan cần ~140 triệu/năm sau thuế.

| Phương án | Bà Lan nhận | Ghi chú |
|-----------|-------------|---------|
| P3: cổ tức tổng 600 triệu | 25% × 600 = 150 gộp, thuế 5% = 7,5, **thực nhận 142,5** | Đáp ứng nhu cầu |
| P2: không cổ tức, tự bán cổ phần | Cần bán: 150 triệu / 20.000đ = 7.500 CP (nếu bán được đúng giá) | Cổ phần chưa niêm yết, khó tìm người mua |
| P2 với chiết khấu thanh khoản 25% | 150 triệu / 15.000đ = **10.000 CP** | Mất thêm 2.500 CP ≈ 50 triệu giá trị |

→ Do chi phí giao dịch/chiết khấu thanh khoản của cổ phần chưa niêm yết rất cao, giả định "homemade dividend" của M&M **không đúng với SME** → cổ tức tiền mặt thực sự có giá trị với bà Lan.

#### Bước 7: Thiết kế chính sách "Thấp đều + thưởng thêm" và stress test

Để tránh lỗi "cổ tức dính" của GE, đề xuất: **cổ tức nền 300đ/CP (300 triệu) + cổ tức bổ sung bằng 10% lợi nhuận sau thuế**. Với NI = 3.000: 300 + 10% × 3.000 = **600 triệu** (đúng bằng P3).

Kịch bản xấu: đơn hàng giảm, NI giảm 30% → 2.100 triệu, FCF gần đúng giảm 900 triệu còn khoảng 2.100.

| Chính sách | Cổ tức khi NI = 3.000 | Cổ tức khi NI = 2.100 | Mức cắt | Hệ số bao phủ FCF/cổ tức (kịch bản xấu) |
|------------|---------|----------|---------|-----------|
| P1 – payout cố định 70% | 2.100 | 1.470 | −30% | 2.100 / 1.470 = 1,43 lần |
| Cố định 600 triệu bất kể lợi nhuận | 600 | 600 | 0% | Payout nhảy lên 28,6% |
| **Nền 300 + 10% NI** | 600 | 300 + 210 = **510** | **−15%** | 2.100 / 510 = **4,1 lần** |

→ Chính sách "nền + bổ sung" giúp cổ tức biến động ít hơn P1 (−15% so với −30%) mà vẫn linh hoạt. Cổ tức nền đạt 300 triệu luôn được bao phủ bằng FCF nhiều lần.

#### Bước 8 (Tùy chọn): Cổ tức bằng cổ phiếu để giữ tiền mặt

Nếu muốn tăng vốn điều lệ mà không chi tiền: phát hành cổ phiếu thưởng 10% → 1.100.000 CP, EPS = 3.000 triệu/1.100.000 = **2.727đ**, giá lý thuyết **18.182đ**; ông Hùng nắm 660.000 CP, giá trị vẫn 12.000 triệu. Không ai giàu thêm, nhưng vốn điều lệ tăng thêm 1.000 triệu (làm tăng quy mô vay ngân hàng được cấp).

#### Kết luận và Khuyến nghị

**Khuyến nghị**: HĐQT đề xuất ĐHĐCĐ chọn **P3 với cấu trúc "cổ tức nền 300đ/CP + 10% LN"** (tổng 600 triệu = 600đ/CP, payout 20%), cụ thể:

1. **Giữ lại 2.400 triệu** đầu tư dự án (NPV +480 triệu) → hưởng tăng trưởng nội sinh $g$ = 20%
2. **Trả 600 triệu** đáp ứng nhu cầu bà Lan (142,5 triệu thực nhận) và khớp đúng nhu cầu tiền mặt của cổ đông – không dư thừa (khác P2), không phải vay để chia (khác P1, tiết kiệm khoảng 90 triệu)
3. **Cam kết bằng văn bản** trong điều lệ/thỏa thuận cổ đông: cổ tức nền 300đ/CP; phần bổ sung tùy lợi nhuận → tránh bẫy tín hiệu kiểu GE
4. **Rà soát hằng năm**: khi dự án hoàn thành và hết cơ hội đầu tư NPV>0, nâng payout (theo vòng đời DN) hoặc cân nhắc thêm cổ tức đặc biệt

> **Ghi chú phương pháp**: Toàn bộ phép tính trong case này (NPV, ROIC, FCF, g, thuế, hệ số bao phủ lãi vay, stress test, cổ tức cổ phiếu) đã được kiểm tra chéo bằng Python để đảm bảo nhất quán số học trước khi đưa vào tài liệu. Giả định "432 triệu/năm vĩnh viễn" là đơn giản hóa; thực tế cần chiết khấu dòng tiền theo vòng đời dự án.

---

## IV. ỨNG DỤNG CHO SME

### 1. Đặc thù chính sách cổ tức của SME Việt Nam so với công ty niêm yết

| Yếu tố | Công ty niêm yết lớn | SME Việt Nam |
|--------|---------------------|--------------|
| Thanh khoản cổ phần | Cao – dễ bán (homemade dividend khả thi) | Rất thấp – gần như không bán lẻ được |
| Cổ đông | Phân tán, nhiều tổ chức | Ít cổ đông, thường gia đình/người sáng lập |
| Người chủ và người quản lý | Tách biệt (agency cost lớn) | Thường trùng nhau (agency cost nhỏ nhưng xung đột giữa cổ đông lớn/nhỏ) |
| Tiếp cận vốn | Nhiều kênh (thị trường vốn) | Chủ yếu ngân hàng, lợi nhuận giữ lại |
| Vai trò của tín hiệu | Rất mạnh (giá cổ phiếu phản ứng) | Yếu về giá, nhưng quan trọng với cổ đông nhỏ và ngân hàng |
| Rủi ro chính | Mất niềm tin thị trường | Cạn tiền mặt, xung đột cổ đông |
| Quy trình quyết định | HĐQT → ĐHĐCĐ, có công bố thông tin | Thương lượng nội bộ |

→ **Hệ quả**: Với SME, "giữ lại tối đa" thường hợp lý (vốn khó huy động), nhưng không thể bỏ qua nhu cầu **thu nhập của cổ đông nhỏ/nghỉ hưu** vì không thể "tự bán cổ phần để lấy tiền".

### 2. Quy trình 6 bước ra quyết định cổ tức cho chủ SME

1. **Kiểm tra điều kiện pháp lý**: LN sau thuế còn lại sau khi bù lỗ, trích lập các quỹ theo điều lệ; vẫn thanh toán đủ nợ đến hạn sau khi chia (theo nguyên tắc chung của Luật Doanh nghiệp – cần đối chiếu điều khoản cụ thể)
2. **Lập danh sách dự án có NPV > 0** và tổng vốn cần → xác định *nhu cầu giữ lại*
3. **Tính FCF** (không chỉ lợi nhuận) → xác định *khả năng chia an toàn* (FCF − vốn đầu tư)
4. **Khảo sát nhu cầu từng nhóm cổ đông** (cần tiền mặt hay tái đầu tư), tính cả thuế 5%
5. **Chọn mô hình chính sách** (Nền + thưởng thêm thường phù hợp nhất cho SME có lợi nhuận biến động) và **stress test** khi lợi nhuận −20–30%
6. **Văn bản hóa** trong điều lệ/thỏa thuận cổ đông, thông báo trước cho cổ đông để quản lý kỳ vọng

### 3. Khuôn khổ pháp lý và thuế (Việt Nam) cần lưu ý

| Nội dung | Quy định/nguyên tắc chung | Ghi chú |
|----------|--------------------------|---------|
| Điều kiện chia cổ tức | Chỉ chia khi đã hoàn thành nghĩa vụ thuế và tài chính khác, bù lỗ, trích lập quỹ theo điều lệ, và vẫn thanh toán được nợ đến hạn | Tham khảo Luật Doanh nghiệp hiện hành |
| Thẩm quyền | ĐHĐCĐ quyết định mức chi trả hằng năm; HĐQT đề xuất và thực hiện | Mức chia không vượt đề xuất của HĐQT |
| Thuế TNCN đối với cổ tức | 5% trên cổ tức tiền mặt cá nhân nhận | Công ty khấu trừ tại nguồn |
| Chuyển nhượng cổ phần CTCP | 0,1% trên giá chuyển nhượng (cá nhân) | Phần vốn góp công ty TNHH: 20% trên chênh lệch |
| Cổ tức bằng cổ phiếu | Cá nhân thường chưa chịu thuế khi nhận, chịu thuế khi chuyển nhượng | Xác nhận lại với tư vấn thuế |
| Pháp nhân nhận cổ tức | Thường được miễn thuế TNDN với cổ tức từ công ty đã nộp thuế | Khi dùng cấu trúc công ty mẹ – con |
| Hợp đồng vay | Covenants có thể hạn chế/cấm chia cổ tức khi vi phạm chỉ tiêu | Đọc kỹ trước khi cam kết |

> **Lưu ý**: Bảng trên chỉ là hướng dẫn tổng quát; luôn tham vấn kế toán/luật sư thuế tại thời điểm chia vì quy định thay đổi.

### 4. Benchmark payout tham khảo cho SME Việt Nam theo giai đoạn

| Giai đoạn SME | Payout tham khảo | Ghi chú |
|---------------|------------------|---------|
| Khởi nghiệp (0–3 năm) | 0% | Giữ lại tất cả, chưa có lợi nhuận ổn định |
| Tăng trưởng (3–7 năm) | 0–30% | Nhiều dự án mở rộng, cổ tức nhỏ để giữ nhà đầu tư |
| Trưởng thành (7+ năm) | 30–60% | Dòng tiền ổn định, cổ đông kỳ vọng thu nhập |
| Bão hòa/Suy giảm | 60–100% | Ít dự án; cân nhắc thanh lý/rút vốn |

*(Khoảng giá trị mang tính tham khảo theo lý thuyết vòng đời, không phải số liệu thống kê điều tra SME Việt Nam.)*

### 5. Những sai lầm phổ biến (Common Mistakes)

| Sai lầm | Hậu quả | Cách tránh |
|---------|---------|-----------|
| Chia cổ tức dựa trên lợi nhuận kế toán, không xét tiền mặt | Cạn tiền, phải vay để trả lương, trả nhà cung cấp | Dùng FCF coverage > 1,5 lần |
| Chia hết để "cho cổ đông vui" khi còn dự án NPV > 0 | Bỏ lỡ cơ hội tăng trưởng | Lập danh sách dự án trước khi quyết định |
| Giữ tiền nhàn rỗi vô thời hạn | Chi phí cơ hội (như P2 ở Case III.3), xung đột cổ đông | Đặt ngưỡng tiền mặt tối đa, chia phần dư |
| Cam kết cổ tức cao rồi cắt đột ngột | Mất niềm tin (bài học GE) | Dùng mô hình nền + bổ sung |
| Vay ngân hàng để chia cổ tức | Rò rỉ thuế + phí + tăng rủi ro | Chỉ vay khi cổ đông có nhu cầu thật và đã stress test |
| Không có văn bản chính sách cổ tức | Tranh chấp giữa cổ đông lớn và nhỏ | Ghi vào điều lệ/thỏa thuận cổ đông |
| Bỏ qua covenant ngân hàng | Vi phạm hợp đồng vay | Kiểm tra điều khoản trước mỗi lần chia |

---

## V. TOOLS & TEMPLATES

### 1. Công cụ/nguồn tra cứu hỗ trợ phân tích cổ tức

| Công cụ/Nguồn | Công dụng | Ghi chú |
|----------------|-----------|---------|
| **Excel/Google Sheets** | Tính payout, FCF coverage, g bền vững, mô phỏng kịch bản | Cấu trúc gợi ý ở mục 2 |
| **Báo cáo tài chính (Bảng cân đối, KQKD, Lưu chuyển tiền tệ)** | Lấy NI, khấu hao, capex, vốn lưu động để tính FCF | Phần mềm kế toán MISA, Fast... xuất sẵn |
| **Dữ liệu cổ tức DN niêm yết (HOSE/HNX, CafeF, Vietstock, SSI iBoard)** | Tham chiếu payout/yield của DN cùng ngành | Cập nhật theo công bố thông tin |
| **Damodaran Online (NYU Stern)** | Bảng payout, yield, buyback theo ngành toàn cầu | Dữ liệu miễn phí, cập nhật hằng năm |
| **Dividend Discount Model trong Excel** | Định giá cổ phiếu theo Gordon | Chỉ khi $g < K_e$ |

### 2. Cấu trúc Excel/Google Sheet mô phỏng chính sách cổ tức cho SME

```
TAB 1 — INPUTS (chỉ nhập liệu tại đây):
  - Lợi nhuận sau thuế (NI), số cổ phần, mệnh giá
  - Vốn chủ sổ sách (để tính ROE), Ke
  - FCF trước chia cổ tức: NI + khấu hao − capex duy trì − Δ vốn lưu động
  - Ngân sách dự án mới + lợi nhuận sau thuế dự kiến của dự án
  - Thuế suất cổ tức (5%), lãi suất vay dự kiến
  - Danh sách cổ đông: % sở hữu, nhu cầu tiền mặt/năm

TAB 2 — ĐÁNH GIÁ DỰ ÁN:
  - ROIC dự án = Lợi nhuận dự án / Vốn đầu tư
  - NPV (vĩnh viễn) = Lợi nhuận / Ke − Vốn đầu tư
  - Cảnh báo: nếu NPV > 0 → ưu tiên giữ lại vốn

TAB 3 — SO SÁNH CHÍNH SÁCH (3–5 cột P1, P2, P3...):
  - Cổ tức = NI × payout, DPS, giữ lại, g = ROE × (1 − payout)
  - Tiền sẵn có đầu tư = FCF − cổ tức; Thiếu hụt/Thừa
  - Thuế cổ tức; thực nhận từng cổ đông
  - Hệ số bao phủ lãi vay; Conditional formatting: đỏ nếu thiếu hụt > 0 hoặc FCF coverage < 1,5

TAB 4 — STRESS TEST:
  - NI giảm 10% / 20% / 30% → cổ tức theo từng chính sách, mức cắt, FCF coverage

TAB 5 — DASHBOARD:
  - Biểu đồ so sánh cổ tức, tiền giữ lại, thiếu hụt giữa các phương án
  - Khuyến nghị tự động bằng hàm IF (ví dụ: nếu thiếu hụt > 0 → "cân nhắc giảm payout")
```

**Công thức Excel mẫu** (giả sử NI ở ô B2, payout ở B3, FCF ở B4, vốn dự án ở B5):

| Chỉ tiêu | Công thức Excel |
|----------|-----------------|
| Cổ tức | `=B2*B3` |
| Lợi nhuận giữ lại | `=B2-B2*B3` |
| Tiền sẵn có đầu tư | `=B4-B2*B3` |
| Thiếu hụt | `=MAX(0,B5-(B4-B2*B3))` |
| Tiền thừa | `=MAX(0,(B4-B2*B3)-B5)` |
| Tốc độ tăng trưởng bền vững | `=ROE*(1-B3)` |

### 3. Mẫu nội dung nghị quyết/đề xuất chính sách cổ tức (Template)

```
ĐỀ XUẤT CHÍNH SÁCH CỔ TỨC NĂM ........

1. Căn cứ: Lợi nhuận sau thuế: ..... triệu; FCF: ..... triệu; Quỹ đã trích lập: .....
2. Nhu cầu đầu tư: Dự án ....., vốn ..... triệu, NPV ..... triệu
3. Mức đề xuất: Cổ tức nền ..... đ/CP + bổ sung ..... % lợi nhuận sau thuế
4. Hình thức: □ Tiền mặt  □ Cổ phiếu  □ Kết hợp
5. Thời điểm: Ngày chốt danh sách ....., ngày thanh toán .....
6. Kiểm tra điều kiện: □ Đã bù lỗ  □ Đã trích quỹ  □ Còn thanh toán đủ nợ đến hạn  □ Không vi phạm covenant
7. Stress test: Khi lợi nhuận −30%, cổ tức nền vẫn được đảm bảo (FCF coverage ..... lần)
8. Phê duyệt: HĐQT ..... / ĐHĐCĐ .....
```

---

## VI. BÀI TẬP THỰC HÀNH

### Bài 1 (Cơ bản – Chỉ số cổ tức)
Công ty có lợi nhuận sau thuế 5.000 triệu, chia cổ tức 2.000 triệu, 2.000.000 CP, giá thị trường 25.000đ/CP, ROE 18%. Tính EPS, DPS, Payout Ratio, Retention Ratio, Dividend Yield, P/E và tốc độ tăng trưởng bền vững.

*(Đáp số đã verify bằng Python: EPS = 2.500đ, DPS = 1.000đ, Payout = 40%, Retention = 60%, Yield = 4,0%, P/E = 10, g = 18% × 60% = 10,8%)*

### Bài 2 (Cơ bản – Homemade Dividend của M&M)
Công ty có giá 20.000đ/CP, chia cổ tức 3.000đ/CP. Nhà đầu tư giữ 100 CP. (a) Tính giá sau cổ tức, tổng tài sản của nhà đầu tư trước và sau. (b) Nếu nhà đầu tư không muốn nhận tiền mặt, anh ta nên làm gì? (c) Giải thích bằng lời tại sao kết quả hỗ trợ M&M.

*(Đáp số đã verify bằng Python: giá sau = 17.000đ; tổng tài sản = 300.000 + 1.700.000 = 2.000.000đ; mua thêm 300.000 / 17.000 ≈ 17,6 CP)*

### Bài 3 (Trung bình – Thuế cổ tức vs thuế chuyển nhượng)
Một cổ đông cá nhân cần 190 triệu tiền mặt sau thuế. (a) Nếu lấy từ cổ tức (thuế 5%), cổ tức gộp cần là bao nhiêu? (b) Nếu bán cổ phiếu đã niêm yết (thuế 0,1% giá bán), cần bán bao nhiêu? (c) Khi nào lợi thế thuế của (b) biến mất?

*(Đáp số đã verify bằng Python: (a) 190 / 0,95 = 200 triệu; (b) 190 / 0,999 ≈ 190,19 triệu; (c) khi cổ phần chưa niêm yết/thanh khoản thấp, chiết khấu thanh khoản và chi phí tìm người mua lớn hơn mức tiết kiệm thuế khoảng 9,8 triệu)*

### Bài 4 (Trung bình – Mô hình Lintner)
Tỷ lệ chi trả mục tiêu 50%, $c$ = 0,4, cổ tức năm trước 1.200đ/CP, EPS năm nay 4.000đ, năm sau 5.000đ, năm thứ ba giảm còn 2.800đ. Tính cổ tức mỗi năm. Nhận xét payout ở năm thứ ba.

*(Đáp số đã verify bằng Python: 1.520đ; 1.912đ; 1.707đ; payout năm 3 = 1.707 / 2.800 ≈ 61%. Cổ tức "dính" nên payout tăng vọt dù EPS giảm.)*

### Bài 5 (Nâng cao – Buyback vs Dividend)
Công ty có lợi nhuận 4.000 triệu, 2.000.000 CP, giá 40.000đ (P/E = 20). DN muốn trả lại 2.000 triệu cho cổ đông. (a) Phương án cổ tức: DPS và giá sau cổ tức? (b) Phương án mua lại: số CP mua, EPS mới, giá cổ phiếu mới? (c) P/E mới là bao nhiêu và vì sao EPS tăng mà giá không tăng?

*(Đáp số đã verify bằng Python: (a) DPS = 1.000đ, giá ex = 39.000đ, tổng = 40.000đ; (b) mua 50.000 CP, còn 1.950.000 CP, EPS = 2.051,3đ, giá = (80.000 − 2.000) triệu / 1.950.000 = 40.000đ; (c) P/E = 19,5 – giảm vì giá không đổi mà EPS tăng; tiền đã rời DN nên vốn hóa giảm tương ứng.)*

### Bài 6 (Nâng cao – Mini Case: Gốm sứ "Bát Tràng Xanh")
Công ty có lợi nhuận sau thuế 1.800 triệu, 600.000 CP, vốn chủ sổ sách 9.000 triệu, FCF trước cổ tức 1.700 triệu, $K_e$ = 16%. Dự án mở rộng lò nung cần 1.200 triệu, tạo thêm lợi nhuận sau thuế 240 triệu/năm (vĩnh viễn). (a) Tính ROIC và NPV dự án. (b) Cổ tức tối đa có thể chia mà không phải vay? (c) Tính DPS, payout, thuế 5%, và hệ số bao phủ FCF. (d) Tính $g$ bền vững tương ứng. (e) Nếu NI giảm 30%, đề xuất cơ cấu nền + thưởng để cổ tức không cắt quá 15%.

*(Đáp số đã verify bằng Python: (a) ROIC = 20%, NPV = 240/0,16 − 1.200 = +300 triệu; (b) 1.700 − 1.200 = 500 triệu; (c) DPS = 833đ, payout = 27,8%, thuế = 25 triệu, bao phủ = 1.700/500 = 3,4 lần; (d) g = 20% × 72,2% ≈ 14,4%; (e) gợi ý: NI kịch bản xấu = 1.260 triệu; ví dụ nền 300 triệu + 11% NI → bình thường 498 triệu, xấu 438,6 triệu (giảm khoảng 12,0%, trong ngưỡng 15%) – học viên tự kiểm tra bằng Excel và đề xuất phương án khác.)*

### Bài 7 (Nâng cao – Áp dụng cho doanh nghiệp của chính bạn)
Áp dụng toàn bộ quy trình 6 bước ở mục IV.2 và các bước tính của Case III.3 (Hương Quê) cho doanh nghiệp/ý tưởng của bạn: tính FCF, xác định dự án NPV>0, so sánh tối thiểu 3 chính sách, nêu nhu cầu từng cổ đông, thực hiện stress test −30%, rồi đưa ra khuyến nghị có văn bản hóa.

---

## PHỤ LỤC: CHECKLIST DIVIDEND POLICY TỔNG HỢP

### 1. Bảng công thức tổng hợp

| Công thức | Ý nghĩa/Dùng để |
|-----------|-----------------|
| $\text{Net Income} = \text{Dividends} + \text{Retained Earnings}$ | Phân chia lợi nhuận |
| $\text{Payout} = \dfrac{DPS}{EPS}$; $b = 1 - \text{Payout}$ | % lợi nhuận chia / giữ lại |
| $\text{Dividend Yield} = \dfrac{D_{annual}}{P_0}$ | Tỷ suất cổ tức đối với nhà đầu tư |
| $\text{Coverage} = \dfrac{FCF}{Dividends}$ | Cổ tức có bền vững bằng dòng tiền không |
| $g = ROE \times (1 - \text{Payout})$ | Tăng trưởng bền vững |
| $P_0 = \dfrac{D_1}{K_e - g}$ (Gordon, $g < K_e$) | Định giá theo cổ tức |
| $K_e = \dfrac{D_1}{P_0} + g$ | Chi phí vốn chủ theo Gordon |
| $\text{Buyback Yield} = \dfrac{Buybacks}{Market\ Cap}$ | Mua lại cổ phiếu / vốn hóa |
| $\text{Total Yield} = \text{Div Yield} + \text{Buyback Yield}$ | Tổng lợi suất trả cho cổ đông |
| $\Delta D_t = c \times (\text{Payout}^{*} \times EPS_t - D_{t-1})$ | Mô hình Lintner |
| $\text{Dividend (Residual)} = NI - (1 - D/V) \times \text{Capex}$ | Cổ tức phần dư |
| $\text{Giá ex-div} = \text{Giá cum-div} - D$ | Giá điều chỉnh sau cổ tức |

### 2. Checklist

```
PHÂN TÍCH:
□ Payout ratio hiện tại so với DN cùng ngành?
□ Payout bền vững (cổ tức < FCF, coverage > 1,5 lần)?
□ Có cơ hội tăng trưởng (dự án NPV > 0) không?
□ Tiền mặt dự trữ đủ sau khi chia cổ tức?
□ Đã hiểu cơ cấu cổ đông (ai cần tiền mặt, ai cần tăng trưởng)?
□ Đã đánh giá tác động thuế (5% VN) lên từng nhóm cổ đông?

QUYẾT ĐỊNH:
□ Đã xác định giai đoạn vòng đời của DN?
□ Tín hiệu mong muốn là gì? (khởi xướng/tăng/giữ nguyên)
□ Mức cam kết có thoải mái không? (duy trì được 3–5 năm?)
□ Cổ tức hay mua lại cổ phiếu – cái nào phù hợp hơn?
□ Tần suất đã quyết định? (quý/nửa năm/năm)
□ Có cần cổ tức đặc biệt cho khoản tiền dư bất thường?
□ Đã stress test khi lợi nhuận giảm 20–30%?

PHÁP LÝ & THỰC THI:
□ Đã bù lỗ, trích lập quỹ, hoàn thành nghĩa vụ thuế theo điều lệ?
□ Sau khi chia, DN vẫn thanh toán được nợ đến hạn?
□ Hợp đồng vay (covenants) cho phép chia cổ tức?
□ Có nghị quyết ĐHĐCĐ/HĐQT, ngày chốt danh sách, ngày thanh toán rõ ràng?
□ Đã khấu trừ thuế TNCN tại nguồn và nộp đúng hạn?

THEO DÕI:
□ Xu hướng payout có bền vững không?
□ Hệ số bao phủ FCF/cổ tức > 1,5 lần?
□ Đối thủ cùng ngành có thay đổi chính sách?
□ Phản ứng của giá cổ phiếu/cổ đông với chính sách?
□ Đã ghi nhận phản hồi cổ đông và rà soát lại hằng năm?
```

---

*Tài liệu tham khảo: Miller & Modigliani "Dividend Policy" (1961); Lintner "Distribution of Incomes" (1956); Black "The Dividend Puzzle" (1976); Brealey, Myers & Allen 14th Ed; DeAngelo & DeAngelo "Dividend Policy" Handbook*
