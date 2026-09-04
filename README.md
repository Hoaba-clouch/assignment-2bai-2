# Báo cáo Phân tích Phân loại Hệ thống Thông tin RikkeiExpress

## Bối cảnh và Yêu cầu bài toán

Ban Giám đốc chuỗi giao vận RikkeiExpress Logistics đang có kế hoạch nâng cấp toàn bộ hệ thống phần mềm. Một thực tập sinh Business Analyst (BA) được giao nhiệm vụ phân loại danh sách các tính năng hiện có vào đúng 3 nhóm hệ thống thông tin chính trong doanh nghiệp: TPS (Transaction Processing System - Hệ thống Xử lý Giao dịch Tác nghiệp), MIS (Management Information System - Hệ thống Thông tin Quản lý), và DSS (Decision Support System - Hệ thống Hỗ trợ Quyết định). Tuy nhiên, bản phân loại của thực tập sinh đang bị lẫn lộn nghiêm trọng. Dưới vai trò System Analyst/Business Analyst, tôi sẽ chữa lỗi phân loại này, cung cấp bảng phân loại chuẩn xác, giải thích căn cứ và xây dựng một chương trình tự động phân loại các tính năng.

## Mục tiêu bài tập

*   Phân biệt bản chất, mục tiêu và đối tượng người dùng của 3 cấp độ Hệ thống thông tin chính.
*   Phát hiện và sửa lỗi lẫn lộn phân loại các tính năng phần mềm.
*   Phân định đúng vị trí và quyền hạn sử dụng tính năng của từng nhóm người dùng.

## Quy tắc nghiệp vụ

Dựa trên đề bài, các quy tắc phân loại được định nghĩa như sau:

*   **TPS (Xử lý giao dịch tác nghiệp):** Gắn liền với các giao dịch hàng ngày của nhân viên thu ngân, nhân viên kho, tài xế; đòi hỏi tốc độ xử lý cực nhanh và độ chính xác cao.
*   **MIS (Thông tin quản lý):** Cung cấp các báo cáo định kỳ/thống kê tổng hợp cho Quản lý bưu cục, Trưởng vùng.
*   **DSS (Hỗ trợ quyết định):** Sử dụng mô hình phân tích dữ liệu lịch sử để hỗ trợ Ban Giám đốc đưa ra quyết định chiến lược (ví dụ: dự báo quá tải, mở thêm bưu cục mới).

## Phần 1 - Chữa lỗi phân loại 3 nhóm HTTT

### 1.1. Các điểm phân loại sai của thực tập sinh

Thực tập sinh đã phân loại sai toàn bộ 5 tính năng được liệt kê trong đề bài. Cụ thể:

1.  **"Báo cáo tổng hợp doanh thu tháng cho Trưởng bưu cục"**: Bị xếp vào nhóm TPS, trong khi bản chất là **MIS**.
2.  **"Công cụ phân tích dự báo điểm nóng quá tải đơn hàng mùa Tết"**: Bị xếp vào nhóm TPS, trong khi bản chất là **DSS**.
3.  **"Tài xế bấm nút "Đã lấy hàng" trên App Mobile"**: Bị xếp vào nhóm MIS, trong khi bản chất là **TPS**.
4.  **"Nhân viên kho quét mã vạch nhập kho"**: Bị xếp vào nhóm MIS, trong khi bản chất là **TPS**.
5.  **"In phiếu cước giao hàng cho khách tại bưu cục"**: Bị xếp vào nhóm DSS, trong khi bản chất là **TPS**.

Tổng cộng có **5/5** tính năng bị phân loại sai.

### 1.2. Bảng phân định chuẩn xác 3 nhóm HTTT cho RikkeiExpress

Dưới đây là bảng phân loại chuẩn xác các tính năng dựa trên quy tắc nghiệp vụ đã nêu, kèm theo căn cứ giải thích chi tiết cho từng trường hợp:

| STT | Tên tính năng                                            | Phân loại sai của thực tập sinh | Phân loại chuẩn xác | Căn cứ giải thích                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :-- | :------------------------------------------------------- | :------------------------------ | :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | Báo cáo tổng hợp doanh thu tháng cho Trưởng bưu cục     | TPS                             | MIS                 | Tính năng này cung cấp các báo cáo định kỳ (tháng) tổng hợp dữ liệu về doanh thu cho cấp quản lý (Trưởng bưu cục) để theo dõi hiệu suất và đưa ra các quyết định điều hành ngắn hạn. Điều này hoàn toàn phù hợp với định nghĩa của MIS: "Cung cấp các báo cáo định kỳ/thống kê tổng hợp cho Quản lý bưu cục, Trưởng vùng."                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 2   | Công cụ phân tích dự báo điểm nóng quá tải đơn hàng mùa Tết | TPS                             | DSS                 | Đây là một công cụ sử dụng mô hình phân tích dữ liệu lịch sử (mùa Tết) để dự báo tình hình tương lai (quá tải đơn hàng), nhằm hỗ trợ Ban Giám đốc/quản lý cấp cao đưa ra các quyết định chiến lược về phân bổ nguồn lực, chuẩn bị nhân sự, v.v. Điều này khớp với định nghĩa của DSS: "Sử dụng mô hình phân tích dữ liệu lịch sử để hỗ trợ Ban Giám đốc đưa ra quyết định chiến lược (ví dụ: dự báo quá tải, mở thêm bưu cục mới)."                                                                                                                                                                                                                                                                                                                                         |
| 3   | Tài xế bấm nút "Đã lấy hàng" trên App Mobile           | MIS                             | TPS                 | Hành động "bấm nút Đã lấy hàng" là một giao dịch tác nghiệp hàng ngày, trực tiếp ghi nhận trạng thái của một đơn hàng cụ thể trong thời gian thực. Nó gắn liền với hoạt động thường nhật của tài xế và yêu cầu cập nhật tức thì, độ chính xác cao để phản ánh trạng thái đơn hàng. Điều này phù hợp với định nghĩa TPS: "Gắn liền với các giao dịch hàng ngày của nhân viên thu ngân, nhân viên kho, tài xế; đòi hỏi tốc độ xử lý cực nhanh và độ chính xác cao."                                                                                                                                                                                                                                                                                                                                                               |
| 4   | Nhân viên kho quét mã vạch nhập kho                     | MIS                             | TPS                 | Hoạt động quét mã vạch khi nhập kho là một giao dịch tác nghiệp cơ bản, diễn ra liên tục hàng ngày để cập nhật thông tin tồn kho và tình trạng hàng hóa. Nó đòi hỏi xử lý nhanh chóng và chính xác để đảm bảo dữ liệu kho luôn được cập nhật kịp thời, tránh sai sót trong quản lý hàng tồn. Điều này phù hợp với định nghĩa TPS: "Gắn liền với các giao dịch hàng ngày của nhân viên thu ngân, nhân viên kho, tài xế; đòi hỏi tốc độ xử lý cực nhanh và độ chính xác cao."                                                                                                                                                                                                                                                                                                                                                      |
| 5   | In phiếu cước giao hàng cho khách tại bưu cục            | DSS                             | TPS                 | Việc in phiếu cước là một phần của quy trình giao dịch trực tiếp với khách hàng tại bưu cục, diễn ra hàng ngày. Đây là một tác nghiệp cơ bản, yêu cầu xử lý nhanh chóng và chính xác để hoàn tất giao dịch, cung cấp chứng từ cho khách hàng và ghi nhận vào hệ thống. Điều này phù hợp với định nghĩa TPS: "Gắn liền với các giao dịch hàng ngày của nhân viên thu ngân, nhân viên kho, tài xế; đòi hỏi tốc độ xử lý cực nhanh và độ chính xác cao."                                                                                                                                                                                                                                                                                                                                                                  |

## Phần 2 - Giải thích & Viết mã nguồn kiểm tra

### 2.1. Giải thích lý do TPS đòi hỏi tốc độ xử lý nhanh và độ chính xác tuyệt đối

Hệ thống Xử lý Giao dịch Tác nghiệp (TPS) là nền tảng của mọi hoạt động kinh doanh hàng ngày tại RikkeiExpress. TPS đòi hỏi tốc độ xử lý nhanh và độ chính xác tuyệt đối vì các lý do sau:

1.  **Tác động trực tiếp đến hoạt động kinh doanh cốt lõi:** Các giao dịch trong TPS (như nhận đơn, lấy hàng, quét mã, in phiếu cước, cập nhật trạng thái) diễn ra liên tục, với số lượng lớn mỗi ngày. Đây là những hoạt động trực tiếp tạo ra giá trị và tương tác với khách hàng, đối tác. Bất kỳ sự chậm trễ hay sai sót nào trong xử lý đều có thể ngay lập tức làm gián đoạn chuỗi cung ứng, gây tắc nghẽn, trì hoãn giao hàng và ảnh hưởng nghiêm trọng đến trải nghiệm khách hàng, uy tín thương hiệu và hiệu suất vận hành.
2.  **Đảm bảo tính nhất quán và toàn vẹn dữ liệu tức thời:** Mỗi giao dịch TPS là một sự kiện kinh doanh độc lập nhưng có mối liên hệ mật thiết với các giao dịch khác và tình trạng chung của hệ thống (ví dụ: trạng thái đơn hàng, thông tin tồn kho, vị trí tài xế). Nếu dữ liệu từ các giao dịch này không chính xác hoặc không được cập nhật kịp thời, nó sẽ dẫn đến thông tin sai lệch trên toàn hệ thống. Điều này không chỉ gây ra lỗi trong hoạt động hiện tại mà còn ảnh hưởng đến độ tin cậy của các báo cáo MIS và kết quả phân tích DSS sau này, làm sai lệch các quyết định quản lý và chiến lược.
3.  **Hậu quả tài chính và rủi ro vận hành:** Một lỗi nhỏ trong việc ghi nhận giao dịch (ví dụ: sai địa chỉ, sai số lượng hàng, sai phí, không ghi nhận trạng thái) có thể dẫn đến thất thoát doanh thu, phát sinh chi phí để sửa chữa, hoặc thậm chí là mất mát hàng hóa. Đối với một chuỗi giao vận, việc đảm bảo mọi đơn hàng được xử lý chính xác từ khâu đầu đến cuối là yếu tố sống còn để duy trì lợi nhuận và tránh các tranh chấp pháp lý.
4.  **Tương tác trực tiếp với người dùng và đối tác:** TPS thường là điểm chạm đầu tiên và thường xuyên nhất giữa hệ thống với nhân viên tuyến đầu (tài xế, nhân viên kho, nhân viên bưu cục) và khách hàng. Một hệ thống chậm chạp hoặc không chính xác sẽ gây khó chịu, giảm năng suất làm việc, tạo ra sự không hài lòng và làm suy giảm lòng tin của các bên liên quan.

Tóm lại, tốc độ và độ chính xác của TPS là yếu tố quyết định sự vận hành trơn tru, hiệu quả và đáng tin cậy của toàn bộ hoạt động giao vận, đồng thời là nền tảng vững chắc cho các hệ thống thông tin cấp cao hơn.

### 2.2. Chương trình Python phân loại tính năng

Tôi đã xây dựng hàm Python `classify_logistics_feature(feature_name)` để tự động kiểm tra và phân loại tính năng vào đúng nhóm TPS, MIS hoặc DSS. Logic của hàm dựa trên các từ khóa và ngữ cảnh đã được phân tích và trình bày chi tiết ở Phần 1, tuân thủ nghiêm ngặt các quy tắc nghiệp vụ.

**File:** `classify_logistics_feature.py`

```python
def classify_logistics_feature(feature_name: str) -> str:
    """
    Phân loại tính năng của hệ thống giao vận RikkeiExpress vào nhóm TPS, MIS hoặc DSS.

    Args:
        feature_name: Tên tính năng cần phân loại.

    Returns:
        Chuỗi "TPS", "MIS", hoặc "DSS" tùy thuộc vào phân loại.
    """
    feature_name_lower = feature_name.lower()

    # Quy tắc phân loại TPS (Tác nghiệp)
    # Gắn liền với các giao dịch hàng ngày của nhân viên thu ngân, nhân viên kho, tài xế;
    # đòi hỏi tốc độ xử lý cực nhanh và độ chính xác cao.
    tps_keywords = [
        "bấm nút", "quét mã vạch", "nhập kho", "lấy hàng", "giao hàng", "in phiếu cước",
        "ghi nhận", "cập nhật trạng thái", "tạo đơn", "xác nhận đơn", "thanh toán",
        "xuất kho", "tác nghiệp"
    ]
    for keyword in tps_keywords:
        if keyword in feature_name_lower:
            return "TPS"

    # Quy tắc phân loại DSS (Hỗ trợ quyết định)
    # Sử dụng mô hình phân tích dữ liệu lịch sử để hỗ trợ Ban Giám đốc đưa ra quyết định chiến lược
    dss_keywords = [
        "dự báo", "phân tích dự báo", "mô hình", "điểm nóng", "chiến lược", "quyết định",
        "phân tích xu hướng", "tối ưu tuyến đường", "mở bưu cục", "đánh giá hiệu quả kinh doanh tổng thể",
        "nghiên cứu thị trường", "kế hoạch mở rộng"
    ]
    for keyword in dss_keywords:
        if keyword in feature_name_lower:
            return "DSS"

    # Quy tắc phân loại MIS (Thông tin quản lý)
    # Cung cấp các báo cáo định kỳ/thống kê tổng hợp cho Quản lý bưu cục, Trưởng vùng.
    # Kiểm tra MIS sau cùng để tránh nhầm lẫn với các tính năng TPS/DSS có thể chứa từ khóa chung như "báo cáo"
    mis_keywords = [
        "báo cáo", "tổng hợp", "thống kê", "theo dõi", "quản lý hiệu suất",
        "doanh thu", "hiệu suất", "tình hình hoạt động", "danh sách", "bảng lương"
    ]
    for keyword in mis_keywords:
        if keyword in feature_name_lower:
            return "MIS"

    # Nếu không khớp với bất kỳ quy tắc nào trên
    return "Không xác định"

if __name__ == "__main__":
    print("--- Kết quả phân loại các tính năng theo yêu cầu đề bài ---")
    # Các tính năng từ đề bài và phân loại đúng
    features_to_test = {
        "Báo cáo tổng hợp doanh thu tháng cho Trưởng bưu cục": "MIS",
        "Công cụ phân tích dự báo điểm nóng quá tải đơn hàng mùa Tết": "DSS",
        "Tài xế bấm nút \"Đã lấy hàng\" trên App Mobile": "TPS",
        "Nhân viên kho quét mã vạch nhập kho": "TPS",
        "In phiếu cước giao hàng cho khách tại bưu cục": "TPS"
    }

    for feature, expected_class in features_to_test.items():
        actual_class = classify_logistics_feature(feature)
        status = "ĐÚNG" if actual_class == expected_class else f"SAI (Dự kiến: {expected_class}, Thực tế: {actual_class})"
        print(f"Tính năng: '{feature}' -> Phân loại: {actual_class} ({status})")

    print("\n--- Kiểm tra thêm các trường hợp biên và ví dụ khác ---")
    additional_features = [
        "Báo cáo thống kê số lượng đơn giao tuần trước", # MIS - Edge case from problem description
        "Dự báo nhu cầu giao hàng 3 tháng tới dựa trên dữ liệu 3 năm", # DSS - Edge case from problem description
        "Tạo yêu cầu giao hàng mới cho khách lẻ", # TPS
        "Xem danh sách tài xế đang hoạt động trong khu vực", # MIS
        "Phân tích hiệu quả chiến dịch khuyến mãi theo từng vùng", # DSS
        "Cập nhật thông tin khách hàng", # TPS
        "Báo cáo tồn kho hàng hóa", # MIS
        "Quyết định mở rộng tuyến đường vận chuyển", # DSS
        "Thanh toán tiền mặt cho đơn hàng", # TPS
        "Theo dõi lộ trình đơn hàng thời gian thực", # MIS (theo dõi tổng quan, không phải hành động trực tiếp)
        "Lập kế hoạch tối ưu hóa đội xe vận chuyển", # DSS
        "Ghi nhận ca làm việc của tài xế" # TPS
    ]

    for feature in additional_features:
        classification = classify_logistics_feature(feature)
        print(f"Tính năng: '{feature}' -> Phân loại: {classification}")
```
