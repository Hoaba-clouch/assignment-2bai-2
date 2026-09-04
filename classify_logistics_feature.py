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