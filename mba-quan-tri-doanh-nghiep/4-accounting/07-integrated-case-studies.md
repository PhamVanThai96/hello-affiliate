# Integrated Case Studies – Kết Hợp Các Phương Pháp Accounting

> **Mục tiêu**: Phân tích các case study áp dụng **kết hợp** nhiều phương pháp accounting: Financial Accounting + Managerial Accounting + Cost Accounting + Budgeting + Variance Analysis + Financial Ratios. Mỗi case đi từ bối cảnh, số liệu, **từng bước tính toán**, diễn giải ý nghĩa kinh doanh đến bài học – để người đọc thấy các phương pháp bổ trợ nhau như thế nào, và **vì sao** từng công thức/chỉ số được dùng.

> **Lưu ý về cấu trúc**: Đây là file **tích hợp nhiều case** (không phải dạng "1 topic/1 file"), nên giữ cấu trúc theo chương thay vì khuôn I–VI của các file topic đơn lẻ.

> **Lưu ý về số liệu**: Tên doanh nghiệp và toàn bộ số liệu trong 4 case là **giả định minh họa** (tự thiết kế, đã kiểm tra nhất quán bằng tính toán), **không** phải số liệu của doanh nghiệp thật. Các quy định pháp lý/thuế/chuẩn mực (VAS, Thông tư 200/2014/TT-BTC, IFRS) chỉ nêu ở mức nguyên tắc – **cần xác nhận quy định hiện hành** với kế toán/kiểm toán trước khi áp dụng. Đơn vị: VNĐ; "tr" = triệu; "tỷ" = tỷ đồng.

---

## CÁCH ĐỌC FILE NÀY – VÌ SAO CẦN "KẾT HỢP" CÁC PHƯƠNG PHÁP?

Mỗi phương pháp accounting trả lời **một câu hỏi khác nhau** và có "điểm mù" riêng. Chỉ dùng một công cụ giống như chỉ nhìn bệnh nhân qua một loại xét nghiệm:

| Phương pháp | Câu hỏi nó trả lời | Điểm mù nếu dùng riêng lẻ | File chi tiết |
|-------------|-------------------|--------------------------|---------------|
| Financial Accounting | "Doanh nghiệp đã làm ra/đang nợ/đang có gì?" (cho bên ngoài) | Nhìn quá khứ, gộp chung, không cho biết sản phẩm/cửa hàng nào lời lỗ | `01-financial-accounting.md` |
| Managerial Accounting (CVP) | "Bán bao nhiêu thì hòa vốn? Nên làm hay bỏ?" | Phụ thuộc vào việc tách đúng định phí/biến phí | `02-managerial-accounting.md` |
| Cost Accounting (ABC/Job) | "Chi phí THỰC của từng sản phẩm là bao nhiêu?" | Không cho biết kế hoạch tương lai | `03-cost-accounting.md` |
| Budgeting & Forecasting | "Năm tới cần bao nhiêu tiền, doanh thu bao nhiêu?" | Kế hoạch sai nếu giả định lạc quan, không có kịch bản | `04-budgeting-and-forecasting.md` |
| Variance Analysis | "Thực tế lệch kế hoạch ở đâu, vì sao?" | Phát hiện mà không hành động thì vô nghĩa | `05-variance-analysis.md` |
| Financial Ratios + DuPont | "Doanh nghiệp khỏe hay yếu, yếu ở đâu?" | Chỉ là triệu chứng, cần các công cụ trên để tìm nguyên nhân | `06-financial-ratios.md` |

**Vòng PDCA** nối các phương pháp: *Plan* (Budget) → *Do* (vận hành, ghi sổ) → *Check* (Variance + Ratios) → *Act* (điều chỉnh bằng CVP/ABC) → quay lại *Plan*.

**Bốn case trong file**:

| Case | Loại | Quy mô | Trọng tâm |
|------|------|--------|-----------|
| 1. Phở Việt Chain | Thành công – F&B SME | 30 tỷ/năm, 8 chi nhánh | Đi qua đủ 5 giai đoạn: CVP → ABC → Budget → Variance → Ratios |
| 2. GreenPack | Thành công – Sản xuất SME | 15 tỷ/năm, gọi vốn Series A | ABC phát hiện sản phẩm "lãi ảo", pro-forma, định giá |
| 3. Mộc Thu (SME VN, mới) | Vận hành – Shop thời trang online | 12 tỷ/năm | Ba báo cáo tài chính khớp nhau, từ báo cáo đến quyết định |
| 4. TechMart | Thất bại – Bán lẻ điện tử | Đỉnh 500 tỷ/năm | Mỗi công cụ "gãy" ở đâu và vì sao |

---

## CHƯƠNG I: CASE STUDY 1 – STARTUP F&B "PHỞ VIỆT CHAIN" (Từ 1 quán đến chuỗi)

### Case Study 1 (Thành công): Phở Việt Chain – từ 1 quán đến chuỗi 8 chi nhánh

#### Bối cảnh

**Phở Việt** (tên giả định) là chuỗi phở cao cấp, bắt đầu với 1 quán tại Quận 1, TP.HCM năm 2020. Đến 2024 có 8 chi nhánh (6 tại TP.HCM, 2 tại Hà Nội), doanh thu 2024 là **30 tỷ VNĐ** (bình quân ~3,75 tỷ/chi nhánh/năm). Ban lãnh đạo đang cân nhắc mở thêm 5 chi nhánh và nhượng quyền. Câu hỏi lớn: *"Chuỗi đã đủ khỏe để mở rộng chưa, và mở rộng thế nào để không tự làm mình kiệt sức?"*

Case đi qua 5 giai đoạn, mỗi giai đoạn dùng **một công cụ phù hợp nhất** với câu hỏi tại thời điểm đó.

#### Giai đoạn 1: Khởi nghiệp (1 quán) – Managerial Accounting + CVP

**Câu hỏi**: Quán có khả thi không? Bao giờ hòa vốn?

**Vì sao dùng CVP (Cost-Volume-Profit)?** Chủ quán chưa có lịch sử số liệu nên không thể dùng ratio hay variance. Thứ duy nhất ước lượng được là *cấu trúc chi phí*: mỗi tô bán ra tốn bao nhiêu (biến phí) và mỗi tháng "dù không bán được tô nào" vẫn phải trả bao nhiêu (định phí). CVP biến hai con số đó thành **một con số quyết định**: sản lượng hòa vốn. Công thức xuất phát từ phương trình lợi nhuận:

$$\text{Lợi nhuận} = (\text{Giá} - \text{Biến phí/đv}) \times Q - \text{Định phí}$$

Đặt Lợi nhuận = 0 ⇒ $Q_{BEP} = \dfrac{\text{Định phí}}{\text{Giá} - \text{Biến phí/đv}}$, trong đó mẫu số là **Số dư đảm phí (Contribution Margin – CM)**: phần mỗi tô bán ra "góp" vào việc trang trải định phí.

**Bước 1 – Số liệu đầu vào (giả định minh họa):**

| Thông số | Giá trị |
|----------|---------|
| Giá bán trung bình/tô | 80.000 VNĐ |
| Biến phí/tô (nguyên liệu, bao bì, gas) | 32.000 VNĐ |
| Định phí/tháng (thuê, lương cố định, điện, khấu hao) | 120.000.000 VNĐ |
| Sức chứa | 60 chỗ, 3 lượt/ngày |

**Bước 2 – Tính toán:**

$$\text{CM/tô} = 80.000 - 32.000 = 48.000 \text{ VNĐ}$$

$$\text{CM\%} = \frac{48.000}{80.000} = 60\%$$

$$\text{BEP (tô/tháng)} = \frac{120.000.000}{48.000} = 2.500 \text{ tô/tháng} = \frac{2.500}{30} \approx 83 \text{ tô/ngày}$$

$$\text{BEP (doanh thu)} = \frac{120.000.000}{60\%} = 200.000.000 \text{ VNĐ/tháng}$$

**Bước 3 – So với sức chứa:** Công suất tối đa = 60 × 3 = 180 lượt/ngày. Với tỷ lệ lấp đầy 50% ⇒ 90 khách/ngày. BEP 83 tô/ngày = 83/180 ≈ **46% công suất**.

**Diễn giải**: Biên an toàn (Margin of Safety) $= \dfrac{90 - 83}{90} \approx 7,8\%$ – **rất mỏng**. Quán "khả thi" nhưng chỉ cần lấp đầy tụt xuống dưới 46% công suất là lỗ. Đây là lý do chủ quán không nên chỉ nhìn kết luận "Khả thi" mà phải theo dõi sát khách/ngày ngay từ tháng đầu (sẽ thành Variance Analysis ở giai đoạn 4).

#### Giai đoạn 2: Tối ưu menu – Cost Accounting (ABC) + Menu Engineering

**Câu hỏi**: Món nào lãi nhất thật sự? Nên đẩy món nào?

**Vì sao cần ABC thay vì phân bổ đều?** Phương pháp truyền thống chia chi phí chung (bếp, nhân công bếp, gas, thiết bị) **đều cho mọi món** – nghĩa là tô phở gà (nấu 10 phút) gánh phần chi phí bếp bằng bún bò Huế (nấu 25 phút, 15 nguyên liệu). ABC (Activity-Based Costing, do Robert Kaplan và Robin Cooper phổ biến cuối thập niên 1980) khắc phục bằng cách **phân bổ theo mức tiêu dùng hoạt động thực tế (cost driver)**. Ở đây cost driver chọn là *số phút chuẩn bị*.

**Bước 1 – Giả định**: Chi phí bếp chung tương ứng **1.000 VNĐ/phút chuẩn bị** (giả định minh họa). Giá bán và food cost từng món:

| Món | Giá bán (k) | Food cost % | Food cost (k) | Phút chuẩn bị | Số nguyên liệu | Tỷ trọng doanh thu |
|-----|-------------|-------------|---------------|---------------|----------------|--------------------|
| Phở bò truyền thống | 70 | 35% | 24,5 | 15 | 8 | 40% |
| Phở bò Wagyu | 150 | 55% | 82,5 | 20 | 12 | 15% |
| Bún bò Huế | 65 | 30% | 19,5 | 25 | 15 | 20% |
| Phở gà | 60 | 25% | 15,0 | 10 | 6 | 15% |
| Đồ uống | 30 | 15% | 4,5 | 3 | 2 | 10% |

**Bước 2 – Quy từ tỷ trọng doanh thu ra tỷ trọng số lượng (popularity)**: số lượng ∝ (tỷ trọng doanh thu ÷ giá). Chuẩn hóa tổng = 100%:

| Món | Tỷ trọng số lượng bán |
|-----|----------------------|
| Phở bò truyền thống | 36,6% |
| Phở bò Wagyu | 6,4% |
| Bún bò Huế | 19,7% |
| Phở gà | 16,0% |
| Đồ uống | 21,3% |

**Bước 3 – Chi phí bếp theo hai cách:**

- *Truyền thống*: phút chuẩn bị bình quân gia quyền $= 0{,}366\times15 + 0{,}064\times20 + 0{,}197\times25 + 0{,}160\times10 + 0{,}213\times3 \approx 13{,}9$ phút ⇒ **mỗi món gánh đều ≈ 13.900 VNĐ**.
- *ABC*: mỗi món gánh `phút × 1.000`.

**Bước 4 – Biên lợi nhuận theo hai cách** $= \dfrac{\text{Giá} - \text{Food cost} - \text{Chi phí bếp}}{\text{Giá}}$:

| Món | Truyền thống | ABC | Chênh | Nhận xét |
|-----|-------------|-----|-------|----------|
| Phở bò truyền thống | 45,1% | **43,6%** | -1,5 | Gần như không đổi |
| Phở bò Wagyu | 35,7% | **31,7%** | -4,0 | Phức tạp hơn mức trung bình |
| Bún bò Huế | 48,6% | **31,5%** | **-17,1** | Bị "đánh giá quá cao" – 25 phút chuẩn bị |
| Phở gà | 51,8% | **58,3%** | +6,5 | Bị "đánh giá quá thấp" |
| Đồ uống | 38,6% | **75,0%** | **+36,4** | Hầu như không tốn công bếp |

**Diễn giải**: Bún bò Huế trông lãi gần 49% nhưng thực tế chỉ ~31,5% vì nó chiếm nhiều thời gian bếp; đồ uống bị truyền thống làm "mất" hơn 36 điểm phần trăm biên lợi nhuận. Nếu quyết định menu dựa trên cách truyền thống, chủ quán sẽ đẩy nhầm món.

**Bước 5 – Menu Engineering (Kasavana & Smith, 1982) – kết hợp độ phổ biến × lợi nhuận tuyệt đối:**

Tiêu chí: *Phổ biến cao* nếu tỷ trọng số lượng ≥ 70% × (1/5 món) = **14%**; *lợi nhuận cao* nếu số dư sau chi phí bếp (Contribution Margin sau ABC) ≥ **mức bình quân gia quyền**.

| Món | CM sau ABC (k/món) | Tỷ trọng số lượng | Phân loại |
|-----|-------------------|--------------------|-----------|
| Phở bò truyền thống | 70 - 24,5 - 15 = **30,5** | 36,6% | Phổ biến + lãi cao |
| Phở bò Wagyu | 150 - 82,5 - 20 = **47,5** | 6,4% | Ít phổ biến + lãi cao |
| Bún bò Huế | 65 - 19,5 - 25 = **20,5** | 19,7% | Phổ biến + lãi thấp |
| Phở gà | 60 - 15 - 10 = **35,0** | 16,0% | Phổ biến + lãi cao |
| Đồ uống | 30 - 4,5 - 3 = **22,5** | 21,3% | Phổ biến + lãi thấp |

CM bình quân gia quyền $= 0{,}366\times30{,}5 + 0{,}064\times47{,}5 + 0{,}197\times20{,}5 + 0{,}160\times35 + 0{,}213\times22{,}5 \approx 28{,}6$k.

```
                      Phổ biến THẤP        │      Phổ biến CAO
  ────────────────────────────────────────┼───────────────────────────────
  CM CAO (≥ 28,6k)    PUZZLE (câu đố)     │   STAR (ngôi sao)
                      Phở bò Wagyu        │   Phở bò truyền thống, Phở gà
  ────────────────────────────────────────┼───────────────────────────────
  CM THẤP (< 28,6k)   DOG (chó)           │   PLOWHORSE (ngựa kéo cày)
                      (không có món nào)  │   Bún bò Huế, Đồ uống
```

**Lưu ý quan trọng**: Phở Wagyu có *biên % thấp* (31,7%) nhưng *CM tuyệt đối cao nhất* (47,5k/món). **Phần trăm và số tiền cho kết luận khác nhau** – menu engineering dùng CM tuyệt đối vì chủ quán trả tiền thuê bằng đồng, không bằng phần trăm.

**Bước 6 – Hành động:**

| # | Món | Phân loại | Hành động | Tính toán kèm theo |
|---|-----|-----------|-----------|---------------------|
| 1 | Phở Wagyu | Puzzle | Đẩy bán (gợi ý của nhân viên, ảnh menu) thay vì cắt; thử tăng giá 150k → 180k | CM mới = 180 - 82,5 - 20 = 77,5k. Lợi nhuận không giảm nếu lượng bán giảm ≤ 1 - 47,5/77,5 ≈ **38,7%** |
| 2 | Phở gà | Star | Giữ chất lượng, đưa lên vị trí nổi bật trong menu | – |
| 3 | Bún bò Huế | Plowhorse | Giảm độ phức tạp: 15 → 10 nguyên liệu, chuẩn hóa sơ chế ⇒ giảm phút chuẩn bị | Nếu giảm 25 → 18 phút, CM tăng 7k/món (=7 × 19,7% ≈ +1,4k trung bình toàn menu) |
| 4 | Đồ uống | Plowhorse | Bán combo "phở + đồ uống" để tăng ghép đôi | – |

#### Giai đoạn 3: Mở rộng chuỗi – Budgeting & Forecasting

**Câu hỏi**: Mở thêm chi nhánh cần bao nhiêu vốn? Với giả định nào thì đáng làm?

**Vì sao dùng Capital Budget + Scenario thay vì một con số dự báo duy nhất?** Mỗi chi nhánh mới là khoản đầu tư lớn, khó đảo ngược (deposit, nội thất). Một con số dự báo duy nhất tạo ảo giác chắc chắn; **kịch bản** buộc ban lãnh đạo hỏi "nếu sai thì mất bao nhiêu?" trước khi ký hợp đồng thuê.

**Bước 1 – Vốn đầu tư cho một chi nhánh:**

| Khoản mục | Chi phí (tr) |
|----------|--------------|
| Tiền thuê đặt cọc (6 tháng) | 300 |
| Thiết kế & thi công nội thất | 500 |
| Thiết bị bếp | 250 |
| Vốn lưu động (3 tháng) | 450 |
| Marketing khai trương | 100 |
| **Tổng đầu tư** | **1.600** |

**Bước 2 – Dự báo cuốn chiếu (Rolling Forecast) 6 tháng đầu** (cùng cấu trúc chi phí với giai đoạn 1: CM 48k/tô, định phí 120 tr/tháng):

| Tháng | Tô/ngày | Doanh thu (tr) = tô × 30 × 80k | Lợi nhuận (tr) = tô × 30 × 48k - 120 |
|-------|---------|-------------------------------|--------------------------------------|
| 1 | 60 | 144,0 | **-33,6** |
| 2 | 80 | 192,0 | **-4,8** |
| 3 | 95 | 228,0 | 16,8 |
| 4 | 105 | 252,0 | 31,2 |
| 5 | 115 | 276,0 | 45,6 |
| 6 | 120 | 288,0 | 52,8 |

Chi nhánh vượt hòa vốn hoạt động (83 tô/ngày) vào khoảng tháng thứ 2–3. Sau khi ổn định (120 tô/ngày = 67% công suất) lợi nhuận hoạt động ≈ **52,8 tr/tháng ≈ 634 tr/năm**.

**Bước 3 – Ba kịch bản và NPV 5 năm** (chiết khấu 15%/năm – giả định minh họa; năm 1 đạt 80% sản lượng ổn định vì giai đoạn khởi động; không tính giá trị thanh lý):

| Kịch bản | Tô/ngày ổn định | Lợi nhuận/tháng (tr) | Dòng tiền Năm 1 / Năm 2–5 (tr) | NPV 5 năm (tr) | Quyết định riêng |
|----------|-----------------|---------------------|-------------------------------|---------------|------------------|
| Bull (tốt) | 150 | 96,0 | 922 / 1.152 | **+2.061** | Mở |
| Base (cơ sở) | 120 | 52,8 | 507 / 634 | **+414** | Mở |
| Bear (xấu) | 90 | 9,6 | 92 / 115 | **-1.234** | Không mở |
| **Kỳ vọng (25%/50%/25%)** | – | – | – | **+414** | Mở – có điều kiện |

$$\text{NPV kỳ vọng} = 0{,}25 \times 2.061 + 0{,}5 \times 414 + 0{,}25 \times (-1.234) \approx +414 \text{ tr}$$

**Diễn giải**:
- Quyết định "Mở" nhưng **kịch bản xấu mất ~1,2 tỷ** (gần 77% vốn đầu tư), nên điều kiện đi kèm là: (i) chọn địa điểm có lưu lượng khách đã kiểm chứng, (ii) thương lượng điều khoản thuê (miễn thuê tháng đầu, giảm đặt cọc) để hạ vốn đầu tư và định phí, (iii) đặt **ngưỡng cắt lỗ** (nếu sau 3 tháng dưới 80 tô/ngày thì hành động, xem giai đoạn 4).
- **Hoàn vốn** (kịch bản cơ sở): lũy kế dòng tiền năm 1 = 507, năm 2 = 1.141, năm 3 = 1.775 > 1.600 ⇒ hoàn vốn khoảng **2,7 năm**.
- Không nên mở nhiều hơn 3 chi nhánh/năm đầu vì vốn lưu động và năng lực quản lý trải mỏng (xem quyết định ở giai đoạn 5).

#### Giai đoạn 4: Kiểm soát chuỗi – Variance Analysis

**Câu hỏi**: Chi nhánh nào đang kém, và kém ở khâu nào?

**Vì sao phân tích chênh lệch?** Kế hoạch (budget) chỉ có giá trị nếu thực tế được so sánh với nó đều đặn. Chênh lệch **thuận lợi (F – Favorable)** làm lợi nhuận tăng; **bất lợi (U – Unfavorable)** làm giảm. Điểm then chốt là phải *tách nguyên nhân* (doanh thu, chi phí nguyên liệu, nhân công) để biết cần hành động ở đâu.

**Bước 1 – Bảng đèn tín hiệu toàn chuỗi (giả định minh họa, so với ngân sách tĩnh):**

| Chi nhánh | Chênh lệch DT | Chênh lệch food cost | Chênh lệch nhân công | Chênh lệch lợi nhuận | Trạng thái |
|----------|--------------|----------------------|----------------------|----------------------|-----------|
| Q1 (flagship) | +5% (F) | -2% (F) | +3% (U) | +4% (F) | Xanh |
| Q3 | +2% (F) | +1% (U) | -1% (F) | +2% (F) | Xanh |
| Q7 | -3% (U) | +5% (U) | +2% (U) | -10% (U) | Đỏ |
| **Thủ Đức** | **-8% (U)** | **+3,5% (U)** | **+15% (U)** | **-110% (U)** | Đỏ đậm |
| Bình Thạnh | +1% (F) | -1% (F) | +1% (U) | +1% (F) | Xanh |
| Tân Bình | -1% (U) | +2% (U) | -2% (F) | -1% (U) | Vàng |
| Hà Nội 1 | +10% (F) | +3% (U) | +4% (U) | +3% (F) | Xanh |
| Hà Nội 2 | -5% (U) | +6% (U) | +7% (U) | -18% (U) | Đỏ |

**Bước 2 – Đào sâu chi nhánh Thủ Đức bằng ngân sách linh hoạt (Flexible Budget).**

*Vì sao cần ngân sách linh hoạt?* Khi doanh thu giảm 8%, food cost tuyệt đối **đương nhiên** phải giảm (bán ít thì dùng ít nguyên liệu). So sánh food cost thực tế với ngân sách tĩnh sẽ che mất việc "dùng nguyên liệu kém hiệu quả". Do đó phải điều chỉnh ngân sách theo doanh thu thực tế rồi mới so sánh.

Ngân sách tháng của Thủ Đức (tr): Doanh thu 320; food cost 32% = 102,4; nhân công 80; thuê 60; chi phí khác 40 ⇒ **Lợi nhuận kế hoạch = 320 - 102,4 - 80 - 60 - 40 = 37,6**.

Thực tế: doanh thu giảm 8% ⇒ 294,4; food cost thực tế 36% doanh thu = 106,0 (tỷ lệ hao hụt 18% so với chuẩn 8%); nhân công 92 (thuê thêm 2 nhân viên, làm thêm giờ); thuê 60; chi phí khác 40 ⇒ **Lợi nhuận thực tế = 294,4 - 106,0 - 92 - 60 - 40 = -3,6**.

Phân rã chênh lệch lợi nhuận **-41,2 tr**:

| Thành phần | Cách tính | Số tiền (tr) | Nguyên nhân gốc (5-Why) |
|-----------|-----------|--------------|--------------------------|
| Chênh lệch khối lượng bán (sales volume) | Doanh thu giảm 25,6; food cost theo chuẩn 32% giảm 8,2 ⇒ -25,6 + 8,2 | **-17,4 (U)** | Khu vực ít dân văn phòng, lưu lượng buổi trưa thấp |
| Chênh lệch hiệu quả food cost | Food cost thực tế 106,0 - food cost linh hoạt (32% × 294,4 = 94,2) | **-11,8 (U)** | Quản lý mới chưa kiểm soát định lượng, hao hụt 18% vs 8% |
| Chênh lệch nhân công | 92 - 80 | **-12,0 (U)** | Thiếu kinh nghiệm → thuê thêm người, làm thêm giờ |
| **Tổng** | -17,4 - 11,8 - 12,0 | **-41,2** | Khớp -3,6 - 37,6 |

**Diễn giải**: Chỉ **42%** (17,4/41,2) thiệt hại đến từ yếu tố ngoài tầm kiểm soát (khu vực); **58%** đến từ vận hành (định lượng, nhân công) – tức **sửa được**. Đây là điều chỉ ngân sách linh hoạt mới chỉ ra; nếu chỉ so sánh với ngân sách tĩnh, ta sẽ đổ hết cho "khu vực xấu".

**Bước 3 – Hành động khắc phục:**

| # | Hành động | Người phụ trách | Hạn | Tác động kỳ vọng |
|---|-----------|----------------|------|-------------------|
| 1 | Đào tạo định lượng (portioning) cho quản lý | Giám đốc vận hành | 2 tuần | Đưa food cost về 32% → +11,8 tr/tháng |
| 2 | Hệ thống chuẩn bị theo kanban, ghi chép hao hụt hằng ngày | Bếp trưởng | 1 tháng | Hao hụt 18% → 10% |
| 3 | Marketing địa phương (GrabFood, ShopeeFood) | Marketing | Ngay | Bù một phần 25,6 tr doanh thu |
| 4 | **Ngưỡng cắt lỗ**: nếu sau 3 tháng vẫn lỗ → xem xét đóng/chuyển địa điểm | CEO | 3 tháng | Tránh "chờ tháng sau sẽ khá hơn" (xem Case 4) |

#### Giai đoạn 5: Đánh giá tổng thể – Financial Ratios + DuPont

**Câu hỏi**: Chuỗi có đủ khỏe để mở rộng không?

**Vì sao cần DuPont thay vì chỉ nhìn ROE?** ROE 30% có thể đến từ lợi nhuận tốt, từ tài sản quay nhanh, hoặc đơn thuần từ vay nhiều. Mô hình DuPont (do công ty DuPont phát triển những năm 1920) tách ROE thành ba nhân tố để biết ROE tốt vì lý do nào, từ đó biết khi nào nó **bền** và khi nào nó **mong manh**:

$$\text{ROE} = \underbrace{\frac{\text{LNST}}{\text{Doanh thu}}}_{\text{Net Margin}} \times \underbrace{\frac{\text{Doanh thu}}{\text{Tổng tài sản}}}_{\text{Asset Turnover}} \times \underbrace{\frac{\text{Tổng tài sản}}{\text{Vốn chủ}}}_{\text{Equity Multiplier}}$$

**Bước 1 – Báo cáo tài chính rút gọn 2024 (giả định minh họa, đơn vị: tr):**

*Kết quả kinh doanh*: Doanh thu 30.000; giá vốn 11.400 (38%) ⇒ lợi nhuận gộp **18.600**; EBIT **3.600**; lãi vay 400; lợi nhuận trước thuế 3.200; thuế và điều chỉnh 800 (thuế suất hiệu dụng 25% do một số chi phí không được trừ – giả định); **LNST 2.400**.

*Cân đối kế toán (đơn vị tr)*:

| Tài sản | Số tiền | Nợ phải trả & Vốn chủ | Số tiền |
|---------|---------|----------------------|---------|
| Tiền | 4.500 | Phải trả nhà cung cấp | 470 |
| Phải thu (sàn giao hàng) | 100 | Lương, thuế phải trả | 1.530 |
| Hàng tồn kho | 250 | Vay ngắn hạn | 1.000 |
| Trả trước | 750 | Voucher/tiền cọc nhận trước | 1.000 |
| **Tài sản ngắn hạn** | **5.600** | **Nợ ngắn hạn** | **4.000** |
| Tài sản dài hạn (nội thất, thiết bị, đặt cọc) | 10.400 | Vay dài hạn | 4.000 |
| | | **Vốn chủ sở hữu** | **8.000** |
| **Tổng tài sản** | **16.000** | **Tổng nguồn vốn** | **16.000** |

Cân đối: 16.000 = 4.000 + 4.000 + 8.000. ✓

**Bước 2 – Tính chỉ số:**

| Chỉ số | Công thức & phép tính | Kết quả | Chuẩn ngành F&B (tham khảo, cần đối chiếu nguồn) | Đánh giá |
|-------|-----------------------|---------|-------------------------------------------------|----------|
| Gross Margin | 18.600 / 30.000 | **62%** | 60–70% | Tốt |
| Operating Margin | 3.600 / 30.000 | **12%** | 8–15% | Tốt |
| Net Margin | 2.400 / 30.000 | **8%** | 5–10% | Tốt |
| Current Ratio | 5.600 / 4.000 | **1,4** | 1,0–1,5 | Ổn |
| Quick Ratio | (4.500 + 100) / 4.000 | **1,15** | > 1,0 | Ổn |
| D/E (tổng nợ / vốn chủ) | 8.000 / 8.000 | **1,0** | 1,0–2,0 | Ổn |
| Interest Coverage | 3.600 / 400 | **9x** | > 3x | Rất an toàn |
| ROE | 2.400 / 8.000 | **30%** | 15–25% | Cao (có sự hỗ trợ của đòn bẩy) |
| ROA | 2.400 / 16.000 | **15%** | 8–12% | Tốt |
| Inventory Turnover | 11.400 / 250 | **45,6x** (DIO ≈ 8 ngày) | 30–60x | Tốt (hàng tươi) |
| DSO | 100 / 30.000 × 365 | 1,2 ngày | – | Gần như thu tiền ngay |
| DPO | 470 / 11.400 × 365 | 15,0 ngày | – | – |
| **CCC** | 8,0 + 1,2 - 15,0 | **-5,8 ngày** | 0–15 | Xuất sắc: khách trả tiền trước khi doanh nghiệp trả nhà cung cấp |

**Vì sao Quick Ratio bỏ hàng tồn kho?** Hàng tồn kho là loại tài sản khó chuyển ra tiền nhanh nhất trong tài sản ngắn hạn (có thể phải giảm giá). Quick Ratio kiểm tra khả năng trả nợ ngắn hạn *khi không dựa vào bán hàng tồn kho*.

**Bước 3 – DuPont:**

$$\text{ROE} = \underbrace{\frac{2.400}{30.000}}_{8\%} \times \underbrace{\frac{30.000}{16.000}}_{1{,}875} \times \underbrace{\frac{16.000}{8.000}}_{2{,}0} = 0{,}08 \times 1{,}875 \times 2{,}0 = 30\%$$

| Thành phần | Giá trị | Diễn giải |
|-----------|---------|-----------|
| Net Margin | 8% | Khỏe; còn dư địa cải thiện bằng cách giảm food cost (các chi nhánh đỏ ở giai đoạn 4) |
| Asset Turnover | 1,875x | Tốt cho F&B – mỗi đồng tài sản tạo 1,875 đồng doanh thu |
| Equity Multiplier | 2,0x | Vừa phải; nợ = vốn chủ |

**Bước 4 – Ma trận quyết định Go/No-go:**

| Tiêu chí | Kết quả | Đánh giá |
|----------|---------|----------|
| Sinh lời (ratio) | Margin, ROE, ROA đạt | Đạt |
| Thanh khoản | Current 1,4; Quick 1,15 | Đạt |
| Đòn bẩy | D/E 1,0; Interest Coverage 9x | Đạt |
| Kinh tế đơn vị (CVP, NPV) | NPV kỳ vọng +414 tr | Đạt (có điều kiện) |
| Kiểm soát vận hành | 3/8 chi nhánh đỏ | **Chưa đạt** |
| Độ chính xác ngân sách | Sai lệch trong ±10% | Đạt |

**Khuyến nghị**: *Mở rộng có điều kiện* – (1) **sửa các chi nhánh đỏ trước** (Thủ Đức, Q7, Hà Nội 2), (2) không mở quá **3 chi nhánh mới** trong năm đầu, (3) nhượng quyền chỉ khi quy trình định lượng và báo cáo chênh lệch đã chuẩn hóa.

#### Bài học tổng hợp Case 1

| Công cụ | Vai trò trong câu chuyện | Giai đoạn |
|---------|-------------------------|-----------|
| CVP (Managerial) | Quyết định mở quán đầu tiên; biên an toàn mỏng ⇒ phải theo dõi sát | Khởi nghiệp |
| ABC (Cost) | Phát hiện bún bò Huế "lãi ảo", đồ uống "lãi thật" | Tối ưu hóa |
| Budgeting + Scenario | Biết trước kịch bản xấu mất ~1,2 tỷ khi mở chi nhánh | Mở rộng |
| Variance (ngân sách linh hoạt) | Tách được 58% thiệt hại có thể sửa | Kiểm soát |
| Ratios + DuPont | Quyết định Go/No-go có điều kiện | Đánh giá |
| Financial Accounting | Cung cấp số liệu gốc, báo cáo cho ngân hàng và nhà đầu tư | Xuyên suốt |

---

## CHƯƠNG II: CASE STUDY 2 – CÔNG TY SẢN XUẤT "GREENPACK" (Bao bì thân thiện môi trường)

### Case Study 2 (Thành công): GreenPack – từ BCTC đến gọi vốn Series A

#### Bối cảnh

**GreenPack** (tên giả định) sản xuất bao bì từ vật liệu tái chế và phân hủy sinh học. Thành lập 2019, 1 nhà máy, 50 nhân viên, doanh thu hiện tại **~15 tỷ/năm**. Công ty cần gọi vốn **Series A** để xây nhà máy thứ hai (CapEx 10 tỷ trong 2 năm). Nhà đầu tư hỏi năm câu: *Số liệu có đáng tin không? Chi phí thật của từng sản phẩm? Kế hoạch có hợp lý không? Vận hành có kiểm soát không? Công ty đáng giá bao nhiêu?*

#### Vấn đề 1: "Show me the numbers" – Financial Accounting

**Vì sao nhà đầu tư quan tâm đến cách ghi nhận kế toán?** Họ định giá công ty dựa trên lợi nhuận và tài sản; nếu doanh thu bị ghi sớm hoặc tài sản bị phồng, định giá bị sai và họ phải trả giá cao hơn thực tế. Trước khi đầu tư, nhà đầu tư thực hiện *due diligence* (thẩm định) và điều chỉnh BCTC về một chuẩn thống nhất. Công ty SME Việt Nam thường lập BCTC theo VAS (Thông tư 200/2014/TT-BTC hoặc thông tư dành cho DN nhỏ và vừa – **cần xác nhận hiện hành**) nhưng nhà đầu tư nước ngoài thường muốn IFRS (hoặc ít nhất bản điều chỉnh).

| Báo cáo | Trước điều chỉnh | Sau điều chỉnh (đối chiếu IFRS) |
|---------|------------------|----------------------------------|
| Balance Sheet | Theo VAS, giá gốc | Kiểm tra giảm giá trị tài sản (impairment), ghi nhận thuê tài sản theo IFRS 16 |
| Income Statement | Ghi doanh thu khi xuất hóa đơn | IFRS 15: ghi khi khách hàng nhận được quyền kiểm soát hàng hóa |
| Cash Flow | Không lập | Lập đầy đủ (phương pháp gián tiếp) |
| Thuyết minh | Sơ sài | Chính sách kế toán, thông tin bộ phận, bên liên quan |

**Cầu nối điều chỉnh lợi nhuận (giả định minh họa, đơn vị: tr):**

Lợi nhuận trước thuế theo VAS: doanh thu 14.950, lợi nhuận gộp 4.640, chi phí hoạt động 3.000 ⇒ EBIT 1.640; lãi vay 200 ⇒ **EBT = 1.440**; thuế 20% (đơn giản hóa) ⇒ **LNST = 1.152**.

| Điều chỉnh | Nội dung | Ảnh hưởng EBT (tr) |
|------------|---------|--------------------|
| EBT theo VAS | | 1.440 |
| (1) Cut-off doanh thu | Doanh thu bị ghi sớm 1 tháng (ghi khi xuất kho, chưa giao); hoãn phần lợi nhuận gộp | -60 |
| (2) Thuê tài sản (IFRS 16) | Chi phí tính theo IFRS 16 (khấu hao + lãi) cao hơn tiền thuê ở giai đoạn đầu hợp đồng | -30 |
| (3) Impairment máy ép | Giá trị ghi sổ 1.200 so với giá trị thực tế có thể thu hồi 800 | -400 |
| **EBT điều chỉnh** | 1.440 - 60 - 30 - 400 | **950** |

$$\text{LNST điều chỉnh} = 950 \times (1 - 20\%) = 760 \quad \Rightarrow \quad \frac{760}{1.152} - 1 = -34\%$$

Nếu bỏ khoản impairment (một lần, không lặp lại): LNST điều chỉnh "chạy đều" $= (1.440 - 90) \times 0{,}8 = 1.080$, thấp hơn VAS khoảng **6,3%**.

**Diễn giải**: Lợi nhuận "hiển thị" giảm mạnh (do khoản impairment một lần) nhưng **lợi nhuận bền vững** chỉ giảm ~6%. BCTC trung thực giúp nhà đầu tư tin tưởng và đàm phán trên cơ sở thật; che giấu để nhìn đẹp sẽ bị phát hiện khi thẩm định và mất uy tín. (Lưu ý: tác động thuế thực tế của từng điều chỉnh phụ thuộc quy định thuế VN – **cần xác nhận với chuyên gia thuế**.)

#### Vấn đề 2: Giá thành sản phẩm chưa rõ – Cost Accounting (Job + ABC)

**Vì sao cần ABC?** GreenPack làm theo đơn hàng (Job Costing) với ba dòng sản phẩm có mức độ phức tạp rất khác nhau. Phân bổ chi phí chung đều theo số lượng khiến sản phẩm đơn giản gánh phí cho sản phẩm phức tạp.

**Bước 1 – Ba nhóm hoạt động và hệ số tiêu thụ (giả định minh họa):**

| Hoạt động | Quỹ chi phí (tr) | Cost driver | Tổng driver | Hộp A (đơn giản) | Hộp B (in custom) | Túi C (compostable) |
|----------|------------------|-------------|-------------|-------------------|--------------------|----------------------|
| Cài đặt máy | 1.000 | Số lần setup | 130 | 20 | 80 | 30 |
| Kiểm tra chất lượng | 600 | Số lần test | 350 | 50 | 100 | 200 |
| Thiết kế/kỹ thuật | 400 | Số thiết kế | 45 | 5 | 30 | 10 |
| **Tổng quỹ** | **2.000** | | | | | |

**Bước 2 – Tính đơn giá cost driver** $= \dfrac{\text{Quỹ chi phí}}{\text{Tổng driver}}$:

- Setup: 1.000 / 130 = **7,692 tr/lần**
- Test: 600 / 350 = **1,714 tr/lần**
- Thiết kế: 400 / 45 = **8,889 tr/thiết kế**

**Bước 3 – Chi phí chung phân bổ cho từng sản phẩm (tr):**

| Hoạt động | Hộp A | Hộp B | Túi C |
|----------|-------|-------|-------|
| Setup | 20 × 7,692 = 153,8 | 80 × 7,692 = 615,4 | 30 × 7,692 = 230,8 |
| Test | 50 × 1,714 = 85,7 | 100 × 1,714 = 171,4 | 200 × 1,714 = 342,9 |
| Thiết kế | 5 × 8,889 = 44,4 | 30 × 8,889 = 266,7 | 10 × 8,889 = 88,9 |
| **Tổng** | **284,0** | **1.053,5** | **662,5** |

(Tổng = 2.000 ✓)

**Bước 4 – Chia cho sản lượng để ra OH/đơn vị:**

| | Hộp A | Hộp B | Túi C |
|---|-------|-------|-------|
| Sản lượng năm (đơn vị) | 1.800.000 | 450.000 | 575.000 |
| Giá bán (VNĐ) | 4.000 | 7.000 | 8.000 |
| Doanh thu (tỷ) | 7,20 | 3,15 | 4,60 |
| **OH/đv theo ABC** = Tổng ÷ sản lượng | **158** | **2.341** | **1.152** |
| **OH/đv truyền thống** = 2.000 tr ÷ 2.825.000 đv | 708 | 708 | 708 |

Tổng doanh thu = 7,20 + 3,15 + 4,60 = **14,95 tỷ** (≈ 15 tỷ).

**Bước 5 – So sánh giá thành và biên lợi nhuận** (Biên $= \dfrac{\text{Giá} - \text{Giá thành}}{\text{Giá}}$):

| VNĐ/đơn vị | Hộp A | Hộp B | Túi C |
|-----------|-------|-------|-------|
| Nguyên vật liệu trực tiếp (DM) | 1.200 | 2.500 | 3.800 |
| Nhân công trực tiếp (DL) | 800 | 1.200 | 1.500 |
| Giá thành truyền thống (DM + DL + 708) | 2.708 | 4.408 | 6.008 |
| Giá thành ABC (DM + DL + OH ABC) | **2.158** | **6.041** | **6.452** |
| Biên truyền thống | 32,3% | **37,0%** | 24,9% |
| Biên ABC | **46,1%** | **13,7%** | 19,3% |

Tổng lợi nhuận gộp hai cách đều **4.637,5 tr** (giá thành tổng không đổi; chỉ cách phân bổ đổi) ⇒ biên gộp chung = 31,0%.

**Diễn giải**: Truyền thống cho rằng Hộp B (in custom) là sản phẩm lãi nhất (37%) – nhưng thực tế **chỉ 13,7%** vì nó chiếm 80 lần setup, 30 thiết kế. Hộp A, bị xem là "lãi ít", thực ra là **bò sữa (cash cow)** với 46%.

**Hành động**: (1) Đẩy sản lượng Hộp A; (2) Hộp B: đặt số lượng tối thiểu/đơn và phí thiết kế riêng – nếu tăng giá 7.000 → 7.800 thì biên ABC từ 13,7% lên $\frac{7.800 - 6.041}{7.800} \approx 22,6\%$; (3) Túi C: tăng quy mô để giảm chi phí kiểm tra trên mỗi đơn vị.

#### Vấn đề 3: Ngân sách cho nhà máy mới – Budgeting & Forecasting

**Vì sao dùng pro-forma 5 năm và FCF?** Nhà đầu tư không mua lợi nhuận kế toán mà mua **dòng tiền tự do (Free Cash Flow – FCF)**, vì chỉ dòng tiền mới dùng để hoàn vốn và chia cổ tức. FCF = Lợi nhuận hoạt động sau thuế + Khấu hao - CapEx - Tăng vốn lưu động (ΔNWC).

**Bước 1 – Giả định (giả định minh họa):** doanh thu tăng theo kế hoạch công suất nhà máy mới; biên gộp tăng nhờ quy mô và điều chỉnh giá sản phẩm B; thuế suất 20%.

| (tỷ VNĐ) | Năm 1 | Năm 2 | Năm 3 | Năm 4 | Năm 5 |
|----------|-------|-------|-------|-------|-------|
| Doanh thu | 18,0 | 25,0 | 35,0 | 45,0 | 55,0 |
| Tăng trưởng | +20,4% | +38,9% | +40,0% | +28,6% | +22,2% |
| Biên gộp | 33% | 36% | 39% | 42% | 45% |
| Giá vốn | (12,06) | (16,00) | (21,35) | (26,10) | (30,25) |
| Lợi nhuận gộp | 5,94 | 9,00 | 13,65 | 18,90 | 24,75 |
| Chi phí hoạt động (OpEx) | (3,8) | (5,0) | (6,6) | (8,2) | (9,8) |
| **EBIT** | **2,14** | **4,00** | **7,05** | **10,70** | **14,95** |
| Biên EBIT | 11,9% | 16,0% | 20,1% | 23,8% | 27,2% |
| Thuế 20% | (0,43) | (0,80) | (1,41) | (2,14) | (2,99) |
| + Khấu hao | 0,6 | 1,0 | 1,2 | 1,2 | 1,2 |
| - CapEx nhà máy 2 | (8,0) | (2,0) | – | – | – |
| - Tăng vốn lưu động | (0,5) | (0,7) | (1,0) | (1,0) | (0,8) |
| **FCF** | **(6,19)** | **1,50** | **5,84** | **8,76** | **12,36** |
| FCF lũy kế | (6,19) | (4,69) | 1,15 | 9,91 | 22,27 |

**Bước 2 – Giá trị hiện tại (chiết khấu 15%, tăng trưởng dài hạn 3% – giả định minh họa):**

$$\text{PV}_{FCF\,1\text{–}5} \approx 10{,}75 \text{ tỷ}; \quad \text{TV}_5 = \frac{12{,}36 \times 1{,}03}{0{,}15 - 0{,}03} \approx 106{,}1 \text{ tỷ}; \quad \text{PV}(\text{TV}_5) = \frac{106{,}1}{1{,}15^5} \approx 52{,}7 \text{ tỷ}$$

$$\text{Giá trị dự án} \approx 10{,}75 + 52{,}7 \approx 63{,}5 \text{ tỷ}$$

**Diễn giải**: Hơn **80%** giá trị đến từ giá trị cuối kỳ (Terminal Value) – tức giá trị này **rất nhạy cảm** với giả định tăng trưởng và tỷ suất chiết khấu. Nhà đầu tư thông minh sẽ kiểm tra kịch bản chậm hơn; do đó GreenPack cũng nên chuẩn bị kịch bản xấu (doanh thu chậm 30% so với kế hoạch) trước khi trình bày. Dự án hoàn vốn (FCF lũy kế dương) vào **Năm 3**.

**Bước 3 – Ngân sách gốc bằng 0 (ZBB) cho OpEx Năm 1.** *Vì sao ZBB?* Ngân sách tăng dần (incremental) thường kế thừa chi phí cũ mà không hỏi "còn cần không". ZBB bắt buộc mỗi gói chi phí phải tự chứng minh giá trị, xếp hạng và cắt từ dưới lên khi vốn hạn chế:

| Gói chi phí | Chi phí (tỷ) | Xếp hạng | Quyết định |
|------------|--------------|----------|-----------|
| Đội bán hàng (5 người) | 1,2 | 1 | Giữ – tạo doanh thu |
| R&D vật liệu | 0,8 | 2 | Giữ – lợi thế cạnh tranh |
| Văn phòng & hành chính | 0,6 | 3 | Giữ – cần thiết |
| Digital marketing | 0,5 | 4 | Giữ – động lực tăng trưởng |
| Quản lý & nhân sự cấp cao | 0,4 | 5 | Giữ |
| Tham gia triển lãm | 0,3 | 6 | Giữ (trong ngân sách) |
| Hoạt động CSR | 0,1 | 7 | **Hoãn sang Năm 2** |
| **OpEx Năm 1 được duyệt** | **3,8** | | (Yêu cầu 3,9 - hoãn 0,1) |

#### Vấn đề 4: Giám sát hiệu suất – Variance + Ratios

**Vì sao kết hợp variance và ratios?** Variance cho biết "lệch ở đâu", ratios cho biết "tổng thể có khỏe không". Báo cáo hằng tháng cần cả hai để ban lãnh đạo nhìn thấy cả cây lẫn rừng.

**Bước 1 – Bảng điểm tháng (tr):**

| Chỉ tiêu | Ngân sách | Thực tế | Chênh lệch | F/U |
|----------|-----------|---------|-----------|-----|
| Doanh thu | 1.250 | 1.330 | +80 (+6,4%) | F |
| Giá vốn (ngân sách 69% DT) | 862,5 | 928 | +65,5 (+7,6%) | U |
| Lợi nhuận gộp | 387,5 | 402 | +14,5 | F |
| Biên gộp | 31,0% | 30,2% | -0,8 điểm % | U |
| Chi phí hoạt động | 250 | 255 | +5 | U |
| **EBIT** | **137,5** | **147** | **+9,5 (+6,9%)** | F |

**Phân rã chênh lệch giá vốn bằng ngân sách linh hoạt**: giá vốn linh hoạt = 69% × 1.330 = 917,7; thực tế 928 ⇒ chênh lệch hiệu quả **-10,3 (U)**. Phần tăng còn lại (917,7 - 862,5 = 55,2) là do bán nhiều hơn – bình thường.

**Bước 2 – Chênh lệch nguyên vật liệu (ví dụ trên một loại nhựa):**

| | Chuẩn | Thực tế |
|---|-------|---------|
| Sản lượng | 100.000 sản phẩm | 100.000 |
| Định mức | 0,10 kg/sp ⇒ 10.000 kg | 10.400 kg |
| Giá | 22.000 VNĐ/kg | 21.500 VNĐ/kg |

$$\text{Chênh lệch giá} = (21.500 - 22.000) \times 10.400 = -5{,}2 \text{ tr (F)}$$

$$\text{Chênh lệch lượng} = (10.400 - 10.000) \times 22.000 = +8{,}8 \text{ tr (U)}$$

Tổng: -5,2 + 8,8 = **+3,6 tr (U)** (kiểm tra: 223,6 - 220,0 = 3,6 ✓). **Diễn giải**: Đàm phán giá tốt (F) bị triệt tiêu bởi hao hụt (U) – nguyên nhân gốc là lô nguyên liệu lỗi số 237. Hành động: khiếu nại nhà cung cấp, siết kiểm tra đầu vào (QC).

**Bước 3 – Ratios chính:** Biên gộp 30,2% (kế hoạch 31%); CCC ~ 25 ngày (mục tiêu ≤ 30); Current Ratio 1,8; D/E 0,8; Inventory Turnover 12x – tất cả trong vùng chấp nhận được (giả định minh họa).

#### Vấn đề 5: Pitch cho nhà đầu tư – Kết hợp tất cả

| Slide | Công cụ | Nội dung chính |
|-------|---------|----------------|
| Thị trường & doanh thu | Financial Accounting | BCTC kiểm toán 3 năm, bảng điều chỉnh sang IFRS |
| Kinh tế đơn vị | ABC | Giá thành từng dòng SP, lộ trình nâng biên Hộp B |
| Sinh lời | Ratios | Biên gộp 31% → 45% trong 5 năm, có lập luận |
| Kế hoạch tăng trưởng | Budgeting | Pro-forma 5 năm, 3 kịch bản, FCF |
| Xuất sắc vận hành | Variance | Bảng điểm hằng tháng, quy trình khắc phục |
| Hiệu quả vốn | DuPont | Phân rã ROE: biên × vòng quay × đòn bẩy |

**Kết quả (giả định minh họa)**: GreenPack huy động **15 tỷ VNĐ** cho **25% cổ phần** (định giá sau đầu tư = 60 tỷ, tương đương ~4x doanh thu hiện tại; ngang với giá trị dự án ước tính ~63,5 tỷ ở trên). Số tiền huy động phủ CapEx 10 tỷ và FCF âm Năm 1 (6,19 tỷ). Cần đối chiếu với điều khoản thực tế khi ký thỏa thuận.

#### Bài học tổng hợp Case 2

> **Accounting tools không hoạt động riêng lẻ.** Sức mạnh đến từ sự kết hợp:
> 1. **Financial Accounting** cung cấp "ngôn ngữ" đáng tin cậy để giao tiếp với bên ngoài
> 2. **Cost Accounting** cho biết "sự thật" về chi phí – Hộp B lãi 13,7% chứ không phải 37%
> 3. **Managerial Accounting** hỗ trợ "quyết định" nội bộ (nên đẩy, nên tăng giá sản phẩm nào)
> 4. **Budgeting** vẽ "lộ trình" đến tương lai, kèm kịch bản
> 5. **Variance Analysis** là "định vị GPS" – biết đang lạc hay đúng hướng
> 6. **Financial Ratios** là "khám sức khỏe" tổng thể

---

## CHƯƠNG III: CASE STUDY 3 (SME VIỆT NAM) – SHOP THỜI TRANG ONLINE "MỘC THU"

### Case Study 3 (SME Việt Nam): Mộc Thu – lãi nhưng thiếu tiền

#### Bối cảnh

**Mộc Thu** (tên giả định) là shop thời trang nữ bán qua Shopee, TikTok Shop, Facebook và website riêng, văn phòng + kho tại TP.HCM, 18 nhân sự. Doanh thu năm 2024 là **12 tỷ VNĐ**, tăng nhanh. Chủ shop tự hào vì "ngày nào cũng có đơn" nhưng cuối năm vẫn **thiếu tiền để nhập hàng Tết** dù báo cáo ghi lợi nhuận gần 1 tỷ. Câu hỏi: *Lãi thế sao lại thiếu tiền? Công cụ kế toán nào chỉ ra nguyên nhân?*

Case này **dựng đủ ba báo cáo tài chính khớp nhau** để cho thấy: lợi nhuận ≠ tiền mặt, và mọi con số đều truy ngược được về một nguồn.

#### Bước 1 – Báo cáo kết quả kinh doanh 2024 (Financial Accounting)

| Khoản mục | Số tiền (tr) | Ghi chú |
|-----------|--------------|--------|
| Doanh thu thuần | 12.000 | |
| Giá vốn hàng bán | (7.200) | 60% doanh thu |
| **Lợi nhuận gộp** | **4.800** | Biên gộp 40% |
| Chi phí bán hàng (quảng cáo, phí sàn, vận chuyển) | (2.400) | 20% doanh thu |
| Chi phí quản lý (lương, thuê kho, phần mềm) | (1.000) | |
| Khấu hao | (120) | |
| **EBIT** | **1.280** | Biên EBIT 10,7% |
| Lãi vay | (80) | |
| **Lợi nhuận trước thuế (EBT)** | **1.200** | |
| Thuế TNDN 20% (giả định) | (240) | |
| **Lợi nhuận sau thuế (LNST)** | **960** | Net Margin 8% |

#### Bước 2 – Bảng cân đối kế toán hai năm

| Khoản mục (tr) | 31/12/2023 | 31/12/2024 | Thay đổi |
|----------------|------------|------------|----------|
| Tiền | 600 | **780** | +180 |
| Phải thu (sàn thanh toán chậm) | 300 | 450 | +150 |
| Hàng tồn kho | 1.500 | 1.800 | +300 |
| Tài sản cố định ròng | 700 | 880 | +180 |
| **Tổng tài sản** | **3.100** | **3.910** | +810 |
| Phải trả nhà cung cấp | 800 | 1.000 | +200 |
| Chi phí phải trả | 100 | 150 | +50 |
| Vay ngắn hạn | 400 | 400 | 0 |
| Vay dài hạn | 500 | 400 | -100 |
| Vốn góp | 800 | 800 | 0 |
| Lợi nhuận giữ lại | 500 | 1.160 | +660 |
| **Tổng nguồn vốn** | **3.100** | **3.910** | +810 |

**Kiểm tra cân đối**: 2023: 800 + 100 + 400 + 500 + 800 + 500 = 3.100 ✓. 2024: 1.000 + 150 + 400 + 400 + 800 + 1.160 = 3.910 ✓. Lợi nhuận giữ lại: 500 + 960 - 300 (cổ tức) = 1.160 ✓. Tài sản cố định: 700 + 300 (mua mới) - 120 (khấu hao) = 880 ✓.

#### Bước 3 – Báo cáo lưu chuyển tiền tệ (phương pháp gián tiếp) – "tiền đi đâu?"

**Vì sao cần báo cáo này?** LNST dựa trên nguyên tắc dồn tích (ghi nhận khi phát sinh, không phải khi thu/chi tiền). Báo cáo lưu chuyển tiền tệ dịch ngược LNST thành dòng tiền thực. Quy tắc: tăng tài sản (không phải tiền) = **tiền bị giữ lại** (trừ); tăng nợ phải trả = **tiền được giữ lại** (cộng).

| Dòng tiền (tr) | Tính toán | Số tiền |
|----------------|-----------|---------|
| LNST | | 960 |
| + Khấu hao (chi phí không dùng tiền) | | +120 |
| - Tăng phải thu | -(450 - 300) | -150 |
| - Tăng hàng tồn kho | -(1.800 - 1.500) | -300 |
| + Tăng phải trả NCC | 1.000 - 800 | +200 |
| + Tăng chi phí phải trả | 150 - 100 | +50 |
| **Dòng tiền từ hoạt động (CFO)** | | **880** |
| Mua tài sản cố định | | -300 |
| **Dòng tiền đầu tư (CFI)** | | **-300** |
| Trả nợ vay dài hạn | | -100 |
| Chia cổ tức | | -300 |
| **Dòng tiền tài chính (CFF)** | | **-400** |
| **Thay đổi tiền thuần** | 880 - 300 - 400 | **+180** |

Tiền đầu kỳ 600 + 180 = **780** = số trên Bảng cân đối ✓.

**Diễn giải**: LNST 960 nhưng CFO là 880 – **hàng tồn kho chiếm 300** và phải thu 150 "nuốt" 450 tiền mặt (một phần được bù bằng 250 nợ NCC và chi phí phải trả). Cộng chi mua tài sản 300, trả nợ và chia cổ tức 400, tiền chỉ tăng 180. Đó là lý do "lãi gần 1 tỷ mà thiếu tiền nhập hàng Tết".

#### Bước 4 – Phân tích chỉ số (Financial Ratios) & DuPont

| Chỉ số | Công thức & phép tính | Kết quả | Diễn giải |
|-------|-----------------------|---------|-----------|
| Current Ratio | (780 + 450 + 1.800) / (1.000 + 150 + 400) = 3.030 / 1.550 | **1,95** | Có vẻ rất an toàn |
| Quick Ratio | (780 + 450) / 1.550 | **0,79** | Dưới 1: nếu không bán được tồn kho, không đủ trả nợ ngắn hạn |
| DIO | [(1.500 + 1.800)/2] / 7.200 × 365 | **83,6 ngày** | Tồn kho quá lâu với thời trang theo mùa |
| DSO | [(300 + 450)/2] / 12.000 × 365 | 11,4 ngày | Chờ sàn thanh toán |
| DPO | [(800 + 1.000)/2] / 7.200 × 365 | 45,6 ngày | Đang khai thác tín dụng NCC |
| **CCC** | 83,6 + 11,4 - 45,6 | **49,4 ngày** | Mỗi đồng vốn bị "đóng băng" gần 50 ngày |
| Interest Coverage | 1.280 / 80 | 16x | Gánh nặng lãi nhẹ |
| ROE (vốn chủ bình quân) | 960 / [(1.300 + 1.960)/2] = 960 / 1.630 | **58,9%** | |

**Vì sao Current Ratio 1,95 vẫn đáng lo?** Hơn một nửa tài sản ngắn hạn là hàng tồn kho (1.800/3.030 = 59%). Quick Ratio loại tồn kho ra để kiểm tra "nếu hàng ế thì sao?" – kết quả 0,79 < 1.

**DuPont (dùng bình quân tài sản và vốn chủ):** Tài sản bình quân = (3.100 + 3.910)/2 = 3.505; vốn chủ bình quân = 1.630.

$$\text{ROE} = \underbrace{\frac{960}{12.000}}_{8\%} \times \underbrace{\frac{12.000}{3.505}}_{3{,}42} \times \underbrace{\frac{3.505}{1.630}}_{2{,}15} = 0{,}08 \times 3{,}42 \times 2{,}15 \approx 58{,}9\%$$

**Diễn giải**: Biên lợi nhuận chỉ 8% (mỏng) nhưng ROE cao do **vòng quay tài sản rất tốt (3,42)** – đặc trưng của mô hình bán online ít tài sản cố định. ROE này **dễ tổn thương**: nếu tồn kho tăng (vòng quay giảm) hoặc phí sàn tăng (biên giảm), ROE giảm rất nhanh.

#### Bước 5 – CVP: điểm hòa vốn và biên an toàn (Managerial Accounting)

Biến phí = giá vốn 60% + chi phí bán hàng 20% = 80% doanh thu ⇒ **CM% = 20%**. Định phí = quản lý 1.000 + khấu hao 120 + lãi vay 80 = 1.200 tr.

$$\text{BEP (doanh thu)} = \frac{1.200}{20\%} = 6.000 \text{ tr}; \quad \text{Biên an toàn} = \frac{12.000 - 6.000}{12.000} = 50\%$$

Kiểm tra: 12.000 × 20% - 1.200 = 1.200 = EBT ✓.

**Diễn giải**: Doanh thu có thể giảm tới 50% mới hòa vốn – vị thế tốt. Tuy nhiên **biên đóng góp chỉ 20%** nên mỗi 1% giảm biên gộp tương đương mất 120 tr lợi nhuận.

#### Bước 6 – Ngân sách và Variance: lợi nhuận gộp lệch ở đâu?

Ngân sách 2024: doanh thu 11.000, biên gộp 42% ⇒ lợi nhuận gộp **4.620**. Thực tế: doanh thu 12.000, biên gộp 40% ⇒ **4.800**. Chênh lệch +180 (F). Tách nguyên nhân:

| Thành phần | Cách tính | Số tiền (tr) |
|-----------|-----------|--------------|
| Chênh lệch khối lượng (bán nhiều hơn) | (12.000 - 11.000) × 42% | **+420 (F)** |
| Chênh lệch biên (giảm giá, khuyến mãi để xả tồn) | (40% - 42%) × 12.000 | **-240 (U)** |
| **Tổng** | | **+180 (F)** |

**Diễn giải**: Doanh thu vượt kế hoạch che lấp việc "bán rẻ để xả hàng tồn". Nếu chỉ nhìn tổng lợi nhuận gộp (+180, có vẻ tốt), chủ shop không thấy được **240 tr bị mất do giảm giá**. Đây là lý do cần tách khối lượng và biên.

#### Bước 7 – Quyết định và khuyến nghị

1. **Hạ vòng quay tồn kho** từ 83,6 xuống 60 ngày: giải phóng tiền mặt $= \dfrac{7.200}{365} \times (83{,}6 - 60) \approx$ **465 tr** – đủ nhập hàng Tết mà không cần vay.
2. **Lập dự báo dòng tiền 13 tuần**, cập nhật hàng tuần, trước mùa cao điểm (Tết, 11.11, 12.12).
3. **Phân tích lợi nhuận từng nhóm sản phẩm bằng ABC/CM** (chi phí chụp ảnh, trả hàng, phí sàn khác nhau theo kênh) để cắt nhóm hàng kém.
4. **Chính sách cổ tức**: chia 300 tr trong khi tiền chỉ tăng 180 tr là quá tay; nên giữ lại làm vốn lưu động cho đến khi CCC được cải thiện.
5. **Theo dõi 4 chỉ số hằng tháng**: DIO, Quick Ratio, biên gộp thực tế so với kế hoạch, tiền mặt khả dụng/chi phí cố định hằng tháng.

#### Bài học tổng hợp Case 3

| Công cụ | Phát hiện |
|---------|-----------|
| Báo cáo lưu chuyển tiền tệ | Lãi 960 nhưng chỉ có 180 tiền tăng thêm – tồn kho "nuốt" tiền |
| Ratios + DuPont | Current Ratio đẹp, Quick Ratio xấu; ROE cao nhờ vòng quay tài sản – mong manh |
| CVP | Biên an toàn 50% – nền tảng vẫn khỏe |
| Variance | Bán nhiều che lấp bán rẻ (-240 tr) |

---

## CHƯƠNG IV: CASE STUDY 4 (THẤT BẠI) – "TECHMART" – Chuỗi bán lẻ điện tử

### Case Study 4 (Thất bại): TechMart – khi công cụ có đủ nhưng không hành động

#### Bối cảnh

**TechMart** (tên giả định) là chuỗi bán lẻ điện tử 15 cửa hàng tại Việt Nam. Doanh thu đỉnh **500 tỷ (2019)** nhưng suy giảm liên tục và đóng 10/15 cửa hàng vào 2023. Câu hỏi không phải "có công cụ kế toán không" mà là: **mỗi công cụ đã gãy ở đâu và vì sao?** Các con số dưới đây là giả định minh họa.

#### Lỗi 1: Financial Accounting – "Số liệu đẹp che đậy thực tế"

| Vấn đề | Chi tiết |
|--------|---------|
| Ghi nhận doanh thu | Ghi doanh thu khi xuất kho cho showroom của chính công ty (chưa bán cho khách hàng cuối) |
| Hàng tồn kho | Không trích lập dự phòng giảm giá hàng điện thoại cũ 2+ năm |
| Hợp đồng thuê | Không công bố/phân tích nghĩa vụ thuê 15 mặt bằng dài hạn (xem lưu ý bên dưới) |
| Khấu hao | Nội thất showroom khấu hao 10 năm (thực tế lỗi thời sau 3 năm) |

*Lưu ý*: Theo VAS, thuê hoạt động thường không đưa lên bảng cân đối – tức bản thân việc "ngoài bảng" **không nhất thiết là sai chuẩn mực**; điểm yếu là ban lãnh đạo **không nhìn thấy** nghĩa vụ thuê đó như một khoản nợ cố định khi phân tích đòn bẩy (IFRS 16 buộc ghi nhận). Cần xác nhận quy định hiện hành.

**Bước 1 – Điều chỉnh lại lợi nhuận 2019** (báo cáo: doanh thu 500, LNST 15, tức Net Margin 3%; tỷ đồng):

| Điều chỉnh | Phép tính | Ảnh hưởng lợi nhuận trước thuế |
|------------|-----------|--------------------------------|
| Khấu hao nội thất đúng tuổi thọ | Nội thất 45 tỷ: 45/3 - 45/10 = 15 - 4,5 | **-10,5** |
| Trích lập dự phòng tồn kho lỗi thời | Ước tính theo tuổi hàng | **-12,0** |
| Đảo doanh thu nội bộ 20 tỷ (biên gộp 12%) | 20 × 12% | **-2,4** |
| **Tổng** | | **-24,9** |

$$\text{LNST điều chỉnh} = 15 + (-24{,}9) \times (1 - 20\%) = 15 - 19{,}9 = \mathbf{-4{,}9 \text{ tỷ}}$$

**Điều chỉnh nợ thuê**: 15 cửa hàng × 1,2 tỷ tiền thuê/năm = 18 tỷ/năm, còn 7 năm, chiết khấu 10%:

$$PV = 18 \times \frac{1 - 1{,}1^{-7}}{0{,}1} = 18 \times 4{,}868 \approx 87{,}6 \text{ tỷ}$$

Vốn chủ 2019 là 100 tỷ, nợ vay 100 tỷ (D/E = 1,0). Cộng nghĩa vụ thuê: $D/E_{điều\,chỉnh} = (100 + 87{,}6)/100 \approx$ **1,88**.

**Diễn giải**: Báo cáo lãi 15 tỷ (ROE 15%) nhưng thực chất **lỗ khoảng 4,9 tỷ**, và đòn bẩy thực tế gần gấp đôi những gì ban lãnh đạo nhìn thấy. Tài sản và lợi nhuận bị thổi phồng, nghĩa vụ bị ẩn đi ⇒ các quyết định đầu tư và vay thêm dựa trên bức tranh sai.

#### Lỗi 2: Cost Accounting – "Không biết chi phí thực"

| Sai lầm | Chi tiết | Hệ quả |
|---------|---------|--------|
| Không ABC | Chi phí khuyến mãi chia đều theo doanh thu | Điện thoại giá rẻ (biên 3%) "ăn" ngân sách khuyến mãi bằng sản phẩm cao cấp (biên 15%) |
| Không P&L từng cửa hàng | Chỉ có P&L hợp nhất | Không biết cửa hàng nào lỗ → giữ tất cả |
| Không P&L theo nhóm hàng | Biên gộp chung 12% | Điện thoại biên 3%, laptop 10%, phụ kiện 37% – điện thoại gần như không có lãi |
| Bỏ qua chi phí logistics | "Miễn phí vận chuyển" xem như marketing | Thực tế logistics = 4% doanh thu, ăn hết biên của nhóm điện thoại |

**Cách làm đúng để thấy sự thật**: Giả sử doanh thu 500 tỷ chia: điện thoại 250 tỷ (biên gộp 3%), laptop 150 tỷ (10%), phụ kiện 100 tỷ (37%). Biên gộp trung bình $= 0{,}5 \times 3\% + 0{,}3 \times 10\% + 0{,}2 \times 37\% = 1{,}5\% + 3{,}0\% + 7{,}4\% = 11{,}9\% \approx 12\%$ (khớp biên gộp 2019). Trừ logistics 4% doanh thu, nhóm điện thoại còn $3\% - 4\% = -1\%$ (lỗ), trong khi **phụ kiện – chỉ 20% doanh thu – tạo ra 62% lợi nhuận gộp** ($37 / 59{,}5$). Công ty chỉ nhìn biên chung 12% sẽ không bao giờ thấy điều đó.

#### Lỗi 3: Budgeting – "Ngân sách lạc quan, không có kịch bản"

| Năm | Doanh thu NS | Thực tế | Chênh lệch | % | Phản ứng |
|-----|--------------|---------|------------|---|----------|
| 2020 | 520 | 380 | -140 (U) | -26,9% | Đổ lỗi COVID |
| 2021 | 450 | 350 | -100 (U) | -22,2% | Đổ lỗi "phục hồi chậm" |
| 2022 | 420 | 280 | -140 (U) | -33,3% | Mới bắt đầu lo |
| 2023 | 350 | 180 | -170 (U) | -48,6% | Quá muộn |

**Sai lầm cấu trúc**:
- **Ngân sách tăng dần** dựa trên đỉnh 2019 – mỗi năm chỉ "giảm nhẹ" so với năm trước, trong khi thị trường chuyển sang online.
- **Không rolling forecast** để cập nhật khi thị trường dịch chuyển.
- **Không kịch bản xấu** – chưa bao giờ mô hình "nếu doanh thu giảm 50% thì sao?".
- **Không ZBB** – vẫn giữ 15 mặt bằng dù 8 cửa hàng dưới điểm hòa vốn.

**Tính tác động của định phí cố định**: nếu định phí thuê 18 tỷ/năm không đổi mà doanh thu giảm từ 500 → 180 tỷ (−64%), với biên gộp 8%: lợi nhuận gộp giảm từ 40 → 14,4 tỷ, không đủ trả tiền thuê 18 tỷ chứ chưa nói lương, điện, lãi vay. **Đòn bẩy hoạt động** (định phí cao) khiến doanh thu giảm ít đã làm lợi nhuận sụp nhiều.

#### Lỗi 4: Variance Analysis – "Biết nhưng không hành động"

```
  BÁO CÁO CHÊNH LỆCH – Hằng tháng

  Tháng 1:  Doanh thu -15% (U)  → "Chờ xem"
  Tháng 2:  Doanh thu -18% (U)  → "Tháng tới sẽ khá hơn"
  Tháng 3:  Doanh thu -22% (U)  → "Đợi đến mùa cao điểm"
  Tháng 4:  Doanh thu -12% (U)  → "Thấy chưa, đang phục hồi!" (nhưng so với cùng kỳ vẫn -20%)
  Tháng 5:  Doanh thu -25% (U)  → "Do thị trường, không phải lỗi mình"
  ...
  Tháng 12: Doanh thu -30% (U)  → "Cần tái cấu trúc" (quá muộn 11 tháng)

  VẤN ĐỀ: Chênh lệch được phát hiện hằng tháng
          nhưng KHÔNG CÓ HÀNH ĐỘNG KHẮC PHỤC
          → Variance Analysis vô nghĩa nếu không hành động
```

**Vì sao điều này xảy ra?** (1) Không có **ngưỡng kích hoạt** (ví dụ "lệch > 10% ba tháng liên tiếp ⇒ họp khẩn"); (2) không gắn người chịu trách nhiệm cho từng chênh lệch; (3) chênh lệch tháng 4 (-12%) bị diễn giải như "phục hồi" vì so với tháng trước chứ không so với kế hoạch/cùng kỳ ("recency bias").

#### Lỗi 5: Financial Ratios & DuPont – "Cờ đỏ bị bỏ qua"

| Chỉ số | 2019 | 2020 | 2021 | 2022 | Cờ đỏ? |
|-------|------|------|------|------|-------|
| Inventory Turnover | 8x | 5x | 3,5x | 2x | Tồn kho ứ đọng |
| DIO (365/Turnover) | 46 | 73 | 104 | 183 ngày | Hàng không bán được |
| Biên gộp | 12% | 10% | 8% | 5% | Chiến tranh giá |
| Current Ratio | 1,5 | 1,2 | 0,9 | 0,6 | Mất thanh khoản |
| D/E | 1,0 | 1,8 | 2,5 | 4,0 | Nợ chồng nợ |
| Interest Coverage | 5x | 2,5x | 1,2x | 0,5x | Không đủ trả lãi |
| ROE | 15% | 5% | -8% | -48% | Mất vốn |
| CCC | 55 | 85 | 120 | 200 ngày | Tiền bị "đóng băng" |

(DIO kiểm tra: 365/8 = 45,6; 365/5 = 73; 365/3,5 = 104,3; 365/2 = 182,5 ✓.)

**DuPont – cho thấy câu chuyện sụp đổ:**

| | 2019 | 2022 | Phép tính |
|---|------|------|-----------|
| Net Margin | 3% | -12% | LNST 2022 = -12% × 280 = -33,6 tỷ |
| Asset Turnover | 2,5x | 0,8x | Tài sản 2019 = 500/2,5 = 200; 2022 = 280/0,8 = 350 |
| Equity Multiplier | 2,0 | 5,0 | Vốn chủ 2019 = 100; 2022 = 350/5 = 70 |
| **ROE** | **15%** | **-48%** | 3% × 2,5 × 2,0 = 15%; -12% × 0,8 × 5,0 = -48% |

(ROE 2022 kiểm tra: -33,6 / 70 = -48% ✓; số vốn chủ cuối kỳ là giả định minh họa.)

**Diễn giải**: ROE rơi từ +15% xuống -48% do cả ba bộ phận cùng xấu: biên lợi nhuận đổi dấu (-15 điểm), vòng quay tài sản giảm 68%, và **đòn bẩy tăng từ 2,0 lên 5,0 khuếch đại phần lỗ**. Equity Multiplier khuếch đại cả chiều thuận lẫn chiều nghịch: khi lãi, nó nhân đôi ROE; khi lỗ, nó nhân lỗ.

#### Tổng hợp: Công cụ nào thất bại ở đâu?

```
┌──────────────────────────────────────────────────────────────┐
│  CHUỖI THẤT BẠI – TechMart                                    │
│                                                                │
│  Financial Accounting     → BCTC gây hiểu lầm (doanh thu sớm, │
│  (File 01)                   tồn kho phồng, lãi 15 → thực lỗ 4,9)│
│       ↓                                                        │
│  Cost Accounting          → Không biết cửa hàng/nhóm hàng nào lỗ│
│  (File 03)                   Trợ giá chéo che giấu lỗ         │
│       ↓                                                        │
│  Budgeting                → NS lạc quan, không kịch bản       │
│  (File 04)                   Định phí quá lớn                  │
│       ↓                                                        │
│  Variance Analysis        → Phát hiện nhưng KHÔNG hành động   │
│  (File 05)                   "Tháng sau sẽ khá hơn"            │
│       ↓                                                        │
│  Financial Ratios         → Cờ đỏ hiện rõ 2+ năm, bị bỏ qua   │
│  (File 06)                                                     │
│       ↓                                                        │
│  KẾT QUẢ: Đóng 10/15 cửa hàng, lỗ lớn                          │
│                                                                │
│  BÀI HỌC: Công cụ VÔ DỤNG nếu thiếu HÀNH ĐỘNG & TRÁCH NHIỆM   │
└──────────────────────────────────────────────────────────────┘
```

#### Bài học Case 4

> 1. **Công cụ chỉ có giá trị khi đi kèm hành động** – TechMart có đủ dữ liệu, nhưng lãnh đạo không sẵn sàng đưa ra quyết định đau đớn (đóng cửa hàng sớm).
> 2. **Mỗi công cụ bổ trợ cho nhau** – BCTC che giấu → Cost Accounting không phát hiện → Ngân sách sai → Variance bị bỏ qua → Ratios cảnh báo muộn.
> 3. **"Thiên kiến lạc quan" (optimism bias) là kẻ thù của kế toán** – Ngân sách lạc quan + "tháng sau sẽ khá hơn" = quyết định muộn.
> 4. **DuPont là "chụp MRI"** – không chỉ thấy ROE mà thấy TẠI SAO ROE đổi (biên, vòng quay hay đòn bẩy).
> 5. **Đặt ngưỡng kích hoạt hành động** (trigger) trước khi sự cố xảy ra, không sau đó.

---

## TỔNG HỢP: SƠ ĐỒ KẾT HỢP 6 PHƯƠNG PHÁP ACCOUNTING

```
┌─────────────────────────────────────────────────────────────┐
│               KHUNG ACCOUNTING TÍCH HỢP                      │
│                                                               │
│                    ┌──────────────┐                           │
│                    │  FINANCIAL   │                           │
│                    │  ACCOUNTING  │ ← Báo cáo cho bên ngoài   │
│                    │  (IFRS/VAS)  │                           │
│                    └──────┬───────┘                           │
│                           │                                   │
│              Cấp dữ liệu  │    Trích xuất dữ liệu             │
│                           │                                   │
│        ┌──────────────────┼──────────────────┐               │
│        │                  │                  │               │
│  ┌─────▼──────┐   ┌──────▼──────┐   ┌───────▼──────┐       │
│  │   COST     │   │ MANAGERIAL  │   │  FINANCIAL   │       │
│  │ ACCOUNTING │   │ ACCOUNTING  │   │   RATIOS     │       │
│  │ (ABC/Job/  │   │ (CVP/       │   │ (DuPont/     │       │
│  │  Process)  │   │  Quyết định)│   │  Thanh khoản)│       │
│  └─────┬──────┘   └──────┬──────┘   └───────┬──────┘       │
│        │                 │                   │               │
│        │    ┌────────────┤                   │               │
│        │    │            │                   │               │
│  ┌─────▼────▼──┐  ┌─────▼──────┐   ┌───────▼──────┐       │
│  │  BUDGETING  │  │  VARIANCE  │   │   KHÁM SỨC   │       │
│  │  & FORECAST │──│  ANALYSIS  │──►│   KHỎE       │       │
│  │  (Kế hoạch) │  │  (Kiểm soát│   │  (Đánh giá)  │       │
│  └─────────────┘  └────────────┘   └──────────────┘       │
│                                                               │
│  Vòng lặp: Plan → Do → Check → Act → Plan (PDCA)             │
└─────────────────────────────────────────────────────────────┘
```

**Khi nào dùng công cụ nào (tóm tắt từ 4 case):**

| Tình huống | Công cụ chính | Case minh họa |
|-----------|--------------|---------------|
| Quyết định mở quán/sản phẩm mới | CVP + Scenario NPV | Case 1 |
| Sản phẩm nào thật sự lãi | ABC + Menu Engineering | Case 1, Case 2 |
| Lãi nhưng thiếu tiền | Báo cáo lưu chuyển tiền + CCC | Case 3 |
| Chi nhánh/bộ phận kém | Ngân sách linh hoạt + Variance | Case 1, Case 3 |
| Gọi vốn / thẩm định | Financial Accounting + FCF + DuPont | Case 2 |
| Phát hiện sớm suy thoái | Ratios + DuPont + Trigger | Case 4 |

---

## PHỤ LỤC: CHECKLIST ÁP DỤNG KẾT HỢP CHO SME TỔNG HỢP

**1. Báo cáo tài chính & nền tảng dữ liệu (Financial Accounting)**
- □ BCTC lập đúng chuẩn đang áp dụng (VAS/IFRS) và đã đối chiếu quy định hiện hành (cần xác nhận)?
- □ Doanh thu ghi nhận đúng thời điểm chuyển giao quyền kiểm soát (không ghi theo xuất kho nội bộ)?
- □ Đã trích lập dự phòng tồn kho/nợ phải thu và khấu hao theo tuổi thọ thực tế?
- □ Có lập báo cáo lưu chuyển tiền tệ, và nó khớp với thay đổi tiền giữa hai kỳ?
- □ Nghĩa vụ thuê dài hạn có được nhìn như nợ cố định khi phân tích đòn bẩy?

**2. Chi phí & quyết định (Cost + Managerial Accounting)**
- □ Biết điểm hòa vốn và biên an toàn: $BEP = \text{Định phí} / \text{CM}$?
- □ Chi phí chung được phân bổ theo hoạt động thực tế (ABC) cho sản phẩm/món/kênh phức tạp?
- □ Có P&L theo từng cửa hàng/dòng sản phẩm/kênh bán, không chỉ P&L hợp nhất?
- □ Phân biệt biên % và đóng góp tuyệt đối (CM) khi chọn sản phẩm đẩy mạnh?
- □ Menu/danh mục sản phẩm được phân loại Star/Plowhorse/Puzzle/Dog và có hành động tương ứng?

**3. Kế hoạch (Budgeting & Forecasting)**
- □ Mọi quyết định đầu tư lớn có ít nhất 3 kịch bản (tốt/cơ sở/xấu) và NPV xác suất?
- □ Biết mức lỗ tối đa ở kịch bản xấu và ngưỡng cắt lỗ?
- □ Có dự báo dòng tiền cuốn chiếu (13 tuần) cho mùa cao điểm?
- □ Ngân sách được rà soát bằng ZBB ít nhất 1 lần/năm cho các khoản chi lớn?
- □ Pro-forma có tính FCF = EBIT(1-t) + khấu hao - CapEx - ΔNWC, không chỉ lợi nhuận?

**4. Kiểm soát (Variance Analysis)**
- □ Báo cáo chênh lệch hằng tháng dùng **ngân sách linh hoạt**, tách khối lượng – giá – hiệu quả?
- □ Chênh lệch nguyên vật liệu tách giá và lượng: $(P_a - P_s)Q_a$ và $(Q_a - Q_s)P_s$?
- □ Có ngưỡng kích hoạt hành động (vd lệch > 10% ba tháng liên tiếp) và người chịu trách nhiệm?
- □ Cửa hàng/bộ phận "đỏ" có kế hoạch khắc phục và thời hạn cắt lỗ?

**5. Sức khỏe tổng thể (Financial Ratios + DuPont)**
- □ Theo dõi: Current/Quick Ratio, DIO – DSO – DPO – CCC, D/E, Interest Coverage, biên gộp?
- □ Phân rã ROE qua DuPont: biên × vòng quay × đòn bẩy; biết ROE cao là nhờ yếu tố nào?
- □ So sánh chỉ số với chuẩn ngành (đã đối chiếu nguồn) và với chính mình qua nhiều kỳ?
- □ Có cảnh báo khi một chỉ số xấu đi 2 kỳ liên tiếp?

**6. Kiểm tra tính nhất quán số liệu (trước khi trình bày)**
- □ Bảng cân đối: Tài sản = Nợ + Vốn chủ? Dòng tiền khớp thay đổi tiền giữa hai kỳ?
- □ Lợi nhuận giữ lại = đầu kỳ + LNST - cổ tức?
- □ Tổng chi phí chung sau phân bổ ABC bằng tổng quỹ ban đầu?
- □ Đã chạy kiểm tra bằng Excel/Python trước khi đưa vào báo cáo hoặc pitch deck?

**7. Bảng công thức tổng hợp dùng trong file**

| Mục đích | Công thức |
|----------|-----------|
| Số dư đảm phí | $CM = \text{Giá} - \text{Biến phí đơn vị}$ |
| Hòa vốn | $Q_{BEP} = \dfrac{\text{Định phí}}{CM}$ ; Biên an toàn $= \dfrac{\text{DT thực tế} - \text{DT hòa vốn}}{\text{DT thực tế}}$ |
| Đơn giá cost driver (ABC) | $\dfrac{\text{Quỹ chi phí hoạt động}}{\text{Tổng driver}}$ |
| NPV | $\sum_{t=1}^{n} \dfrac{CF_t}{(1+r)^t} - I_0$ |
| FCF | $EBIT(1-t) + D\&A - CapEx - \Delta NWC$ |
| Chênh lệch giá NVL | $(P_{thực} - P_{chuẩn}) \times Q_{thực}$ |
| Chênh lệch lượng NVL | $(Q_{thực} - Q_{chuẩn}) \times P_{chuẩn}$ |
| Chênh lệch khối lượng (lợi nhuận gộp) | $(\text{DT thực} - \text{DT NS}) \times \text{biên NS}$ ; Chênh lệch biên $= (\text{biên thực} - \text{biên NS}) \times \text{DT thực}$ |
| CCC | $DIO + DSO - DPO$ |
| DuPont | $ROE = \dfrac{LNST}{DT} \times \dfrac{DT}{TS} \times \dfrac{TS}{VCSH}$ |
| Interest Coverage | $\dfrac{EBIT}{\text{Lãi vay}}$ |

---

## TÀI LIỆU THAM KHẢO

1. **Kaplan & Norton** – "The Balanced Scorecard" (Integrated performance management)
2. **Horngren, Datar & Rajan** – "Cost Accounting: A Managerial Emphasis"
3. **Garrison, Noreen & Brewer** – "Managerial Accounting"
4. **McKinsey** – "Valuation" (Integrated financial analysis)
5. **Harvard Business School** – Case Study methodology
6. **IMA** – Management Accounting Competency Framework
7. **CFA Institute** – Financial Reporting and Analysis (Level I-III)
