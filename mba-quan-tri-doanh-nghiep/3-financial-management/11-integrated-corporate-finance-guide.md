# CẨM NANG TOÀN DIỆN VỀ TÀI CHÍNH DOANH NGHIỆP: QUẢN TRỊ CHIẾN LƯỢC, ĐỊNH LƯỢNG TOÁN HỌC VÀ 13 KHẢO SÁT CASE STUDY CHUYÊN SÂU

> **Mục tiêu**: Hệ thống hóa toàn bộ kiến thức Tài chính Doanh nghiệp (Corporate Finance) cấp độ Thạc sĩ Quản trị Kinh doanh (MBA), tích hợp cơ sở lý thuyết hàn lâm quốc tế với các công thức toán học chứng minh hoàn chỉnh, đi kèm các case study thực tế và phân tích đại diện cho các quyết định chi phối vốn, cấu trúc vốn, quản trị rủi ro danh mục, chính sách cổ tức, sáp nhập & mua bán doanh nghiệp (M&A) và định giá nội tại (Valuation). Tài liệu được cấu trúc chặt chẽ, sử dụng thuật ngữ tài chính chuẩn mực và đảm bảo tính ứng dụng cao.

---

## SƠ ĐỒ DÒNG CHUYỂN VỐN VÀ HỆ THỐNG QUYẾT ĐỊNH TÀI CHÍNH

```
                       THỊ TRƯỜNG TÀI CHÍNH (FINANCIAL MARKETS)
                       (Nhà đầu tư: Cổ đông & Chủ nợ cung cấp vốn)
                                    │
                                    ├─── (1) Phát hành Cổ phiếu / Nợ vay (Huy động vốn)
                                    ▼
                        HẠ TẦNG ĐIỀU HÀNH DOANH NGHIỆP (FIRM)
                 ┌──────────────────────────────────────────────┐
                 │  Quyết định huy động cấu trúc vốn (WACC)     │
                 │  - Cost of Equity (CAPM) & Cost of Debt      │
                 └──────────────┬───────────────────────────────┘
                                │
                                ├─── (2) Tái đầu tư vào tài sản dài hạn (Capital Budgeting)
                                ▼
                       DỰ ÁN SẢN XUẤT KINH DOANH & TÀI SẢN
                 ┌──────────────────────────────────────────────┐
                 │  Tạo dòng tiền hoạt động (Free Cash Flow)   │
                 │  - Quản lý dòng vốn lưu động ròng (CCC)      │
                 └──────────────┬───────────────────────────────┘
                                │
                                ├─── (3) Dòng tiền tạo ra quay ngược về DN (FCF)
                                ▼
                        PHÂN BỔ GIÁ TRỊ VÀ QUYẾT ĐỊNH HOÀN VỐN
                 ┌──────────────────────────────────────────────┐
                 │  - Trả nợ gốc & lãi vay cho chủ nợ           │
                 │  - Chi trả cổ tức & Mua lại cổ phiếu         │
                 │  - Giữ lại lợi nhuận tái đầu tư tăng trưởng   │
                 └──────────────────────────────────────────────┘
```

---

## CÁCH ĐỌC CẨM NANG NÀY

Đây là file **tích hợp** nhiều chủ đề: mỗi chương gồm (1) phần cơ sở lý thuyết, trong đó mỗi công thức đều được giải thích **vấn đề kinh doanh nó giải quyết, logic xây dựng và nguồn gốc lịch sử**, và (2) các case study phân tích từng bước, hiển thị đầy đủ phép tính. Cấu trúc này khác khuôn "1 topic/1 file" của các file 01-10 trong cùng thư mục, nên file không theo khung I-VI mà thay vào đó kết thúc bằng một **PHỤ LỤC: CHECKLIST** tổng hợp.

| Chương | Chủ đề | Case study trong chương |
|--------|--------|--------------------------|
| I | Giá trị thời gian của tiền & Hoạch định ngân sách vốn | Case 1 (GEC - Real Options), Case 2 (X-Refinery - bẫy IRR) |
| II | Chi phí sử dụng vốn (WACC) & Đòn bẩy rủi ro | Case 3 (VTE), Case 4 (Fly-Ind) |
| III | Lý thuyết cấu trúc vốn | Case 5 (R-Center), Case 6 (Ever-G) |
| IV | Quản trị vốn lưu động | Case 7 (S-Mart), Case 8 (Home-Pro) |
| V | Chính sách cổ tức & mua lại cổ phiếu | Case 9 (C-Pharma), Case 10 (H-Hotel) |
| VI | Danh mục đầu tư Markowitz & Risk - Return | Case 11 (Pan-Capital) |
| VII | Sáp nhập & mua bán doanh nghiệp (M&A) | Case 12 (Bev-Co) |
| VIII | Định giá doanh nghiệp tích hợp | Mô hình định giá S-Green |
| IX - X | Chuẩn mực IFRS & Quản trị rủi ro định lượng | Bài tập VaR |
| XI | Tích hợp cho SME Việt Nam | **Case 13 (Quán cà phê "Nhà Rang" - chi nhánh 2)** |
| XII | Tài liệu tham khảo | - |
| Phụ lục | Ma trận tổng hợp, công thức tổng hợp và checklist | - |

**Lưu ý về số liệu**: các doanh nghiệp trong Case 1-12 (GEC, X-Refinery, VTE, ...) là **tình huống giả định mang tính minh họa**, được thiết kế để mỗi con số tự nhất quán về mặt toán học (đã kiểm tra lại bằng tính toán). Chúng không phải số liệu báo cáo tài chính của doanh nghiệp có thật. Đơn vị tiền tệ ghi rõ trong từng case (USD cho tập đoàn lớn, triệu/tỷ VNĐ cho doanh nghiệp Việt Nam).

---

## CHƯƠNG I: GIÁ TRỊ THỜI GIAN CỦA TIỀN (TVM) & HOẠCH ĐỊNH NGÂN SÁCH VỐN (CAPITAL BUDGETING)

Bản chất của mọi quyết định đầu tư tài chính dài hạn nằm ở việc hoán đổi các dòng tiền hiện tại lấy các dòng tiền kỳ vọng lớn hơn trong tương lai dưới sự ảnh hưởng của yếu tố rủi ro và thời gian. Xem thêm cơ sở lý thuyết dự án đầu tư tại [02-capital-budgeting.md](02-capital-budgeting.md).

### 1. Cơ sở lý thuyết toán học chuyên sâu

#### A. Công thức tổng quát về Giá trị Hiện tại của Dòng tiền (Present Value - PV)
Đối với một chuỗi dòng tiền không đều phát sinh liên tục trong $n$ kỳ, giá trị hiện tại được chiết khấu theo tỷ suất lợi nhuận ròng yêu cầu ($r$):

$$PV = \sum_{t=1}^{n} \frac{CF_t}{(1+r)^t}$$

**Tại sao phải chiết khấu? Vấn đề kinh doanh công thức này giải quyết**

Một đồng nhận hôm nay luôn có giá trị hơn một đồng nhận sau này vì ba lý do: (1) **chi phí cơ hội** - đồng tiền nhận sớm có thể đem gửi hoặc đầu tư để sinh lời ngay; (2) **lạm phát** - cùng một đồng tiền mua được ít hàng hơn trong tương lai; (3) **rủi ro** - dòng tiền càng xa càng kém chắc chắn. Công thức PV chỉ là **phép nghịch đảo của lãi kép**: nếu gửi $PV$ với lãi suất $r$ trong $t$ năm thì nhận được $FV = PV(1+r)^t$, suy ra $PV = FV/(1+r)^t$. Mục đích của nó là đưa mọi dòng tiền xuất hiện ở những thời điểm khác nhau về **cùng một mốc thời gian (hôm nay)** để có thể cộng trừ và so sánh trực tiếp với nhau - giống như quy đổi nhiều loại ngoại tệ về VNĐ trước khi cộng.

Về lịch sử, Irving Fisher (*The Theory of Interest*, 1930) là người hệ thống hóa mối quan hệ giữa lãi suất và giá trị thời gian của tiền, còn John Burr Williams (*The Theory of Investment Value*, 1938) là người đầu tiên đề xuất định giá một tài sản bằng cách chiết khấu toàn bộ dòng tiền tương lai của nó - nền tảng của mọi mô hình DCF hiện đại.

*Ví dụ ngắn*: nhận 100 triệu VNĐ sau 3 năm, với tỷ suất yêu cầu 10%/năm, giá trị hiện tại chỉ là $100/(1{,}10)^3 = 75{,}13$ triệu VNĐ. Nói cách khác, bạn chỉ nên trả tối đa 75,13 triệu hôm nay để mua quyền nhận 100 triệu sau 3 năm; trả hơn mức này là chấp nhận lợi suất thấp hơn 10%.

#### B. Chứng minh công thức Hệ số Hiện giá Dòng tiền đều (Annuity Present Value Factor - PVIFA)
Dòng tiền đều $PMT$ phát sinh đều đặn mỗi kỳ từ năm $1$ đến năm $n$. Giá trị hiện tại $PV$ là:

$$PV = \frac{PMT}{1+r} + \frac{PMT}{(1+r)^2} + \dots + \frac{PMT}{(1+r)^n} \quad (1)$$

Nhân cả hai vế với $\frac{1}{1+r}$:

$$PV \left(\frac{1}{1+r}\right) = \frac{PMT}{(1+r)^2} + \frac{PMT}{(1+r)^3} + \dots + \frac{PMT}{(1+r)^{n+1}} \quad (2)$$

Lấy phương trình $(1)$ trừ phương trình $(2)$:

$$PV \left(1 - \frac{1}{1+r}\right) = \frac{PMT}{1+r} - \frac{PMT}{(1+r)^{n+1}}$$

$$PV \left(\frac{r}{1+r}\right) = \frac{PMT}{1+r} \left[1 - \frac{1}{(1+r)^n}\right]$$

$$PV = \frac{PMT}{r} \left[1 - \frac{1}{(1+r)^n}\right]$$

Do đó, hệ số hiện giá dòng tiền đều (PVIFA) được định nghĩa là:

$$PVIFA(r, n) = \frac{1 - (1+r)^{-n}}{r}$$

Hệ số PVIFA cho phép chúng ta dễ dàng tính toán giá trị hiện tại của một hợp đồng vay dài hạn trả góp, hợp đồng thuê tài sản, hoặc giá định giá trị trái phiếu định kỳ trả lãi cố định.

***Bài tập ứng dụng định lượng số 1***: Tính toán giá trị hiện tại ($PV$) của một hợp đồng thuê văn phòng kéo dài $10$ năm ($n=10$), với số tiền thanh toán đều đặn vào cuối mỗi năm là $PMT = 10,000$ USD. Chi phí sử dụng vốn của doanh nghiệp được áp dụng ở mức lãi suất $r = 8\%$/năm.
*   *Bước 1: Tính toán hệ số PVIFA*:
    $$PVIFA(0.08, 10) = \frac{1 - (1+0.08)^{-10}}{0.08} = \frac{1 - 0.4632}{0.08} = 6.7101$$
*   *Bước 2: Xác định Giá trị hiện tại của chuỗi tiền*:
    $$PV = 10,000 \times 6.7101 = \textbf{67,101 USD}$$

#### C. Công thức Dòng tiền đều vô hạn tăng trưởng (Growing Perpetuity)
Chứng minh toán học cho giá trị hiện tại của dòng tiền đều tăng trưởng mãi mãi với tốc độ không đổi ($g$), điều kiện $r > g$:

$$PV = \sum_{t=1}^{\infty} \frac{CF_1(1+g)^{t-1}}{(1+r)^t}$$

Áp dụng công thức tổng cấp số nhân lùi vô hạn với công bội $q = \frac{1+g}{1+r}$, do $r > g \Rightarrow q < 1$:

$$PV = \frac{CF_1}{1+r} \times \frac{1}{1 - q} = \frac{CF_1}{1+r} \times \frac{1}{1 - \frac{1+g}{1+r}} = \frac{CF_1}{1+r} \times \frac{1+r}{(1+r) - (1+g)} = \frac{CF_1}{r - g}$$

Đây là công thức nền tảng trong tài chính doanh nghiệp để tính toán Giá trị cuối cùng của doanh nghiệp (Terminal Value) trong các mô hình định giá DCF.

#### D. Ghép lãi liên tục (Continuous Compounding)
Khi khoảng thời gian ghép lãi tiến về vô cùng nhỏ (tần suất ghép lãi $m \to \infty$), giá trị tương lai $FV$ của khoản đầu tư ban đầu $PV$ sau $t$ năm được tính bằng cơ số Euler $e$:

$$FV_t = PV \times e^{r \times t}$$

Lãi suất hiệu dụng năm (Effective Annual Rate - EAR) tương ứng được tính bằng công thức:

$$EAR = e^r - 1$$

Việc ghép lãi liên tục ngày càng trở nên phổ biến trong các mô hình tài chính định lượng cao cấp, giao dịch phái sinh (như mô hình Black-Scholes) và định giá tài sản có mức độ thanh khoản cao.

#### E. Hoạch định dòng tiền dự án (Capital Budgeting Cash Flow Estimation)
Xây dựng dòng tiền dự án đòi hỏi việc tuân thủ nguyên tắc dòng tiền tăng thêm (Incremental Cash Flows). Dòng tiền dự án gồm 3 cấu phần lớn:
1.  **Vốn đầu tư ban đầu (Initial Outlay - $CF_0$)**:
    $$CF_0 = \text{CapEx} + \Delta NWC - \text{Salva}_0 + T_c \times (\text{Salva}_0 - \text{Book}_0)$$
    Trong đó, $\text{CapEx}$ là chi phí mua sắm tài sản, $\Delta NWC$ là nhu cầu vốn lưu động ròng ban đầu, $\text{Salva}_0$ và $\text{Book}_0$ lần lượt là giá bán thanh lý và giá trị sổ sách của tài sản cũ bị thay thế.
2.  **Dòng tiền hoạt động hàng năm (Operating Cash Flows - OCF)**:
    $$OCF = (\text{Sales} - \text{OpEx} - \text{Depr}) \times (1 - T_c) + \text{Depr}$$
    $$OCF = (\text{Sales} - \text{OpEx}) \times (1 - T_c) + T_c \times \text{Depr}$$
    Biểu thức thứ hai bộc lộ rõ vai trò của "Lá chắn thuế khấu hao" ($T_c \times \text{Depr}$).
3.  **Dòng tiền thanh lý kết thúc dự án (Terminal Cash Flow - TCF)**:
    $$TCF = \text{Salva}_n - T_c \times (\text{Salva}_n - \text{Book}_n) + \Delta NWC_{\text{thu hồi}}$$

#### F. Ảnh hưởng của Lạm phát đến Hoạch định vốn (Inflation and Capital Budgeting)
Khi ước tính dòng tiền dự án, các nhà quản lý luôn phải đồng bộ hóa cách hạch toán lạm phát. Dòng tiền thực tế có hai loại:
*   *Dòng tiền danh nghĩa (Nominal Cash Flows)*: Phản ánh trực tiếp mức giá của từng thời kỳ chịu ảnh hưởng của lạm phát.
*   *Dòng tiền thực tế (Real Cash Flows)*: Biểu thị theo sức mua của thời điểm hiện tại.
Nguyên tắc đồng bộ: Nếu dòng tiền tính theo danh nghĩa thì tỷ suất chiết khấu phải dùng danh nghĩa; nếu dòng thực tế, tỷ suất chiết khấu phải đưa về mức thực. Theo phương trình Fisher:
$$1 + r_{\text{nominal}} = (1 + r_{\text{real}}) \times (1 + \text{Inflation})$$

#### G. Khác biệt cốt lõi giữa các tiêu chuẩn quyết định đầu tư: NPV, IRR, MIRR, PI và DPP
*   **Giá trị Hiện tại ròng (NPV - Net Present Value)**: Đo lường mức độ thay đổi trực tiếp tới tài sản của cổ đông. Đây là công cụ tối cao và chính xác nhất trong mọi hoàn cảnh đầu tư:
    $$NPV = \sum_{t=1}^{n} \frac{CF_t}{(1+r)^t} - CF_0$$
*   **Tỷ suất Sinh lời Nội tại (IRR - Internal Rate of Return)**: Là tỷ suất chiết khấu làm cho NPV của dự án bằng 0:
    $$NPV(IRR) = \sum_{t=1}^{n} \frac{CF_t}{(1+IRR)^t} - CF_0 = 0$$
    *Hạn chế*: Phương thức định vị IRR ngầm định rằng tất cả các dòng tiền trung hạn sinh ra sẽ được **tái đầu tư với lãi suất bằng chính tỷ lệ IRR**. Điều này rất phi thực tế đối với các dự án có tỷ lệ siêu lợi nhuận (IRR rất cao). Đồng thời, nếu dòng tiền đổi dấu nhiều lần (ví dụ: dòng tiền âm vào cuối vòng đời dự án do chi phí xử lý môi trường hoặc sửa chữa lớn), phương trình đa thức sẽ xuất hiện nhiều giá trị IRR (Multiple IRRs).
*   **Tỷ suất Sinh lời Nội tại sửa đổi (MIRR - Modified Internal Rate of Return)**: Khắc phục hạn chế của IRR bằng cách giả định toàn bộ dòng tiền thu về trung hạn được tái đầu tư với chi phí vốn của doanh nghiệp ($WACC$ - $r$) và chi phí tài trợ vốn đầu tư ban đầu chiết khấu ngược với lãi suất tài trợ ($f$):
    $$MIRR = \sqrt[n]{\frac{TV(Inflows @ r)}{PV(Outflows @ f)}} - 1$$
    Trong đó $TV(Inflows @ r)$ là giá trị tích lũy tương lai (Terminal Value) tính đến cuối vòng đời dự án của toàn bộ dòng tiền hoạt động thu về:
    $$TV = \sum_{t=1}^{n} CF_t (1+r)^{n-t}$$
*   **Chỉ số khả năng sinh lời (Profitability Index - PI)**: Đo lường hiệu quả sử dụng một đồng vốn đầu tư ban đầu. Đặc biệt hữu dụng trong bối cảnh phân bổ vốn bị giới hạn (Capital Rationing):
    $$PI = \frac{\sum_{t=1}^{n} \frac{CF_t}{(1+r)^t}}{CF_0} = 1 + \frac{NPV}{CF_0}$$
*   **Thời gian hoàn vốn có chiết khấu (Discounted Payback Period - DPP)**: Số năm cần thiết để tổng giá trị hiện tại của các dòng tiền thu về bù đắp được chi phí đầu tư ban đầu. Đây là thước đo hữu ích cho việc đánh giá rủi ro thanh khoản ngắn hạn:
    $$\sum_{t=1}^{DPP} \frac{CF_t}{(1+r)^t} = CF_0$$

**Tại sao NPV được xem là tiêu chuẩn tối cao, còn IRR chỉ là thước đo phụ?**

NPV trả lời đúng câu hỏi của cổ đông: *"Dự án này làm giàu thêm cho tôi bao nhiêu đồng (tính theo tiền hôm nay)?"*. Vì NPV tính bằng tiền nên có tính **cộng được** (NPV của hai dự án độc lập bằng tổng NPV từng dự án), và nó dùng đúng chi phí cơ hội của vốn làm tỷ suất chiết khấu. IRR trả lời một câu hỏi khác - *"dự án sinh lời bao nhiêu phần trăm mỗi năm?"* - nên dễ trực quan với nhà quản lý (thích nói bằng %), nhưng có ba điểm yếu: (1) bỏ qua quy mô (dự án đầu tư 10 triệu với IRR 50% chưa chắc tốt hơn dự án 1 tỷ với IRR 20%); (2) ngầm giả định tái đầu tư ở chính IRR; (3) có thể có nhiều nghiệm hoặc vô nghiệm khi dòng tiền đổi dấu nhiều lần. **MIRR** ra đời để vá hai lỗ hổng sau cùng bằng cách *áp đặt* một mức tái đầu tư thực tế (thường là WACC) thay vì để công thức tự giả định; **PI** (chỉ số sinh lời) chuẩn hóa NPV theo vốn bỏ ra để xếp hạng khi bị giới hạn ngân sách; **DPP** bổ sung thông tin về rủi ro thanh khoản (bao lâu mới lấy lại vốn).

#### H. Lý thuyết Quyền chọn Thực (Real Options) trong Capital Budgeting
Các phương pháp thẩm định đầu tư truyền thống (NPV tĩnh) thường bỏ qua khả năng ứng phó linh hoạt của nhà quản lý trước các thay đổi bất thường của thị trường. Lý thuyết Quyền chọn thực tế bổ sung giá trị linh hoạt này vào công thức:

$$\text{NPV}_{\text{Tích Hợp}} = \text{NPV}_{\text{Tĩnh}} + \text{Giá trị Quyền chọn thực}$$

Các quyền chọn thực bao gồm:
*   *Quyền chọn trì hoãn đầu tư (Option to Delay)*: Quyền chờ đợi thông tin chính sách rõ ràng hơn trước khi rót vốn lớn.
*   *Quyền chọn mở rộng kinh doanh (Option to Expand)*: Quyền nâng công suất nhà máy nếu nhu cầu thực tế vượt xa kỳ vọng dự báo ban đầu.
*   *Quyền chọn thu hẹp/từ bỏ (Option to Abandon)*: Quyền chấm dứt sớm dự án và bán thanh lý tài sản để thu hồi gốc vốn ngăn khoản lỗ phát sinh thêm.

**Tại sao cần Real Options? Logic đằng sau công thức**

NPV truyền thống ngầm giả định doanh nghiệp "cam kết cứng": một khi đã duyệt dự án thì phải thực hiện đúng kế hoạch đến cùng, bất kể thị trường thay đổi. Thực tế quản lý luôn có quyền điều chỉnh - hoãn, mở rộng, hoặc dừng lại - và **quyền (không phải nghĩa vụ) hành động** đó có giá trị, giống hệt quyền chọn mua (call option) trên thị trường tài chính mà Black-Scholes (1973) đã định giá. Stewart Myers là người đặt ra thuật ngữ "real options" (1977) khi nhận thấy tài sản thực của doanh nghiệp cũng chứa các quyền chọn như vậy. Quyền chọn có giá trị lớn nhất khi **độ bất định cao** (vì phía xấu được chặn lại bằng quyền từ bỏ, còn phía tốt vẫn hưởng trọn) và khi doanh nghiệp có thể chờ thêm thông tin trước khi chi tiền không hoàn lại. Case 1 bên dưới tính toán chi tiết điều này.

---

### 2. Case Study 1 (Thành công): TẬP ĐOÀN ĐIỆN LỰC GEC – Đầu tư Điện gió ngoài khơi Bình Thuận nhờ Real Options

#### Bối cảnh

Tập đoàn Năng lượng tái tạo GEC đang cân nhắc dự án điện gió ngoài khơi công suất 500MW tại thềm lục địa Bình Thuận. Vốn đầu tư ban đầu là **800 triệu USD** ($CF_0$). Vấn đề lớn nhất không nằm ở kỹ thuật mà ở **chính sách giá điện (FIT - Feed-in Tariff)** của Chính phủ chưa có khung pháp lý rõ ràng. Hai kịch bản cùng có xác suất 50%:

| Kịch bản | Giá bán điện | Dòng tiền đều hằng năm (20 năm) |
|----------|--------------|----------------------------------|
| Thuận lợi (High) | Giá FIT cao | 120 triệu USD/năm |
| Bất lợi (Low) | Giá FIT thấp | 70 triệu USD/năm |

Chi phí sử dụng vốn $WACC = 10\%$.

#### Bước 1: Tính NPV tĩnh (đầu tư ngay lập tức)

Cả hai kịch bản đều là dòng tiền đều 20 năm nên dùng hệ số hiện giá PVIFA (chứng minh ở mục 1.B):

$$PVIFA(10\%, 20) = \frac{1 - (1{,}10)^{-20}}{0{,}10} = 8{,}5136$$

$$PV_{\text{High}} = 120 \times 8{,}5136 = 1.021{,}63 \text{ triệu USD} \qquad PV_{\text{Low}} = 70 \times 8{,}5136 = 595{,}95 \text{ triệu USD}$$

NPV của từng kịch bản (nếu biết chắc kịch bản đó xảy ra):

$$NPV_{\text{High}} = 1.021{,}63 - 800 = +221{,}63 \qquad NPV_{\text{Low}} = 595{,}95 - 800 = -204{,}05 \text{ (triệu USD)}$$

NPV tĩnh kỳ vọng (bình quân theo xác suất):

$$\text{NPV}_{\text{Tĩnh}} = 0{,}5 \times 221{,}63 + 0{,}5 \times (-204{,}05) = \textbf{+8{,}79 triệu USD}$$

**Diễn giải**: NPV kỳ vọng dương nhẹ nên theo quy tắc "NPV > 0 thì nhận" dự án vẫn được duyệt. Nhưng con số +8,79 triệu chỉ chiếm ~1% vốn đầu tư và là kết quả của việc **bù trừ** giữa +221,63 và -204,05. Nếu GEC rót 800 triệu ngay hôm nay và rơi vào kịch bản bất lợi, khoản lỗ là **204,05 triệu USD** - đủ làm tổn thương bảng cân đối của cả tập đoàn. Xác suất hòa vốn kỳ vọng là $p^* = (800 - 595{,}95)/(1.021{,}63 - 595{,}95) = 47{,}9\%$: chỉ cần xác suất giá cao thấp hơn 47,9% là dự án chuyển sang NPV âm.

#### Bước 2: Mua quyền chọn trì hoãn (Option to Delay)

GEC chi **15 triệu USD** để mua quyền khảo sát địa chất và giữ độc quyền khu vực biển trong 2 năm. Sau 2 năm, chính sách giá điện được công bố và hết bất định. Quy tắc quyết định tại năm 2:

- Nếu giá cao ($PV_{\text{High}} = 1.021{,}63 > 800$): đầu tư, thu về $NPV = 221{,}63$ (tính tại năm 2).
- Nếu giá thấp ($PV_{\text{Low}} = 595{,}95 < 800$): **bỏ dự án**, chỉ mất 15 triệu đã chi, tức giá trị thu về là $\max(595{,}95 - 800,\ 0) = 0$.

Kỳ vọng NPV tại năm 2 là $0{,}5 \times 221{,}63 + 0{,}5 \times 0 = 110{,}81$ triệu USD. Chiết khấu 2 năm về hôm nay và trừ phí quyền chọn:

$$\text{NPV}_{\text{Tích hợp}} = -15 + \frac{0{,}50 \times \max(PV_{\text{High}} - 800,\ 0) + 0{,}50 \times \max(PV_{\text{Low}} - 800,\ 0)}{(1{,}10)^2} = -15 + \frac{110{,}81}{1{,}21} = -15 + 91{,}58 = \textbf{+76{,}58 triệu USD}$$

$$\text{Giá trị Quyền chọn thực} = 76{,}58 - 8{,}79 = \textbf{67{,}79 triệu USD}$$

#### Bước 3: Kiểm tra độ nhạy theo xác suất kịch bản thuận lợi

| Xác suất giá cao | NPV tĩnh (đầu tư ngay) | NPV tích hợp (trì hoãn 2 năm) | Lợi thế của trì hoãn |
|------------------|------------------------|-------------------------------|----------------------|
| 30% | -76,35 | +39,95 | +116,30 |
| 50% | +8,79 | +76,58 | +67,79 |
| 70% | +93,92 | +113,21 | +19,29 |

#### Diễn giải ý nghĩa kinh doanh

1. Quyền chọn **phát huy giá trị lớn nhất khi bất định cao** (xác suất 30% - 50%): lúc đó đầu tư ngay là bài toán lỗ hoặc hòa, nhưng trì hoãn vẫn cho NPV dương rõ rệt. Khi chắc chắn gần như 100% giá cao thì quyền chọn mất dần giá trị (chờ đợi chỉ làm mất 2 năm dòng tiền).
2. Giá trị quyền chọn **trước khi trừ phí** là $91{,}58 - 8{,}79 = 82{,}79$ triệu USD, nên đây là **mức phí tối đa hợp lý GEC có thể trả**; mức phí thực tế 15 triệu USD là "món hời", để lại giá trị ròng 67,79 triệu USD cho GEC.
3. Cái giá của quyền chọn là **chi phí chờ đợi**: 2 năm doanh thu bị bỏ lỡ, rủi ro đối thủ chiếm khu vực biển và rủi ro khung pháp lý theo hướng xấu hơn mà mô hình đã giả định bằng 0.

**Bài học**: không duyệt dự án lớn có độ bất định chính sách cao chỉ bằng một con số NPV tĩnh. Hãy hỏi "có thể chia dự án thành các giai đoạn, trả phí nhỏ để mua thêm thông tin trước khi cam kết vốn lớn không?". Tư duy này áp dụng được cho cả SME khi thuê thử mặt bằng ngắn hạn trước khi ký hợp đồng 5 năm (xem Case 13).

---

### 3. Case Study 2 (Thất bại): DỰ ÁN LỌC DẦU X-REFINERY – Bẫy IRR ảo khi dòng tiền đổi dấu nhiều lần

#### Bối cảnh

Ban quản trị dự án lọc dầu X-Refinery trình hội đồng đầu tư một mô hình Excel với kết quả **IRR = 24,5%/năm**, vượt xa chi phí vốn $WACC = 12\%$ của tập đoàn, kết luận "duyệt ngay". Để làm rõ cơ chế sai lầm, ta đơn giản hóa dòng tiền dự án thành ba mốc thời gian (đơn vị: triệu USD):

| Mốc thời gian | Diễn biến | Dòng tiền |
|---------------|-----------|-----------|
| Năm 0 | Xây dựng nhà máy | -1.000 |
| Năm 1 | Khách hàng bao tiêu thanh toán trước toàn bộ hợp đồng cung cấp dài hạn | +2.845 |
| Năm 2 | Chi phí nhập dầu thô để thực hiện hợp đồng, đại tu và xử lý môi trường | -1.992 |

#### Bước 1: Vì sao Excel báo IRR = 24,5%?

IRR là nghiệm của phương trình $NPV(r) = 0$. Đặt $v = 1/(1+r)$, phương trình trở thành $1.992\,v^2 - 2.845\,v + 1.000 = 0$ - **phương trình bậc hai, có hai nghiệm**: $v_1 = 0{,}8032$ và $v_2 = 0{,}625$, tương ứng $r_1 = \textbf{24,5\%}$ và $r_2 = \textbf{60\%}$. Dòng tiền đổi dấu hai lần (âm → dương → âm) nên xuất hiện **nhiều IRR (Multiple IRR)**. Excel chỉ trả về nghiệm gần giá trị đoán ban đầu, nên ban dự án thấy 24,5% và dừng lại.

#### Bước 2: Kiểm tra bằng NPV tại các mức chiết khấu

$$NPV(12\%) = -1.000 + \frac{2.845}{1{,}12} - \frac{1.992}{(1{,}12)^2} = -1.000 + 2.540{,}18 - 1.588{,}01 = \textbf{-47{,}83 triệu USD}$$

| Tỷ suất chiết khấu | 0% | 10% | 12% | 20% | 24,5% | 30% | 50% | 60% | 70% |
|--------------------|----|-----|-----|-----|-------|-----|-----|-----|-----|
| NPV (triệu USD) | -147,00 | -59,92 | **-47,83** | -12,50 | 0,00 | +9,76 | +11,33 | 0,00 | -15,74 |

NPV chỉ dương trong khoảng chiết khấu **24,5% đến 60%**; tại $WACC = 12\%$ - mức chi phí vốn thực của tập đoàn - NPV **âm**. "IRR = 24,5% > WACC = 12%" thoạt nhìn là tín hiệu duyệt dự án, nhưng quy tắc "IRR > WACC thì nhận" chỉ đúng với dòng tiền thông thường (đổi dấu một lần). Với dòng tiền này, IRR cho tín hiệu sai.

#### Bước 3: Tính MIRR để phá vỡ giả định tái đầu tư

MIRR giả định dòng tiền thu về được tái đầu tư ở WACC (12%) và chi phí đền bù được tài trợ ở WACC:

$$TV(\text{Inflows}) = 2.845 \times 1{,}12^{\,2-1} = 3.186{,}40 \qquad PV(\text{Outflows}) = 1.000 + \frac{1.992}{1{,}12^2} = 2.588{,}01$$

$$MIRR = \sqrt[2]{\frac{3.186{,}40}{2.588{,}01}} - 1 = \sqrt{1{,}2312} - 1 = \textbf{10{,}96\%}$$

MIRR = 10,96% **thấp hơn** WACC = 12%, khớp với kết luận NPV âm: dự án phá hủy giá trị.

#### Hậu quả và bài học

X-Refinery vẫn khởi công vì IRR 24,5%. Khi tiền ứng trước của khách hàng được dùng hết, nghĩa vụ chi ở năm 2 không có nguồn bù đắp tương ứng, dự án rơi vào thiếu hụt thanh khoản, phải bán tài sản giá rẻ.

- **Dòng tiền đổi dấu nhiều lần** (đại tu, hoàn nguyên môi trường, tiền ứng trước) là dấu hiệu bắt buộc phải dùng **NPV hoặc MIRR**, không dùng IRR đơn thuần.
- Luôn vẽ **đồ thị NPV theo tỷ suất chiết khấu** để thấy toàn bộ hình dạng thay vì tin một con số.
- Khi một dự án có khoản thu lớn sớm (tiền ứng trước) và khoản chi lớn muộn, hãy xem đó là **khoản vay ngầm** và đánh giá đúng chi phí của nó.

---

## CHƯƠNG II: CHI PHÍ SỬ DỤNG VỐN (COST OF CAPITAL - WACC) & ĐÒN BẨY RỦI RO

Chi phí sử dụng vốn bình quân gia quyền ($WACC$) là rào cản tối thiểu (Hurdle Rate) mà một dự án đầu tư của doanh nghiệp phải vượt qua để có thể tạo thêm giá trị thực thặng dư cho cổ đông sở hữu. Chi tiết cấu thành tỷ trọng tài sản nợ/vốn xem tại [03-cost-of-capital.md](03-cost-of-capital.md).

### 1. Cơ sở lý thuyết toán học chuyên sâu

#### A. Công thức tổng quát tính WACC (Weighted Average Cost of Capital)
$$WACC = \left( \frac{E}{V} \times r_e \right) + \left( \frac{D}{V} \times r_d \times (1 - T_c) \right) + \left( \frac{P}{V} \times r_p \right)$$

Trong đó:
*   $E, D, P$: Giá trị thị trường lần lượt của Vốn chủ sở hữu (Equity), Nợ vay (Debt), và Cổ phiếu ưu đãi (Preferred Stock).
*   $V = E + D + P$: Tổng cấu trúc vốn của doanh nghiệp.
*   $r_e$: Chi phí sử dụng vốn chủ sở hữu (Cost of Equity).
*   $r_d$: Chi phí sử dụng nợ vay của DN trước thuế (Cost of Debt).
*   $r_p$: Chi phí sử dụng vốn cổ phần ưu đãi (Cost of Preferred Stock):
    $$r_p = \frac{D_{pref}}{P_{pref} \times (1 - f)}$$
    (Với $D_{pref}$ là cổ tức ưu đãi cố định hàng năm, $P_{pref}$ là giá phát hành hiện tại, $f$ là tỷ lệ chi phí phát hành).
*   $T_c$: Thuế suất thuế thu nhập doanh nghiệp (Corporate Tax Rate).

**Tại sao WACC có dạng bình quân gia quyền, và tại sao chỉ chi phí nợ được nhân $(1 - T_c)$?**

Mỗi đồng vốn doanh nghiệp huy động đều có "giá" mà nhà cung cấp vốn đòi hỏi: chủ nợ đòi lãi vay, cổ đông đòi lợi suất kỳ vọng. Một dự án chỉ tạo giá trị nếu lợi suất của nó **vượt mức bình quân của tất cả các nguồn vốn đã tài trợ cho nó** - đó chính là lý do WACC là một trung bình có trọng số: trọng số là **tỷ trọng giá trị thị trường** của từng nguồn (không dùng giá trị sổ sách, vì chi phí cơ hội mà nhà đầu tư đang yêu cầu gắn với giá trị thị trường hiện tại, không phải số tiền đã góp trong quá khứ). Nhân $(1 - T_c)$ chỉ ở thành phần nợ vì **lãi vay được khấu trừ khi tính thuế thu nhập doanh nghiệp** - mỗi đồng lãi vay trả ra thực chất chỉ "đau" $(1 - T_c)$ đồng, phần còn lại do ngân sách nhà nước gánh; còn cổ tức trả sau thuế nên không có khoản tiết kiệm tương tự. Nền tảng lý thuyết của công thức này đến từ công trình năm 1958 và 1963 của Modigliani - Miller (xem Chương III).

*Ví dụ ngắn*: vốn 60% chủ sở hữu với $r_e = 15\%$ và 40% nợ vay lãi 10%, $T_c = 20\%$ cho $WACC = 0{,}6 \times 15\% + 0{,}4 \times 10\% \times 0{,}8 = 9\% + 3{,}2\% = 12{,}2\%$. Dự án phải sinh lời trên 12,2% mới tạo giá trị cho cổ đông.

#### B. Mô hình Định giá Tài sản Vốn (CAPM - Capital Asset Pricing Model) định vị Cost of Equity
Mô hình CAPM giả lập mối quan hệ tuyến tính giữa lợi nhuận yêu cầu của một tài sản và rủi ro hệ thống của nó.
Công thức CAPM:
$$r_e = R_f + \beta \times [E(R_m) - R_f]$$

*   **Chứng minh nguồn gốc (Security Market Line - SML)**:
    Theo lý thuyết danh mục đầu tư, phần bù rủi ro của một cổ phiếu đơn lẻ tỷ lệ thuận với đóng góp rủi ro của nó vào danh mục thị trường rộng ($COV(R_i, R_m)$). Ta có định nghĩa Beta:
    $$\beta_i = \frac{COV(R_i, R_m)}{\sigma_m^2}$$
    Trong trạng thái thị trường cân bằng, tỷ suất sinh lời vượt trội trên mỗi đơn vị rủi ro hệ thống của mọi tài sản phải bằng nhau và bằng phần bù rủi ro thị trường ($E(R_m) - R_f$). Do đó, ta thiết lập được phương trình SML biểu diễn CAPM như trên.

**Tại sao chỉ rủi ro hệ thống (Beta) mới được "thưởng" trong CAPM?**

Trước thập niên 1960, giới đầu tư chưa có cách định lượng rõ ràng *"cổ phiếu rủi ro hơn thì phải đòi lợi suất cao hơn bao nhiêu"*. William Sharpe (1964), cùng với John Lintner (1965) và Jan Mossin (1966), phát triển CAPM từ lý thuyết danh mục của Markowitz (Sharpe nhận giải Nobel Kinh tế năm 1990). Logic cốt lõi: rủi ro **riêng của từng doanh nghiệp** (đình công, sản phẩm lỗi, đổi CEO) có thể bị **triệt tiêu bằng đa dạng hóa** nên thị trường không trả thêm phần thưởng cho nó; chỉ phần rủi ro **không thể đa dạng hóa** - phản ứng của cổ phiếu trước biến động chung của toàn thị trường, đo bằng Beta - mới được bù đắp. Vì vậy chi phí vốn chủ sở hữu là lãi suất phi rủi ro cộng với phần bù rủi ro thị trường nhân với Beta.

*Lưu ý khi áp dụng ở Việt Nam*: $R_f$ thường lấy từ lợi suất trái phiếu Chính phủ kỳ hạn 10 năm; phần bù rủi ro thị trường ($ERP$) của thị trường mới nổi cao hơn thị trường phát triển; với doanh nghiệp nhỏ chưa niêm yết, thực hành phổ biến là cộng thêm **phần bù quy mô/thanh khoản** (size/illiquidity premium) vì nhà đầu tư không thể dễ dàng bán lại phần vốn của mình (xem Case 13).

#### C. Giao điểm tối ưu: Đường MCC và Đường cơ hội đầu tư IOS (Investment Opportunity Schedule)
Điểm giao nhau giữa đường Chi phí vốn biên mậu (MCC) và Đường cơ hội đầu tư (IOS) xác định quy mô của ngân sách đầu tư tối ưu của doanh nghiệp (Optimal Capital Budget). 
*   *Lý thuyết*: Doanh nghiệp chỉ nên thông qua các dự án đầu tư có tỷ suất sinh lời vượt trên chi phí vốn biên mậu gánh chịu để tài trợ chính cho dự án đó. Điểm cắt nhau này triệt tiêu hoàn toàn sự lãng phí vốn và tối đa hóa của cải tích lũy của cổ đông.

#### D. Công thức Hamada giải phóng và tái áp dụng đòn bẩy rủi ro hệ thống (Unlevering & Relevering Beta)
Khi một công ty thay đổi cấu trúc vốn (thay tỷ lệ nợ vay), hệ số rủi ro hệ thống $\beta$ sẽ dịch chuyển tương ứng do chịu thêm rủi ro tài chính của áp lực nợ vay. 
*   **Hệ số Beta không có đòn bẩy rủi ro tài sản thuần (Unlevered Asset Beta - $\beta_u$)**: Phản ánh rủi ro kinh doanh thuần của ngành sản xuất:
    $$\beta_u = \frac{\beta_l}{1 + (1 - T_c) \times \frac{D}{E}}$$
*   **Hệ số Beta có đòn bẩy nợ của cấu trúc mới (Relevered Equity Beta - $\beta_{lh}$)**:
    $$\beta_{lh} = \beta_u \times \left[ 1 + (1 - T_c) \times \frac{D_{new}}{E_{new}} \right]$$

**Tại sao Beta thay đổi theo đòn bẩy? Logic của công thức Hamada**

Beta quan sát được trên thị trường ($\beta_l$) là Beta của *cổ phiếu*, tức đã bao gồm hai lớp rủi ro: **rủi ro kinh doanh** (ngành nghề, chu kỳ doanh thu, đòn bẩy hoạt động) và **rủi ro tài chính** (do vay nợ). Khi so sánh với đối thủ cùng ngành có cơ cấu vốn khác, hoặc khi tính cho một cơ cấu vốn mới, ta phải *gỡ* lớp rủi ro tài chính ra để lấy Beta tài sản thuần ($\beta_u$), rồi *gắn lại* lớp rủi ro tài chính theo cơ cấu vốn đích. Robert Hamada (1972) là người đưa ra công thức này bằng cách kết hợp CAPM với mô hình M&M có thuế. Phần $(1 - T_c) \times D/E$ cho thấy: vay càng nhiều so với vốn chủ thì cổ đông càng gánh nhiều rủi ro biến động hơn, nhưng lá chắn thuế giảm nhẹ mức khuếch đại này. Công thức giả định Beta của nợ bằng 0 và nợ duy trì vĩnh viễn nên chỉ là xấp xỉ - một điểm cần ghi nhớ khi đọc kết quả của Case 3 và Case 4.

#### E. Đo lường Chi phí sử dụng Nợ vay ($r_d$) thực tế
Chi phí sử dụng nợ không đơn thuần là lãi suất danh nghĩa ghi trên hợp đồng tín dụng mà phải được tính bằng tỷ suất sinh lời khi đáo hạn (Yield to Maturity - YTM) của các cấu phần nợ phát hành công khai, hoặc tính toán dựa trên mức xếp hạng tín nhiệm và phần bù rủi ro tín dụng (Synthetic Rating Method):

$$r_d = R_f + \text{Default Spread}$$

Mức sụt giảm tín nhiệm cấp độ cao có thể đẩy một doanh nghiệp rơi thẳng từ nhóm "Investment Grade" xuống vùng "Speculative Grade" (Junk bond), trực tiếp bóp nghẹt khả năng huy động vốn của doanh nghiệp.

#### F. Chi phí vốn biên mậu (Marginal Cost of Capital - MCC) và Điểm gãy (Break Points)
Khi quy mô huy động vốn tăng vượt quá một mức nhất định, chi phí sử dụng của từng nguồn vốn riêng lẻ sẽ tăng lên (ví dụ: hết lợi nhuận giữ lại giá rẻ, buộc phải phát hành cổ phiếu mới chịu chi phí phát hành $f$ cao).
*   Công thức xác định Điểm gãy cấu trúc vốn (Break Point - BP):
    $$BP = \frac{\text{Lượng vốn tối đa của nguồn có chi phí thấp}}{\text{Tỷ trọng của nguồn đó trong cấu trúc vốn}}$$

---

### 2. Case Study 3 (Thành công): TẬP ĐOÀN CÔNG NGHỆ VTE – Hạ Hurdle Rate bằng cấu trúc vốn hợp lý

#### Bối cảnh

VTE thiết kế phần mềm điều khiển công nghiệp, hoạt động hoàn toàn bằng vốn chủ sở hữu ($D/E = 0$). Các thông số thị trường: Beta cổ phiếu $\beta_l = 1{,}6$, lãi suất phi rủi ro $R_f = 6\%$, phần bù rủi ro thị trường $ERP = 5\%$, thuế suất TNDN $T_c = 20\%$.

#### Bước 1: Tính WACC ban đầu (thuần vốn chủ)

Không có nợ nên WACC chính bằng chi phí vốn chủ sở hữu theo CAPM:

$$r_e = R_f + \beta_l \times ERP = 6\% + 1{,}6 \times 5\% = 14{,}0\% \quad \Rightarrow \quad WACC_{\text{ban đầu}} = \textbf{14,0\%}$$

Hurdle rate 14% khiến nhiều dự án mở rộng hạ tầng máy chủ có lợi suất 11,5% - 13,8% liên tục bị bác bỏ.

#### Bước 2: Phương án tái cấu trúc - phát hành trái phiếu 8% để mua lại cổ phiếu, đưa $D/E$ lên 1,0

Với $D/E = 1{,}0$ thì $D/V = 50\%$, $E/V = 50\%$; lãi suất trái phiếu $r_d = 8\%$.

- **Beta tài sản**: vì ban đầu không có nợ nên $\beta_u = \beta_l = 1{,}6$.
- **Beta cổ phiếu sau khi vay nợ** (công thức Hamada):

$$\beta_{lh} = 1{,}6 \times [1 + (1 - 0{,}20) \times 1{,}0] = 1{,}6 \times 1{,}8 = \textbf{2,88}$$

- **Chi phí vốn chủ sở hữu mới** (rủi ro tài chính khuếch đại):

$$r_{e,\text{new}} = 6\% + 2{,}88 \times 5\% = \textbf{20,4\%}$$

- **WACC mới**:

$$WACC_{\text{new}} = 0{,}50 \times 20{,}4\% + 0{,}50 \times 8\% \times (1 - 0{,}20) = 10{,}2\% + 3{,}2\% = \textbf{13,4\%}$$

#### Bước 3: Khảo sát WACC theo các mức đòn bẩy khác nhau

Giữ nguyên $r_d = 8\%$, $\beta_u = 1{,}6$:

| $D/E$ | $D/V$ | $\beta_{lh}$ | $r_e$ | WACC |
|-------|-------|--------------|-------|------|
| 0 | 0% | 1,60 | 14,0% | 14,00% |
| 0,25 | 20% | 1,92 | 15,6% | 13,76% |
| 0,5 | 33,3% | 2,24 | 17,2% | 13,60% |
| 1,0 | 50% | 2,88 | 20,4% | **13,40%** |
| 2,0 | 66,7% | 4,16 | 26,8% | 13,20% |

#### Diễn giải ý nghĩa kinh doanh

1. Vay thêm làm $r_e$ tăng mạnh (14% lên 20,4%), nhưng WACC vẫn **giảm** từ 14,0% xuống 13,4% (giảm 60 điểm cơ bản). Nguyên nhân: nợ vay 8% vừa rẻ hơn vốn chủ, vừa được khấu trừ thuế (chi phí thực chỉ 6,4%), và tỷ trọng nợ 50% đủ lớn để kéo trung bình xuống.
2. Hiệu quả thực tế: một dự án đầu tư 100 triệu USD, lợi suất vĩnh viễn 13,8%/năm (dòng tiền 13,8 triệu USD/năm) có $NPV = 13{,}8/0{,}14 - 100 = \textbf{-1{,}43}$ triệu USD tại hurdle 14% (bị bác bỏ), nhưng $NPV = 13{,}8/0{,}134 - 100 = \textbf{+2{,}99}$ triệu USD tại hurdle 13,4% (được duyệt). Nhờ cơ cấu vốn mới, VTE thực hiện được dự án.
3. **Hạn chế quan trọng**: bảng trên giả định $r_d$ cố định ở 8% ở mọi mức đòn bẩy, nên WACC giảm đều khi vay thêm. Thực tế lãi suất sẽ tăng khi doanh nghiệp vay quá nhiều - điều đưa ta đến Case 4.

---

### 3. Case Study 4 (Thất bại): HÃNG HÀNG KHÔNG FLY-IND – Đòn bẩy cực đoan làm WACC bùng nổ

#### Bối cảnh

Fly-Ind mở rộng đội bay bằng vay nợ, đưa $D/E$ lên **4,0** ($D/V = 80\%$, $E/V = 20\%$). Beta tài sản ngành hàng không $\beta_u = 0{,}90$; $R_f = 6\%$, $ERP = 5\%$, $T_c = 20\%$. Khi tính toán, Fly-Ind chỉ cập nhật tăng $r_e$ mà quên rằng ngân hàng cũng sẽ định giá lại rủi ro.

#### Bước 1: Beta cổ phiếu ở mức đòn bẩy 4,0

$$\beta_{lh} = 0{,}90 \times [1 + (1 - 0{,}20) \times 4{,}0] = 0{,}90 \times 4{,}2 = \textbf{3,78}$$

#### Bước 2: Chi phí vốn chủ sở hữu

$$r_e = 6\% + 3{,}78 \times 5\% = \textbf{24,9\%}$$

#### Bước 3: Chi phí nợ tăng do bị hạ xếp hạng tín nhiệm

Với $D/V = 80\%$ ngân hàng áp phụ phí rủi ro: $r_d$ tăng từ 8% lên **16%** trước thuế (chi phí sau thuế $16\% \times 0{,}8 = 12{,}8\%$).

#### Bước 4: WACC

$$WACC = 0{,}20 \times 24{,}9\% + 0{,}80 \times 16\% \times (1 - 0{,}20) = 4{,}98\% + 10{,}24\% = \textbf{15,22\%}$$

#### Bước 5: Tách riêng hai tác động bằng bảng so sánh

| Chỉ tiêu | Cơ cấu cân bằng ($D/E = 1$, $r_d = 8\%$) | $D/E = 4$ nhưng $r_d$ vẫn 8% (giả định) | $D/E = 4$, $r_d = 16\%$ (thực tế) |
|----------|-------------------------------------------|-------------------------------------------|-------------------------------------|
| $\beta_{lh}$ | 1,62 | 3,78 | 3,78 |
| $r_e$ | 14,1% | 24,9% | 24,9% |
| $r_d$ trước thuế | 8% | 8% | 16% |
| **WACC** | **10,25%** | 10,10% | **15,22%** |

#### Diễn giải ý nghĩa kinh doanh

- Nếu thị trường vẫn cho vay ở 8%, WACC gần như **không đổi** (10,10% so với 10,25%) - đúng như mô hình M&M dự đoán rằng $r_e$ tăng vừa đủ bù lợi ích nợ rẻ. Phần WACC tăng vọt thêm **5,12 điểm phần trăm** (từ 10,10% lên 15,22%) hoàn toàn đến từ **chi phí kiệt quệ tài chính**: lãi suất vay tăng vọt vì rủi ro vỡ nợ.
- Với WACC từ 10,25% lên 15,22%, mọi dự án mua thêm máy bay có lợi suất dưới 15,22% đều bị bác bỏ, dù trước đó chúng rất hấp dẫn. Doanh nghiệp rơi vào vòng xoáy: không đầu tư được, dòng tiền không cải thiện, gánh nợ gốc đến hạn, mất khả năng huy động nợ mới và phải tái cơ cấu theo thủ tục bảo hộ phá sản.

**Bài học**: lá chắn thuế chỉ là một mặt của đồng xu; quá điểm tối ưu, chi phí kiệt quệ tài chính (trực tiếp và gián tiếp) triệt tiêu và vượt lợi ích thuế. Khi mô hình hóa cơ cấu vốn, **luôn để $r_d$ biến thiên theo $D/E$** (hoặc theo chỉ số bao phủ lãi vay), không giữ cố định như bảng giản lược của Case 3.

---

## CHƯƠNG III: LÝ THUYẾT CẤU TRÚC VỐN (CAPITAL STRUCTURE TRADEOFF & MM)

Lựa chọn tỷ lệ tối ưu giữa Nợ vay và Vốn chủ sở hữu quyết định năng lực trường vốn của một doanh nghiệp trong dài hạn. Đọc thêm các công thức cơ cấu vốn tại [04-capital-structure.md](04-capital-structure.md).

### 1. Cơ sở lý thuyết toán học chuyên sâu

#### A. Định đề Modigliani-Miller (M&M) năm 1958 - Trong bối cảnh không thuế và không chi phí vỡ nợ
*   **M&M Định đề I (Irrelevance Proposition)**: Giá trị của doanh nghiệp có sử dụng nợ ($V_l$) bằng giá trị của doanh nghiệp hoạt động hoàn toàn bằng vốn chủ sở hữu ($V_u$). Cấu trúc nợ không làm thay đổi giá trị nội tại tổng thể:
    $$V_l = V_u$$
*   **M&M Định đề II**: Chi phí sử dụng vốn chủ sở hữu tăng tuyến tính theo tỷ trọng nợ để bù đắp rủi ro tài chính của cổ đông:
    $$r_e = r_0 + \frac{D}{E} \times (r_0 - r_d)$$
    (Trong đó $r_0$ là chi phí sử dụng vốn của doanh nghiệp khi không vay nợ).

**Tại sao M&M chứng minh cấu trúc vốn "không quan trọng" - và vì sao điều đó lại quan trọng?** Trước năm 1958 giới thực hành tin rằng nợ rẻ hơn vốn chủ nên cứ vay nhiều là WACC giảm. Franco Modigliani và Merton Miller đặt câu hỏi ngược: *trong điều kiện nào thì cơ cấu vốn không tác động đến giá trị?* Bằng lập luận arbitrage (nhà đầu tư có thể tự vay nợ cá nhân để tái tạo đòn bẩy - "homemade leverage"), họ chứng minh rằng ở thị trường hoàn hảo (không thuế, không chi phí phá sản, thông tin đối xứng), giá trị doanh nghiệp chỉ do **tài sản và dòng tiền hoạt động** quyết định, còn cơ cấu vốn chỉ là cách *chia* giá trị đó cho chủ nợ và cổ đông (giống chia một chiếc bánh pizza thành các phần khác nhau mà không làm bánh lớn thêm). Giá trị thực của định lý là nó chỉ ra **các "ma sát" cần xét** - thuế, chi phí phá sản, bất cân xứng thông tin, chi phí đại diện - để từ đó giải thích cơ cấu vốn quan trọng ở đâu. Phân tích chi tiết hơn xem [04-capital-structure.md](04-capital-structure.md).

#### B. Định đề M&M năm 1963 - Bổ sung Lá chắn thuế thu nhập doanh nghiệp
Khi tích hợp thuế, tiền lãi vay được tính trừ vào thu nhập chịu thuế trước khi nộp, tạo ra dòng tiết kiệm thuế khổng lồ:
*   **Giá trị doanh nghiệp tăng thêm bằng giá trị hiện tại của lá chắn thuế kéo dài vô tận**:
    $$V_l = V_u + (T_c \times D)$$
*   **M&M Định đề II với thuế**:
    $$r_e = r_0 + \frac{D}{E} \times (1 - T_c) \times (r_0 - r_d)$$

**Tại sao thêm thuế làm đổi kết luận?** Năm 1963, chính M&M tự điều chỉnh: khi có thuế TNDN, lãi vay được **khấu trừ** trước thuế còn cổ tức thì không, nên mỗi đồng nợ tạo ra một khoản tiết kiệm thuế $T_c \times r_d \times D$ mỗi năm. Nếu nợ duy trì vĩnh viễn và chiết khấu ở $r_d$ (vì dòng tiền tiết kiệm thuế chắc chắn như chính khoản nợ), giá trị hiện tại của lá chắn thuế là $\frac{T_c \times r_d \times D}{r_d} = T_c \times D$ - $r_d$ triệt tiêu. Đó là lý do công thức $V_l = V_u + T_c D$ gọn đến vậy. Một hệ quả "quá đẹp": nếu chỉ có lá chắn thuế, doanh nghiệp tối ưu nên vay 100% - kết luận phi thực tế, nên cần thêm chi phí kiệt quệ tài chính (mục E).

#### C. Mô hình Miller (1977) tích hợp cả Thuế cá nhân (Personal Taxes)
Miller mở rộng định đề M&M bằng cách đưa thêm thuế TNCN đối với thu nhập từ vốn cổ phần ($T_s$) và thu nhập từ lãi tiền gửi/lãi vay của chủ nợ ($T_d$). Công thức giá trị doanh nghiệp có sử dụng nợ trở thành:

$$V_l = V_u + \left[ 1 - \frac{(1 - T_c) \times (1 - T_s)}{1 - T_d} \right] \times D$$

*   Nếu $(1 - T_c) \times (1 - T_s) = 1 - T_d$, lợi thế lá chắn thuế doanh nghiệp sẽ bị triệt tiêu hoàn toàn bởi gánh nặng thuế cá nhân của các chủ đầu tư bên ngoài.

**Tại sao cần thêm thuế cá nhân?** M&M 1963 chỉ xét thuế ở cấp doanh nghiệp. Merton Miller (1977, bài *Debt and Taxes*) nhận xét: nhà đầu tư cuối cùng nhận lãi vay (thu nhập từ nợ, thường chịu thuế suất cá nhân $T_d$ cao) hay cổ tức/lãi vốn (chịu thuế $T_s$ thấp hơn). Nếu thuế cá nhân đánh vào lãi cao hơn đủ để bù phần doanh nghiệp tiết kiệm được, lợi thế ròng của nợ thu hẹp hoặc bằng 0 - đúng như điều kiện $(1-T_c)(1-T_s) = 1 - T_d$ ở trên. Mô hình này giải thích vì sao thực tế ở nhiều nước lợi ích nợ nhỏ hơn dự đoán của M&M 1963.

#### D. Quyết định tái cấu trúc vốn (Leveraged Recapitalization)
Leveraged Recap là quyết định tài chính mà công ty chủ động phát hành thêm một lượng lớn nợ vay để lấy tiền mặt mua sắm lại cổ phiếu quỹ trên thị trường nhằm định hình mức tối ưu của cấu trúc. Quyết định này giúp nâng cao tức khắc hệ số đòn bẩy nợ và tạo áp lực bắt buộc các nhà điều hành hoạt động hiệu quả hiệu suất cao.

#### E. Lý thuyết Đánh đổi Cấu trúc Vốn (Static Trade-off Theory)
Tích hợp rủi ro vỡ nợ tài chính của doanh nghiệp thực tế. Giá trị thực của doanh nghiệp vay nợ bằng:

$$V_l = V_u + (T_c \times D) - \text{PV(Chi phí kiệt quệ tài chính)} - \text{PV(Chi phí đại diện)}$$

```
  Giá trị DN (Value)
     │                                     /  Lá chắn thuế tối đa (M&M 1963)
     │                                   / 
     │                         * * * *  <─── Điểm Tối Ưu Cấu Trúc Vốn (Trade-off)
     │                     *            *
     │                 *                  *  <─── Giá trị Thực tế V_l
     │             *                        *
     │         *──────────────────────────────────
     │       *   Giá trị Công ty V_u (Không nợ)
     │     *
     └───────────────────────────────────────────── Tỷ lệ Nợ (D/E)
```

*   **Chi phí kiệt quệ tài chính trực tiếp**: Chi phí tòa án, chi phí pháp lý, kế toán thẩm định khi thanh lý tài sản.
*   **Chi phí kiệt quệ tài chính gián tiếp**: Sự suy giảm doanh số bởi hành vi tẩy chay của người tiêu dùng, nhà thầu xiết chặt công nợ, nhân tài giỏi bỏ trốn do lo ngại rủi ro công ty phá sản.

#### F. Lý thuyết Phát tín hiệu dòng vốn (Signaling Theory - Ross 1977)
Chỉ ra việc phát hành nợ vay như một tín hiệu tích cực (Positive Signal) bắn ra thị trường. Chỉ những doanh nghiệp tự tin có dòng tiền mặt cực kỳ dồi dào trong tương lai mới dám gánh chịu áp lực thanh toán gốc lãi nợ cố định kỳ hạn, còn các doanh nghiệp yếu kém hụt hơi sẽ tránh xa nợ nần. Ngược lại, việc bất ngờ phát hành thêm cổ phiếu mới ra công chúng có thể bị xem là tín hiệu tiêu cực (Negative Signal) ám chỉ thị trường đang định giá cổ phiếu của doanh nghiệp quá cao (Overvalued).

#### G. Mâu thuẫn Đại diện (Agency Costs of Debt vs Equity)
1.  **Agency Costs of Debt (Mâu thuẫn giữa Cổ đông và Chủ nợ)**:
    *   *Rủi ro chuyển dịch tài sản (Risk-Shifting / Asset Substitution)*: Khi gặp khó khăn tài chính, cổ đông có xu hướng dốc tiền túi đi vay đầu tư vào các dự án rủi ro siêu cao "được ăn cả ngã về không", đẩy hiểm họa cháy túi cho chủ nợ gánh chịu.
    *   *Rủi ro sụt giảm đầu tư (Underinvestment / Debt Overhang)*: Cổ đông từ chối góp vốn thêm để thông qua các dự án tốt có NPV dương vì toàn bộ lợi nhuận sau đó tạo ra sẽ bị thu hồi ráo riết để thanh toán nợ cũ cho chủ nợ trước tiên.
2.  **Agency Costs of Equity (Mâu thuẫn giữa Giám đốc làm thuê và Cổ đông sở hữu)**:
    *   *Thuyết Dòng tiền tự do (Free Cash Flow Hypothesis - Jensen 1986)*: Khi công ty tích lũy lượng dòng tiền tự do quá lớn, nhà quản lý làm thuê có xu hướng lãng phí vào các thương vụ thâu tóm vô bổ tốn kém hoặc xa xĩ phẩm thay vì chia lại tiền cho cổ đông. Việc ép dùng đòn bẩy nợ cao buộc nhà quản lý phải kiểm soát chi phí hoạt động chặt chẽ để trả nợ.

#### H. Lý thuyết Trật tự phân bổ vốn (Pecking-Order Theory của Myers & Majluf năm 1984)
Dựa trên hiện tượng thông tin bất cân xứng (Asymmetric Information) giữa giới quản lý nội bộ và các nhà đầu tư bên ngoài. Giám đốc có xu hướng phân bổ vốn theo thứ tự ưu tiên chi phí thấp và rủi ro gián đoạn thông tin tăng dần:

$$\text{1. Lợi nhuận giữ lại tích lũy} \longrightarrow \text{2. Phát hành nợ vay phát triển} \longrightarrow \text{3. Phát hành thêm cổ phiếu mới (Biện pháp cuối cùng)}$$

**Tại sao doanh nghiệp lại theo trật tự này? Logic của thông tin bất cân xứng.** Gordon Donaldson (1961) quan sát thực tế các công ty ưu tiên tài trợ bằng lợi nhuận giữ lại; Stewart Myers và Nicholas Majluf (1984) giải thích bằng mô hình: ban quản lý biết rõ giá trị thật của công ty hơn nhà đầu tư bên ngoài. Nếu quản lý tin cổ phiếu đang bị định giá thấp, phát hành cổ phiếu là *bán rẻ* phần của cổ đông hiện hữu cho người mới; nhà đầu tư hiểu logic này nên **coi việc phát hành cổ phiếu là tin xấu** và bán xuống giá. Vì vậy doanh nghiệp chọn nguồn vốn ít "nhạy cảm với thông tin" nhất trước (lợi nhuận giữ lại, rồi nợ), chỉ phát hành cổ phiếu khi buộc phải làm. Điều này khác với Trade-off Theory ở chỗ **không có tỷ lệ nợ mục tiêu**: cơ cấu vốn là hệ quả của lịch sử huy động, không phải kết quả của việc tối ưu hóa.

---

### 2. Case Study 5 (Thành công): TẬP ĐOÀN BÁN LẺ R-CENTER – Giá trị của lá chắn thuế nợ vay

#### Bối cảnh

R-Center là doanh nghiệp không vay nợ: giá trị thị trường vốn chủ sở hữu $V_u = 1.000$ triệu USD, lợi nhuận trước thuế và lãi vay ổn định $EBIT = 150$ triệu USD/năm, chi phí vốn khi không có nợ $r_0 = 12\%$, thuế suất TNDN $T_c = 20\%$. Công ty phát hành **400 triệu USD** trái phiếu dài hạn (lãi suất cố định $r_d = 7\%$, duy trì vĩnh viễn) rồi dùng toàn bộ tiền mua lại cổ phiếu. Hoạt động kinh doanh cốt lõi (EBIT) không đổi.

#### Bước 0: Kiểm tra giá trị công ty ban đầu

Lợi nhuận sau thuế khi không nợ:

$$NI_{\text{old}} = EBIT \times (1 - T_c) = 150 \times 0{,}80 = 120 \text{ triệu USD/năm}$$

Giá trị công ty là dòng tiền vĩnh viễn chiết khấu ở $r_0$: $V_u = 120 / 0{,}12 = 1.000$ triệu USD - khớp với giá trị thị trường đã cho, nên bộ số liệu nhất quán.

#### Bước 1: Giá trị công ty sau khi vay nợ (M&M 1963)

$$V_l = V_u + T_c \times D = 1.000 + 0{,}20 \times 400 = \textbf{1.080 triệu USD}$$

$$E = V_l - D = 1.080 - 400 = \textbf{680 triệu USD}$$

#### Bước 2: Chi phí vốn chủ sở hữu mới (M&M Định đề II có thuế)

$$r_e = r_0 + \frac{D}{E}(1 - T_c)(r_0 - r_d) = 12\% + \frac{400}{680} \times 0{,}80 \times (12\% - 7\%) = 12\% + 0{,}5882 \times 0{,}80 \times 5\% = \textbf{14,35\%}$$

#### Bước 3: Dòng tiền hằng năm cho các nhà tài trợ vốn

| Khoản mục | Không nợ | Có nợ 400 triệu |
|-----------|----------|------------------|
| EBIT | 150,0 | 150,0 |
| Lãi vay ($400 \times 7\%$) | 0 | 28,0 |
| EBT | 150,0 | 122,0 |
| Thuế TNDN (20%) | 30,0 | 24,4 |
| Lợi nhuận ròng (cho cổ đông) | 120,0 | 97,6 |
| **Tổng dòng tiền cho cổ đông + chủ nợ** | **120,0** | **125,6** |

Chênh lệch dòng tiền = $125{,}6 - 120{,}0 = 5{,}6$ triệu USD/năm, đúng bằng thuế tiết kiệm được: $T_c \times \text{Lãi vay} = 0{,}20 \times 28 = 5{,}6$ (thuế giảm từ 30,0 xuống 24,4). Đây là tiền "chuyển" từ Kho bạc sang túi nhà đầu tư.

#### Bước 4: Quy đổi lá chắn thuế về giá trị hiện tại

Lá chắn thuế chắc chắn như khoản nợ nên chiết khấu ở $r_d$:

$$PV(\text{Tax Shield}) = \frac{5{,}6}{0{,}07} = \textbf{80 triệu USD} = T_c \times D = 0{,}20 \times 400$$

#### Bước 5: Kiểm chứng chéo bằng WACC

$$WACC_{\text{new}} = \frac{680}{1.080} \times 14{,}35\% + \frac{400}{1.080} \times 7\% \times 0{,}80 = 9{,}04\% + 2{,}07\% = 11{,}11\%$$

$$V_l = \frac{EBIT \times (1 - T_c)}{WACC} = \frac{120}{0{,}1111} = 1.080 \text{ triệu USD}$$

Hai cách tính cho cùng kết quả: WACC giảm từ 12% xuống 11,11%, đồng nghĩa giá trị công ty tăng từ 1.000 lên 1.080 triệu USD. Đồng thời, kiểm tra lợi suất cổ đông: $97{,}6/680 = 14{,}35\%$ khớp với $r_e$ ở Bước 2.

#### Diễn giải ý nghĩa kinh doanh

- Giá trị tăng thêm **80 triệu USD (+8%)** đến từ việc tái cấu trúc tài chính thuần túy, không cần bán thêm một sản phẩm nào. Cổ đông sở hữu cổ phiếu trước khi công bố hưởng toàn bộ phần tăng này.
- Giá trị này chỉ tồn tại khi công ty **luôn có lợi nhuận để khấu trừ lãi vay**: với EBIT 150 và lãi 28, khả năng bao phủ lãi vay là $150/28 = 5{,}4$ lần, rất an toàn. Nếu EBIT tụt gần bằng lãi vay, lá chắn thuế biến mất và rủi ro vỡ nợ xuất hiện (xem Case 6).
- Mô hình giả định nợ vĩnh viễn, không có chi phí kiệt quệ tài chính; vì vậy 80 triệu USD là **mức tối đa lý thuyết**, thực tế thấp hơn.

**Bài học**: đòn bẩy vừa phải tạo ra giá trị nhờ lá chắn thuế; cần so sánh nó với chi phí kiệt quệ tài chính trước khi quyết định mức vay.

---

### 3. Case Study 6 (Thất bại): TẬP ĐOÀN BẤT ĐỘNG SẢN EVER-G – Nợ ngắn hạn lãi cao và sự sụp đổ của lá chắn thuế

#### Bối cảnh

Ever-G tích lũy quỹ đất bằng cách phát hành trái phiếu doanh nghiệp ngắn hạn, lãi suất cam kết lên tới **22%/năm**, tổng dư nợ **3.500 triệu USD**, trong khi bỏ qua thứ tự ưu tiên tài trợ của lý thuyết Pecking Order (lợi nhuận giữ lại, rồi nợ hợp lý, cổ phiếu là cuối cùng). Giả sử EBIT bình thường của Ever-G là **500 triệu USD/năm**, và 60% dư nợ đáo hạn trong 12 tháng tới, tiền mặt hiện có 200 triệu USD.

#### Bước 1: Đo khả năng bao phủ lãi vay (Interest Coverage Ratio = EBIT / Lãi vay)

| Lãi suất trái phiếu | Lãi vay/năm | EBIT | Lợi nhuận trước thuế (EBT) | ICR |
|---------------------|-------------|------|----------------------------|-----|
| 9% (mức hợp lý) | 315 | 500 | +185 | 1,59 lần |
| 12% | 420 | 500 | +80 | 1,19 lần |
| **22% (thực tế Ever-G)** | **770** | 500 | **-270** | **0,65 lần** |

#### Bước 2: Phân tích rủi ro tái cấp vốn (Refinancing Risk)

Nợ đáo hạn 12 tháng tới: $3.500 \times 60\% = 2.100$ triệu USD; trừ tiền mặt 200, **thiếu hụt 1.900 triệu USD** phải tái tài trợ. Đòn bẩy $D/EBIT = 3.500/500 = 7{,}0$ lần.

#### Bước 3: Phân tích hậu quả

- **ICR = 0,65 < 1**: EBIT không đủ trả lãi, mỗi năm thiếu 270 triệu USD phải bù bằng bán tài sản hoặc vay thêm; EBT âm nên **lá chắn thuế biến mất** - lợi ích duy nhất của nợ không còn.
- Khi nhà nước siết quản lý phát hành trái phiếu bất động sản (giai đoạn 2022 - 2024), thị trường không còn nhận trái phiếu mới, Ever-G không thể tái cấp 1.900 triệu USD.
- **Chi phí đại diện của nợ** bùng phát: chủ nợ muốn thanh lý tài sản thu hồi vốn, cổ đông sáng lập lại muốn "đánh cược" bằng các dự án rủi ro để cứu vốn chủ (risk-shifting). **Vấn đề đầu tư dưới mức (debt overhang)**: các dự án sạch tốt có NPV dương cũng bị bỏ vì lợi nhuận tạo ra sẽ bị dùng trả nợ cũ.

Kết quả: Ever-G vỡ nợ trái phiếu 3.500 triệu USD, bị hàng vạn trái chủ khởi kiện và mất giao dịch.

**Bài học**: (1) Đừng để chi phí nợ vượt lợi suất hoạt động: lãi suất vay phải được kiểm chứng bằng ICR tối thiểu (thường > 2,5 - 3 lần); (2) Không dùng nợ ngắn hạn tài trợ tài sản dài hạn (bất động sản) vì rủi ro tái cấp vốn; (3) Tôn trọng Pecking Order và ranh giới của Trade-off Theory.

---

## CHƯƠNG IV: QUẢN TRỊ VỐN LƯU ĐỘNG RÒNG (WORKING CAPITAL MANAGEMENT)

Sức khỏe ngắn hạn và năng lực sống sót chống chọi khủng hoảng của một doanh nghiệp trong từng ngày vận hành phụ thuộc hoàn toàn vào cách họ quản trị dòng tiền lưu động quay vòng. Tham khảo chi tiết tối ưu vốn ngắn hạn tại [06-working-capital-management.md](06-working-capital-management.md).

### 1. Cơ sở lý thuyết toán học chuyên sâu

#### A. Chu kỳ chuyển đổi tiền mặt (Cash Conversion Cycle - CCC)
CCC đo lường thời gian (số ngày) nhị phân từ khi doanh nghiệp chính thức chi trả tiền mặt mua nguyên liệu đầu vào cho đến khi thực tế thu hồi về tiền mặt từ hoạt động thu nợ bán sản phẩm đầu ra:

$$CCC = DIO + DSO - DPO$$

**Tại sao cần CCC? Vấn đề mà công thức này giải quyết.** Một doanh nghiệp có thể báo lãi trên P&L nhưng vẫn cạn tiền, vì lợi nhuận được ghi nhận khi *bán hàng* còn tiền mặt chỉ về khi *khách trả tiền*. Chỉ số này do Verlyn Richards và Eugene Laughlin đề xuất năm 1980 (bài *A Cash Conversion Cycle Approach to Liquidity Analysis*) để đo **số ngày tiền mặt của doanh nghiệp bị "đóng băng"** trong hoạt động. Logic ba thành phần: tiền bị khóa trong *hàng tồn kho* (DIO ngày) và trong *khoản phải thu* (DSO ngày), nhưng được *nhà cung cấp tài trợ* trong DPO ngày; khoảng chênh lệch còn lại chính là số ngày doanh nghiệp phải tự tìm nguồn tài trợ. Do đó CCC càng thấp (hoặc càng âm) thì nhu cầu vốn lưu động càng nhỏ.

```
   ┌──────────────────────────────────────────────────────────────┐
   │                  HÀNH TRÌNH CHU KỲ CHUYỂN ĐỔI TIỀN MẶT (CCC) │
   │                                                              │
   │  Chi tiền mua NVL           Bán hàng hóa        Thu tiền khách│
   │  (Day 0 - Trả tiền)         (Day 40)            (Day 70)      │
   │  ├──────────────────────────┼───────────────────┤             │
   │  │◄───────── DIO ──────────►│◄────── DSO ──────►│             │
   │  │                          (Số ngày tồn kho)   (Số ngày thu) │
   │  │                                                            │
   │  │◄─────────────────────── Operating Cycle ──────────────────►│
   │  │                                                            │
   │  ├───────── DPO ───────────►│◄───────── CCC ─────────────────►│
   │  (Số ngày hoãn trả)        (Chu kỳ chuyển đổi tiền thực)  │
   └──────────────────────────────────────────────────────────────┘
```

#### B. Các phương thức tính toán chi tiết thành phần số ngày:
*   **Số ngày tồn kho trung bình (Days Inventory Outstanding - DIO)**:
    $$DIO = \frac{\text{Hàng tồn kho trung bình}}{\text{Giá vốn hàng bán (COGS)}} \times 365$$
*   **Số ngày phải thu khách hàng (Days Sales Outstanding - DSO)**:
    $$DSO = \frac{\text{Khoản phải thu trung bình}}{\text{Doanh thu thuần}} \times 365$$
*   **Số ngày phải trả nhà cung cấp (Days Payable Outstanding - DPO)**:
    $$DPO = \frac{\text{Khoản phải trả trung bình}}{\text{Giá vốn hàng bán (COGS)}} \times 365$$

#### C. Công thức Đo lường Vốn lưu động ròng (Net Working Capital - NWC)
$$NWC = \text{Tài sản ngắn hạn} - \text{Nợ ngắn hạn}$$

#### D. Đo lường Hệ số Thanh toán ngắn hạn (Liquidity Ratios)
1.  **Hệ số thanh toán hiện hành (Current Ratio)**:
    $$\text{Current Ratio} = \frac{\text{Tài sản ngắn hạn}}{\text{Nợ ngắn hạn}}$$
2.  **Hệ số thanh toán nhanh (Quick Ratio)**: Loại bỏ hàng tồn kho có tính thanh khoản thấp nhất:
    $$\text{Quick Ratio} = \frac{\text{Tiền và tương đương tiền} + \text{Đầu tư ngắn hạn} + \text{Khoản phải thu}}{\text{Nợ ngắn hạn}}$$
3.  **Hệ số thanh toán tức thời (Cash Ratio)**:
    $$\text{Cash Ratio} = \frac{\text{Tiền và tương đương tiền} + \text{Đầu tư tài chính ngắn hạn}}{\text{Nợ ngắn hạn}}$$

**Tại sao Quick Ratio loại hàng tồn kho?** Current Ratio coi mọi tài sản ngắn hạn là như nhau, nhưng hàng tồn kho phải bán được mới thành tiền, và khi doanh nghiệp bị ép thanh toán gấp, hàng tồn kho thường chỉ bán được với giá chiết khấu mạnh. Vì vậy các chủ ngân hàng thế kỷ 20 dùng "acid test" (phép thử bằng axit - nguyên là cách thử vàng thật) để kiểm tra doanh nghiệp *chỉ với phần tài sản gần như tiền mặt* có trả được nợ ngắn hạn hay không. Cash Ratio là phiên bản nghiêm khắc nhất.

#### E. Mô hình quản lý lượng hàng tồn kho tối ưu (Economic Order Quantity - EOQ)
Giúp giảm thiểu tối đa tổng chi phí quản lý hàng tồn kho, bao gồm chi phí đặt hàng (Ordering Cost) và chi phí lưu kho bảo quản (Holding Cost).
*   **Chứng minh toán học công thức EOQ**:
    Tổng chi phí tồn kho năm ($TC$):
    $$TC = \left(\frac{D}{Q} \times S\right) + \left(\frac{Q}{2} \times H\right)$$
    Trong đó:
    *   $D$: Tổng nhu cầu hàng hóa sử dụng trong năm (đơn vị sản phẩm).
    *   $Q$: Quy mô của mỗi đơn hàng đặt sỉ (đơn vị sản phẩm).
    *   $S$: Chi phí cố định cho mỗi lần đặt hàng phát sinh.
    *   $H$: Chi phí lưu kho bảo quản cho một đơn vị hàng hóa trong một năm.
    Để tìm quy mô đơn hàng tối ưu $Q^*$ triệt tiêu chi phí, ta lấy đạo hàm bậc nhất của $TC$ theo $Q$ và cho bằng mốc 0:
    $$\frac{dTC}{dQ} = -\frac{D \times S}{Q^2} + \frac{H}{2} = 0$$
    $$\frac{H}{2} = \frac{D \times S}{Q^2}$$
    $$Q^2 = \frac{2 \times D \times S}{H}$$
    $$Q^* = \sqrt{\frac{2 \times D \times S}{H}}$$

**Tại sao EOQ có dạng căn bậc hai?** Đặt hàng *ít lần, mỗi lần nhiều* thì giảm chi phí đặt hàng nhưng tăng chi phí lưu kho; đặt *nhiều lần, mỗi lần ít* thì ngược lại. Hai chi phí này đi ngược chiều nhau nên tồn tại một điểm cân bằng, và tại điểm đó **chi phí đặt hàng đúng bằng chi phí lưu kho** (ở ví dụ dưới đều là 1.000 USD). Ford W. Harris công bố công thức năm 1913 (*How Many Parts to Make at Once*). Dạng căn bậc hai cho thấy: nhu cầu tăng gấp 4 lần thì lô hàng tối ưu chỉ tăng gấp đôi - lý do các doanh nghiệp lớn không cần lượng kho tỷ lệ thuận với doanh số.

***Bài tập ứng dụng định lượng số 2***: Một nhà máy sản xuất cần sử dụng $D = 10,000$ đơn vị bán sản phẩm mỗi năm. Chi phí cho mỗi lần phát lệnh đặt mua hàng cố định là $S = 50$ USD/đơn hàng. Chi phí lưu trữ bảo quản tồn kho hàng năm được tính ở mức $H = 4$ USD/đơn vị/năm.
*   *Bước 1: Áp dụng công thức tối ưu EOQ*:
    $$Q^* = \sqrt{\frac{2 \times 10,000 \times 50}{4}} = \sqrt{\frac{1,000,000}{4}} = \sqrt{250,000} = \textbf{500 đơn vị / đơn hàng}$$
*   *Bước 2: Tính tổng chi phí quản lý tồn kho tối thiểu đạt được*:
    $$TC^* = \left(\frac{10,000}{500} \times 50\right) + \left(\frac{500}{2} \times 4\right) = 1,000 + 1,000 = \textbf{2,000 USD / năm}$$

#### F. Hoạch định dòng tiền tối ưu: Mô hình Baumol-Allais-Tobin (BAT) và Miller-Orr

**Tại sao cần các mô hình này?** Giữ nhiều tiền mặt thì an toàn nhưng mất lãi (chi phí cơ hội); giữ ít tiền mặt thì phải thường xuyên bán chứng khoán/rút tiền, tốn chi phí giao dịch. William Baumol (1952) áp dụng đúng logic của EOQ cho tiền mặt - "tiền mặt cũng là hàng tồn kho"; James Tobin (1956) độc lập đưa ra mô hình tương tự. Merton Miller và Daniel Orr (1966) mở rộng cho trường hợp thực tế hơn khi dòng tiền biến động ngẫu nhiên thay vì đều đặn.

1.  **Mô hình BAT (Baumol)**: Giả định mức sử dụng tiền mặt đều đặn tuyến tính:
    $$C^* = \sqrt{\frac{2 \times T \times F}{r}}$$
    Trong đó: $C^*$ là lượng tiền mặt rút tối ưu mỗi đợt, $T$ là tổng nhu cầu tiền mặt cả kỳ, $F$ là chi phí cố định mỗi lần giao dịch, $r$ là lãi suất cơ hội (lãi gửi/lãi chứng khoán ngắn hạn).

    *Ví dụ*: một SME cần chi $T = 1.200$ triệu VNĐ tiền mặt trong năm, mỗi lần chuyển đổi từ tiết kiệm sang tiền mặt tốn $F = 0{,}5$ triệu, lãi tiết kiệm $r = 6\%$.
    $$C^* = \sqrt{\frac{2 \times 1.200 \times 0{,}5}{0{,}06}} = \sqrt{20.000} = \textbf{141{,}4 triệu VNĐ/lần} \Rightarrow \text{rút} \; \frac{1.200}{141{,}4} = 8{,}5 \; \text{lần/năm}$$
    Kiểm tra: chi phí giao dịch $= 8{,}49 \times 0{,}5 = 4{,}24$ triệu; chi phí cơ hội $= \frac{141{,}4}{2} \times 6\% = 4{,}24$ triệu - hai khoản bằng nhau, tổng chi phí tối thiểu 8,49 triệu/năm.

2.  **Mô hình Miller-Orr**: Áp dụng khi dòng tiền ròng hằng ngày biến động ngẫu nhiên. Doanh nghiệp đặt một **mức sàn** $L$ (số dư tối thiểu an toàn), tính **điểm quay về** $Z$ và **mức trần** $H$:
    $$\text{Khoảng giãn cách (spread)} = 3 \times \left( \frac{3 \times F \times \sigma^2}{4 \times r} \right)^{1/3}$$
    $$Z = L + \frac{\text{spread}}{3} \qquad H = L + \text{spread}$$
    Trong đó $\sigma^2$ là phương sai dòng tiền ròng hằng ngày, $r$ là lãi suất theo ngày, $F$ là chi phí mỗi lần giao dịch. Quy tắc: nếu số dư chạm trần $H$ thì mua chứng khoán đưa số dư về $Z$; nếu chạm sàn $L$ thì bán chứng khoán đưa số dư về $Z$.

    *Ví dụ*: sàn $L = 10$ triệu, độ lệch chuẩn dòng tiền ngày $\sigma = 5$ triệu ($\sigma^2 = 25$), $F = 0{,}5$ triệu, lãi suất ngày $r = 6\%/365 = 0{,}0164\%$.
    $$\left( \frac{3 \times 0{,}5 \times 25}{4 \times 0{,}000164} \right)^{1/3} = 38{,}49 \Rightarrow \text{spread} = 115{,}48$$
    $$Z = 10 + 38{,}49 = \textbf{48{,}49 triệu}; \quad H = 10 + 115{,}48 = \textbf{125{,}48 triệu}$$
    Khi dòng tiền biến động mạnh hơn (tăng $\sigma$) thì khoảng giãn cách rộng hơn - doanh nghiệp cần đệm tiền mặt lớn hơn.

---

### 2. Case Study 7 (Thành công): CHUỖI SIÊU THỊ THỰC PHẨM S-MART – Đưa chu kỳ CCC xuống mức âm

#### Bối cảnh

S-Mart vận hành 120 điểm bán, doanh thu **12.000 tỷ VNĐ/năm**, giá vốn hàng bán (COGS) **10.200 tỷ VNĐ/năm** (85% doanh thu). Ban giám đốc muốn tăng ROA mà không phát hành thêm nợ, nên tập trung tối ưu ba thành phần của chu kỳ chuyển đổi tiền mặt.

| Thành phần | Trước cải tổ | Sau cải tổ | Giải pháp |
|------------|--------------|------------|-----------|
| DIO (ngày tồn kho) | 45 | 12 | Hàng ký gửi (consignment) + kho tự động RFID, chỉ thanh toán khi khách quẹt thẻ ở quầy |
| DSO (ngày phải thu) | 6 | 0 | Thu tiền ngay qua thẻ/ví điện tử, không bán chịu cho khách sỉ nhỏ |
| DPO (ngày phải trả) | 30 | 65 | Dùng sức mua tập trung của cả chuỗi để đàm phán kéo dài hạn thanh toán |

#### Bước 1: Tính CCC trước và sau

$$CCC_{\text{trước}} = 45 + 6 - 30 = \textbf{+21 ngày} \qquad CCC_{\text{sau}} = 12 + 0 - 65 = \textbf{-53 ngày}$$

Chu kỳ vận hành (Operating Cycle) rút từ 51 ngày xuống 12 ngày.

#### Bước 2: Quy đổi ra số dư vốn lưu động ròng thương mại (tỷ VNĐ)

Dùng công thức $DIO = \frac{\text{Tồn kho}}{COGS} \times 365$ suy ngược lại $\text{Tồn kho} = \frac{DIO}{365} \times COGS$ (tương tự với phải thu theo doanh thu và phải trả theo COGS):

| Khoản mục | Trước | Sau |
|-----------|-------|-----|
| Hàng tồn kho ($45/365 \times 10.200$; $12/365 \times 10.200$) | 1.257,5 | 335,3 |
| Phải thu ($6/365 \times 12.000$; $0$) | 197,3 | 0 |
| Phải trả nhà cung cấp ($30/365 \times 10.200$; $65/365 \times 10.200$) | (838,4) | (1.816,4) |
| **Vốn lưu động ròng thương mại** | **+616,4** | **-1.481,1** |

#### Bước 3: Giá trị tiền mặt giải phóng

$$\text{Tiền mặt giải phóng} = 616{,}4 - (-1.481{,}1) = \textbf{2.097,5 tỷ VNĐ}$$

Nếu trước đây nguồn vốn này phải đi vay ngắn hạn với lãi suất 8%/năm, mức tiết kiệm lãi hằng năm là $2.097{,}5 \times 8\% = 167{,}8$ tỷ VNĐ (sau thuế 20% còn 134,2 tỷ VNĐ).

#### Diễn giải ý nghĩa kinh doanh

CCC âm 53 ngày nghĩa là siêu thị **thu tiền khách hàng trước 53 ngày so với lúc phải trả tiền cho nhà cung cấp**; trong khoảng thời gian đó S-Mart dùng nguồn vốn không lãi suất của nhà cung cấp để vận hành và đầu tư, thậm chí đem gửi ngân hàng lấy lãi. Đây là lợi thế cạnh tranh tài chính: tăng trưởng doanh số không "ngốn" vốn mà ngược lại còn **tạo thêm vốn** (mô hình tương tự các chuỗi bán lẻ lớn trên thế giới và các sàn thương mại điện tử).

**Rủi ro cần quản lý**: (1) Phụ thuộc vào sức mạnh thương lượng - nếu nhà cung cấp siết điều khoản, tiền mặt phải trả lại ngay; (2) DPO kéo quá dài có thể làm mất nhà cung cấp tốt hoặc bị tăng giá bán; (3) Khi doanh số giảm, lợi thế đảo ngược (số dư phải trả lớn nhưng tiền thu về ít đi), do đó phải giữ quỹ dự phòng thanh khoản.

---

### 3. Case Study 8 (Thất bại): THƯƠNG HIỆU LẮP RÁP THIẾT BỊ HOME-PRO – Bẫy tăng trưởng quá nóng (Overtrading)

#### Bối cảnh

Home-Pro lắp ráp đồ điện gia dụng. Để chiếm thị phần, công ty nới lỏng công nợ cho đại lý, đẩy mạnh nhập linh kiện dự trữ. Doanh thu tăng **2,5 lần (từ 200 lên 500 tỷ VNĐ)** trong một năm. Giả sử giá vốn bằng 80% doanh thu, chi phí hoạt động 31 tỷ VNĐ, thuế TNDN 20%:

$$\text{Lợi nhuận ròng} = (500 - 400 - 31) \times (1 - 0{,}20) = 69 \times 0{,}8 = \textbf{55,2 tỷ VNĐ}$$

Báo cáo kết quả kinh doanh (P&L) rất đẹp: lãi hơn 55 tỷ VNĐ.

#### Bước 1: So sánh CCC trước và sau tăng trưởng

| Thành phần | Trước (giả định) | Sau |
|------------|------------------|-----|
| DIO | 45 ngày | **90 ngày** (gom linh kiện dự trữ bừa bãi) |
| DSO | 30 ngày | **115 ngày** (đại lý chây ì) |
| DPO | 40 ngày | **15 ngày** (nhà cung cấp linh kiện bị chậm trả nên siết điều khoản, buộc trả gần như ngay) |
| **CCC** | **+35 ngày** | $90 + 115 - 15 = \textbf{+190 ngày} |

#### Bước 2: Tính nhu cầu vốn lưu động ròng

| Khoản mục (tỷ VNĐ) | Trước (S = 200, COGS = 160) | Sau (S = 500, COGS = 400) |
|--------------------|------------------------------|-----------------------------|
| Tồn kho ($DIO/365 \times COGS$) | 19,7 | 98,6 |
| Phải thu ($DSO/365 \times S$) | 16,4 | 157,5 |
| Phải trả ($DPO/365 \times COGS$) | (17,5) | (16,4) |
| **Vốn lưu động ròng thương mại** | **18,6** | **239,7** |

$$\Delta NWC = 239{,}7 - 18{,}6 = \textbf{221,1 tỷ VNĐ}$$

#### Bước 3: So sánh lợi nhuận và tiền mặt thực sự tạo ra

$$\text{Khoản thiếu hụt tài trợ} = \Delta NWC - \text{Lợi nhuận ròng} = 221{,}1 - 55{,}2 = \textbf{165,9 tỷ VNĐ}$$

Tức là lãi 55,2 tỷ nhưng để tăng trưởng, công ty phải "đóng băng" thêm 221,1 tỷ vào hàng tồn và công nợ. Giả sử hạn mức thấu chi ngân hàng tối đa 100 tỷ VNĐ, vẫn thiếu **65,9 tỷ VNĐ** để trả lương, nộp thuế và thanh toán gốc nợ đến hạn.

#### Diễn giải ý nghĩa kinh doanh

- CCC 190 ngày nghĩa là mỗi đồng chi ra mua linh kiện phải **hơn 6 tháng** mới quay lại tay công ty, trong khi nhà cung cấp chỉ cho trả chậm 15 ngày. Tăng trưởng càng nhanh, khoảng thiếu hụt càng lớn: đây chính là hiện tượng **Overtrading** - kinh doanh vượt quá nguồn vốn lưu động.
- Công ty vỡ nợ dù báo lãi, vì két sắt trống: tiền nằm trong hàng tồn chưa lắp ráp và hóa đơn đại lý chưa thu. Doanh thu là ý niệm, lợi nhuận là quan điểm, **tiền mặt mới là sự thật (Cash is King)**.

**Bài học**: (1) Trước khi nới tín dụng hoặc đẩy tồn kho, hãy tính $\Delta NWC$ và nguồn tài trợ cho nó; (2) theo dõi CCC hằng tháng; (3) tốc độ tăng trưởng bền vững bị giới hạn bởi dòng tiền, không phải bởi nhu cầu thị trường; (4) thưởng cho đội kinh doanh dựa trên **tiền thu về**, không chỉ doanh số ghi nhận.

---

## CHƯƠNG V: CHÍNH SÁCH CHI TRẢ CỔ TỨC & THU HỒI CỔ PHIẾU QUỸ (DIVIDEND POLICY & BUYBACKS)

Sử dụng dòng tiền thặng dư tự do thu về của doanh nghiệp để phân phối lại cho cổ đông thế nào cho tối ưu hóa giá trị công ty là một nghệ thuật tài chính phức tạp. Đối chiếu lý thuyết chính sách cổ tức tại [07-dividend-policy.md](07-dividend-policy.md).

### 1. Cơ sở lý thuyết toán học chuyên sâu

#### A. Định lý Vô hại về Cổ tức của Modigliani-Miller (1961) - Trong bối cảnh không thuế
Miller và Modigliani chứng minh rằng trong một thị trường tài chính hoàn hảo (không thuế, không chi phí giao dịch, không thông tin bất cân xứng), chính sách cổ tức hoàn toàn **không ảnh hưởng** đến giá trị nội tại của doanh nghiệp hay tỷ suất sinh lời của cổ đông. Giá trị công ty thuần túy được quyết định bởi năng lực tạo sinh lời từ tài sản cốt lõi ($EBIT$):

$$V_{\text{with dividend}} = V_{\text{without dividend}}$$

**Tại sao M&M cho rằng cổ tức "vô hại"?** Merton Miller và Franco Modigliani (1961, bài *Dividend Policy, Growth, and the Valuation of Shares*) lập luận: giá trị doanh nghiệp do khả năng sinh lời của tài sản quyết định, không phụ thuộc vào việc chia lợi nhuận bằng cổ tức hay giữ lại. Một cổ đông muốn tiền mặt mà công ty không chia cổ tức có thể **tự tạo cổ tức** (homemade dividend) bằng cách bán một phần cổ phiếu; ngược lại, cổ đông muốn tái đầu tư có thể dùng cổ tức mua thêm cổ phiếu. Khi một công ty trả 1 đồng cổ tức, giá cổ phiếu giảm đúng 1 đồng - tổng tài sản cổ đông không đổi. Nhà đầu tư vì vậy không quan tâm tới chính sách cổ tức nếu không có thuế, chi phí giao dịch và bất cân xứng thông tin; các lý thuyết ở các mục B, C, D sau đây lần lượt nới lỏng từng giả định này.

#### B. Thuyết "Con chim trong tay" (Bird-in-the-Hand Theory của Gordon & Lintner)
Bác bỏ định lý MM bằng việc cho rằng cổ đông thích nhận 1 đồng cổ tức bằng tiền mặt trả ngay hôm nay hơn là lời cam kết lợi nhuận giữ lại tạo tăng trưởng thặng dư vốn tương lai bất định (vì rủi ro tăng cao theo thời gian):

$$r_{equity} = \frac{D_1}{P_0} + g$$

Nhận cổ tức đều đặn làm giảm bớt mức lợi suất yêu cầu kỳ vọng ($r_{equity}$), do đó trực tiếp kéo tăng giá cổ phiếu hôm nay ($P_0$).

**Tại sao lại có tranh luận "Con chim trong tay"?** Myron Gordon (1959) và John Lintner (1962) cho rằng cổ đông coi trọng 1 đồng cổ tức nhận ngay hơn 1 đồng thặng dư vốn kỳ vọng trong tương lai (vì dòng tiền xa thì bất định hơn), nên công ty chi cổ tức cao sẽ có chi phí vốn thấp hơn và giá cổ phiếu cao hơn. M&M phản bác rằng rủi ro của cổ phiếu nằm ở **dòng tiền hoạt động của tài sản**, không phải ở cách chia: việc công ty giữ lại lợi nhuận để tái đầu tư vào dự án sinh lời không làm cổ đông rủi ro hơn. Bằng chứng thực nghiệm chưa ngã ngũ, nhưng quan sát chung là nhà đầu tư thực tế **có phản ứng** với thay đổi cổ tức - phản ứng này chủ yếu do tín hiệu thông tin (mục D) chứ không phải do "thích tiền mặt".

#### C. Thuyết Bất lợi về Thuế (Tax-Preference Theory)
Cho rằng do thuế suất đánh vào thu nhập cổ tức nhận ngay (Dividend Tax Rate) thường cao hơn hẳn mức thuế suất ưu đãi đánh vào chênh lệch thăng dư vốn bán cổ phiếu (Capital Gains Tax Rate), đồng thời thuế thặng dư vốn chỉ phát sinh khi cổ đông thực hiện bán chốt lời (cho phép hoãn thuế). Do đó, cổ đông thích doanh nghiệp giữ lại tiền tái đầu tư tăng giá hơn là chi trả cổ tức cao để tránh bớt gánh nặng thuế tức thì.

#### D. Thuyết Khách hàng ưu ái (Clientele Effect) và Hiệu ứng Tín hiệu (Signaling Effect)
*   **Clientele Effect**: Các nhóm cổ đông khác nhau ưu tiên các phương án chi trả riêng biệt. Nhóm hưu trí, quỹ bảo hiểm cần dòng tiền mặt ổn định thích cổ tức cao; nhóm nhà đầu tư thu nhập cao muốn tránh thuế thu nhập thích doanh nghiệp tích lũy giữ lại vốn tái đầu tư tăng giá trị cổ phiếu.
*   **Signaling Effect**: Do bất cân xứng thông tin, hành động bất ngờ điều chỉnh cổ tức của ban chỉ đạo đóng vai trò truyền đi thông điệp vô cùng mạnh mẽ về tình hình sức khỏe thực sự của công ty:
    $$\text{Tăng cổ tức tịnh tiến} \longrightarrow \text{Tín hiệu DN phát triển dồi dào}$$
    $$\text{Cắt giảm cổ tức đột ngột} \longrightarrow \text{Tín hiệu DN cạn tiền mặt rủi ro cao}$$

#### E. Mô hình Cổ tức Lintner (Lintner's Dividend Model - 1956)
Mô tả cách thức các doanh nghiệp thiết lập chính sách cổ tức mục tiêu dài hạn bám theo sự thay đổi của lợi nhuận ròng có độ trễ:

$$D_t = D_{t-1} + \text{SOA} \times [(\text{Target Payout} \times \text{EPS}_t) - D_{t-1}]$$

Trong đó: $\text{SOA}$ (Speed of Adjustment Coefficient) là tốc độ tự điều chỉnh (dao động từ 0 đến 1), biểu cảm mức độ thận trọng của ban quản trị trước các dòng biến động bất thường của thu nhập doanh nghiệp.

**Tại sao mô hình Lintner lại có dạng "điều chỉnh từng phần"?** Năm 1956, John Lintner phỏng vấn ban lãnh đạo 28 công ty Mỹ và phát hiện: (1) họ **rất ngại cắt giảm cổ tức** và ngại tăng cổ tức nếu chưa chắc mức lợi nhuận mới sẽ bền vững; (2) mục tiêu quan trọng hơn là **ổn định cổ tức** theo thời gian chứ không phải bám sát lợi nhuận từng năm. Công thức phản ánh đúng hành vi này: cổ tức năm nay chỉ dịch chuyển một phần ($SOA$) trong khoảng cách giữa mức cổ tức đang trả và mức cổ tức mục tiêu. $SOA$ càng nhỏ thì cổ tức càng "mượt", nhưng cũng chậm phản ứng với khủng hoảng - nguyên nhân của thảm họa ở Case 10.

#### F. Chương trình Tái đầu tư Cổ tức (DRIPs - Dividend Reinvestment Plans)
Một công cụ tài chính hiện đại cho phép cổ đông tự động hoán đổi dòng cổ tức bằng tiền mặt để lấy thêm cổ phiếu phát hành mới của doanh nghiệp (thường được mua với mức chiết khấu từ 1% - 5% so với thị giá hiện tại và không phải trả chi phí môi giới hoặc giao dịch).
*   *Lợi ích cho doanh nghiệp*: Giúp giữ vững tệp cổ đông trung thành dài hạn và âm thầm tăng tỷ lệ giữ lại vốn (Capital Retention) mà không kích sụt rủi ro Signaling tiêu cực khi công bố cắt giảm cổ tức.

#### G. Biên trình tự thời gian chi trả Cổ tức thực chiến (The Dividend Timeline)
Mọi chính sách chia cổ tức đều được vận hành nghiêm cẩn dọc theo 4 mốc mốc thời gian pháp lý đặc biệt:

```
Declaration Date      Ex-Dividend Date       Holder-of-Record Date       Payment Date
     (Day 0)              (Day 15)                 (Day 17)                (Day 30)
──────┼───────────────────────┼────────────────────────┼───────────────────────┼──────
Công bố cổ tức        Ngày GD Không hưởng     Chốt danh sách cổ đông     Tiền mặt chuyển 
HĐQT phê duyệt        Giá cổ phiếu sụt giảm   chính thức ghi nhận sổ     về ví tài khoản
```

1.  **Declaration Date (Ngày công bố)**: Ban quản trị họp HĐQT thông qua quyết định, quy định chi tiết mức chi trả cổ tức cho mỗi cổ đông.
2.  **Ex-Dividend Date (Ngày giao dịch không hưởng quyền)**: Mốc quan trọng nhất. Nhà đầu tư mua cổ phiếu vào ngày này hoặc sau đó sẽ **không** được hưởng quyền nhận đợt cổ tức hiện hữu. Giá cổ phiếu mở cửa phiên này sẽ tự động bị sở giao dịch kéo sụt tương ứng mức tiền mặt chia ra.
3.  **Holder-of-Record Date (Ngày chốt danh sách)**: Ngày công ty rà soát đóng sổ ghi nhận chính danh toàn bộ cổ đông được nhận tiền. (Cách ngày Ex-Dividend đúng 1 hoặc 2 ngày làm việc).
4.  **Payment Date (Ngày thanh toán)**: Ngày tiền cổ tức thực sự đổ về tài khoản ngân hàng của cổ đông sở hữu.

---

### 2. Case Study 9 (Thành công): TẬP ĐOÀN TIÊU DÙNG NHANH C-PHARMA – Chọn mua lại cổ phiếu hay trả cổ tức

#### Bối cảnh

C-Pharma sản xuất hàng tiêu dùng gia đình, không có nợ vay, doanh thu tăng đều 5%/năm. Lợi nhuận ròng $NI = 200$ triệu USD; 100 triệu cổ phiếu đang lưu hành; giá thị trường $P_0 = 36$ USD. Ban lãnh đạo có **180 triệu USD** tiền mặt dư thừa không có dự án đầu tư tốt hơn và phải quyết định trả lại cho cổ đông bằng cách nào.

$$EPS_0 = \frac{200}{100} = 2{,}0 \text{ USD} \qquad P/E = \frac{36}{2{,}0} = 18{,}0x \qquad \text{Vốn hóa} = 100 \times 36 = 3.600 \text{ triệu USD}$$

#### Bước 1: Phương án A - Trả cổ tức tiền mặt

Cổ tức mỗi cổ phiếu $= 180/100 = 1{,}80$ USD. Vào ngày giao dịch không hưởng quyền, giá cổ phiếu giảm tương ứng:

$$P_{\text{ex-div}} = 36{,}00 - 1{,}80 = 34{,}20 \text{ USD}$$

Tổng tài sản của cổ đông trên mỗi cổ phiếu trước thuế: $34{,}20 + 1{,}80 = 36{,}00$ USD - **không đổi** (đúng như M&M dự đoán). Nếu thuế thu nhập từ cổ tức là 10% (giả định), thực nhận $1{,}80 \times 0{,}9 = 1{,}62$ USD, tổng tài sản sau thuế $34{,}20 + 1{,}62 = 35{,}82$ USD - **mất 0,18 USD** vì thuế, và cổ đông bị đánh thuế ngay dù không muốn bán cổ phiếu.

#### Bước 2: Phương án B - Mua lại cổ phiếu quỹ trên thị trường

Với giá 36 USD:

$$\text{Số cổ phiếu mua} = \frac{180}{36} = 5 \text{ triệu} \quad \Rightarrow \quad \text{Số cổ phiếu còn lại} = 100 - 5 = 95 \text{ triệu}$$

$$EPS_{\text{new}} = \frac{200}{95} = \textbf{2,105 USD} \quad (\text{tăng } 5{,}26\%)$$

Nếu thị trường giữ nguyên hệ số P/E = 18x:

$$P_{\text{new}} = 18 \times 2{,}105 = \textbf{37,89 USD} \quad (\text{tăng } 1{,}89 \text{ USD, } +5{,}26\%)$$

Cổ đông không bị đánh thuế ngay mà chỉ phải trả thuế thặng dư vốn khi bán, tức có quyền **hoãn thuế**.

#### Bước 3: Phân tích sâu - EPS tăng không đồng nghĩa với tạo ra giá trị

Kết quả 37,89 USD ở Bước 2 phụ thuộc vào giả định "P/E giữ nguyên 18x". Để kiểm tra thực chất, ta tính theo **giá trị nội tại**: giả sử giá trị nội tại của vốn chủ (bao gồm 180 triệu tiền mặt) là $45 \times 100 = 4.500$ triệu USD. Sau khi chi 180 triệu để mua lại ở giá $P$, giá trị còn lại cho cổ đông ở lại chia cho số cổ phiếu còn lại:

| Giá mua lại $P$ | Số cổ phiếu mua (triệu) | Cổ phiếu còn lại (triệu) | Giá trị nội tại/cổ phiếu $= 4.320 / \text{còn lại}$ | So với 45 USD |
|-----------------|-------------------------|---------------------------|--------------------------------------------------|----------------|
| 36 (thấp hơn nội tại) | 5,00 | 95,00 | 45,47 | **+0,47** |
| 45 (bằng nội tại) | 4,00 | 96,00 | 45,00 | 0,00 |
| 55 (cao hơn nội tại) | 3,27 | 96,73 | 44,66 | **-0,34** |

#### Diễn giải ý nghĩa kinh doanh

1. **Cổ tức** là lựa chọn trung tính về giá trị trước thuế, bất lợi về thuế và gửi tín hiệu "cam kết" cho thị trường (nên khó cắt giảm về sau).
2. **Mua lại cổ phiếu** chỉ làm tăng giá trị cho cổ đông ở lại khi **giá mua thấp hơn giá trị nội tại**: phần giá trị tăng thêm 0,47 USD/cổ phiếu thực chất được chuyển từ những cổ đông bán ra (bán ở 36 trong khi đáng giá 45). Nếu ban lãnh đạo mua lại khi giá cổ phiếu đang quá cao (55 USD), họ **phá hủy** 0,34 USD giá trị cho mỗi cổ phiếu ở lại.
3. EPS tăng cơ học (+5,26%) chỉ là phép chia với mẫu số nhỏ hơn; không nên dùng nó để khoe "hiệu quả" nếu giá mua cao.
4. Linh hoạt: mua lại cổ phiếu không tạo kỳ vọng lặp lại như cổ tức, nên phù hợp với dòng tiền dư thừa **không đều** hằng năm.

**Bài học**: quyết định hoàn vốn cho cổ đông bắt đầu từ câu hỏi "giá cổ phiếu hiện đang cao hay thấp so với giá trị nội tại?" - không phải từ câu hỏi "EPS tăng bao nhiêu".

---

### 3. Case Study 10 (Thất bại): CHUỖI KHÁCH SẠN H-HOTEL – Cổ tức cứng nhắc đưa doanh nghiệp tới phá sản

#### Bối cảnh

H-Hotel duy trì cổ tức tiền mặt cố định **3,00 USD/cổ phiếu** suốt 10 năm, kể cả khi kinh doanh sa sút, để duy trì "tín hiệu khỏe mạnh" (Signaling Effect). Giả sử công ty có 20 triệu cổ phiếu, giá cổ phiếu 45 USD. Năm 2020, đại dịch khiến EPS tụt xuống **0,50 USD**.

#### Bước 1: Đo hệ số chi trả cổ tức (Payout Ratio)

$$\text{Payout Ratio} = \frac{DPS}{EPS} = \frac{3{,}00}{0{,}50} = \textbf{600\%}$$

Lợi nhuận ròng $= 0{,}50 \times 20 = 10$ triệu USD, nhưng tiền cổ tức phải trả $3{,}00 \times 20 = 60$ triệu USD. Mỗi năm thiếu hụt $60 - 10 = 50$ triệu USD, tương đương 2,50 USD/cổ phiếu.

#### Bước 2: Mô phỏng hậu quả khi bù thiếu hụt bằng nợ vay (lãi suất 9%, thuế 20%)

| Năm | Lợi nhuận trước chi phí lãi phát sinh thêm | Lãi vay phát sinh thêm sau thuế | Lợi nhuận ròng | Cổ tức chi | Vay thêm trong năm | Nợ tích lũy cuối năm |
|-----|-----------------------------------------------|---------------------------------|-----------------|------------|---------------------|-----------------------|
| 1 | 10,0 | 0 | 10,0 | 60 | 50,0 | 50,0 |
| 2 | 10,0 | $50 \times 9\% \times 0{,}8 = 3{,}6$ | 6,4 | 60 | 53,6 | 103,6 |

Sau 2 năm, công ty vay thêm **103,6 triệu USD chỉ để trả cổ tức**, trong khi lợi nhuận suy giảm vì gánh lãi vay. Xếp hạng tín nhiệm tụt xuống mức rác, ngân hàng cắt hạn mức thấu chi, công ty không còn tiền trả lương, đành xin bảo hộ phá sản; giá cổ phiếu rơi từ 45 USD xuống 2 USD.

#### Bước 3: Phương án đúng - dùng mô hình Lintner để điều chỉnh

Với mục tiêu chi trả 50% EPS và tốc độ điều chỉnh $SOA$ khác nhau, cổ tức năm khủng hoảng là $D_t = D_{t-1} + SOA \times (0{,}5 \times EPS - D_{t-1})$:

| SOA | Cổ tức mới | Payout so với EPS 0,50 | Tiết kiệm trên 20 triệu cổ phiếu |
|-----|------------|--------------------------|-----------------------------------|
| 0,4 (quá thận trọng) | $3{,}00 + 0{,}4 \times (0{,}25 - 3{,}00) = 1{,}90$ | 380% | 22 triệu USD/năm |
| 0,7 | $3{,}00 + 0{,}7 \times (0{,}25 - 3{,}00) = 1{,}075$ | 215% | 38,5 triệu USD/năm |
| 1,0 (điều chỉnh ngay) | $0{,}25$ | 50% | **55 triệu USD/năm** |

#### Diễn giải ý nghĩa kinh doanh

Mô hình Lintner mô tả hành vi "mượt hóa" cổ tức của quản lý, nhưng **mượt hóa quá mức khi nền tảng kinh doanh sụp đổ là nguy hiểm**: ở $SOA = 0{,}4$ cổ tức vẫn gấp 3,8 lần EPS. Cắt giảm cổ tức trong khủng hoảng gửi tín hiệu tiêu cực ngắn hạn nhưng bảo vệ thanh khoản; không cắt thì tín hiệu tiêu cực đến muộn và lớn hơn nhiều (phá sản).

**Bài học**: chính sách cổ tức cần **linh hoạt theo dòng tiền tự do thực tế** (mô hình cổ tức thặng dư - Residual Dividend Policy: giữ lại vốn cho dự án NPV dương trước, chia phần dư), cộng với quỹ dự phòng thanh khoản; không đi vay để trả cổ tức chỉ nhằm bảo vệ "bộ mặt" trên thị trường.

---

## CHƯƠNG VI: THUYẾT DANH MỤC ĐẦU TƯ HIỆU QUẢ MARKOWITZ & CHỈ SỐ RISK - RETURN

Xác định mức bù đắp và định lượng mối quan hệ giữa rủi ro gánh chịu và lợi suất sinh lời thặng dư trong quá trình cơ cấu dòng tiền đầu tư. Xem thêm chi tiết chỉ số rủi ro tại [08-risk-and-return.md](08-risk-and-return.md).

### 1. Cơ sở lý thuyết toán học chuyên sâu

#### A. Công thức tính Lợi suất và Rủi ro của Danh mục đầu tư 2 Tài sản
*   **Lợi suất kỳ vọng của danh mục (Expected Return of Portfolio - $E(R_p)$)**:
    $$E(R_p) = w_A E(R_A) + w_B E(R_B)$$
*   **Phương sai đo lường rủi ro của danh mục (Portfolio Variance - $\sigma_p^2$)**:
    $$\sigma_p^2 = w_A^2 \sigma_A^2 + w_B^2 \sigma_B^2 + 2 w_A w_B \sigma_A \sigma_B \rho_{AB}$$

Trong đó:
*   $w_A, w_B$: Tỷ trọng phân bổ tài chính vào tài sản A và B ($w_A + w_B = 1$).
*   $\sigma_A, \sigma_B$: Độ lệch chuẩn rủi ro của tài sản A và B.
*   $\rho_{AB}$: Hệ số tương quan (Correlation Coefficient) của hai tài sản (Biến thiên từ $-1.0$ đến $+1.0$).

**Tại sao công thức phương sai danh mục có số hạng thứ ba?** Harry Markowitz (1952, bài *Portfolio Selection*; Nobel Kinh tế 1990) nhận ra điều mà trực giác "đừng bỏ trứng vào một giỏ" chưa lượng hóa được: rủi ro của danh mục *không phải* là trung bình rủi ro các thành phần. Hai số hạng đầu $w_A^2\sigma_A^2 + w_B^2\sigma_B^2$ là rủi ro riêng từng tài sản; số hạng thứ ba $2w_Aw_B\sigma_A\sigma_B\rho_{AB}$ đo **mức độ hai tài sản "cùng lên cùng xuống"**. Khi $\rho = +1$, số hạng này lớn nhất và rủi ro danh mục bằng đúng trung bình có trọng số - không có lợi ích đa dạng hóa. Khi $\rho < 1$, số hạng này nhỏ đi, và khi $\rho < 0$ thì nó trở thành *âm*, trực tiếp kéo rủi ro danh mục xuống thấp hơn cả tài sản an toàn nhất. Đây là lý do vì sao Markowitz khẳng định: nhà đầu tư không nên đánh giá từng tài sản riêng lẻ mà phải đánh giá **đóng góp của nó vào cả danh mục**.

#### B. Phép màu đa dạng hóa rủi ro của Harry Markowitz (1952)
Nếu hệ số tương quan giữa hai tài sản nhỏ hơn 1 hoàn toàn ($\rho_{AB} < 1$), độ lệch chuẩn rủi ro của danh mục sẽ luôn **nhỏ hơn** mức trung bình bình quyền độ lệch chuẩn của từng tài sản riêng lẻ:

$$\sigma_p < w_A \sigma_A + w_B \sigma_B$$

Nếu đạt mốc tương quan phủ định hoàn hảo tối ưu ($\rho_{AB} = -1.0$), ta có thể thiết kế một danh mục đầu tư tích hợp triệt tiêu hoàn toàn rủi ro phi hệ thống về mốc 0 tuyệt đối.

```
 Lợi suất E(R)
     │                                 * * *  <─── Danh mục Hiệu Quả (Efficient Frontier)
     │                             *
     │                          *
     │                       *  <─── Điểm Tối Thiểu Rủi Ro (MVP - Minimum Variance Portfolio)
     │                       *
     │                          *
     │                             *
     │                                 *
     └───────────────────────────────────────────── Rủi ro (Độ lệch chuẩn \sigma)
```

#### C. Thống nhất mô hình: Đường biên hiệu quả (Efficient Frontier) và Điểm tiếp xúc (Tangency Portfolio)
Đường biên hiệu quả là tập hợp tất cả các danh mục đầu tư tối ưu đem lại mức sinh lời kỳ vọng lớn nhất ứng với mỗi mức độ rủi ro gánh chịu nhất định. Khi tích hợp thêm tài sản phi rủi ro ($R_f$) vào mô hình, ta xây dựng được **Đường thị trường vốn (Capital Market Line - CML)** nối từ $R_f$ tiếp xúc trực tiếp với Đường biên hiệu quả tại **Điểm tiếp xúc tối ưu (Tangency Portfolio)** - nơi danh mục sở hữu tỷ suất Sharpe là lớn nhất toàn hệ thống.

#### D. So sánh Đường thị trường vốn (CML) và Đường thị trường chứng khoán (SML)
*   **Đường thị trường vốn (CML - Capital Market Line)**: Thể hiện mối quan hệ giữa lợi suất kỳ vọng và **tổng rủi ro (độ lệch chuẩn $\sigma$)** của các danh mục đầu tư hiệu quả. Chỉ những danh mục nằm trên CML mới là danh mục tối ưu.
*   **Đường thị trường chứng khoán (SML - Security Market Line)**: Thể hiện mối quan hệ giữa lợi suất kỳ vọng và **hệ số rủi ro hệ thống Beta ($\beta$)**. SML áp dụng cho mọi loại chứng khoán riêng lẻ cũng như danh mục bất kỳ. Tất cả các tài sản định giá đúng trên thị trường cân bằng bắt buộc phải nằm chính xác trên SML.

#### E. Thước đo đánh giá hiệu quả quản trị rủi ro danh mục (Performance Metrics)
1.  **Chỉ số Sharpe (Sharpe Ratio)**: Đo lường mức bù lợi nhuận trên 1 đơn vị tổng rủi ro ($\sigma_p$):
    $$\text{Sharpe Ratio} = \frac{E(R_p) - R_f}{\sigma_p}$$
2.  **Chỉ số Treynor (Treynor Ratio)**: Đo lường mức bù lợi nhuận trên 1 đơn vị rủi ro hệ thống ($\beta_p$):
    $$\text{Treynor Ratio} = \frac{E(R_p) - R_f}{\beta_p}$$
3.  **Hệ số Alpha của Jensen (Jensen's Alpha)**: Đo lường khả năng tạo lợi nhuận vượt trội của quỹ so với kỳ vọng định vị của mô hình thị trường CAPM:
    $$\alpha_p = R_p - [R_f + \beta_p(R_m - R_f)]$$
    *   Nếu **$\alpha_p > 0$**: Nhà quản lý tạo giá trị thực thặng dư cho nhà đầu tư (Outperform).
    *   Nếu **$\alpha_p < 0$**: Nhà quản lý hoạt động kém hiệu quả hơn chỉ số thị trường (Underperform).

**Tại sao có ba thước đo khác nhau (Sharpe, Treynor, Jensen)?** Chỉ nhìn lợi suất thì quỹ lãi 20% với rủi ro gấp đôi chưa chắc tốt hơn quỹ lãi 12%. William Sharpe (1966) chuẩn hóa phần lợi suất vượt $R_f$ theo **tổng rủi ro** ($\sigma$) - phù hợp khi đánh giá *toàn bộ* danh mục của nhà đầu tư. Jack Treynor (1965) chuẩn hóa theo **rủi ro hệ thống** ($\beta$) - phù hợp khi quỹ chỉ là *một phần* của danh mục lớn hơn đã đa dạng hóa. Michael Jensen (1968) hỏi trực tiếp: sau khi trừ đi phần lợi suất mà CAPM đã "giải thích" bằng Beta, nhà quản lý còn tạo thêm được bao nhiêu (alpha)? Ba thước đo cùng đánh giá "lợi suất điều chỉnh rủi ro", khác nhau ở loại rủi ro được dùng làm mẫu số.

#### F. Mở rộng đa nhân tố: Mô hình Fama-French 3-Factor và 5-Factor
Khắc phục nhược điểm chỉ dựa vào một hệ số Beta duy nhất của CAPM, Fama và French (1993, 2015) cải tiến mô hình đo lường rủi ro hệ thống thông qua các yếu tố hành vi thực nghiệm:
1.  **Hệ thống 3-Factor**:
    $$R_{it} - R_{ft} = \alpha_i + \beta_{i1}(R_{mt} - R_{ft}) + \beta_{i2}\text{SMB}_t + \beta_{i3}\text{HML}_t + \epsilon_{it}$$
    *   $\text{SMB}$ (Small Minus Big): Phần bù quy mô (Vốn hóa nhỏ vs Vốn hóa lớn).
    *   $\text{HML}$ (High Minus Low): Phần bù giá trị (Book-to-Market cao vs thấp).
2.  **Hệ thống 5-Factor**: Bổ sung thêm hai nhân tố quyết định hiệu quả sinh lợi rực rỡ dài hạn của công ty:
    *   $\text{RMW}$ (Robust Minus Weak): Chênh lệch lợi nhuận ròng hoạt động cực tốt và cực yếu.
    *   $\text{CMA}$ (Conservative Minus Aggressive): Chênh lệch giữa doanh nghiệp tái đầu tư bảo thủ, khoa học tài chính vs doanh nghiệp đầu tư quá ồ ạt, rủi ro cao.

**Tại sao cần Fama-French?** CAPM dự đoán lợi suất chỉ phụ thuộc Beta, nhưng dữ liệu thị trường Mỹ cho thấy cổ phiếu vốn hóa nhỏ và cổ phiếu giá trị (book-to-market cao) liên tục đem lại lợi suất vượt mức CAPM giải thích. Eugene Fama và Kenneth French (1993) bổ sung hai nhân tố SMB và HML để "bắt" những phần bù này; năm 2015 họ thêm RMW (lợi nhuận) và CMA (đầu tư) vì thực nghiệm cho thấy doanh nghiệp sinh lời cao, đầu tư thận trọng cũng đem lại lợi suất vượt trội.

---

### 2. Case Study 11 (Thành công): QUỸ ĐẦU TƯ PAN-CAPITAL – Giảm rủi ro nhờ đổi tương quan thay vì đổi lợi suất

#### Bối cảnh

Pan-Capital quản lý danh mục **500 triệu USD**, gồm cổ phiếu A (bất động sản xây dựng, tỷ trọng 60% = 300 triệu USD) và cổ phiếu B (thép xây dựng, tỷ trọng 40% = 200 triệu USD). Do cùng phụ thuộc chu kỳ xây dựng nên hai cổ phiếu có tương quan rất cao.

| Tài sản | Lợi suất kỳ vọng | Độ lệch chuẩn | Ghi chú |
|---------|------------------|----------------|---------|
| A (Bất động sản) | 15% | 25% | - |
| B (Thép) | 11% | 18% | $\rho_{AB} = +0{,}80$ |
| C (Chứng chỉ vàng) | 9% | 12% | $\rho_{AC} = -0{,}30$ |

Lãi suất phi rủi ro $R_f = 5\%$.

#### Bước 1: Hiệu suất danh mục ban đầu (60% A + 40% B)

$$E(R_p) = 0{,}60 \times 15\% + 0{,}40 \times 11\% = 9{,}0\% + 4{,}4\% = \textbf{13,4\%}$$

$$\sigma_p^2 = (0{,}60^2 \times 0{,}25^2) + (0{,}40^2 \times 0{,}18^2) + (2 \times 0{,}60 \times 0{,}40 \times 0{,}25 \times 0{,}18 \times 0{,}80)$$

$$\sigma_p^2 = 0{,}0225 + 0{,}005184 + 0{,}01728 = 0{,}044964 \quad \Rightarrow \quad \sigma_p = \sqrt{0{,}044964} = \textbf{21,2\%}$$

$$\text{Sharpe} = \frac{13{,}4\% - 5\%}{21{,}2\%} = \textbf{0,396}$$

Rủi ro trung bình có trọng số nếu không có đa dạng hóa là $0{,}6 \times 25\% + 0{,}4 \times 18\% = 22{,}2\%$; thực tế $21{,}2\%$ - gần như không hưởng được lợi ích đa dạng hóa vì $\rho = 0{,}80$ quá cao.

#### Bước 2: Chỉ riêng tương quan quyết định bao nhiêu rủi ro? (giữ nguyên 60% A + 40% B)

| $\rho_{AB}$ | +1,0 | +0,8 | +0,5 | 0 | -0,5 | -1,0 |
|-------------|------|------|------|---|------|------|
| $\sigma_p$ | 22,20% | 21,20% | 19,62% | 16,64% | 12,99% | 7,80% |

Chỉ cần giảm tương quan từ +0,8 xuống 0 là rủi ro giảm từ 21,2% còn 16,6% mà lợi suất kỳ vọng không đổi.

#### Bước 3: Tái cơ cấu - thay toàn bộ Thép (B) bằng chứng chỉ Vàng (C)

Chuyển 200 triệu USD từ B sang C (tỷ trọng 60% A, 40% C):

$$E(R_{p,\text{new}}) = 0{,}60 \times 15\% + 0{,}40 \times 9\% = 9{,}0\% + 3{,}6\% = \textbf{12,6\%}$$

$$\sigma_{p,\text{new}}^2 = 0{,}0225 + (0{,}40^2 \times 0{,}12^2) + (2 \times 0{,}60 \times 0{,}40 \times 0{,}25 \times 0{,}12 \times (-0{,}30))$$

$$\sigma_{p,\text{new}}^2 = 0{,}0225 + 0{,}002304 - 0{,}00432 = 0{,}020484 \quad \Rightarrow \quad \sigma_{p,\text{new}} = \textbf{14,31\%}$$

$$\text{Sharpe}_{\text{new}} = \frac{12{,}6\% - 5\%}{14{,}31\%} = \textbf{0,531}$$

| Chỉ tiêu | Danh mục cũ (A + B) | Danh mục mới (A + C) | Thay đổi |
|----------|---------------------|------------------------|----------|
| Lợi suất kỳ vọng | 13,4% | 12,6% | -0,8 điểm |
| Rủi ro ($\sigma$) | 21,20% | 14,31% | **-6,89 điểm** |
| Sharpe | 0,396 | 0,531 | **+34%** |

#### Bước 4 (mở rộng): Tìm danh mục phương sai nhỏ nhất giữa A và C

Tỷ trọng A tại điểm phương sai nhỏ nhất (MVP) của hai tài sản là $w_A = \frac{\sigma_C^2 - \rho\sigma_A\sigma_C}{\sigma_A^2 + \sigma_C^2 - 2\rho\sigma_A\sigma_C} = \frac{0{,}0144 + 0{,}009}{0{,}0625 + 0{,}0144 + 0{,}018} = 24{,}66\%$, cho $\sigma_p = 9{,}29\%$, $E(R_p) = 10{,}48\%$, Sharpe $= (10{,}48 - 5)/9{,}29 = \textbf{0,590}$ - còn cao hơn cả danh mục 60/40 mới. Điều này cho thấy tỷ trọng 60% A vẫn nghiêng về rủi ro; Pan-Capital có thể chọn điểm trên Đường biên hiệu quả phù hợp với khẩu vị rủi ro của nhà đầu tư.

#### Diễn giải ý nghĩa kinh doanh

- Lợi suất kỳ vọng chỉ giảm 0,8 điểm phần trăm trong khi rủi ro giảm 6,89 điểm: nhà đầu tư nhận mỗi đơn vị rủi ro được bù nhiều hơn 34%.
- Nguồn gốc của sự cải thiện là hệ số tương quan **$\rho_{AC} = -0{,}30$** (vàng là tài sản trú ẩn, thường tăng khi bất động sản giảm), làm số hạng thứ ba của phương sai âm (-0,00432).
- Cảnh báo: tương quan **không cố định** - trong khủng hoảng thanh khoản, nhiều tài sản cùng giảm nên tương quan có thể tăng đột biến về +1. Cần stress-test danh mục với các giả định tương quan xấu hơn.

**Bài học**: muốn giảm rủi ro, không nhất thiết phải chọn tài sản ít rủi ro hơn; hãy chọn tài sản có **tương quan thấp hoặc âm** với phần còn lại của danh mục.

---

## CHƯƠNG VII: SÁP NHẬP & MUA BÁN DOANH NGHIỆP (M&A) & ĐỊNH GIÁ SYNERGY

M&A là công cụ mở rộng quy mô phi hữu cơ (Inorganic Growth) mạnh mẽ nhất giúp doanh nghiệp nhanh chóng thâu tóm chuỗi giá trị nhưng đòi hỏi kỹ năng định giá đồng thuận vô cùng phức tạp. Cơ sở lý thuyết sáp nhập được mô tả đầy đủ tại [09-mergers-and-acquisitions.md](09-mergers-and-acquisitions.md).

### 1. Cơ sở lý thuyết toán học chuyên sâu

#### A. Công thức Tính toán Giá trị Đồng thuận Sáp nhập (Synergy Value)
Giá trị sáp nhập cộng hưởng tổng thể ($V_{AB}$) lớn hơn tổng thể giá trị đứng độc lập riêng lẻ của công ty Thâu tóm ($V_A$) và công ty Mục tiêu ($V_B$):

$$V_{AB} = V_A + V_B + \text{Synergies} - \text{Expenses}$$

Trong đó, các giá trị đồng thuận sáp nhập (Synergies) gồm:
1.  **Cost Synergies (Cộng hưởng cắt giảm chi phí)**: Giảm bớt bộ máy trùng lặp hoạt động, tinh giản trụ sở, gom đầu mối hoạt động chuỗi cung ứng vật tư sỉ lẻ:
    $$\text{Cost Synergies} = \sum_{t=1}^{n} \frac{\Delta \text{Cost Savings}_t}{(1 + WACC)^t}$$
2.  **Revenue Synergies (Cộng hưởng gia tăng doanh thu)**: Bán chéo dòng sản phẩm (Cross-selling), tăng sức mạnh chi phối thị trường nâng giá bán, thâm nhập tệp khách hàng phân phối chéo.

**Tại sao phải định giá synergy riêng, và vì sao đa số thương vụ M&A thất bại?** Khi mua một công ty, bên mua đã phải trả giá thị trường của công ty đó (đã phản ánh giá trị đứng riêng). Giá trị **chỉ phát sinh từ việc hai công ty kết hợp** (cắt giảm chi phí trùng lặp, bán chéo sản phẩm...) mới là nguồn lợi ích thực của thương vụ. Vấn đề là bên bán biết rõ điều này và sẽ đòi một phần synergy dưới dạng **premium**; nếu premium vượt synergy thì bên mua làm giàu cho cổ đông bên bán bằng tiền của cổ đông mình. Công thức $NPV_{\text{Acquisition}} = \text{Synergies} - \text{Premium}$ là thước đo kỷ luật này. Richard Roll (1986) đưa ra "giả thuyết kiêu ngạo" (hubris hypothesis): các nhà quản lý bên mua thường đánh giá quá cao khả năng tạo synergy nên trả giá quá cao, đó là một nguyên nhân phổ biến khiến giá trị cho cổ đông bên mua bị hao hụt.

#### B. Phân bổ thặng dư thâu tóm và định vị Giá mua tối đa thương lượng (Premium limits)
*   **Mức giá mua đề xuất (Premium paid)**: Khoản tiền bên mua chi trả vượt quá giá trị thị trường nội tại đứng riêng lẻ của công ty đích ($V_B$):
    $$\text{Premium} = \text{Price Paid} - V_B$$
*   **Giá trị ròng thu về cho cổ đông bên mua sau sáp nhập (NPV of Acquisition)**:
    $$NPV_{\text{Acquisition}} = \text{Synergies} - \text{Premium}$$
    *   Toàn bộ nỗ lực thâu tóm của bên mua chỉ thực sự tạo ra thêm giá trị cho cổ đông của mình khi và chỉ khi: **$\text{Premium} < \text{Synergies}$**.
    *   **Mức giá mua kịch trần tối đa chấp thuận (Maximum Walk-away purchase price)**:
        $$\text{Price}_{\text{Max}} = V_B + \text{Synergies}$$

#### C. Phân tích hoán đổi cổ phần (Stock-For-Stock Swap)
Quyết định tỷ lệ trao đổi cổ phiếu ($ER$ - Exchange Ratio) tối ưu bám theo thị giá của cả hai bên bán và mua:

$$ER = \frac{\text{Số lượng cổ phần mới phát hành trao đổi}}{\text{Số lượng cổ phần sẵn có của công ty Mục Tiêu}}$$

*   Tỷ số này cho phép định lượng mức độ pha loãng thu nhập trên mỗi cổ phần ($EPS$) của bên thâu tóm sau thương vụ sáp nhập.
*   Nếu P/E của bên thâu tóm cao hơn hẳn P/E của công ty đích, chỉ số EPS của công ty sau sáp nhập sẽ tự động được gia tăng cơ học (**Accretive**). Ngược lại, nếu mua một công ty có định giá P/E cao vọt bằng cổ phiếu P/E thấp của mình, EPS sẽ bị pha loãng thê thảm (**Dilutive**), kích hoạt làn sóng bán tháo thanh lý của cổ đông lớn.

#### D. Ma trận kỹ thuật phòng vệ chống thâu tóm thù địch (Takeover Defenses)

| Kỹ thuật phòng thủ | Cơ chế hoạt động nội tại của tài sản | Tác dụng cản trở đối thủ |
|---------------------|-------------------------------------|---------------------------|
| **1. Poison Pill** | Cho phép cổ đông mua thêm cổ phần với giá cực rẻ sát sạt | Làm loãng cực mạnh tỷ lệ sở hữu của bên thôn tính |
| **2. Greenmail** | Công ty dùng tiền mua lại cổ phần của kẻ đi thâu tóm với Premium cao | Kẻ thâu tóm tháo chạy nhận khoản tài chênh lệch |
| **3. Golden Parachute**| Ký hợp đồng bồi thường khổng lồ cho ban quản trị nếu bị sa thải | Tạo gánh nặng tài chính ép nản lòng địch thủ |
| **4. White Knight** | Tìm kiếm đồng minh thân tín mua lại thân thiện với giá cao hơn | Cứu doanh nghiệp thoát khỏi bàn tay chiếm hữu tàn bạo |

---

### 2. Case Study 12 (Thành công): TẬP ĐOÀN ĐỒ UỐNG BEV-CO – Thâu tóm thương hiệu trà đóng chai Tea-Pro

#### Bối cảnh

Bev-Co (giá trị độc lập $V_A = 8.000$ triệu USD, lợi nhuận ròng 400 triệu USD, 400 triệu cổ phiếu giá 20 USD, P/E = 20x) muốn mua thương hiệu trà xanh đóng chai Tea-Pro (giá trị độc lập $V_B = 200$ triệu USD, lợi nhuận ròng giả định 10 triệu USD). Tea-Pro tăng trưởng chững lại vì hệ thống phân phối yếu, còn Bev-Co có mạng lưới cửa hàng tiện lợi rộng.

#### Bước 1: Định giá Synergy

- **Cost synergies**: sáp nhập hai trụ sở, hợp nhất mua sắm vật tư giúp tiết kiệm **8 triệu USD/năm** sau thuế, dòng tiền vĩnh viễn, chiết khấu ở $WACC = 10\%$:

$$PV(\text{Cost}) = \frac{8}{0{,}10} = \textbf{80 triệu USD}$$

- **Revenue synergies**: đưa Tea-Pro vào mạng lưới phân phối của Bev-Co, thêm **12 triệu USD/năm** dòng tiền ròng:

$$PV(\text{Revenue}) = \frac{12}{0{,}10} = \textbf{120 triệu USD}$$

$$\text{Tổng Synergies} = 80 + 120 = \textbf{200 triệu USD}$$

#### Bước 2: Xác định khung giá có thể trả

$$\text{Price}_{\text{Max}} = V_B + \text{Synergies} = 200 + 200 = \textbf{400 triệu USD}$$

Trả đến 400 triệu thì Bev-Co hòa vốn (NPV = 0), chuyển 100% synergy sang cổ đông Tea-Pro. Bev-Co chào giá **premium 40%**:

$$\text{Price Paid} = 200 \times 1{,}40 = \textbf{280}; \quad \text{Premium} = 280 - 200 = \textbf{80 triệu USD}$$

#### Bước 3: Thanh toán bằng tiền mặt - NPV của thương vụ

$$NPV_{\text{Bev-Co}} = \text{Synergies} - \text{Premium} = 200 - 80 = \textbf{+120 triệu USD}$$

Giá trị Bev-Co sau thương vụ (đã trừ tiền mặt trả ra):

$$V_{\text{Bev-Co sau}} = V_A + V_B + \text{Synergies} - \text{Price Paid} = 8.000 + 200 + 200 - 280 = \textbf{8.120 triệu USD}$$

(tức tăng 120 triệu so với 8.000). Phân chia thặng dư: cổ đông Tea-Pro nhận 80 triệu (premium), cổ đông Bev-Co nhận 120 triệu, tổng đúng bằng 200 triệu synergy. Bev-Co giữ **60%** thặng dư vì chỉ nhượng 40%.

#### Bước 4: Thanh toán bằng cổ phiếu - phân tích hoán đổi và EPS

Nếu trả bằng cổ phiếu Bev-Co (giá 20 USD): phát hành $280/20 = 14$ triệu cổ phiếu mới, tổng 414 triệu cổ phiếu (Tea-Pro nắm 3,38%).

| Chỉ tiêu | Chưa tính synergy | Tính cả synergy sau thuế 20 triệu USD/năm |
|----------|--------------------|--------------------------------------------|
| Lợi nhuận hợp nhất | $400 + 10 = 410$ | $410 + 20 = 430$ |
| EPS sau sáp nhập | $410/414 = 0{,}990$ USD | $430/414 = 1{,}039$ USD |
| So với EPS trước (1,000) | **-0,97% (Dilutive)** | **+3,86% (Accretive)** |

Lý do: Bev-Co trả P/E $280/10 = 28x để mua công ty có lợi nhuận nhỏ, cao hơn P/E của chính mình (20x), nên ban đầu EPS bị pha loãng; synergy sẽ bù đắp. Chia sẻ rủi ro/thặng dư: nếu synergy đúng như kỳ vọng, giá trị hợp nhất $= 8.000 + 200 + 200 = 8.400$ triệu USD, giá trị mỗi cổ phiếu $8.400/414 = 20{,}29$ USD. Cổ đông cũ Bev-Co thu được $400 \times 20{,}29 - 8.000 = +115{,}9$ triệu USD; cổ đông Tea-Pro $14 \times 20{,}29 - 200 = +84{,}1$ triệu USD (tổng 200). Khi trả bằng cổ phiếu, Tea-Pro **cùng gánh rủi ro synergy**: nếu synergy không xảy ra, họ chịu thiệt cùng Bev-Co, trong khi thanh toán tiền mặt đẩy toàn bộ rủi ro về phía Bev-Co.

#### Diễn giải ý nghĩa kinh doanh

1. Thương vụ thành công vì Bev-Co (a) định giá synergy có căn cứ (200 triệu), (b) tự đặt **giá trần 400 triệu** không vượt qua, (c) trả premium 80 triệu - chỉ 40% synergy.
2. Nhưng synergy là **ước tính**: nếu chỉ đạt được 50% (100 triệu), NPV còn $100 - 80 = +20$ triệu; nếu chỉ đạt 30% (60 triệu) thì NPV $= 60 - 80 = -20$ triệu - **lỗ**. Hãy luôn tính điểm hòa vốn: synergy tối thiểu để không lỗ bằng đúng premium (80 triệu, tức 40% dự kiến).
3. Chi phí tích hợp (integration costs), nhân sự rời đi, xung đột văn hóa chưa được tính trong con số này và cần trừ đi trong thực tế.

**Bài học**: kỷ luật định giá M&A là *không bao giờ trả quá phần synergy mà chắc chắn thực hiện được*.

---

## CHƯƠNG VIII: ĐỊNH GIÁ DOANH NGHIỆP TÍCH HỢP (CORPORATE VALUATION DCF & MULTIPLES)

Thực hành lập mô hình tài chính dự phóng liên kết 3 báo cáo tài chính và tìm kiếm giá trị kinh tế nội tại của một dòng tài sản đầu tư thực tế. Tham khảo khung lý thuyết định giá doanh nghiệp tại [10-corporate-valuation.md](10-corporate-valuation.md).

### 1. Cơ sở lý thuyết toán học chuyên sâu

#### A. Mô hình chiết khấu dòng tiền tự do doanh nghiệp (FCFF - Free Cash Flow to Firm)
FCFF phản ánh dòng tiền thặng dư thực tế tạo sinh dành cho toàn bộ các nhà nhà tài trợ vốn bao gồm cả Cổ đông lớn và các Chủ nợ đứng sau.

$$FCFF = EBIT \times (1 - T_c) + \text{Depreciation} - \text{Net CapEx} - \Delta NWC$$

**Tại sao chiết khấu FCFF bằng WACC (còn FCFE bằng $r_e$)?** FCFF là dòng tiền thuộc về *tất cả* các nhà tài trợ vốn (chủ nợ và cổ đông) *trước khi* trả lãi vay, nên phải chiết khấu ở mức chi phí vốn bình quân của cả hai nhóm - tức WACC. Việc tính thuế trên EBIT (thay vì EBT) là có chủ đích: FCFF được tính *như thể doanh nghiệp không vay nợ*, còn lợi ích của lá chắn thuế đã được đưa vào WACC thông qua thành phần $r_d(1-T_c)$. Nếu vừa tính thuế sau lãi vay trong dòng tiền, vừa dùng WACC đã giảm thuế, ta sẽ **tính hai lần** lá chắn thuế. Ý tưởng chiết khấu dòng tiền tự do để định giá bắt nguồn từ John Burr Williams (1938); các công trình hiện đại của Aswath Damodaran và McKinsey (xem Chương XII) hệ thống hóa thành quy trình định giá chuẩn mực.

Trong đó:
*   $\text{Depreciation}$ (Khấu hao tài sản hữu hình và vô hình).
*   $\text{Net CapEx} = \text{CapEx} - \text{Thanh lý}$: Lượng vốn tái đầu tư ròng mua sắm tài sản cố định dài hạn.
*   $\Delta NWC = NWC_{\text{end}} - NWC_{\text{begin}}$: Lượng thay đổi tài trợ nhu cầu tồn kho vốn lưu động ròng.

#### B. Khác biệt với Mô hình Dòng tiền tự do thuộc Vốn chủ sở hữu (FCFE - Free Cash Flow to Equity)
FCFE phản ánh dòng tiền thặng dư thực tế chỉ dành riêng cho cổ đông sở hữu sau khi đã thực hiện thanh toán ráo riết nghĩa vụ nợ lãi vay và nợ gốc dài hạn, đồng thời chiết khấu trực tiếp bằng Cost of Equity ($r_e$) thay vì $WACC$:

$$FCFE = FCFF - [\text{Interest} \times (1 - T_c)] + \text{Net Borrowing}$$

$$\text{Tài sản Vốn chủ (Equity Value)} = \sum_{t=1}^{\infty} \frac{FCFE_t}{(1+r_e)^t}$$

#### C. Định giá trị Hiện tại Doanh nghiệp (Enterprise Value - EV) chiết khấu dòng FCFF
$$\text{Enterprise Value (EV)} = \sum_{t=1}^{n} \frac{FCFF_t}{(1+WACC)^t} + \frac{\text{Terminal Value}_n}{(1+WACC)^n}$$

#### D. Công thức tính Giá trị tương lai vô hạn cuối kỳ dự báo (Terminal Value - TV)
1.  **Dựa trên Mô hình Tăng trưởng Vĩnh cửu Gordon (Gordon Growth Model)**: Giả định doanh nghiệp từ năm thứ $n$ đi vào giai đoạn ổn định vô hạn với tốc độ tăng trưởng đều đặn vĩnh cửu là $g_n$:
    $$\text{Terminal Value}_n = \frac{FCFF_{n+1}}{WACC - g_n} = \frac{FCFF_n \times (1 + g_n)}{WACC - g_n}$$
2.  **Dựa trên bội số định giá thoát vốn khi thoái vốn (Exit Multiple Method)**: Thường lấy từ bội số EV/EBITDA trung bình của ngành:
    $$\text{Terminal Value}_n = EBITDA_n \times \text{Bội số Exit Multiple}$$

**Tại sao cần Terminal Value, và vì sao nó nguy hiểm?** Không ai dự báo chi tiết được 50 năm, nhưng doanh nghiệp đang hoạt động có thể tồn tại lâu hơn nhiều so với 5 năm dự báo. Terminal Value gom toàn bộ giá trị sau năm dự báo cuối về một con số bằng công thức tăng trưởng vĩnh viễn (xem mục 1.C: $PV = CF_1/(r-g)$). Vì phần giá trị này thường chiếm **60 - 80% tổng EV**, kết quả định giá cực kỳ nhạy với hai giả định: $g$ và WACC. Quy tắc an toàn: $g$ không vượt quá tốc độ tăng trưởng danh nghĩa dài hạn của nền kinh tế (thường 2 - 4%), và phải kiểm tra tính hợp lý bằng bội số ngầm định (implied multiple) như trong mô hình S-Green.

#### E. Xác định Giá trị Vốn chủ sở hữu của cổ phần (Equity Value) và Giá cổ phiếu nội tại ($P_{\text{intrinsic}}$)
Sau khi đo lường thành công Enterprise Value (EV), ta bóc tách phần nợ ròng để phục vụ phân định riêng rẽ giá trị cổ đông:

$$\text{Equity Value} = EV - \text{Debt} + \text{Cash & Equivalents} - \text{Cổ phần thiểu số}$$

$$\text{Giá cổ phiếu nội tại } P_{\text{intrinsic}} = \frac{\text{Equity Value}}{\text{Số lượng Cổ phiếu Lưu hành}}$$

#### F. Phương pháp Định giá tương đối dựa trên Bội số (Relative Valuation Multiples)
Hỗ trợ đối chiếu chéo kết quả DCF bằng cách quan sát thị trường giao dịch đồng dạng:
1.  **Bội số Vốn hợp (Equity Multiples)**:
    *   *Hệ số P/E (Price-to-Earnings)*: Thích hợp định giá các ngành dịch vụ công nghệ ổn định.
    *   *Hệ số P/B (Price-to-Book)*: Đặt biệt phù hợp cho định giá các định chế tài chính, Ngân hàng, Bảo hiểm nhờ tính ổn định của giá trị sổ sách tài sản.
2.  **Bội số Doanh nghiệp (Enterprise-level Multiples)**:
    *   *Hệ số EV/EBITDA*: Loại bỏ hoàn toàn sự khác biệt về cấu trúc nợ vay lá chắn thuế ($r_d$) và chính sách kế toán khấu hao tài sản ròng, được xem là công cụ so sánh quốc tế tối cao.

---

### 2. Mô hình định giá thực chiến: Nhà máy S-Green

#### Bối cảnh và giả định đầu vào

Nhà máy S-Green sản xuất bao bì tái chế hoàn thành lắp đặt dây chuyền cuối năm 2025. Ban giám đốc cần định giá nội tại tại đầu năm 2026 ($t = 0$) làm cơ sở gọi vốn Series A.

| Giả định | Giá trị |
|----------|---------|
| Cơ cấu vốn mục tiêu dài hạn | $D/V = 40\%$, $E/V = 60\%$ (hiện tại mới vay ~10% EV, sẽ tăng dần khi mở rộng) |
| Lãi suất vay trước thuế $r_d$ / Thuế TNDN $T_c$ | 8,0% / 20% |
| Chi phí vốn chủ sở hữu $r_e$ | 12,0% |
| Tăng trưởng vĩnh viễn sau 2030 ($g$) | 3,0%/năm |
| Nợ vay hiện tại / Tiền mặt | 60 triệu USD / 10 triệu USD |
| Số cổ phiếu lưu hành | 10 triệu cổ phiếu |

$$WACC = 0{,}60 \times 12{,}0\% + 0{,}40 \times 8{,}0\% \times (1 - 0{,}20) = 7{,}20\% + 2{,}56\% = \textbf{9,76\%/năm}$$

#### Bước 1: Dự phóng dòng tiền tự do FCFF 5 năm (triệu USD)

| Khoản mục | 2026 (Y1) | 2027 (Y2) | 2028 (Y3) | 2029 (Y4) | 2030 (Y5) |
|-----------|-----------|-----------|-----------|-----------|-----------|
| **Doanh thu thuần** | 100,00 | 130,00 | 162,50 | 195,00 | 224,25 |
| *Tăng trưởng* | - | 30,0% | 25,0% | 20,0% | 15,0% |
| Giá vốn & chi phí vận hành (OpEx, chưa gồm khấu hao) | (65,00) | (81,25) | (97,50) | (113,10) | (125,58) |
| Khấu hao | (10,00) | (12,00) | (14,00) | (15,50) | (16,50) |
| **EBIT** | **25,00** | **36,75** | **51,00** | **66,40** | **82,17** |
| *Biên EBIT* | 25,0% | 28,3% | 31,4% | 34,1% | 36,6% |
| Thuế TNDN 20% trên EBIT | (5,00) | (7,35) | (10,20) | (13,28) | (16,43) |
| **NOPAT** (lợi nhuận sau thuế, trước lãi vay) | 20,00 | 29,40 | 40,80 | 53,12 | 65,74 |
| Cộng: Khấu hao | +10,00 | +12,00 | +14,00 | +15,50 | +16,50 |
| Trừ: CapEx ròng | (15,00) | (18,00) | (20,00) | (22,00) | (23,00) |
| Trừ: Tăng vốn lưu động ($\Delta NWC$) | (5,00) | (6,00) | (6,50) | (7,00) | (7,50) |
| **FCFF** | **10,00** | **17,40** | **28,30** | **39,62** | **51,74** |
| Hệ số chiết khấu $1/(1{,}0976)^t$ | 0,9111 | 0,8301 | 0,7563 | 0,6890 | 0,6277 |
| **PV của FCFF** | **9,11** | **14,44** | **21,40** | **27,30** | **32,48** |

Ví dụ cách tính cột 2028: $EBIT = 162{,}50 - 97{,}50 - 14{,}00 = 51{,}00$; thuế $= 51{,}00 \times 0{,}2 = 10{,}20$; $NOPAT = 40{,}80$; $FCFF = 40{,}80 + 14{,}00 - 20{,}00 - 6{,}50 = 28{,}30$; $PV = 28{,}30 \times 0{,}7563 = 21{,}40$.

Tổng PV của 5 năm dự báo: $9{,}11 + 14{,}44 + 21{,}40 + 27{,}30 + 32{,}48 = \textbf{104,73}$ triệu USD.

#### Bước 2: Giá trị cuối kỳ (Terminal Value) vào cuối năm 2030

$$FCFF_{2031} = 51{,}74 \times 1{,}03 = 53{,}29 \qquad TV_5 = \frac{53{,}29}{0{,}0976 - 0{,}03} = \frac{53{,}29}{0{,}0676} = \textbf{788,29 triệu USD}$$

#### Bước 3: Chiết khấu TV về hiện tại

$$PV(TV) = \frac{788{,}29}{(1{,}0976)^5} = 788{,}29 \times 0{,}6277 = \textbf{494,84 triệu USD}$$

#### Bước 4: Giá trị doanh nghiệp (Enterprise Value)

$$EV = 104{,}73 + 494{,}84 = \textbf{599,57 triệu USD}$$

#### Bước 5: Từ EV sang giá trị vốn chủ sở hữu và giá cổ phiếu

$$\text{Equity Value} = EV - \text{Debt} + \text{Cash} = 599{,}57 - 60{,}00 + 10{,}00 = \textbf{549,57 triệu USD}$$

$$P_{\text{intrinsic}} = \frac{549{,}57}{10{,}0} = \textbf{54,96 USD/cổ phiếu}$$

#### Bước 6: Kiểm tra tính hợp lý (sanity check)

| Kiểm tra | Phép tính | Kết luận |
|----------|-----------|----------|
| Tỷ trọng TV trong EV | $494{,}84 / 599{,}57 = 82{,}5\%$ | Rất cao - định giá phụ thuộc mạnh vào $g$ và WACC |
| Bội số EV/EBITDA năm 1 | $599{,}57 / (25 + 10) = 17{,}1x$ | Cao, hợp lý với doanh nghiệp tăng trưởng 20 - 30%/năm |
| Bội số thoát vốn ngầm định | $TV_5 / EBITDA_{2030} = 788{,}29 / (82{,}17 + 16{,}5) = 8{,}0x$ | Hợp lý so với bội số nhà máy trưởng thành |
| Tỷ lệ tái đầu tư cuối kỳ | $(23{,}0 - 16{,}5 + 7{,}5)/65{,}74 = 21{,}3\%$ | Mức tái đầu tư năm 2030 là cơ sở để tài trợ tăng trưởng vĩnh viễn 3% (kiểm tra ở dòng dưới) |
| ROIC ngầm định trên vốn mới | $g/\text{tỷ lệ tái đầu tư} = 3\% / 21{,}3\% = 14{,}1\%$ | Cao hơn WACC 9,76% - giả định bền vững nhưng cần xác nhận lợi thế cạnh tranh |

#### Bước 7: Ma trận độ nhạy (giá cổ phiếu, USD)

Thay đổi chéo WACC và tốc độ tăng trưởng vĩnh viễn $g$:

| WACC \ $g$ | 2,0% | 2,5% | **3,0%** | 3,5% | 4,0% |
|------------|------|------|----------|------|------|
| 8,76% | 57,12 | 61,49 | 66,62 | 72,72 | 80,10 |
| 9,26% | 52,33 | 56,03 | 60,32 | 65,35 | 71,34 |
| **9,76%** | 48,16 | 51,33 | **54,96** | 59,17 | 64,11 |
| 10,26% | 44,51 | 47,24 | 50,35 | 53,91 | 58,05 |
| 10,76% | 41,28 | 43,65 | 46,34 | 49,39 | 52,89 |

#### Diễn giải ý nghĩa kinh doanh

- Chỉ cần WACC tăng 1 điểm phần trăm (9,76% lên 10,76%) thì giá cổ phiếu giảm từ 54,96 xuống 46,34 USD (**-15,7%**); WACC giảm 1 điểm thì tăng lên 66,62 USD (**+21,2%**). Giảm $g$ từ 3,0% xuống 2,0% làm giá giảm 12,4%. Mối quan hệ không đối xứng vì giá trị là hàm nghịch đảo của $(WACC - g)$.
- Khi gọi vốn Series A nên trình bày **khoảng giá trị** (khoảng 46 - 66 USD ứng với WACC 8,76% - 10,76%, $g = 3\%$) thay vì một con số.
- Với phần TV chiếm 82,5% EV, nhà đầu tư nên tập trung kiểm chứng giả định dài hạn (lợi thế cạnh tranh, tăng trưởng bền vững) hơn là tranh luận từng khoản mục chi phí năm 1.
- Thực hành tốt: kết hợp DCF với định giá bội số (P/E, EV/EBITDA của doanh nghiệp cùng ngành) để kiểm chứng chéo.

---

## CHƯƠNG IX: LIÊN KẾT TÀI CHÍNH DOANH NGHIỆP VÀ BÁO CÁO KẾ TOÁN (IFRS ADOPTION)

Một mô hình định giá hay dự báo tài chính không thể vận hành độc lập: mọi con số đầu vào (doanh thu, EBIT, nợ vay) đều đến từ báo cáo tài chính, nên cách ghi nhận kế toán (VAS hay IFRS) ảnh hưởng trực tiếp tới FCFF, WACC và các chỉ số đòn bẩy. Tại Việt Nam, Bộ Tài chính đã ban hành lộ trình áp dụng chuẩn mực báo cáo tài chính quốc tế (Quyết định 345/QĐ-BTC năm 2020), nên các CFO cần hiểu hai chuẩn mực có tác động lớn nhất dưới đây. Xem thêm liên kết toán học tại [07-integrated-case-studies.md](../4-accounting/07-integrated-case-studies.md).

### 1. Ghi nhận doanh thu theo IFRS 15 tác động tới FCFF

**Tại sao có IFRS 15?** Trước đây quy tắc ghi nhận doanh thu của từng ngành, từng quốc gia khác nhau, dễ dẫn tới việc ghi nhận sớm. IFRS 15 áp dụng một mô hình 5 bước thống nhất, trong đó cốt lõi là **phân bổ giá hợp đồng cho từng nghĩa vụ thực hiện (performance obligation) theo giá bán độc lập (standalone selling price)** và ghi nhận khi nghĩa vụ đó hoàn thành.

*Ví dụ*: hợp đồng 120 triệu VNĐ bán một máy kèm bảo trì 3 năm. Giá bán độc lập: máy 100 triệu, bảo trì 3 năm 50 triệu (tổng 150 triệu).
- Phân bổ giá hợp đồng: máy $= 120 \times 100/150 = \textbf{80}$ triệu; bảo trì $= 120 \times 50/150 = \textbf{40}$ triệu (13,33 triệu/năm).
- Theo cách ghi nhận cũ (gộp toàn bộ vào ngày bán): doanh thu năm 1 là 120 triệu. Theo IFRS 15: doanh thu năm 1 $= 80 + 13{,}33 = 93{,}33$ triệu, phần còn lại 26,67 triệu ghi vào **doanh thu chưa thực hiện** (Deferred Revenue) và ghi nhận ở năm 2 - 3.
- **Tác động tài chính**: EBIT và thuế năm 1 thấp hơn, nhưng **tiền mặt thu về không đổi**. Vì vậy khi dự phóng FCFF cần điều chỉnh khoản phải thu/doanh thu chưa thực hiện trong $\Delta NWC$ để dòng tiền không bị méo.

### 2. Vốn hóa thuê tài sản theo IFRS 16 thay đổi WACC

**Tại sao có IFRS 16?** Trước đây thuê hoạt động (operating lease) chỉ là chi phí trên P&L, khiến các doanh nghiệp thuê nhiều (hàng không, bán lẻ) có bảng cân đối trông "nhẹ nợ" hơn thực tế. IFRS 16 yêu cầu hợp đồng thuê trên 12 tháng phải ghi nhận **tài sản quyền sử dụng (ROU)** và **nợ thuê (Lease Liability)** bằng giá trị hiện tại của các khoản thanh toán thuê.

*Ví dụ*: thuê mặt bằng 10 triệu USD/năm trong 5 năm, lãi suất chiết khấu 8%.
- Nợ thuê ghi nhận $= 10 \times PVIFA(8\%, 5) = 10 \times 3{,}9927 = \textbf{39,93 triệu USD}$.
- Năm 1: chi phí lãi vay thuê $= 39{,}93 \times 8\% = 3{,}19$; khấu hao ROU $= 39{,}93/5 = 7{,}99$; tổng chi phí $11{,}18$ triệu (cao hơn 10 triệu tiền thuê ở năm đầu, thấp dần về sau).
- **EBITDA tăng 10 triệu USD** vì toàn bộ tiền thuê rời khỏi OpEx; EBIT tăng 2,01 triệu; nợ có lãi tăng 39,93 triệu USD.

**Hệ quả** cho phân tích tài chính:
1. EBITDA và EBIT cao hơn mà bản chất kinh doanh không đổi - **không so sánh bội số EV/EBITDA giữa công ty áp dụng IFRS 16 với công ty chưa áp dụng** nếu chưa điều chỉnh.
2. Tỷ lệ nợ $D/E$ và $D/V$ tăng, kéo theo Beta có đòn bẩy cao hơn và WACC dịch chuyển; nếu EV bao gồm nợ thuê thì phải trừ nợ thuê khi chuyển sang Equity Value.
3. Dòng tiền không đổi, chỉ đổi cách phân loại giữa dòng tiền hoạt động và dòng tiền tài chính.

---

## CHƯƠNG X: QUẢN TRỊ RỦI RO ĐỊNH LƯỢNG CAO CẤP (QUANTITATIVE RISK MANAGEMENT)

Đánh giá rủi ro không dừng ở mô tả định tính ("rủi ro cao/thấp"); CFO cần những con số cho biết **có thể mất tối đa bao nhiêu** và **xác suất xảy ra** để quyết định mức vốn dự phòng.

### 1. Giá trị chịu rủi ro (Value at Risk - VaR)

**Tại sao có VaR?** VaR được ngân hàng JP Morgan phổ biến rộng rãi từ đầu thập niên 1990 (hệ thống RiskMetrics) vì yêu cầu của chủ tịch ngân hàng: *"Cho tôi một con số duy nhất để biết hôm nay chúng ta có thể mất bao nhiêu"*. VaR trả lời: *"Với độ tin cậy $\alpha$ (95% hoặc 99%), tổn thất tối đa trong khoảng thời gian $T$ là bao nhiêu?"*. Sau đó Basel Accords (ngân hàng) dùng nó để tính vốn dự phòng.

**Công thức VaR tham số (giả định lợi suất phân phối chuẩn)**, biểu diễn tổn thất là số dương:

$$VaR_{\alpha} = V_p \times (z_{\alpha} \times \sigma_p - \mu_p)$$

Trong đó $V_p$ là giá trị danh mục, $\mu_p$ và $\sigma_p$ là lợi suất kỳ vọng và độ lệch chuẩn theo kỳ, $z_{\alpha}$ là giá trị tới hạn của phân phối chuẩn tắc ($z = 1{,}645$ cho 95%; $z = 2{,}326$ cho 99%).

***Bài tập ứng dụng định lượng số 3***: Danh mục tài chính $V_p = 10.000.000$ USD, lợi suất kỳ vọng ngày $\mu_p = 0{,}15\%$, độ lệch chuẩn ngày $\sigma_p = 1{,}2\%$.

- *Bước 1 - VaR 1 ngày, độ tin cậy 95%*:
$$VaR_{95\%} = 10.000.000 \times (1{,}645 \times 0{,}012 - 0{,}0015) = 10.000.000 \times 0{,}01824 = \textbf{182.400 USD}$$
Ý nghĩa: với 95% tin cậy, tổn thất trong 1 ngày không vượt 182.400 USD; trong 5% số ngày xấu nhất, tổn thất sẽ vượt mức này.
- *Bước 2 - VaR 1 ngày, độ tin cậy 99%*:
$$VaR_{99\%} = 10.000.000 \times (2{,}326 \times 0{,}012 - 0{,}0015) = 10.000.000 \times 0{,}026412 = \textbf{264.120 USD}$$
- *Bước 3 - VaR 10 ngày (mở rộng thời gian)*: độ lệch chuẩn tăng theo $\sqrt{T}$ còn lợi suất kỳ vọng tăng theo $T$: $\sigma_{10} = 1{,}2\% \times \sqrt{10} = 3{,}795\%$; $\mu_{10} = 1{,}5\%$.
$$VaR_{95\%,10d} = 10.000.000 \times (1{,}645 \times 0{,}03795 - 0{,}015) = \textbf{474.234 USD}$$
- *Bước 4 - Expected Shortfall (ES) 95%*: trung bình tổn thất *khi đã vượt VaR*, với phân phối chuẩn $ES = V_p \times (\sigma_p \times \phi(z)/(1-\alpha) - \mu_p)$, $\phi(1{,}645) = 0{,}1031$:
$$ES_{95\%} = 10.000.000 \times (0{,}012 \times 0{,}1031/0{,}05 - 0{,}0015) = \textbf{232.466 USD}$$

**Hạn chế của VaR**: (1) giả định phân phối chuẩn thường đánh giá thấp "đuôi dày" (sự kiện cực đoan, như khủng hoảng 2008); (2) VaR chỉ cho biết ngưỡng, không cho biết tổn thất *bao nhiêu khi vượt ngưỡng* - đó là lý do Expected Shortfall được các quy định hiện đại ưa chuộng; (3) dựa trên dữ liệu quá khứ nên không dự báo được thay đổi cấu trúc.

### 2. Mô phỏng Monte Carlo (Monte Carlo Simulation)

**Tại sao cần?** Phân tích kịch bản (tốt/trung bình/xấu) chỉ cho 3 điểm rời rạc và bỏ qua việc các biến đầu vào thay đổi **đồng thời** theo phân phối xác suất. Phương pháp Monte Carlo bắt nguồn từ công trình của Stanislaw Ulam và John von Neumann thời Dự án Manhattan (thập niên 1940); David Hertz (1964, *Harvard Business Review*) là người đầu tiên đề xuất dùng nó cho thẩm định đầu tư. Cơ chế: gán phân phối xác suất cho các biến đầu vào bất định (giá nguyên liệu, sản lượng, tỷ giá), chạy hàng chục nghìn lần, thu được **phân phối của NPV** và có thể đọc trực tiếp *xác suất NPV âm*, NPV ở bách phân vị thứ 5 (tình huống xấu) hay thứ 95. Một ví dụ cụ thể với dự án SME ở Chương XI (Case 13).

---

## CHƯƠNG XI: CASE STUDY TÍCH HỢP CHO SME VIỆT NAM

Các case từ Chương I đến X chủ yếu là tập đoàn lớn tính bằng triệu USD. Chương này đưa toàn bộ bộ công cụ vào **một quyết định thực tế của chủ SME Việt Nam**: có nên vay ngân hàng mở thêm chi nhánh hay không? Một quyết định duy nhất kết nối đủ năm khối kiến thức: hoạch định vốn đầu tư (Chương I), chi phí vốn (II), cơ cấu vốn (III), vốn lưu động (IV) và rủi ro (X). Tình huống mang tính minh họa, số liệu tự nhất quán (đã kiểm tra lại bằng tính toán).

### 1. Case Study 13 (SME Việt Nam): QUÁN CÀ PHÊ "NHÀ RANG" – Quyết định mở chi nhánh thứ hai bằng vốn vay

#### Bối cảnh

Anh Minh sở hữu quán cà phê "Nhà Rang" đã hoạt động ổn định 3 năm tại TP. Biên Hòa và muốn mở chi nhánh thứ hai tại khu dân cư mới. Anh cần quyết định có đầu tư không, vay bao nhiêu và có đủ an toàn về dòng tiền hay không. Đơn vị: **triệu VNĐ**.

| Khoản mục đầu tư ban đầu ($CF_0$) | Số tiền |
|-----------------------------------|---------|
| Cải tạo mặt bằng, trang trí (khấu hao 5 năm) | 1.100 |
| Máy pha cà phê, thiết bị, nội thất (khấu hao 5 năm) | 700 |
| Đặt cọc mặt bằng (hoàn lại cuối hợp đồng) | 200 |
| Vốn lưu động ban đầu (tồn kho + quỹ tiền mặt đệm) | 100 |
| **Tổng nhu cầu vốn** | **2.100** |

Phương án tài trợ: vay ngân hàng **840 triệu** (40%), lãi suất 11%/năm, trả gốc và lãi đều trong 5 năm; vốn tự có **1.260 triệu** (60%). Thuế TNDN 20%.

Giả định vận hành: doanh thu năm 1 là 3.000 triệu (≈ 250 triệu/tháng, ≈ 8,3 triệu/ngày, tương đương ~150 khách chi 55.000 đồng), tăng 15% - 8% - 5% - 3% ở các năm 2 - 5; giá vốn 33% doanh thu; nhân sự 24%; chi phí khác 10%; tiền thuê mặt bằng 480 triệu/năm (tăng 3%/năm). Hợp đồng thuê 5 năm, sau đó không có giá trị chuyển nhượng quán nào ngoài thanh lý thiết bị 180 triệu.

#### Bước 1: Xác định tỷ suất chiết khấu - WACC của một SME

**Tại sao không dùng lãi suất vay 11% làm tỷ suất chiết khấu?** Vì lãi vay chỉ là chi phí của 40% vốn; 60% còn lại là tiền của anh Minh, vốn cũng có chi phí cơ hội (anh có thể gửi tiết kiệm, đầu tư chỗ khác với rủi ro tương đương). Ta dùng CAPM mở rộng:

- Lãi suất phi rủi ro $R_f = 3{,}5\%$ (lợi suất trái phiếu Chính phủ, giả định); phần bù thị trường $ERP = 8{,}0\%$; Beta tài sản ngành F&B $\beta_u = 0{,}85$; phần bù quy mô/thanh khoản của doanh nghiệp chưa niêm yết $= 4{,}0\%$.
- $D/E = 840/1.260 = 0{,}667$:

$$\beta_{lh} = 0{,}85 \times [1 + (1 - 0{,}20) \times 0{,}667] = 0{,}85 \times 1{,}533 = \textbf{1,303}$$

$$r_e = 3{,}5\% + 1{,}303 \times 8{,}0\% + 4{,}0\% = \textbf{17,93\%}$$

$$WACC = 0{,}60 \times 17{,}93\% + 0{,}40 \times 11\% \times (1 - 0{,}20) = 10{,}76\% + 3{,}52\% = \textbf{14,28\%}$$

#### Bước 2: Mức vay 40% có hợp lý? (quyết định cơ cấu vốn)

Ngân hàng tính lãi suất cao hơn khi anh vay nhiều hơn (rủi ro tăng). Giả định lãi suất tăng theo tỷ lệ vay:

| Tỷ trọng nợ $D/V$ | Lãi vay $r_d$ | $\beta_{lh}$ | $r_e$ | WACC |
|-------------------|----------------|--------------|-------|------|
| 0% | - | 0,850 | 14,30% | 14,30% |
| **40%** | **11%** | **1,303** | **17,93%** | **14,28%** |
| 60% | 12% | 1,870 | 22,46% | 14,74% |
| 70% | 13% | 2,437 | 26,99% | 15,38% |

**Diễn giải**: WACC thấp nhất ở khoảng 40% vay (14,28%) - nhưng chênh lệch so với không vay (14,30%) **gần như bằng không**, vì lãi vay 11% khá cao và phần bù quy mô cộng cố định 4% vào $r_e$. Với SME, **động cơ chính của việc vay không phải là hạ WACC mà là giữ quyền sở hữu và nhân vốn chủ**; còn vượt quá 40% - 50% thì WACC tăng nhanh do chi phí kiệt quệ tài chính (Trade-off Theory, Case 4). Vì vậy 40% là mức hợp lý.

#### Bước 3: Dòng tiền tự do của dự án (FCFF)

| Triệu VNĐ | Năm 1 | Năm 2 | Năm 3 | Năm 4 | Năm 5 |
|-----------|-------|-------|-------|-------|-------|
| Doanh thu | 3.000,0 | 3.450,0 | 3.726,0 | 3.912,3 | 4.029,7 |
| Giá vốn (33%) | (990,0) | (1.138,5) | (1.229,6) | (1.291,1) | (1.329,8) |
| Nhân sự (24%) | (720,0) | (828,0) | (894,2) | (939,0) | (967,1) |
| Chi phí khác (10%) | (300,0) | (345,0) | (372,6) | (391,2) | (403,0) |
| Thuê mặt bằng | (480,0) | (494,4) | (509,2) | (524,5) | (540,2) |
| **EBITDA** | **510,0** | **644,1** | **720,3** | **766,6** | **789,5** |
| Khấu hao | (360,0) | (360,0) | (360,0) | (360,0) | (360,0) |
| **EBIT** | 150,0 | 284,1 | 360,3 | 406,6 | 429,5 |
| Thuế TNDN 20% | (30,0) | (56,8) | (72,1) | (81,3) | (85,9) |
| NOPAT | 120,0 | 227,3 | 288,3 | 325,2 | 343,6 |
| Cộng khấu hao | +360,0 | +360,0 | +360,0 | +360,0 | +360,0 |
| Dòng tiền thanh lý cuối kỳ | - | - | - | - | +444,0 |
| **FCFF** | **480,0** | **587,3** | **648,3** | **685,2** | **1.147,6** |

Dòng tiền thanh lý năm 5 $= 100$ (thu hồi vốn lưu động) $+ 200$ (nhận lại tiền cọc) $+ 180 \times (1 - 0{,}20) = 144$ (bán thiết bị còn giá trị sổ sách bằng 0 nên chịu thuế 20% trên 180) $= \textbf{444}$.

#### Bước 4: Các tiêu chí thẩm định

Dòng tiền: $-2.100;\ 480{,}0;\ 587{,}3;\ 648{,}3;\ 685{,}2;\ 1.147{,}6$. Hệ số chiết khấu $1/(1{,}1428)^t$: 0,8751; 0,7658; 0,6701; 0,5864; 0,5131. PV từng năm: 420,0; 449,7; 434,4; 401,8; 588,9.

$$NPV = (420{,}0 + 449{,}7 + 434{,}4 + 401{,}8 + 588{,}9) - 2.100 = 2.294{,}9 - 2.100 = \textbf{+194,9 triệu VNĐ}$$

| Tiêu chí | Kết quả | Diễn giải |
|----------|---------|-----------|
| NPV @ 14,28% | **+194,9** | > 0: tạo giá trị |
| IRR | **17,6%** | > WACC 14,28% (biên an toàn chỉ 3,3 điểm) |
| MIRR (tái đầu tư ở WACC) | 16,3% | Vẫn > WACC; thận trọng hơn IRR |
| PI | 1,093 | Mỗi đồng vốn tạo 1,093 đồng giá trị hiện tại |
| Hoàn vốn thường | $3 + 384{,}4/685{,}2 = $ **3,56 năm** | Khoảng 43 tháng trong hợp đồng 60 tháng |
| Hoàn vốn có chiết khấu (DPP) | $4 + 394{,}0/588{,}9 = $ **4,67 năm** | Chỉ còn ~0,3 năm đệm trước khi hết hợp đồng thuê |

**Kiểm tra chéo về chọn sai tỷ suất chiết khấu**:

| Tỷ suất dùng | NPV | Quyết định |
|--------------|-----|------------|
| Lãi vay 11% (sai) | +415,6 | Quá lạc quan, đánh giá cao gấp ~2,1 lần |
| WACC 14,28% (đúng) | +194,9 | Nhận, nhưng biên an toàn mỏng |
| Chi phí vốn chủ 17,93% (quá thận trọng nếu 40% là vay) | -17,8 | Bác bỏ sai |

#### Bước 5: Kiểm tra khả năng trả nợ (dòng tiền của chủ nợ)

Khoản vay 840 triệu, 11%/năm, 5 năm: số tiền trả đều hằng năm $= 840 / PVIFA(11\%, 5) = 840 / 3{,}6959 = \textbf{227,3 triệu/năm}$.

| Năm | Lãi | Gốc | Dư nợ cuối năm | DSCR $=(EBITDA - \text{Thuế}) / 227{,}3$ |
|-----|-----|-----|----------------|-------------------------------------------|
| 1 | 92,4 | 134,9 | 705,1 | **2,11** |
| 2 | 77,6 | 149,7 | 555,4 | 2,58 |
| 3 | 61,1 | 166,2 | 389,2 | 2,85 |
| 4 | 42,8 | 184,5 | 204,8 | 3,02 |
| 5 | 22,5 | 204,8 | 0 | 3,10 |

DSCR (Debt Service Coverage Ratio) > 1,5 thường là mức ngân hàng chấp nhận; năm 1 đạt 2,11 là an toàn. Lợi suất trên vốn chủ (IRR của dòng tiền vốn chủ sau khi trả nợ) $= \textbf{22,2\%}$, cao hơn $r_e = 17{,}93\%$: đòn bẩy làm vốn của anh Minh sinh lời cao hơn so với tỷ suất của dự án (17,6%) vì dự án sinh lời cao hơn lãi vay sau thuế (8,8%).

#### Bước 6: Vốn lưu động - quán cà phê có chu kỳ tiền mặt âm

Khách thanh toán ngay (DSO = 0), tồn kho nguyên liệu quay vòng nhanh (DIO ≈ 10 ngày), nhà cung cấp cho trả chậm khoảng 18 ngày (DPO = 18): $CCC = 10 + 0 - 18 = \textbf{-8 ngày}$. Với giá vốn năm 1 là 990 triệu: tồn kho $= 10/365 \times 990 = 27{,}1$; phải trả $= 18/365 \times 990 = 48{,}8$; nhu cầu vốn lưu động thương mại $= -21{,}7$ (nhà cung cấp tài trợ thêm). Do đó khoản 100 triệu vốn lưu động chủ yếu là **quỹ tiền mặt đệm ≈ 73 triệu** (đủ trả khoản chi cố định trong lúc doanh thu chưa ổn định), không phải vốn nằm ở hàng tồn kho.

#### Bước 7: Kiểm tra sức chịu đựng (stress test) và mô phỏng Monte Carlo

NPV tại WACC 14,28% khi doanh thu thấp hơn kế hoạch:

| Doanh thu so với kế hoạch | 100% | 90% | 85% | 80% | 75% |
|---------------------------|------|-----|-----|-----|-----|
| NPV (triệu VNĐ) | +194,9 | -125,3 | -285,3 | -453,8 | -622,6 |
| IRR | 17,6% | 12,1% | 9,2% | 6,2% | 3,0% |

- **Điểm hòa vốn NPV**: doanh thu chỉ cần thấp hơn kế hoạch **6,1%** (≈ 2.817 triệu năm 1, ≈ 7,8 triệu/ngày) là NPV về 0. Mỗi 1% doanh thu thiếu hụt làm NPV giảm ~32 triệu VNĐ.
- **Mô phỏng Monte Carlo** (20.000 lần, doanh thu thực tế dao động chuẩn quanh kế hoạch với độ lệch chuẩn 10%, seed 42): NPV trung bình **+195,9**, độ lệch chuẩn 322,9; bách phân vị thứ 5: **-333,6**; thứ 95: **+729,6**; **xác suất NPV âm ≈ 27%** (khớp với tính giải tích $\Phi(-0{,}61) = 27{,}1\%$).
- **Độ nhạy theo giá thuê mặt bằng** (yếu tố chủ quan đàm phán được):

| Giá thuê năm 1 | 480 | 420 | 360 |
|----------------|-----|-----|-----|
| NPV | +194,9 | +367,3 | +539,8 |
| IRR | 17,6% | 20,5% | 23,3% |

Giảm 60 triệu/năm tiền thuê tăng NPV thêm ~172 triệu - một thỏa thuận thuê tốt đáng giá hơn nhiều chiến dịch quảng cáo.

#### Quyết định và khuyến nghị

1. **Nên triển khai nhưng có điều kiện**: NPV dương, IRR vượt WACC và DSCR an toàn, tuy nhiên biên an toàn mỏng (doanh thu chỉ cần hụt 6% là mất giá trị) và rủi ro 27% NPV âm.
2. **Đàm phán thuê mặt bằng** xuống tối đa 420 triệu/năm hoặc xin ân hạn/giảm giá thuê 3 - 6 tháng đầu; đây là đòn bẩy giá trị lớn nhất.
3. **Mua quyền chọn trước khi cam kết (Real Options)**: chạy thử quầy mang đi/pop-up vài tháng tại khu vực mới để kiểm chứng doanh thu (mục tiêu ≥ 250 triệu/tháng) trước khi ký hợp đồng thuê 5 năm.
4. **Duy trì quỹ dự phòng trả nợ ≥ 6 tháng** $= 227{,}3/2 \approx 114$ triệu VNĐ ngoài 100 triệu vốn lưu động, để không phụ thuộc hoàn toàn vào doanh thu tháng.
5. **Không vay vượt 40 - 50%** tổng nhu cầu vốn, tránh vùng WACC tăng (Bước 2).

#### Những sai lầm phổ biến của SME khi ra quyết định đầu tư

- Dùng lãi vay ngân hàng làm tỷ suất chiết khấu (đánh giá cao NPV gấp hơn 2 lần ở case này).
- Chỉ nhìn "hoàn vốn sau 3,5 năm" mà bỏ qua giá trị thời gian của tiền và dòng tiền sau hoàn vốn.
- Quên tiền cọc, vốn lưu động và thuế khi thanh lý trong dòng tiền; hoặc ngược lại quên rằng hợp đồng thuê hết hạn nên không có giá trị cuối kỳ vĩnh viễn.
- Không tính DSCR hoặc không chuẩn bị quỹ dự phòng, dẫn tới vỡ nợ dù dự án "sinh lời" trên giấy (xem Case 8).
- Lập kế hoạch với một kịch bản duy nhất thay vì stress test.

---

## CHƯƠNG XII: DANH MỤC THAM KHẢO HÀN LÂM QUỐC TẾ CAO CẤP

1.  **Richard A. Brealey, Stewart C. Myers, Franklin Allen** – *Principles of Corporate Finance (14th Edition)* – Bộ kinh điển về tài chính doanh nghiệp thế giới.
2.  **Stephen A. Ross, Randolph W. Westerfield, Jeffrey Jaffe** – *Corporate Finance (13th Edition)* – Sách giáo khoa chuẩn mực giảng dạy mức cấu trúc tài chính MBA.
3.  **Aswath Damodaran** – *Investment Valuation: Tools and Techniques for Determining the Value of Any Asset (3rd Edition)* – Bộ sách bảo vật kinh điển của giáo sư định giá tối cao trường đại học New York NYU Stern.
4.  **Tim Koller, Marc Goedhart, David Wessels (McKinsey & Company)** – *Valuation: Measuring and Managing the Value of Companies (7th Edition)* – Cẩm nang thực hành định giá tối cao của các tập đoàn tư vấn tinh hoa toàn cầu.
5.  **CFA Program Curriculum (Levels I, II, and III)** – *Corporate Issuers and Portfolio Management Collections* – Khung chuẩn mực đo lường kiểm định trình độ phân tích tài chính quốc tế của CFA Institute.

---

## PHỤ LỤC: CHECKLIST TÀI CHÍNH DOANH NGHIỆP TỔNG HỢP

### A. Ma trận tổng hợp kiểm tra sức khỏe các bài toán tài chính

| Phân vùng kiến thức | Công cụ định lượng | Chỉ số kiểm tra | Chân lý quản trị cốt lõi |
|---------------------|--------------------|------------------|----------------------------|
| **1. Đầu tư (Capital)** | NPV, IRR, MIRR, PI, DPP, Real Options | NPV > 0; MIRR > WACC; đồ thị NPV theo tỷ suất | IRR ngầm giả định tái đầu tư ở chính IRR và có thể có nhiều nghiệm; ra quyết định theo NPV |
| **2. Hurdle Rate** | CAPM, WACC, Hamada | Beta tài sản, Beta có đòn bẩy, $r_e$ | Nợ hạ WACC chỉ ở mức vừa phải; lạm dụng làm $r_d$ và $r_e$ tăng vọt |
| **3. Cấu trúc vốn (Structure)** | M&M, Trade-off, Pecking Order | Lá chắn thuế $T_c D$, ICR, chi phí kiệt quệ | Cơ cấu tối ưu nằm ở điểm cân bằng lá chắn thuế và chi phí kiệt quệ tài chính |
| **4. Thanh khoản (Liquidity)** | CCC, EOQ, BAT, Miller-Orr | DIO, DSO, DPO, NWC, Quick Ratio | Lợi nhuận P&L không phải tiền mặt; tăng trưởng phải có nguồn vốn lưu động |
| **5. Chi trả (Payout)** | Dividend theories, Lintner, Buyback | Payout ratio, giá mua lại so với giá trị nội tại | Mua lại cổ phiếu chỉ tạo giá trị khi mua dưới giá trị nội tại |
| **6. Rủi ro - Lợi suất** | Markowitz, CML/SML, Sharpe, Treynor, Jensen | Hệ số tương quan, Sharpe | Đa dạng hóa hiệu quả khi tài sản có tương quan thấp hoặc âm |
| **7. Định giá (Valuation)** | DCF (FCFF), Multiples, M&A synergy | EV, TV/EV, Premium so với Synergy | Giá trị = dòng tiền tự do tương lai chiết khấu theo rủi ro; TV rất nhạy với $g$ và WACC |
| **8. Quản trị rủi ro** | VaR, ES, Monte Carlo, Stress test | VaR/ES, xác suất NPV âm, DSCR | Lượng hóa tổn thất và xác suất để dự phòng vốn thay vì dự đoán một kịch bản |

### B. Công thức tổng hợp

| Chủ đề | Công thức |
|--------|-----------|
| Giá trị hiện tại | $PV = \sum_{t} \frac{CF_t}{(1+r)^t}$ |
| Dòng tiền đều | $PV = PMT \times \frac{1-(1+r)^{-n}}{r}$ |
| Tăng trưởng vĩnh viễn | $PV = \frac{CF_1}{r-g}$ |
| NPV / PI | $NPV = \sum \frac{CF_t}{(1+r)^t} - CF_0$; $PI = 1 + NPV/CF_0$ |
| MIRR | $MIRR = \sqrt[n]{TV_{\text{inflows}} / PV_{\text{outflows}}} - 1$ |
| CAPM | $r_e = R_f + \beta (E(R_m) - R_f)$ |
| WACC | $WACC = \frac{E}{V} r_e + \frac{D}{V} r_d (1-T_c)$ |
| Hamada | $\beta_l = \beta_u [1 + (1-T_c) D/E]$ |
| M&M có thuế | $V_l = V_u + T_c D$; $r_e = r_0 + \frac{D}{E}(1-T_c)(r_0 - r_d)$ |
| CCC | $CCC = DIO + DSO - DPO$ |
| EOQ / BAT | $Q^* = \sqrt{2DS/H}$; $C^* = \sqrt{2TF/r}$ |
| Lintner | $D_t = D_{t-1} + SOA \times (\text{Target Payout} \times EPS_t - D_{t-1})$ |
| Phương sai danh mục 2 tài sản | $\sigma_p^2 = w_A^2\sigma_A^2 + w_B^2\sigma_B^2 + 2w_Aw_B\sigma_A\sigma_B\rho_{AB}$ |
| Sharpe / Jensen | $\frac{E(R_p)-R_f}{\sigma_p}$; $\alpha = R_p - [R_f + \beta(R_m-R_f)]$ |
| NPV thâu tóm | $NPV = \text{Synergies} - \text{Premium}$; $\text{Price}_{\max} = V_B + \text{Synergies}$ |
| FCFF / Terminal Value | $FCFF = EBIT(1-T_c) + Dep - CapEx - \Delta NWC$; $TV = \frac{FCFF_n(1+g)}{WACC-g}$ |
| Equity Value | $EV - \text{Debt} + \text{Cash}$ |
| VaR tham số | $VaR_\alpha = V_p (z_\alpha \sigma_p - \mu_p)$ |
| DSCR | $DSCR = (EBITDA - \text{Thuế}) / (\text{Gốc} + \text{Lãi})$ |

### C. Checklist trước khi ra quyết định tài chính

**1. Thẩm định đầu tư**
- □ Dòng tiền là dòng tiền **tăng thêm** (incremental), đã tính thuế, vốn lưu động và giá trị thanh lý/tiền cọc?
- □ Tỷ suất chiết khấu là WACC phản ánh rủi ro của dự án (không phải lãi vay, không phải lợi suất kỳ vọng chung)?
- □ Đã tính NPV, IRR, MIRR, PI, thời gian hoàn vốn có chiết khấu? Dòng tiền có đổi dấu nhiều lần không (nguy cơ nhiều IRR)?
- □ Đã stress test doanh thu giảm 10 - 20% và tìm điểm hòa vốn NPV?
- □ Có thể mua "quyền chọn" (chạy thử, thuê ngắn hạn, chia giai đoạn) trước khi cam kết vốn lớn?

**2. Chi phí vốn và cơ cấu vốn**
- □ Đã dùng tỷ trọng giá trị thị trường (hoặc cơ cấu mục tiêu) cho WACC?
- □ $r_d$ có tăng khi tỷ lệ nợ tăng (không giữ cố định)? ICR > 2,5 - 3 lần?
- □ DSCR từng năm > 1,5? Có quỹ dự phòng trả nợ ≥ 6 tháng?
- □ Nợ ngắn hạn có đang tài trợ tài sản dài hạn không (rủi ro tái cấp vốn)?

**3. Vốn lưu động**
- □ Đã đo CCC, DIO, DSO, DPO hằng tháng? CCC có đang tăng khi doanh thu tăng?
- □ Mỗi lần nới tín dụng/tăng tồn kho đã tính $\Delta NWC$ và nguồn tài trợ?
- □ Có hạn mức tín dụng dự phòng và quỹ tiền mặt đệm?

**4. Chính sách chi trả**
- □ Cổ tức/mua lại có nằm trong khả năng của dòng tiền tự do, không đi vay để trả cổ tức?
- □ Mua lại cổ phiếu chỉ khi giá thấp hơn giá trị nội tại?
- □ Chính sách cổ tức có linh hoạt khi khủng hoảng (không cứng nhắc)?

**5. Danh mục và rủi ro**
- □ Đã xem hệ số tương quan giữa các tài sản và kiểm tra khi khủng hoảng (tương quan có thể tăng)?
- □ Đã tính Sharpe/Treynor thay vì chỉ nhìn lợi suất?
- □ Đã tính VaR/ES hoặc mô phỏng Monte Carlo cho các quyết định lớn?

**6. M&A và định giá**
- □ Synergy đã được định lượng và chiết khấu; premium < synergy chắc chắn thực hiện được? Giá trần đã đặt?
- □ DCF: TV chiếm bao nhiêu % EV? $g$ ≤ tăng trưởng danh nghĩa dài hạn? Đã kiểm tra bội số ngầm định?
- □ Đã lập ma trận độ nhạy WACC - $g$ và trình bày khoảng giá trị thay vì một con số?
- □ Đã kiểm tra tác động IFRS 15/IFRS 16 tới EBITDA, nợ và so sánh bội số giữa các công ty?

**7. Kiểm tra tính nhất quán số liệu (trước khi trình bày)**
- □ Bảng cân đối: Tài sản = Nợ + Vốn chủ; dòng tiền khớp thay đổi tiền mặt giữa hai kỳ?
- □ Các con số trong bảng tính tự khớp với nhau (EBIT = Doanh thu - OpEx - Khấu hao; FCFF cộng đúng)?
- □ Đã chạy kiểm tra bằng Excel/Python trước khi đưa vào báo cáo?
