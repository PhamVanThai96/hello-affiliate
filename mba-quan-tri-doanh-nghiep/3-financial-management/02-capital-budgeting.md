# Capital Budgeting – Hoạch Định Ngân Sách Vốn

> **Mục tiêu**: Nắm vững bản chất và cách dùng các phương pháp đánh giá dự án đầu tư – NPV, IRR, MIRR, Payback, PI – quy trình ước lượng dòng tiền, phân tích rủi ro và ra quyết định phân bổ vốn, kèm case study chi tiết từng bước (kể cả SME Việt Nam).

---

## I. KHÁI NIỆM & LÝ THUYẾT

### 1. Định nghĩa

**Capital Budgeting** (Hoạch định ngân sách vốn / Thẩm định dự án đầu tư) là quy trình **đánh giá và lựa chọn các dự án đầu tư dài hạn** (thường kéo dài trên 1 năm) để quyết định phân bổ nguồn vốn khan hiếm, nhằm tối đa hóa giá trị doanh nghiệp (và giá trị tài sản của chủ sở hữu).

> **"The most important decision a CEO makes is how to allocate capital."** – Warren Buffett

**Câu hỏi cốt lõi**: Với số tiền X đang có (hoặc đi vay), nên mua cái máy này, mở chi nhánh kia, hay không làm gì cả? Làm sao để trả lời bằng **con số** thay vì cảm tính?

### 2. Nguồn gốc lý thuyết

| Học giả | Đóng góp | Năm |
|---------|----------|-----|
| **Irving Fisher** & **Jack Hirshleifer** | Nền tảng của quy tắc NPV; tách bạch quyết định đầu tư (investment) với quyết định tài trợ (financing) | 1930s-1950s |
| **Joel Dean** | Cuốn "Capital Budgeting" – đặt tên và hệ thống hóa lý thuyết | 1951 |
| **Lorie & Savage** | Vấn đề đa nghiệm IRR (multiple IRR) và phân bổ vốn khi bị giới hạn (capital rationing) | 1955 |
| **Stewart Myers** | Tư duy quyền chọn thực (Real Options) trong thẩm định dự án | 1977 |

> **Ghi chú về năm tháng**: các mốc trên là cách các giáo trình tài chính thường trích dẫn; khi dùng vào công trình học thuật nên đối chiếu lại bản gốc.

#### Tại sao lại sinh ra các phương pháp thẩm định? — Bối cảnh lịch sử

Trước thập niên 1950, đa số doanh nghiệp quyết định đầu tư dựa trên **kinh nghiệm** và một thước đo rất thô: *"bao lâu thì thu hồi lại vốn?"* (Payback). Cách này dễ hiểu nhưng có hai lỗ hổng chết người: (1) coi 1 đồng nhận hôm nay bằng 1 đồng nhận sau 5 năm; (2) hoàn toàn bỏ qua dòng tiền sau thời điểm hoàn vốn. Hệ quả: doanh nghiệp bỏ lỡ dự án dài hạn giá trị cao và ưu ái dự án "hoàn vốn nhanh nhưng chết sớm".

Sau khi tài chính doanh nghiệp hiện đại hình thành (Fisher, rồi Dean, Lorie-Savage), nguyên tắc được thống nhất: **một dự án chỉ đáng làm nếu nó tạo ra giá trị hiện tại ròng dương**, tức là dòng tiền nó mang về (đã quy về hiện tại theo chi phí vốn) lớn hơn số tiền bỏ ra. Từ nguyên tắc đó sinh ra NPV (đo trực tiếp), IRR (diễn đạt thành tỷ suất cho dễ giao tiếp), PI (xếp hạng khi thiếu vốn)... Hiểu được chuỗi lý do này giúp bạn không học thuộc lòng công thức mà biết **mỗi công cụ sinh ra để vá lỗ hổng nào**.

### 3. Tại sao Capital Budgeting quan trọng?

| Lý do | Giải thích |
|-------|-----------|
| **Số tiền lớn** | Quyết định hàng tỷ → sai lầm cực tốn kém, khó sửa |
| **Tính không thể đảo ngược (Irreversibility)** | Xây nhà máy xong không "undo" dễ dàng; máy móc chuyên dụng bán lại chỉ được giá rất thấp |
| **Tác động dài hạn** | Ảnh hưởng 5-20 năm, định hình toàn bộ tương lai doanh nghiệp |
| **Chi phí cơ hội (Opportunity cost)** | Đầu tư A = từ bỏ B (vốn khan hiếm) |
| **Lợi thế cạnh tranh** | Đầu tư đúng → có lợi thế; sai → tụt hậu |
| **Giá trị cổ đông** | Mục tiêu cuối: tối đa hóa NPV = tối đa hóa tài sản chủ sở hữu |

### 4. Các loại dự án Capital Budgeting

```
┌─────────────────────────────────────────────────────────────────┐
│                  CÁC LOẠI DỰ ÁN ĐẦU TƯ                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. EXPANSION (Mở rộng)                                        │
│     - Mở nhà máy mới, chi nhánh mới, thị trường mới           │
│     - Ra sản phẩm/dịch vụ mới                                  │
│                                                                 │
│  2. REPLACEMENT (Thay thế)                                      │
│     - Thay máy cũ bằng máy mới hiệu quả hơn                   │
│     - Nâng cấp hệ thống IT, ERP                                │
│                                                                 │
│  3. MANDATORY (Bắt buộc)                                        │
│     - Tuân thủ pháp luật (môi trường, PCCC, an toàn)           │
│     - Không có lựa chọn "không đầu tư"                          │
│                                                                 │
│  4. R&D / INNOVATION                                            │
│     - Nghiên cứu sản phẩm mới, patent                          │
│     - Chuyển đổi số, AI implementation                          │
│                                                                 │
│  5. M&A (Mua lại / Sáp nhập)                                   │
│     - Mua đối thủ, startup, vertical integration                │
│     - Đặc biệt: capital budgeting + valuation                   │
│                                                                 │
│  6. STRATEGIC / EXPLORATORY                                     │
│     - Pilot projects, market entry test                         │
│     - Option value > immediate NPV                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

PHÂN LOẠI THEO QUAN HỆ GIỮA CÁC DỰ ÁN:
• Independent projects (độc lập): Chấp nhận/từ chối riêng từng dự án (NPV > 0 → làm hết)
• Mutually exclusive (loại trừ lẫn nhau): Chọn 1 trong nhiều (chọn NPV cao nhất)
• Contingent (phụ thuộc): Dự án B chỉ làm được nếu có dự án A
```

**Tại sao phải phân loại?** Vì quy tắc ra quyết định thay đổi theo loại. Với dự án **độc lập**, chỉ cần NPV > 0 là làm. Với dự án **loại trừ lẫn nhau**, phải so sánh và chọn một — đây chính là nơi NPV và IRR thường "cãi nhau" (xem mục II.G). Với dự án **bắt buộc** (ví dụ lắp hệ thống xử lý nước thải theo luật), NPV có thể âm nhưng vẫn phải làm; lúc đó bài toán là chọn phương án **chi phí hiện tại ròng thấp nhất**.

### 5. Quy trình 7 bước

```
Bước 1: IDEA GENERATION (Hình thành ý tưởng)
   │  ← R&D, nghiên cứu thị trường, đối thủ, nhân viên
   ▼
Bước 2: PRELIMINARY SCREENING (Sàng lọc sơ bộ)
   │  ← Loại dự án không phù hợp chiến lược
   ▼
Bước 3: CASH FLOW ESTIMATION (Ước lượng dòng tiền)
   │  ← Initial, operating, terminal cash flows
   │  ← Incremental CF, sau thuế, loại sunk cost
   ▼
Bước 4: FINANCIAL ANALYSIS (Phân tích tài chính)
   │  ← NPV, IRR, Payback, PI → Xếp hạng
   ▼
Bước 5: PROJECT SELECTION (Lựa chọn dự án)
   │  ← Ràng buộc vốn, phù hợp chiến lược, rủi ro
   ▼
Bước 6: IMPLEMENTATION (Triển khai)
   │  ← Quản lý dự án, milestone, kiểm soát ngân sách
   ▼
Bước 7: POST-AUDIT (Kiểm toán sau đầu tư)
   ← Thực tế vs Dự phóng → Rút kinh nghiệm
```

**Tại sao Bước 7 (Post-audit) quan trọng nhất mà hay bị bỏ?** Vì đây là bước duy nhất giúp doanh nghiệp *học*. Nếu không so sánh thực tế với dự phóng, mỗi người làm dự báo sẽ tiếp tục lạc quan quá mức (optimism bias) mà không bao giờ bị "hiệu chỉnh". Nhiều tập đoàn buộc người đề xuất dự án phải chịu trách nhiệm với chính dự phóng của mình qua post-audit hằng quý.

### 6. Capital Budgeting trong thời đại số (4.0)

#### Thay đổi trong kỷ nguyên số

| Truyền thống | Thời đại số |
|------------|-------------|
| Dòng tiền tăng tuyến tính | Tăng trưởng hàm mũ / đường cong chữ S |
| Tài sản hữu hình (nhà máy) | Tài sản vô hình (dữ liệu, nền tảng, mạng lưới) |
| Quy mô thị trường đã biết | Thị trường có thể chưa tồn tại |
| Cạnh tranh ổn định | Người thắng lấy phần lớn (winner-take-all/most) |
| Chân trời 5 năm | Thời gian sinh lời 10-15+ năm |
| CAPEX trước rồi OPEX | Nặng OPEX (cloud, thuê bao) |

#### Khung điều chỉnh

$$\text{Digital NPV} = NPV_{traditional} + NPV_{network\,effects} + NPV_{data\,asset} + Option\,Value$$

**Tại sao cần điều chỉnh?** NPV truyền thống chỉ đếm dòng tiền "thấy được" của chính dự án. Với nền tảng số, một dự án có thể làm tăng giá trị của các dự án khác (hiệu ứng mạng), tạo ra tài sản dữ liệu dùng lại về sau, và mở ra quyền chọn mở rộng sang thị trường mới. Nếu bỏ qua các thành phần này, NPV truyền thống sẽ **định giá thấp** dự án (xem case AWS ở mục III.1). Tuy nhiên đây là khung tư duy định tính — các thành phần $NPV_{network\,effects}$, $NPV_{data\,asset}$ rất dễ bị "thổi phồng" để biện minh dự án; phải đặt giả định minh bạch và kiểm tra bằng kịch bản.

---

## II. CHI TIẾT TỪNG THÀNH PHẦN

### A. Ước lượng dòng tiền dự án (Cash Flow Estimation)

#### A.1. Tại sao phải dùng dòng tiền, không dùng lợi nhuận kế toán?

Lợi nhuận kế toán chứa các khoản **không phải tiền** (khấu hao) và theo nguyên tắc dồn tích (doanh thu ghi nhận khi bán chịu chưa chắc đã thu tiền). Nhà đầu tư chỉ tiêu được **tiền thật**, và tiền thật nhận sớm có giá trị hơn nhận muộn. Vì vậy thẩm định dự án luôn dựa trên **dòng tiền tự do sau thuế** của dự án, rồi chiết khấu về hiện tại.

#### A.2. Sáu nguyên tắc cốt lõi

| Nguyên tắc | Mô tả | Ví dụ |
|-----------|-------|-------|
| **Incremental CF** (dòng tiền tăng thêm) | Chỉ tính CF THAY ĐỔI do dự án | CF có dự án – CF không có dự án |
| **After-tax** (sau thuế) | Thuế là dòng tiền chảy ra thật | $EBIT \times (1-T) + Dep$ |
| **Include opportunity cost** | Tài sản sẵn có không "miễn phí" | Xưởng trống đang cho thuê 60 triệu/năm → phải tính 60 triệu đó là chi phí của dự án |
| **Exclude sunk cost** (loại chi phí chìm) | Chi phí đã chi dù quyết định thế nào | 500 triệu nghiên cứu đã chi → KHÔNG tính |
| **Include externalities** | Tác động phụ lên dự án khác | Sản phẩm mới "ăn" doanh số sản phẩm cũ (cannibalization) |
| **Ignore financing CF** | Không tính lãi vay, trả nợ gốc | Chi phí vốn đã nằm trong lãi suất chiết khấu (WACC) — tính lại sẽ bị "đếm hai lần" |

**Tại sao loại chi phí chìm?** Vì quyết định đầu tư là quyết định *hướng tới tương lai*. Dù bạn làm hay không làm, khoản chi chìm đã mất rồi và không thể lấy lại; chỉ những dòng tiền **thay đổi theo quyết định** mới liên quan. Đây là gốc của "ngụy biện chi phí chìm" (sunk cost fallacy) khiến Iridium tiếp tục đổ tiền (case III.2).

**Tại sao không tính lãi vay trong dòng tiền?** Vì WACC (xem `03-cost-of-capital.md`) đã phản ánh chi phí của *cả* nợ lẫn vốn chủ. Nếu vừa trừ lãi vay trong dòng tiền vừa chiết khấu theo WACC thì ta "phạt" dự án hai lần.

#### A.3. Dòng tiền hoạt động (Operating Cash Flow – OCF)

$$OCF = EBIT \times (1 - T) + Dep = (Revenue - COGS - OpEx - Dep)\times(1-T) + Dep$$

Khi dự án không có lãi vay: $OCF = \text{Lợi nhuận sau thuế} + Dep$.

**Tại sao cộng lại khấu hao?** Khấu hao là chi phí *kế toán* giúp giảm lợi nhuận chịu thuế, nhưng không có tiền nào chảy ra ngoài trong năm đó (tiền đã chi từ năm 0 khi mua máy). Do đó phải trừ nó khi tính thuế (để hưởng lá chắn thuế) rồi cộng lại khi tính tiền.

#### A.4. Cấu trúc dòng tiền đầy đủ

```
INITIAL INVESTMENT (Năm 0):
  - CAPEX (mua tài sản, xây dựng)
  - Chi phí lắp đặt, vận chuyển, chạy thử
  + Thu từ bán tài sản cũ (nếu thay thế)
  - Thuế trên lãi bán tài sản cũ (hoặc + tiết kiệm thuế nếu lỗ)
  - Tăng Net Working Capital (NWC: vốn lưu động ròng)
  = TOTAL INITIAL OUTFLOW

OPERATING CF (Năm 1 → n):
  = EBIT × (1-Tax) + Depreciation
  - ΔNet Working Capital hàng năm
  - Maintenance CAPEX

TERMINAL CF (Năm cuối):
  + Salvage value (giá trị thu hồi tài sản)
  - Thuế trên phần chênh lệch (giá bán – giá trị sổ sách)
  + Thu hồi NWC
  = TOTAL TERMINAL CF
```

**Tại sao phải có NWC?** Mở rộng kinh doanh thì phải tăng tồn kho và công nợ phải thu (tiền "kẹt" lại trong hoạt động) — đây là dòng tiền chi ra thật ở đầu dự án, và được thu hồi lại khi dự án kết thúc. Nhiều SME quên khoản này nên thiếu tiền mặt ngay tháng thứ 3 dù dự án "có lãi" trên giấy (xem thêm `06-working-capital-management.md`).

#### A.5. Lá chắn thuế khấu hao (Depreciation Tax Shield)

$$\text{Tax Shield} = Dep \times T$$

**Ví dụ**: Máy giá 1 tỷ, khấu hao đường thẳng 5 năm = 200 triệu/năm. Thuế TNDN T = 20%.
→ Tax Shield = 200 × 20% = **40 triệu/năm tiết kiệm thuế**.

**Tại sao gọi là "lá chắn"?** Khấu hao làm lợi nhuận chịu thuế nhỏ lại, nên số thuế nộp giảm đúng bằng $Dep \times T$. Phần thuế "được tiết kiệm" đó là dòng tiền thật thuộc về dự án — vì thế khấu hao tuy không phải tiền nhưng **làm tăng NPV** (khấu hao nhanh hơn → lá chắn đến sớm hơn → giá trị hiện tại lớn hơn).

---

### B. Giá trị hiện tại ròng (Net Present Value – NPV)

#### B.1. Tại sao NPV được coi là "tiêu chuẩn vàng" (Gold Standard)?

NPV trả lời trực tiếp câu hỏi mà chủ doanh nghiệp quan tâm: *"Làm dự án này, tôi giàu thêm bao nhiêu đồng (tính theo tiền hôm nay)?"* Ý tưởng gồm hai bước: (1) quy mọi dòng tiền tương lai về hiện tại bằng chi phí vốn (vì 1 đồng sau này có giá trị thấp hơn 1 đồng hôm nay — cơ hội đầu tư khác và rủi ro); (2) trừ đi vốn bỏ ra. Nếu kết quả dương, dự án sinh ra nhiều hơn mức mà nhà đầu tư đòi hỏi tối thiểu → **tạo thêm giá trị**. NPV còn có tính **cộng được** (additive): NPV(A+B) = NPV(A) + NPV(B), nên cộng giá trị các dự án lại là ra giá trị cả công ty — đặc tính mà IRR không có.

#### B.2. Công thức

$$NPV = \sum_{t=0}^{n} \frac{CF_t}{(1+r)^t} = -C_0 + \frac{CF_1}{(1+r)^1} + \frac{CF_2}{(1+r)^2} + ... + \frac{CF_n}{(1+r)^n}$$

- $CF_t$: dòng tiền ròng của dự án năm $t$ ($CF_0 = -C_0$ là vốn đầu tư ban đầu)
- $r$: tỷ suất chiết khấu = chi phí vốn của dự án (thường là WACC, điều chỉnh theo rủi ro dự án)
- $n$: số năm của dự án

#### B.3. Quy tắc

- **NPV > 0** → Đầu tư (dự án tạo giá trị)
- **NPV < 0** → Từ chối (phá hủy giá trị)
- **NPV = 0** → Hòa vốn về mặt kinh tế (vừa đủ trả chi phí vốn)
- **Nhiều dự án loại trừ nhau** → Chọn NPV cao nhất

#### B.4. Ưu / nhược điểm

- ✅ Tính đến giá trị thời gian của tiền (TVM) và rủi ro (qua $r$)
- ✅ Cộng được; đo trực tiếp lượng giá trị tuyệt đối tạo ra
- ❌ Phụ thuộc vào tỷ suất chiết khấu — chọn $r$ sai thì kết quả sai
- ❌ Dòng tiền dài hạn khó dự báo chính xác

---

### C. Tỷ suất hoàn vốn nội bộ (Internal Rate of Return – IRR)

#### C.1. Tại sao có IRR khi đã có NPV?

NPV cho ra một con số tiền (ví dụ +240 triệu), nhưng nhiều người — nhất là nhà quản lý và ngân hàng — quen nghĩ theo **tỷ lệ phần trăm** ("lãi bao nhiêu %/năm?"). IRR sinh ra để diễn đạt chất lượng dự án thành một tỷ suất, có thể so thẳng với lãi suất vay hay chi phí vốn. Về bản chất IRR là **mức chiết khấu làm NPV bằng 0**; nghĩa là dự án "chịu được" chi phí vốn tối đa bằng IRR. Nếu chi phí vốn thực tế thấp hơn IRR, dự án còn dư địa tạo giá trị.

#### C.2. Công thức

$$0 = -C_0 + \sum_{t=1}^{n} \frac{CF_t}{(1+IRR)^t}$$

(IRR không có công thức đóng; tính bằng thử-sai hoặc hàm `IRR` trong Excel.)

#### C.3. Quy tắc

IRR > WACC (hoặc tỷ suất yêu cầu) → Đầu tư.

#### C.4. Vấn đề đa nghiệm (Multiple IRR)

Khi dòng tiền đổi dấu nhiều lần (ví dụ: bỏ vốn, thu lợi, rồi lại phải chi lớn để phục hồi môi trường cuối dự án), phương trình có thể có nhiều nghiệm.

```
Ví dụ: CF = -100, +230, -132
  Thử IRR = 10%: -100 + 230/1,10 - 132/1,21 = -100 + 209,09 - 109,09 = 0 ✓
  Thử IRR = 20%: -100 + 230/1,20 - 132/1,44 = -100 + 191,67 - 91,67 = 0 ✓
→ Hai IRR (10% và 20%) → không biết tin con số nào!

Giải pháp: Dùng NPV hoặc MIRR.
```

#### C.5. IRR điều chỉnh (Modified IRR – MIRR) và tại sao cần nó

IRR ngầm giả định mọi dòng tiền dương nhận được sẽ được **tái đầu tư với chính mức IRR** — điều phi thực tế khi IRR rất cao (ví dụ 40%). MIRR sửa bằng cách giả định tái đầu tư ở **chi phí vốn** (tỷ lệ thực tế hơn):

$$MIRR = \left(\frac{FV_{\text{dòng tiền dương, ghép lãi đến cuối kỳ ở tỷ suất tái đầu tư}}}{PV_{\text{dòng tiền âm, chiết khấu ở lãi vay}}}\right)^{1/n} - 1$$

- Luôn cho **một** giá trị duy nhất (khắc phục multiple IRR).
- **Ví dụ**: dòng tiền -1.000; 400; 500; 600 (triệu), tái đầu tư 10%/năm. IRR ≈ 21,65%. Ghép lãi dòng dương đến năm 3: $400 \times 1{,}1^2 + 500 \times 1{,}1 + 600 = 484 + 550 + 600 = 1.634$. $MIRR = (1.634/1.000)^{1/3} - 1 \approx 17,78\%$ → thấp hơn IRR vì thực tế hơn.

---

### D. Thời gian hoàn vốn (Payback Period – PP) và Hoàn vốn có chiết khấu (DPP)

#### D.1. Tại sao PP vẫn còn được dùng dù có nhiều nhược điểm?

PP trả lời câu hỏi rất "đời thường": *"Bao lâu tôi lấy lại được vốn?"* Với SME, nó là **thước đo thanh khoản và rủi ro**: dự án hoàn vốn càng nhanh thì càng ít thời gian để rủi ro xảy ra, và tiền được giải phóng sớm để dùng cho việc khác. Vì thế PP nên dùng như **bộ lọc phụ** chứ không phải tiêu chí quyết định chính.

#### D.2. Ví dụ tính PP

| Năm | CF (triệu) | CF tích lũy |
|-----|-----------|-------------|
| 0 | -500 | -500 |
| 1 | +150 | -350 |
| 2 | +150 | -200 |
| 3 | +150 | -50 |
| 4 | +150 | +100 |

$$PP = 3 + \frac{50}{150} = 3{,}33 \text{ năm}$$

(Phần nguyên là năm cuối cùng tích lũy còn âm; phần lẻ = số tiền còn thiếu / dòng tiền năm kế tiếp.)

#### D.3. Nhược điểm nghiêm trọng của PP

- ❌ Bỏ qua giá trị thời gian của tiền
- ❌ Bỏ qua mọi dòng tiền SAU thời điểm hoàn vốn (dự án giá trị lớn về sau bị loại oan)
- ❌ Ngưỡng chấp nhận (ví dụ "phải dưới 3 năm") mang tính tùy ý

#### D.4. Hoàn vốn có chiết khấu (Discounted Payback Period – DPP)

DPP khắc phục lỗ hổng thời gian của tiền: chiết khấu từng dòng tiền về hiện tại **trước** khi tích lũy. Với ví dụ trên, chiết khấu 10% và thêm dòng tiền năm 5 = +150:

| Năm | CF | PV @10% | PV tích lũy |
|-----|----|---------|-------------|
| 0 | -500 | -500,00 | -500,00 |
| 1 | 150 | 136,36 | -363,64 |
| 2 | 150 | 123,97 | -239,67 |
| 3 | 150 | 112,70 | -126,97 |
| 4 | 150 | 102,45 | -24,52 |
| 5 | 150 | 93,14 | +68,62 |

$$DPP = 4 + \frac{24{,}52}{93{,}14} \approx 4{,}26 \text{ năm}$$

→ DPP (4,26 năm) dài hơn PP (3,33 năm) vì tiền nhận về sau bị "giảm giá". Dự án vẫn còn NPV dương nhưng phải sống ít nhất hơn 4,3 năm mới hòa vốn thực sự — thông tin mà PP đơn thuần che giấu. DPP vẫn bỏ qua dòng tiền sau thời điểm hoàn vốn, nên không thay thế được NPV.

---

### E. Chỉ số sinh lời (Profitability Index – PI) và phân bổ vốn khi bị giới hạn

#### E.1. Tại sao cần PI?

NPV cho biết *số tiền* giá trị tạo ra nhưng không cho biết *hiệu quả trên mỗi đồng vốn*. Khi tổng vốn bị giới hạn (**capital rationing** – rất phổ biến ở SME vì hạn mức vay có hạn), ta cần chọn tổ hợp dự án **tối đa hóa tổng NPV trong ngân sách**. PI = "mỗi đồng vốn bỏ ra tạo ra bao nhiêu đồng giá trị hiện tại" nên là công cụ xếp hạng tự nhiên.

$$PI = \frac{PV \text{ of future CF}}{Initial\ Investment} = 1 + \frac{NPV}{C_0}$$

- **PI > 1** → Đầu tư (tương đương NPV > 0).

#### E.2. Ví dụ phân bổ vốn khi ngân sách chỉ có 3.000 triệu

| Dự án | Vốn (triệu) | NPV (triệu) | PI = 1 + NPV/Vốn |
|-------|-------------|-------------|------------------|
| X | 1.500 | 300 | 1,200 |
| Y | 1.200 | 264 | 1,220 |
| Z | 1.000 | 140 | 1,140 |
| W | 800 | 200 | 1,250 |

- **Xếp theo NPV** (X, Y, W, Z): chọn X (1.500) + Y (1.200) = 2.700; không còn đủ cho Z hay W → Tổng NPV = 300 + 264 = **564**.
- **Xếp theo PI** (W, Y, X, Z): W (800) + Y (1.200) = 2.000; X không vừa (cần 1.500 > 1.000 còn lại); Z (1.000) vừa → tổng vốn 3.000; Tổng NPV = 200 + 264 + 140 = **604** > 564.

→ Khi thiếu vốn, xếp hạng theo PI (rồi kiểm tra các tổ hợp) cho kết quả tốt hơn xếp theo NPV. Lưu ý: PI xếp hạng tốt khi dự án chia nhỏ được hoặc kiểm tra tổ hợp; với tổ hợp phức tạp nên dùng quy hoạch nguyên (Solver trong Excel).

---

### F. Dòng tiền tương đương hằng năm (Equivalent Annual Annuity – EAA) khi các dự án có vòng đời khác nhau

#### Tại sao cần EAA?

So sánh NPV của hai dự án có vòng đời khác nhau (ví dụ máy bền 3 năm so với máy bền 5 năm) là **không công bằng**: dự án dài tự nhiên cộng thêm nhiều năm dòng tiền. EAA chuyển NPV thành *dòng tiền đều hằng năm* tương đương, để so sánh "mỗi năm tạo ra bao nhiêu":

$$EAA = \frac{NPV}{\text{PVIFA}(r, n)} = NPV \times \frac{r}{1-(1+r)^{-n}}$$

**Ví dụ** (r = 12%): Máy 1: vốn 300, CF 150/năm × 3 năm → NPV = 150 × 2,4018 – 300 = **60,27**; EAA = 60,27 × 0,4163 = **25,10**/năm. Máy 2: vốn 450, CF 170/năm × 5 năm → NPV = 170 × 3,6048 – 450 = **162,81**; EAA = 162,81 × 0,2774 = **45,17**/năm. → Máy 2 vượt trội cả sau khi quy về cùng đơn vị "mỗi năm" (giả định có thể thay thế máy với cùng điều kiện khi hết vòng đời).

---

### G. Xung đột NPV vs IRR – chọn thế nào?

#### G.1. Tại sao hai phương pháp có thể cho kết luận ngược nhau?

Với dự án **độc lập** và dòng tiền thông thường (âm một lần rồi dương), NPV và IRR luôn cho cùng kết luận Chấp nhận/Từ chối. Nhưng với dự án **loại trừ lẫn nhau**, có hai nguyên nhân gây xung đột:

1. **Quy mô khác nhau (scale)**: IRR là tỷ suất, "mù" quy mô. Dự án nhỏ lãi 50% có thể kém hơn dự án lớn lãi 30% về tiền tuyệt đối.
2. **Thời điểm dòng tiền khác nhau (timing)**: IRR giả định tái đầu tư ở chính IRR; NPV giả định ở chi phí vốn — thực tế hơn.

#### G.2. Cách giải quyết

NPV luôn là phán quyết cuối cùng, vì nó đo trực tiếp giá trị tạo ra và giả định tái đầu tư thực tế. Công cụ chẩn đoán: **IRR gia tăng (incremental IRR)** — tính IRR của dòng tiền *chênh lệch* giữa dự án lớn và dự án nhỏ. Nếu IRR gia tăng > chi phí vốn, khoản đầu tư thêm đáng giá → chọn dự án lớn. Ví dụ đầy đủ ở case SME (mục III.3, bước 9).

---

### H. Bảng tổng hợp so sánh các phương pháp

| Phương pháp | TVM? | Rủi ro? | Quy mô (Scale)? | Dễ hiểu? | Xếp hạng |
|------------|------|---------|-----------------|----------|----------|
| **NPV** | ✅ | ✅ | ✅ | ⚠️ | **#1** |
| **IRR** | ✅ | ✅ | ❌ | ✅ | #2 |
| **MIRR** | ✅ | ✅ | ❌ | ✅ | #2.5 |
| **PI** | ✅ | ✅ | ✅ (tương đối) | ✅ | #3 |
| **Payback** | ❌ | ❌ | ❌ | ✅✅ | Bổ trợ |
| **DPP** | ✅ | ⚠️ | ❌ | ✅ | Bổ trợ |

---

### I. Phân tích rủi ro trong Capital Budgeting

**Tại sao cần phân tích rủi ro?** Mọi dòng tiền trong NPV đều là **dự báo**, không phải sự thật. Một con số NPV duy nhất trông chính xác nhưng che giấu độ bất định. Phân tích rủi ro trả lời: *"Nếu dự báo sai thì NPV thay đổi ra sao, và biến nào đáng lo nhất?"*

#### I.1. Phân tích độ nhạy (Sensitivity Analysis)

Thay đổi MỘT biến, giữ nguyên các biến khác → NPV thay đổi thế nào?

| Biến thay đổi | Base Case | Bi quan | Lạc quan | ΔNPV |
|--------------|-----------|---------|----------|------|
| Doanh thu –20% / +20% | NPV = 124 | NPV = -15 | NPV = 263 | ±139 |
| WACC +3% / -3% | NPV = 124 | NPV = 52 | NPV = 215 | ±82 |
| CAPEX +30% / -30% | NPV = 124 | NPV = -26 | NPV = 274 | ±150 |
| Chi phí hoạt động +15% / -15% | NPV = 124 | NPV = 41 | NPV = 207 | ±83 |

→ **Nhạy nhất**: CAPEX và doanh thu → cần dồn nguồn lực để dự báo chính xác hai biến này. (Bảng minh họa phương pháp, đơn vị: triệu đồng.)

#### I.2. Phân tích kịch bản (Scenario Analysis)

Thay đổi *đồng thời* nhiều biến theo các kịch bản nhất quán (tốt/cơ sở/xấu) và gán xác suất.

| Kịch bản | Xác suất | NPV | NPV có trọng số |
|----------|----------|-----|-----------------|
| Tốt nhất | 25% | +350 tr | +87,5 |
| Cơ sở | 50% | +124 tr | +62,0 |
| Xấu nhất | 25% | -80 tr | -20,0 |
| **NPV kỳ vọng** | | | **+129,5** |

$$E[NPV] = \sum p_i \times NPV_i, \qquad \sigma_{NPV} = \sqrt{\sum p_i \times (NPV_i - E[NPV])^2}$$

Tính độ lệch chuẩn: $\sigma = \sqrt{0{,}25(350-129{,}5)^2 + 0{,}5(124-129{,}5)^2 + 0{,}25(-80-129{,}5)^2} \approx 152{,}1$ triệu.

**Diễn giải**: NPV kỳ vọng +129,5 triệu nhưng độ lệch chuẩn 152,1 triệu (lớn hơn cả kỳ vọng) → dự án sinh lời trung bình, song kết quả dao động rất mạnh; cần cân nhắc khả năng chịu lỗ (-80 triệu ở kịch bản xấu) của doanh nghiệp.

#### I.3. Phân tích hòa vốn (Break-even Analysis)

Tìm giá trị của một biến đầu vào (doanh thu, EBITDA, sản lượng) làm **NPV = 0**. Khoảng cách giữa giá trị dự báo và giá trị hòa vốn là **biên an toàn** (margin of safety). Ví dụ ở case SME III.3: biên an toàn EBITDA khoảng 15-16%.

#### I.4. Quyền chọn thực (Real Options)

| Quyền chọn | Giá trị | Khi nào? |
|-----------|--------|---------|
| **Option to Expand** | Mở rộng nếu dự án thành công | Pilot → Full rollout |
| **Option to Delay** | Chờ thêm thông tin trước khi đầu tư | Thị trường bất định |
| **Option to Abandon** | Dừng & bán tài sản nếu thất bại | Salvage value > tiếp tục |
| **Option to Switch** | Chuyển đổi sản phẩm/công nghệ | Sản xuất linh hoạt |

$$\text{Strategic NPV} = \text{Traditional NPV} + \text{Option Value}$$

**Tại sao Real Options quan trọng?** NPV truyền thống giả định bạn "đóng đinh" kế hoạch từ đầu đến cuối. Nhưng trong thực tế, nhà quản lý *có thể* mở rộng nếu thuận lợi, dừng lại nếu xấu. Quyền chủ động đó có giá trị tài chính (nhất là khi bất định cao) mà NPV bỏ sót. Ví dụ định lượng ở case AWS (III.1).

---

### J. Ưu điểm và nhược điểm của Capital Budgeting

#### ✅ Ưu điểm:
1. **Ra quyết định có hệ thống** – Khung rõ ràng, không dựa cảm tính
2. **Tối đa hóa giá trị** – NPV dương = tăng tài sản cổ đông
3. **Phân bổ hiệu quả** – Vốn khan hiếm → đúng dự án nhất
4. **Trách nhiệm giải trình** – Post-audit giúp cải thiện các quyết định sau
5. **Nhận diện rủi ro** – Phân tích độ nhạy/kịch bản lượng hóa rủi ro
6. **Kỷ luật** – Buộc ban lãnh đạo biện minh khoản đầu tư bằng dữ liệu

#### ❌ Nhược điểm:
1. **Ước lượng dòng tiền khó** – Doanh thu/chi phí 5-10 năm → bất định cao
2. **Tỷ suất chiết khấu không chắc chắn** – WACC thay đổi, rủi ro dự án khó đo
3. **Bỏ qua yếu tố vô hình** – Giá trị chiến lược, thương hiệu, tri thức khó lượng hóa
4. **Thiên lệch lạc quan (Optimism bias)** – Người đề xuất thổi phồng dự phóng để dự án được duyệt
5. **Bỏ sót Real Options** – NPV truyền thống bỏ qua giá trị linh hoạt
6. **Áp lực ngắn hạn** – Ưa thích Payback → bỏ lỡ giá trị dài hạn
7. **Tư duy "ốc đảo" (Silo)** – Đánh giá từng dự án riêng lẻ, bỏ qua hiệu ứng danh mục

---

## III. CASE STUDIES THỰC TẾ

### 1. Case Study Thành công: Amazon AWS – Capital Budgeting Táo Bạo

#### Bối cảnh

- Giai đoạn đầu-giữa thập niên 2000: Amazon đầu tư mạnh vào hạ tầng điện toán đám mây (dịch vụ S3 ra mắt năm 2006) — tức là đầu tư hàng tỷ USD vào một thị trường gần như chưa tồn tại.
- Độ bất định cực cao: không có dữ liệu về quy mô thị trường, không có khách hàng mẫu ngoài chính Amazon.
- Câu hỏi của hội đồng quản trị: dùng tiền cho thương mại điện tử (đã chứng minh) hay cho hạ tầng (chưa chứng minh)?

> **Lưu ý về độ tin cậy số liệu**: bảng dòng tiền dưới đây là **mô hình giả lập minh họa** cách tư duy capital budgeting, không phải số liệu nội bộ của Amazon. Số liệu kết quả (doanh thu, lợi nhuận AWS) lấy từ báo cáo công khai nhưng đã làm tròn; cần đối chiếu lại báo cáo thường niên mới nhất khi trích dẫn.

#### Phân tích Capital Budgeting (giả lập)

| Năm | Hạng mục | CF (triệu USD) |
|-----|----------|----------------|
| 0-2 | CAPEX trung tâm dữ liệu | -$3.000 |
| 1-3 | Lỗ hoạt động | -$1.500 |
| 4-5 | Hòa vốn, doanh thu tăng tốc | +$500 → +$2.000 |
| 6-8 | Dẫn đầu thị trường, mở rộng quy mô | +$5.000 → +$15.000 |
| 10+ | Thống trị, mở rộng biên lợi nhuận | +$25.000/năm |

NPV (r = 12%, 10 năm) kỳ vọng lớn hơn rất nhiều +$50 tỷ; IRR vượt xa 35% **nếu kịch bản thành công xảy ra**. Nhưng điểm mấu chốt: tại thời điểm quyết định, **không ai biết trước** kịch bản đó có xảy ra không — nên cách phân tích đúng không phải là một NPV duy nhất.

#### Phân tích định lượng: giá trị của "quyền chọn" (minh họa)

Thay vì đặt cược toàn bộ, coi khoản đầu tư ban đầu là **mua một quyền chọn mở rộng**. Giả sử (giả định minh họa):
- Chi phí giai đoạn thử nghiệm/xây nền: $3.000 triệu, và bản thân dòng tiền giai đoạn này không đem lại lãi (NPV độc lập ≈ -$3.000).
- Xác suất thị trường đám mây bùng nổ: 30%. Nếu bùng nổ, giá trị mở rộng toàn diện có NPV +$20.000 triệu tại năm 4.
- Chiết khấu 12%: PV = 20.000 / 1,12⁴ = 20.000 / 1,5735 ≈ **$12.710 triệu**.

$$E[\text{giá trị}] = 0{,}30 \times 12.710 - 3.000 \approx +\$813 \text{ triệu}$$

- **Xác suất hòa vốn của quyền chọn** = 3.000 / 12.710 ≈ **23,6%**: chỉ cần thị trường có hơn ~24% khả năng bùng nổ là khoản cược đáng làm.
- Nếu thất bại: mất tối đa $3.000 triệu (có giới hạn). Nếu thành công: lãi nhiều lần (không giới hạn trên) → **tương quan lợi nhuận bất đối xứng**.

→ NPV "một đường thẳng" với giả định thận trọng có thể âm, nhưng NPV chiến lược (cộng giá trị quyền chọn) lại dương. Đây chính là công thức $\text{Strategic NPV} = \text{Traditional NPV} + \text{Option Value}$.

#### Kết quả thực tế (số liệu công khai, làm tròn, ~năm tài chính 2024)

- Doanh thu AWS: khoảng **$100 tỷ+/năm**
- Lợi nhuận hoạt động: khoảng **$37-40 tỷ** (biên khoảng 37%)
- AWS đóng góp phần lớn lợi nhuận hoạt động của Amazon (khoảng 60%+)
- Thị phần đám mây toàn cầu: khoảng **30%** (vị trí số 1)
- Giá trị ngụ ý: hàng trăm tỷ USD (ước tính phân tích, không phải con số niêm yết)

#### Bài học Capital Budgeting

1. **Real Options khổng lồ**: $3 tỷ ban đầu = "mua quyền chọn" trên toàn thị trường đám mây. Thất bại: mất $3 tỷ. Thắng: lãi hàng trăm tỷ. Lợi nhuận bất đối xứng!
2. **NPV truyền thống đánh giá thấp**: ước lượng bảo thủ → NPV có thể âm; cộng giá trị chiến lược + quyền chọn → dương rất lớn.
3. **Post-audit & lặp lại**: liên tục thêm dịch vụ → giá trị cộng dồn.
4. **Cần dũng khí**: tầm nhìn CEO + quyết tâm đầu tư bất chấp nỗi đau ngắn hạn.
5. **Cẩn trọng với "hiệu ứng người sống sót"**: AWS là trường hợp thắng; không phải mọi khoản cược kiểu này đều thành công. Bài học là *cách cấu trúc quyết định* (có xác suất hòa vốn, có giới hạn thua lỗ, đầu tư theo giai đoạn), không phải "cứ liều là thắng".

---

### 2. Case Study Thất bại: Iridium Satellite – $5 tỷ Capital Budgeting Thảm họa

#### Bối cảnh

- Cuối thập niên 1980 đến 1998: Motorola và các đối tác đầu tư khoảng **5 tỷ USD** vào chòm 66 vệ tinh quỹ đạo thấp (LEO) để cung cấp điện thoại toàn cầu, kể cả nơi chưa có sóng di động.
- Ý tưởng được phê duyệt khi mạng di động mặt đất còn rất hạn chế. Dự án thường được coi là một trong những thất bại capital budgeting kinh điển nhất lịch sử.

#### Phân tích NPV tại thời điểm phê duyệt vs thực tế

| Giả định | Dự phóng (theo các nguồn thường trích dẫn) | Thực tế |
|----------|-------------------------------------------|---------|
| Số thuê bao mục tiêu | Hàng triệu thuê bao (thường trích ~5 triệu vào khoảng 2000) | Khoảng 55.000 khi phá sản |
| Giá máy | Kỳ vọng giảm theo thời gian | Khoảng $3.000/máy; cước gọi vài USD/phút |
| CAPEX | ~$3,4 tỷ | ~$5 tỷ (vượt khoảng 47%) |
| Thời điểm có lãi | Khoảng 2001 | KHÔNG BAO GIỜ |
| NPV (r = 15%) | Dương hàng tỷ USD (ước tính) | Âm hàng tỷ USD |

> **Lưu ý độ tin cậy số liệu**: các con số dự phóng (5 triệu thuê bao, CAPEX 3,4 tỷ, NPV +8 tỷ) được trích dẫn trong nhiều giáo trình/case nhưng không thống nhất giữa các nguồn; dùng như số liệu *minh họa*. Một số bản trước đây ghi nhầm "doanh thu/thuê bao/tháng $3.000" – thực ra $3.000 là **giá máy**, không phải doanh thu hằng tháng.

#### Tại sao Capital Budgeting sai?

| Nguyên nhân | Chi tiết |
|------------|---------|
| **Bỏ qua thay đổi công nghệ** | Mạng di động mặt đất phủ sóng nhanh hơn dự kiến, máy rẻ hơn nhiều → Iridium lỗi thời gần như TRƯỚC khi ra mắt |
| **Ngụy biện chi phí chìm** | Đã đầu tư hàng tỷ USD → "Phải tiếp tục" → đổ thêm tiền vào khoản lỗ |
| **Không có phân tích kịch bản** | Không xét kỹ "Nếu di động mặt đất thắng thì sao?" |
| **Vượt CAPEX** | $3,4 tỷ → $5 tỷ (+47%). Không có dự phòng (contingency) |
| **Nghiên cứu thị trường yếu** | Số thuê bao kỳ vọng quá lớn; thực tế máy to, đắt, không dùng được trong nhà |
| **Thiếu linh hoạt** | 66 vệ tinh đã cam kết – không thể dừng/điều chỉnh giữa chừng |
| **Thiên lệch lạc quan** | Các kỹ sư/lãnh đạo tin vào công nghệ của mình quá mức |

#### Minh họa định lượng: bao nhiêu thuê bao mới hòa vốn?

Giả sử (giả định minh họa) tổng vốn $5.000 triệu, chi phí vốn 15%, vòng đời 10 năm. Hệ số hiện giá niên kim $PVIFA(15\%,10) = \frac{1-1{,}15^{-10}}{0{,}15} \approx 5{,}0188$.

$$\text{Dòng tiền ròng cần mỗi năm} = \frac{5.000}{5{,}0188} \approx \$996 \text{ triệu/năm}$$

Nếu mỗi thuê bao đóng góp dòng tiền ròng giả định $1.500/năm → số thuê bao cần = 996 triệu / 1.500 ≈ **664.000** — gấp khoảng **12 lần** so với 55.000 thực tế. Chỉ riêng phép tính hòa vốn đơn giản này đã cho thấy dự án cần thị trường lớn hơn thực tế rất nhiều: một bài kiểm tra **break-even** có thể đã phát hiện vấn đề sớm.

#### Kết quả

- Năm 1999: nộp đơn phá sản Chapter 11 (chỉ khoảng 9 tháng sau khi ra mắt thương mại cuối 1998).
- Tài sản bị bán cho nhà đầu tư mới với giá khoảng **25 triệu USD** (chỉ ~0,5% chi phí đầu tư).
- Motorola ghi nhận khoản lỗ/xóa sổ khoảng $2,6 tỷ (theo báo cáo thường trích).

#### Bài học từ thất bại

```
1. STAGE-GATE PROCESS: Không cam kết toàn bộ $5B ngay từ đầu
   → Chia giai đoạn, rà soát mỗi cổng

2. REAL OPTIONS THINKING: Có quyền chọn từ bỏ ở mỗi cổng
   → Dừng sớm nếu giả định sai

3. COMPETITIVE DYNAMICS: Capital budgeting PHẢI xét
   phản ứng của đối thủ & công nghệ thay thế

4. SUNK COST DISCIPLINE: "Đã tiêu $2B" ≠ lý do để tiếp tục
   → Chỉ đánh giá NPV HƯỚNG TỚI TƯƠNG LAI

5. POST-AUDIT CULTURE: Theo dõi giả định hằng quý
   → Nếu thuê bao << dự phóng → DỪNG

6. INDEPENDENT REVIEW: Kỹ sư quá lạc quan về công nghệ của mình
   → Cần kiểm chứng thị trường độc lập
```

#### So sánh AWS vs Iridium

| Tiêu chí | AWS (Thành công) | Iridium (Thất bại) |
|----------|------------------|--------------------|
| Thời điểm thị trường | Đúng (nhu cầu đám mây tăng) | Sai (di động mặt đất triệt tiêu nhu cầu) |
| Giải pháp thay thế | Chưa có giải pháp cạnh tranh tương đương | Mạng di động = rẻ và tốt hơn |
| Tính linh hoạt | Mô-đun (thêm dịch vụ dần) | Cam kết cứng (66 vệ tinh) |
| Cam kết vốn | Đầu tư theo giai đoạn | $5B khóa ngay từ đầu |
| Kiểm chứng nhu cầu | Dùng nội bộ trước (Amazon.com) | Gần như không kiểm chứng trước khi chi |
| Phản ứng cạnh tranh | Người đi đầu, không có sản phẩm thay thế | Các nhà mạng hạ giá |
| Post-audit | Theo dõi liên tục | Bỏ qua tín hiệu cảnh báo |

---

### 3. Case Study SME: Công ty In ấn & Bao bì "Minh Tâm" chọn máy in – bài toán hai dự án loại trừ nhau

#### Bối cảnh doanh nghiệp

Công ty TNHH In ấn & Bao bì Minh Tâm (Long An) sản xuất hộp giấy cho các cơ sở thực phẩm, đã hoạt động 6 năm. Do đơn hàng tăng, ban giám đốc cần mua thêm **một máy in** (chỉ mua một trong hai, tức hai dự án **loại trừ lẫn nhau**):

- **Máy A** (bán tự động): vốn mua 1.500 triệu.
- **Máy B** (tự động hoàn toàn): vốn mua 2.400 triệu, công suất và tiết kiệm nhân công lớn hơn.

**Dữ kiện chung**
- Vòng đời phân tích: 5 năm; khấu hao đường thẳng về 0 trong 5 năm.
- Thuế TNDN T = 20%.
- Chi phí vốn của doanh nghiệp (WACC, đã tính trong bài `03-cost-of-capital.md`) r = **12%/năm**.
- Chi phí khảo sát 40 triệu đã chi trước khi ra quyết định là **chi phí chìm** → không đưa vào phân tích.
- EBITDA tăng thêm (đã trừ nhân công, nguyên liệu, và chi phí cơ hội sử dụng xưởng trống; chưa trừ khấu hao):

| | Máy A | Máy B |
|---|---|---|
| Vốn đầu tư máy | 1.500 | 2.400 |
| Vốn lưu động (NWC) tăng thêm cần ở năm 0 (thu hồi cuối năm 5) | 100 | 150 |
| EBITDA tăng thêm mỗi năm (năm 1-5) | 520 | 820 |
| Giá bán lại máy cuối năm 5 (giá trị sổ sách = 0) | 150 | 240 |

Đơn vị: triệu đồng.

**Câu hỏi**: Chọn máy nào? NPV, IRR, PI có cho cùng đáp án không? Phương án nào chịu được rủi ro tốt hơn?

#### Bước 1: Dòng tiền đầu tư ban đầu (Năm 0)

Khoản chi năm 0 = Vốn mua máy + Vốn lưu động tăng thêm:
- Máy A: 1.500 + 100 = **1.600** triệu
- Máy B: 2.400 + 150 = **2.550** triệu

#### Bước 2: Dòng tiền hoạt động hằng năm (OCF, năm 1-5)

Quy trình: Khấu hao = Vốn máy / 5 → EBIT = EBITDA – Khấu hao → Thuế = 20% × EBIT → NOPAT = EBIT – Thuế → OCF = NOPAT + Khấu hao.

| Khoản mục (triệu đồng/năm) | Máy A | Máy B |
|---|---|---|
| EBITDA | 520 | 820 |
| (–) Khấu hao (1.500/5 ; 2.400/5) | 300 | 480 |
| = EBIT | 220 | 340 |
| (–) Thuế 20% | 44 | 68 |
| = NOPAT (EBIT sau thuế) | 176 | 272 |
| (+) Khấu hao | 300 | 480 |
| **= OCF** | **476** | **752** |

Kiểm tra bằng công thức khác: Máy A: OCF = EBITDA×(1–T) + Dep×T = 520×0,8 + 300×0,2 = 416 + 60 = 476 ✓. Máy B: 820×0,8 + 480×0,2 = 656 + 96 = 752 ✓. Trong đó lá chắn thuế khấu hao: A = 60/năm, B = 96/năm.

#### Bước 3: Dòng tiền kết thúc dự án (Terminal CF, năm 5)

Giá trị sổ sách bằng 0 nên toàn bộ giá bán lại là lãi chịu thuế 20%:
- Máy A: 150 × (1 – 0,2) + 100 (thu hồi NWC) = 120 + 100 = **220**
- Máy B: 240 × (1 – 0,2) + 150 = 192 + 150 = **342**

#### Bước 4: Bảng dòng tiền tổng hợp

| Năm | Máy A | Máy B |
|---|---|---|
| 0 | -1.600 | -2.550 |
| 1 | 476 | 752 |
| 2 | 476 | 752 |
| 3 | 476 | 752 |
| 4 | 476 | 752 |
| 5 | 476 + 220 = 696 | 752 + 342 = 1.094 |

#### Bước 5: Tính NPV (r = 12%)

Hệ số chiết khấu: 1/1,12 = 0,8929; 1/1,12² = 0,7972; 1/1,12³ = 0,7118; 1/1,12⁴ = 0,6355; 1/1,12⁵ = 0,5674.

| Năm | PV Máy A | PV Máy B |
|---|---|---|
| 0 | -1.600,00 | -2.550,00 |
| 1 | 476 / 1,12 = 425,00 | 752 / 1,12 = 671,43 |
| 2 | 476 / 1,12² = 379,46 | 752 / 1,12² = 599,49 |
| 3 | 476 / 1,12³ = 338,81 | 752 / 1,12³ = 535,26 |
| 4 | 476 / 1,12⁴ = 302,51 | 752 / 1,12⁴ = 477,91 |
| 5 | 696 / 1,12⁵ = 394,93 | 1.094 / 1,12⁵ = 620,76 |
| **Tổng PV dòng tiền tương lai** | **1.840,71** | **2.904,85** |
| **NPV** | **+240,71** | **+354,85** |

Cả hai đều NPV > 0 (tạo giá trị); **B cao hơn A khoảng 114 triệu**.

#### Bước 6: Tính IRR

IRR là mức r làm NPV = 0 (tính bằng hàm `=IRR()` hoặc thử-sai):
- Máy A: **IRR ≈ 17,60%**. Kiểm tra: tại r = 18% NPV ≈ –15,3 (đã âm) và tại r = 15% NPV = +105,0 → nghiệm nằm giữa, gần 17,6%.
- Máy B: **IRR ≈ 17,19%**. Kiểm tra: tại r = 18% NPV ≈ –48,9; tại r = 15% NPV = +140,9.

→ **IRR(A) 17,60% > IRR(B) 17,19%** — IRR chọn A, NPV chọn B: có **xung đột**.

#### Bước 7: Tính PI

$$PI_A = \frac{1.840{,}71}{1.600} = 1{,}150 \qquad PI_B = \frac{2.904{,}85}{2.550} = 1{,}139$$

→ PI cũng nghiêng về A (1,150 > 1,139), cùng hướng với IRR vì cả hai là thước đo *tỷ lệ*.

#### Bước 8: Payback và Discounted Payback

Dòng tiền tích lũy (chưa chiết khấu) cuối năm 3: A = –172; B = –294.

$$PP_A = 3 + \frac{172}{476} \approx 3{,}36 \text{ năm} \qquad PP_B = 3 + \frac{294}{752} \approx 3{,}39 \text{ năm}$$

Dòng tiền chiết khấu tích lũy cuối năm 4: A = –154,22; B = –265,91 (PV năm 5: A = 394,93; B = 620,76).

$$DPP_A = 4 + \frac{154{,}22}{394{,}93} \approx 4{,}39 \text{ năm} \qquad DPP_B = 4 + \frac{265{,}91}{620{,}76} \approx 4{,}43 \text{ năm}$$

→ Hai máy gần như tương đương về tốc độ hoàn vốn; PP/DPP không phân định được.

#### Bước 9: Giải quyết xung đột bằng IRR gia tăng (Incremental IRR) và đồ thị NPV

**Dòng tiền chênh lệch (B – A)**: Năm 0: –2.550 – (–1.600) = **–950**; năm 1-4: 752 – 476 = **+276** mỗi năm; năm 5: 1.094 – 696 = **+398**.

NPV của khoản đầu tư thêm (r = 12%) = –950 + 276×(0,8929+0,7972+0,7118+0,6355) + 398×0,5674 ≈ **+114,14** (bằng đúng chênh lệch NPV giữa B và A ✓). **IRR gia tăng ≈ 16,50%** > 12%.

Bảng NPV theo mức chiết khấu (đồ thị NPV – "NPV profile"):

| r | NPV Máy A | NPV Máy B |
|---|---|---|
| 0% | 1.000,0 | 1.552,0 |
| 5% | 633,2 | 973,7 |
| 10% | 341,0 | 513,0 |
| **12%** | **240,7** | **354,9** |
| 15% | 105,0 | 140,9 |
| 16,5% | ≈ NPV hai máy bằng nhau (điểm giao – Crossover) | |
| 20% | –88,1 | –163,6 |

**Diễn giải**: Hai đường NPV cắt nhau tại r ≈ 16,5% (chính là IRR gia tăng). Nếu chi phí vốn **thấp hơn 16,5%** (như 12% của Minh Tâm) thì B có NPV cao hơn; nếu chi phí vốn **cao hơn 16,5%** thì A thắng. Vì IRR gia tăng (16,5%) cao hơn nhiều so với 12%, khoản **950 triệu đầu tư thêm** để lên Máy B vẫn sinh lời cao hơn chi phí vốn → đáng làm. IRR(A) cao hơn chỉ vì A là dự án *nhỏ hơn*, nên tỷ suất cao nhưng tổng giá trị tạo ra thấp hơn.

#### Bước 10: Phân tích độ nhạy (NPV, triệu đồng, r = 12% trừ khi nêu khác)

| Biến thay đổi (các biến khác giữ nguyên) | Máy A | Máy B |
|---|---|---|
| Base case | +240,7 | +354,9 |
| EBITDA –10% | +90,8 | +118,4 |
| EBITDA –20% | **–59,2** | **–118,1** |
| CAPEX máy +20% (NWC giữ nguyên) | –16,0 | –55,9 |
| Không bán lại được máy (giá thu hồi = 0) | +172,6 | +245,9 |
| WACC = 15% | +105,0 | +140,9 |
| WACC = 18% | –15,3 | –48,9 |

#### Bước 11: Phân tích hòa vốn EBITDA (NPV = 0)

Giải ngược bằng Goal Seek: EBITDA hòa vốn của Máy A ≈ **436,5** triệu/năm (thấp hơn dự báo 520 khoảng **16,1%**); của Máy B ≈ **697,0** triệu/năm (thấp hơn dự báo 820 khoảng **15,0%**).

#### Bước 12: Kết luận và khuyến nghị

1. **Quy tắc quyết định**: với dự án loại trừ nhau, NPV là tiêu chí cuối cùng. **Máy B có NPV cao hơn (+354,9 so với +240,7 triệu)** và IRR gia tăng 16,5% > WACC 12% → B tạo thêm ~114 triệu giá trị.
2. **Rủi ro**: B có đòn bẩy hoạt động cao hơn — khi EBITDA giảm 20%, NPV âm sâu hơn (–118,1 so với –59,2) và nhạy hơn với CAPEX vượt dự toán. Biên an toàn của hai máy gần nhau (khoảng 15-16%).
3. **Khuyến nghị**: chọn **Máy B nếu** doanh nghiệp có đơn hàng đã ký/hợp đồng khung cho thấy EBITDA ≥ khoảng 700 triệu/năm khả thi, và có thể huy động thêm 950 triệu với chi phí vốn dưới 16,5%. **Nếu chưa chắc về sản lượng, chọn Máy A** như phương án thận trọng và giữ quyền chọn nâng cấp sau (option to expand).
4. **Bài học phương pháp**: (a) IRR và PI cao không đồng nghĩa dự án tốt hơn khi quy mô khác nhau; (b) luôn tính IRR gia tăng khi NPV và IRR mâu thuẫn; (c) luôn chạy độ nhạy và hòa vốn, vì một con số NPV duy nhất che giấu rủi ro.

---

## IV. ỨNG DỤNG CHO SME

### 1. Đặc thù thẩm định dự án của SME Việt Nam

| Yếu tố | Tập đoàn lớn | SME Việt Nam |
|--------|--------------|--------------|
| Quy mô dữ liệu | Có phòng phân tích, dữ liệu lịch sử dài | Thiếu dữ liệu, dựa nhiều vào ước tính của chủ doanh nghiệp |
| Tiếp cận vốn | Đa dạng nguồn | Chủ yếu vốn tự có và vay ngân hàng có tài sản thế chấp (lãi suất cao hơn) |
| Chi phí vốn $r$ | WACC tính bằng CAPM | Thường lấy theo lãi suất vay + phần bù rủi ro (xem `04-capital-structure.md` mục IV); ví dụ 12-15% |
| Hạn chế vốn (capital rationing) | Ít gặp | **Rất phổ biến** → dùng PI và xếp hạng tổ hợp |
| Thanh khoản | Chịu được dự án dài hạn | Dòng tiền eo hẹp → Payback/DPP là bộ lọc phụ rất hữu ích |

### 2. Quy tắc thực hành cho chủ SME

1. **Dùng NPV làm tiêu chí chính; dùng Payback/DPP làm bộ lọc thanh khoản** (ví dụ: "NPV > 0 VÀ DPP ≤ 60% vòng đời tài sản").
2. **Tỷ suất chiết khấu**: tối thiểu bằng lãi suất vay ngân hàng đang áp dụng cộng một phần bù rủi ro dự án (2-5%); không dùng lãi suất tiết kiệm.
3. **Ước lượng thận trọng**: giảm doanh thu dự báo 10-20% so với kỳ vọng của người đề xuất; tăng CAPEX dự phòng 10-15%.
4. **Không quên NWC** và **chi phí cơ hội** của tài sản/nhân sự sẵn có.
5. **Phân kỳ đầu tư (stage-gate)**: thử một chi nhánh/một dây chuyền trước khi nhân rộng; đặt "tiêu chí dừng" trước khi bắt đầu.
6. **Tách khoản chi phí chìm**: nếu đã trót chi khảo sát, thiết kế, đặt cọc, hãy hỏi *"nếu chưa chi gì, hôm nay tôi có làm không?"*

### 3. Các sai lầm thường gặp của SME

| Sai lầm | Hậu quả | Cách tránh |
|---------|---------|-----------|
| Chỉ nhìn Payback | Bỏ dự án dài hạn tốt, chọn dự án "hoàn vốn nhanh rồi chết" | Luôn tính NPV song song |
| Lẫn lộn lợi nhuận kế toán với dòng tiền | Quên khấu hao, NWC, thuế | Lập bảng dòng tiền năm 0-n |
| Tính lãi vay vào dòng tiền *và* chiết khấu bằng WACC | Đếm hai lần chi phí vốn | Loại lãi vay khỏi dòng tiền dự án |
| Không tính chi phí cơ hội (ví dụ xưởng sẵn có) | Đánh giá quá cao dự án | Ghi giá thuê thị trường vào chi phí |
| So sánh dự án khác vòng đời bằng NPV thuần túy | Thiên lệch dự án dài | Dùng EAA |
| Chọn dự án có IRR cao nhưng quy mô nhỏ | Bỏ lỡ giá trị tuyệt đối | Tính IRR gia tăng, so NPV |
| Không có post-audit | Lặp lại sai lầm dự báo | Đối chiếu thực tế sau 6-12 tháng |

### 4. Ngưỡng tham chiếu để "sanity check"

| Chỉ số | Ngưỡng tham khảo cho SME | Ghi chú |
|--------|--------------------------|---------|
| NPV | > 0 (kèm biên an toàn ≥ 10-15% đối với dự báo doanh thu/EBITDA) | Biên an toàn từ phân tích hòa vốn |
| IRR | ≥ WACC + 3-5% | Dư địa chống sai số dự báo |
| PI | > 1,1 | Khi thiếu vốn, ưu tiên PI cao |
| DPP | ≤ 50-60% vòng đời | Tùy ngành |
| Chi phí vượt dự toán CAPEX | Dự phòng 10-15% | Bài học Iridium (+47%) |

---

## V. TOOLS & TEMPLATES

### 1. Hàm Excel / Google Sheets

| Mục đích | Hàm | Lưu ý |
|----------|-----|-------|
| NPV | `=NPV(r, CF1:CFn) + CF0` | Hàm NPV của Excel mặc định coi dòng đầu tiên là cuối năm 1 → **cộng CF0 riêng** |
| IRR | `=IRR(CF0:CFn)` | Có thể cho nhiều nghiệm; cung cấp `guess` nếu cần |
| MIRR | `=MIRR(CF0:CFn, lãi_vay, tỷ_suất_tái_đầu_tư)` | Luôn ra một nghiệm |
| NPV khi ngày không đều | `=XNPV(r, values, dates)` | Dự án theo ngày thực tế |
| Hệ số hiện giá niên kim | `=PV(r, n, -CF)` | Cho dòng tiền đều |
| Dòng tiền đều tương đương | `=PMT(r, n, -NPV)` | Tính EAA |
| Goal Seek (hòa vốn) | Data → What-If → Goal Seek | Đặt NPV = 0 bằng cách đổi EBITDA |
| Data Table (độ nhạy) | Data → What-If → Data Table | Lập bảng NPV theo 1-2 biến |
| Solver (phân bổ vốn) | Add-in Solver | Chọn tổ hợp dự án (biến nhị phân) tối đa hóa NPV với ràng buộc ngân sách |

### 2. Template bảng tính thẩm định dự án (cấu trúc đơn giản)

```
SHEET 1 – ASSUMPTIONS (ô nhập liệu, tô xanh):
  Vốn đầu tư | Vòng đời | Khấu hao (đường thẳng) | Thuế TNDN | WACC
  EBITDA/Doanh thu - chi phí hằng năm | NWC | Giá bán lại

SHEET 2 – CASH FLOW:
  Năm:             0     1     2    ...   n
  EBITDA                 …
  - Khấu hao             …
  = EBIT                 …
  - Thuế                 …
  = NOPAT                …
  + Khấu hao             …
  - ΔNWC            …    …
  - CAPEX         …
  + Terminal CF                        …
  = FCF           …
  Hệ số chiết khấu   1   1/(1+r)  ...
  PV              …
  Cumulative PV   …

SHEET 3 – OUTPUT: NPV | IRR | MIRR | PI | PP | DPP

SHEET 4 – SENSITIVITY & SCENARIO:
  Data table NPV theo (Doanh thu, CAPEX, WACC) | Best/Base/Worst + xác suất

SHEET 5 – CHECKS:
  Kiểm tra: NPV(hàm) = Σ PV | Tổng khấu hao = Vốn máy | Terminal CF đã gồm thu hồi NWC
```

> Tham khảo thêm cách dựng mô hình tài chính đầy đủ trong `../templates/financial-model-excel-guide.md`.

### 3. Phần mềm / nguồn tham khảo

| Công cụ | Dùng để | Chi phí tham khảo |
|---------|---------|-------------------|
| Microsoft Excel / Google Sheets | Mọi phép tính ở mục V.1 | Có sẵn / miễn phí (Google Sheets) |
| @RISK / Crystal Ball | Mô phỏng Monte Carlo cho NPV | Phí bản quyền (cao – chủ yếu doanh nghiệp lớn) |
| Python (numpy-financial, scipy) | Tự động hóa tính NPV/IRR hàng loạt | Miễn phí |
| Số liệu lãi suất, thuế | Website các ngân hàng, Tổng cục Thuế | Miễn phí (kiểm tra quy định hiện hành) |

---

## VI. BÀI TẬP THỰC HÀNH

### Bài 1 (Cơ bản – Tính NPV, IRR, PP)
Dự án mở thêm 1 quán cà phê: vốn đầu tư 800 triệu; dòng tiền ròng sau thuế 250 triệu/năm trong 5 năm; chi phí vốn 12%. Tính NPV, PI, Payback, Discounted Payback; có đáng đầu tư không?

### Bài 2 (Cơ bản – Hiểu bản chất)
Giải thích bằng lời của bạn: (a) Vì sao khi tính dòng tiền dự án không trừ lãi vay? (b) Vì sao khấu hao – vốn không phải tiền – lại làm tăng NPV? (c) Chi phí nghiên cứu thị trường 30 triệu đã trả trước có nên tính vào dự án không?

### Bài 3 (Trung bình – Dòng tiền sau thuế)
Máy giá 1,2 tỷ, khấu hao đường thẳng 6 năm về 0; EBITDA tăng thêm 400 triệu/năm; thuế 20%; NWC tăng 80 triệu (thu hồi cuối kỳ); bán lại máy 100 triệu cuối năm 6. (a) Lập bảng dòng tiền 0-6; (b) tính lá chắn thuế mỗi năm; (c) NPV tại r = 11%.

### Bài 4 (Trung bình – Xung đột NPV vs IRR)
Dự án P: dòng tiền –100, +60, +60. Dự án Q: –500, 0, +630 (r = 10%). Tính NPV, IRR từng dự án; tính IRR gia tăng; kết luận chọn dự án nào nếu loại trừ lẫn nhau.
*Gợi ý đáp số*: NPV(P) ≈ +4,13, IRR(P) ≈ 13,07%; NPV(Q) ≈ +20,66, IRR(Q) ≈ 12,25% → NPV và IRR xếp hạng ngược nhau. Dòng chênh lệch Q – P = –400, –60, +570: NPV gia tăng ≈ +16,53, IRR gia tăng ≈ 12,11% > 10% → chọn Q.

### Bài 5 (Trung bình – Capital rationing)
Ngân sách 2.000 triệu; 4 dự án (vốn / NPV): A (800 / 160), B (700 / 154), C (600 / 90), D (900 / 171). Tính PI từng dự án, chọn tổ hợp tối đa hóa tổng NPV.
*Gợi ý đáp số*: PI = 1,20 (A), 1,22 (B), 1,15 (C), 1,19 (D). Xếp theo PI chọn B rồi A (1.500 triệu, NPV 314), nhưng tổ hợp tối ưu là A + D (1.700 triệu, NPV 331) → khi ngân sách không chia hết, PI chỉ là heuristic, cần thử mọi tổ hợp (Solver).

### Bài 6 (Nâng cao – Mini Case: Xưởng may "Hòa Bình")
Xưởng may cân nhắc (i) mua 10 máy may công nghiệp mới thay máy cũ, hoặc (ii) giữ nguyên. Tự lập dòng tiền gia tăng gồm: bán máy cũ (có lãi/lỗ sổ sách → thuế), tiết kiệm nhân công, giảm phế phẩm, chi phí đào tạo, vốn lưu động. Tính NPV, IRR, DPP; chạy độ nhạy cho tiết kiệm nhân công ±20% và giá máy +15%; lập khuyến nghị.

### Bài 7 (Nâng cao – Real Options)
Một chuỗi trà sữa muốn thử 1 cửa hàng pilot (vốn 600 triệu, NPV độc lập –150 triệu), nếu thành công (xác suất 40%) sẽ nhân rộng 10 cửa hàng với NPV hiện tại +2.000 triệu. Tính giá trị kỳ vọng của chiến lược "thử rồi mở rộng" và xác suất hòa vốn; so sánh với NPV truyền thống.

### Bài 8 (Nâng cao – Tự thực hành)
Chọn một dự án thật của doanh nghiệp bạn (hoặc quán quen). Lập đủ 5 sheet theo template mục V.2, tính NPV/IRR/PI/DPP, chạy 3 kịch bản, và viết 1 trang khuyến nghị gồm "tiêu chí dừng".

---

## PHỤ LỤC: CHECKLIST CAPITAL BUDGETING TỔNG HỢP

### Bảng công thức tổng hợp

| Chỉ số | Công thức | Quy tắc |
|--------|-----------|---------|
| OCF | $EBIT\times(1-T)+Dep$ | Dòng tiền hoạt động sau thuế |
| Tax Shield | $Dep\times T$ | Lá chắn thuế khấu hao |
| NPV | $\sum_{t=0}^{n}\frac{CF_t}{(1+r)^t}$ | NPV > 0 → Đầu tư |
| IRR | $\sum\frac{CF_t}{(1+IRR)^t}=0$ | IRR > WACC → Đầu tư |
| MIRR | $\left(\frac{FV_{+}}{PV_{-}}\right)^{1/n}-1$ | MIRR > WACC |
| PI | $1+\frac{NPV}{C_0}$ | PI > 1; xếp hạng khi thiếu vốn |
| Payback | Năm cuối còn âm + (thiếu / CF kế tiếp) | So với ngưỡng |
| DPP | Như Payback nhưng dùng PV | So với ngưỡng |
| EAA | $NPV\times\frac{r}{1-(1+r)^{-n}}$ | So sánh khác vòng đời |
| E[NPV], σ | $\sum p_iNPV_i$ ; $\sqrt{\sum p_i(NPV_i-E)^2}$ | Rủi ro kịch bản |
| Strategic NPV | NPV truyền thống + Option Value | Dự án có tính linh hoạt |

### Checklist

```
CHUẨN BỊ:
□ Dự án phù hợp chiến lược DN?
□ Xác định đầy đủ CF: initial + operating + terminal?
□ Chỉ tính incremental CF (loại sunk cost, tính opportunity cost)?
□ Dòng tiền sau thuế?
□ Đã tính lá chắn thuế khấu hao?
□ Đã tính thay đổi vốn lưu động (NWC) và thu hồi cuối kỳ?
□ Không tính lãi vay trong dòng tiền (đã nằm trong WACC)?

PHÂN TÍCH:
□ Đã tính NPV? NPV > 0?
□ Đã tính IRR? IRR > WACC?
□ Payback Period / DPP chấp nhận được?
□ PI > 1? (đặc biệt khi bị giới hạn vốn)
□ Xung đột NPV vs IRR đã được giải quyết (IRR gia tăng)?
□ Dự án khác vòng đời đã so sánh bằng EAA?

RỦI RO:
□ Đã phân tích độ nhạy (Sensitivity)?
□ Đã phân tích kịch bản (tốt/cơ sở/xấu) + xác suất?
□ Đã phân tích hòa vốn (biên an toàn)?
□ Đã xem xét Real Options?
□ Đã xét phản ứng của đối thủ và công nghệ thay thế?

QUYẾT ĐỊNH & THEO DÕI:
□ Có người độc lập rà soát giả định?
□ Có quy trình stage-gate cho dự án lớn?
□ Có kế hoạch post-audit?
□ Theo dõi thực tế vs dự phóng?
□ Đã định nghĩa tiêu chí dừng (kill criteria)?
```

---

*Tài liệu tham khảo: Brealey, Myers & Allen "Principles of Corporate Finance" 14th Ed; Ross, Westerfield & Jordan "Corporate Finance" 13th Ed; Dixit & Pindyck "Investment Under Uncertainty" (Real Options); CFA Level I – Corporate Issuers*
