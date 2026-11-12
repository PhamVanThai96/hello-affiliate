# Kết quả kiểm chứng ngoài mẫu của công cụ phân tích kỹ thuật (yfinance, cổ phiếu Việt Nam)

Phương pháp: tại mỗi ngày T chỉ dùng dữ liệu <= T, chấm bằng diễn biến thật 5/10/20 phiên sau; tách train (< 2020) và test (>= 2020); so với mức nền (mọi ngày). 12 mã: MSN, VRE, HPG, VNM, FPT, MWG, STB, VCB, SSI, PNJ, TCB, ACB (dữ liệu từ 2010-2018 tuỳ mã đến 11/2026). Mã kiểm thử là script dùng một lần, đã gỡ khỏi repo sau khi chạy (11/2026); có thể dựng lại theo phương pháp trên. Số liệu là tần suất lịch sử, KHÔNG bảo đảm tương lai.

## 1. Hướng giá (mũi tên dự báo)
- Mũi tên cũ (suy ra từ nhãn MUA/BÁN/THEO DÕI) đúng ~47,6% ở 10 phiên (ngoài mẫu 2020+): kém đồng xu.
- Nhận định hiệu chuẩn v3 (chế độ thị trường chung + điểm xu hướng): đúng ~52,0% trên 1.576 ngày có nhận định, nền "luôn tăng" 50,8%; không khác biệt có ý nghĩa. Xác suất tăng 10 phiên theo từng nhóm chỉ dao động 47-59%.
- Giá trị dự báo đổi dấu theo chế độ: thị trường chung trên MA200 -> quán tính (IC +0,10); dưới MA200 -> hồi quy (IC -0,13); nhưng hiệu chuẩn học từ giai đoạn trước không bền (tỷ lệ đúng từng năm 19%-86%).
- **Vùng biến động** (ATR% x sqrt(h) x k): dự báo tốt; vùng 80% phủ thực tế 82,7% (ngoài mẫu).
- Kết luận: hướng 10-20 phiên gần như không dự báo được chỉ từ giá; biên độ dự báo được.

## 2. Kênh giá
- Kênh cũ (hồi quy toàn bộ 12 tháng): chứa 10 phiên kế tiếp 31%; báo "phá vỡ" ~26% số ngày.
- Kênh v3 (giai đoạn gần nhất 60-150 phiên, hồi quy + biên song song ở phân vị 99%/1% của High/Low): chứa 77% (bề rộng 15-17% giá); hiệu quả chứa/bề rộng ~5,8 so với 3,3 (cũ).
- Giá đóng cửa vượt biên trên kênh v3 (~2% số ngày): 57-67% quay lại trong kênh trong 5 phiên (phá vỡ giả); lợi suất 10 phiên sau không hơn nền.
- Loại kênh sau 10 phiên: kênh tăng +1,0% (54% tăng), kênh giảm +0,1% (52%), đi ngang +0,4% (50%): thiên hướng yếu.

## 3. Mẫu hình nến Nhật (Steve Nison)
- Mật độ phát hiện 0,49 mẫu hình/ngày (gần một nửa số ngày có "mẫu hình đảo chiều"): quá nhiều để có ý nghĩa.
- Không có giá trị dự báo bền: tỷ lệ tăng 10 phiên 0,46-0,60 so với nền 0,51-0,53; lợi suất vượt nền đổi dấu giữa train và test (vd Hanging Man -0,65%/+0,59%, Rising Window +0,75%/-0,60%).
- Bullish reversal ở vùng giá thấp (dưới MA50, sát đáy 20 phiên): vượt nền -0,74% (train) và -0,82% (test): bắt đáy theo nến thường SAI (giá tiếp tục giảm).
- Bearish reversal ở vùng giá cao: giá vẫn có xu hướng tăng tiếp (vượt nền 0 đến +0,8%): nến đảo chiều giảm không báo đỉnh.
- Kết luận: chỉ dùng để mô tả, không dùng làm tín hiệu vào/ra.

## 4. Hộp tích lũy (cửa sổ 12 phiên biên độ <= 8%)
- Mua gần đáy hộp (<=25% biên độ): vượt nền -0,77% (test), -1,11% (train), tỷ lệ tăng 45-49%: quy tắc "mua ở cạnh dưới hộp" SAI trên dữ liệu.
- Breakout lên + khối lượng >= 2x TB20: vượt nền +0,99% (train), +0,34% (test), tỷ lệ tăng ~53-55% (n=198-302): nhỉnh hơn nền nhẹ.
- Breakout lên không kèm khối lượng: không lợi thế (vượt nền +0,50%/-0,20%).
- Breakdown (thủng đáy): không nhất quán (vượt nền -1,24% train, -0,29% test).

## 5. Vùng hỗ trợ / kháng cự từ đỉnh-đáy cực trị (>= 3 lần chạm)
- Chạm hỗ trợ mạnh rồi giữ được: tỷ lệ không thủng -3% trong 10 phiên 61-66% so với mức ngẫu nhiên 62-67%: KHÔNG tốt hơn một mức giá ngẫu nhiên; lợi suất 10 phiên sau chạm hỗ trợ -0,15% (nền +0,6-0,9%).
- Kết luận: các vùng này là "nơi giá từng đảo chiều" chứ không phải điểm tựa đáng tin.

## 6. Auction Market Theory trên khung ngày (Value Area 60 phiên trước, num_bins=40)
- Đóng cửa trên VAH: tăng 10 phiên 55-56%, lợi suất +1,2% đến +1,5% (nền ~+0,5-0,9%): quán tính nhẹ, nhất quán cả 2 giai đoạn.
- Dưới VAL: không có lợi thế (tăng 48-52%, +0,0% đến +0,1%): không phải điểm mua đảo chiều.
- Hồi về POC trong 10 phiên khi giá ngoài Value Area: 41-50% (coin flip): kịch bản A (D-shape mean reversion) không được ủng hộ trên khung ngày.
- Tín hiệu vào lệnh AMT chỉ sinh với dữ liệu trong ngày (15m...), chưa kiểm chứng (yfinance cho mã .VN không đảm bảo dữ liệu trong ngày).

## 7. Bộ lọc luật MUA/BÁN (generate_recommendation_v2)
- Nhãn "MUA" (sau khi bỏ nhánh mua đáy hộp tích lũy; ngoài mẫu từ 2020, 244 lần trên 12 mã): tăng 10 phiên 61,1%, lợi suất TB +1,30% (nhãn "THEO DÕI" +0,73%, "BÁN" +0,31%); tăng 20 phiên 58,6%.
- Mô phỏng giao dịch MUA (cắt lỗ SL, chốt lời TP1/TP2, hết 20 phiên): thắng 55% (test) và 52% (train); lợi suất TB +0,73% và +0,76% mỗi lệnh TRƯỚC phí/thuế. Thoát lệnh: TP1 197, SL 175, hết hạn 165, TP2 0 lần.
- Hạn chế: các nhãn MUA xuất hiện dồn cụm theo thời gian nên số mẫu độc lập nhỏ hơn nhiều so với 244; sau phí giao dịch và thuế bán (khoảng 0,25-0,4% khứ hồi) lợi thế còn mỏng; chưa đủ để kết luận chắc.
- Cảnh báo "phân phối đỉnh" (n=12 trong lượt trước): giá sau đó tăng thêm ~4-5% (ngược cảnh báo); mẫu quá nhỏ.
- Nhãn "BÁN" (giá < MA200) và "THEO DÕI": không khác nền (tăng 10 phiên 51-53%): không có giá trị dự báo.

## Ràng buộc thị trường Việt Nam cần nhớ khi diễn giải
- Nhà đầu tư cá nhân không bán khống: tín hiệu "SHORT" không khả thi; chỉ có "không mua / giảm tỷ trọng / đứng ngoài".
- Biên độ giá: HOSE +-7%, HNX +-10%, UPCoM +-15%; T+2 (thường là T+1,5 thực tế); phiên khớp lệnh định kỳ ATO/ATC; nghỉ trưa 11:30-13:00.
- yfinance: giá điều chỉnh, có thể trễ/thiếu; không có ^VNINDEX (dùng rổ cổ phiếu thay chỉ số).
