# 1. Phân tích Input/Output:
# Input:
# số_lượng_chi_nhánh: Số nguyên dương (Integer).
# số_học_viên: Số nguyên (Integer) đại diện cho sĩ số đi học của từng lớp. Sẽ được nhập liên tục cho 2 lớp của mỗi chi nhánh.
# Output:Chuỗi văn bản (String) thông báo trạng thái của lớp học tương ứng với số học viên vừa nhập.
# Các thông báo lỗi (String) nếu người dùng nhập số âm hoặc sai định dạng.

# Đề xuất giải pháp:
# Quản lý luồng bằng vòng lặp: Sử dụng vòng lặp for lồng nhau.
# Vòng lặp ngoài duyệt qua tổng số lượng chi nhánh. Vòng lặp trong chạy chính xác 
# 2 lần (vì mỗi chi nhánh mặc định có 2 lớp học).
# Xử lý Bẫy dữ liệu 1 (Số học viên âm): Sử dụng vòng lặp while True tại bước nhập 
# số học viên. Nếu người dùng nhập số < 0, hệ thống in ra cảnh báo và tiếp 
# tục lặp để yêu cầu nhập lại cho đến khi nhận được số >=0.
# Xử lý Bẫy dữ liệu 2 (Lớp vắng toàn bộ) & Đánh giá: Dùng cấu trúc rẽ nhánh if - elif - else ngay sau khi đã có 
# dữ liệu hợp lệ:Nếu bằng 0: In thông báo vắng toàn bộ.Nếu nhỏ hơn 20: In thông báo nhắc nhở.Nếu từ 20 
# trở lên: In thông báo ổn định.3. Thiết kế thuật toán (Pseudocode):

# BẮT ĐẦU
#   Nhập num_branches (số lượng chi nhánh)
#   VÒNG LẶP branch_idx TỪ 1 ĐẾN num_branches:
#     In "Chi nhánh {branch_idx}:"
#     VÒNG LẶP class_idx TỪ 1 ĐẾN 2:
#       # Bắt đầu xử lý nhập dữ liệu và bẫy lỗi số âm
#       VÒNG LẶP VÔ HẠN:
#         Nhập num_students (số học viên)
#         NẾU num_students < 0:
#           In "Số học viên không hợp lệ. Vui lòng nhập lại."
#         NGƯỢC LẠI:
#           THOÁT VÒNG LẶP VÔ HẠN (Break)      
#       # Đánh giá trạng thái
#       NẾU num_students == 0:
#         In "Chi nhánh {branch_idx} - Lớp {class_idx}: Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái."
#       NẾU 0 < num_students < 20:
#         In "Chi nhánh {branch_idx} - Lớp {class_idx}: Lớp cần được nhắc nhở theo dõi"
#       NẾU num_students >= 20:
#         In "Chi nhánh {branch_idx} - Lớp {class_idx}: Lớp học ổn định"
# KẾT THÚC

num_branches = int(input("Nhập số lượng chi nhánh: "))
for branch_idx in range(1, num_branches + 1):
    print(f"Chi nhánh {branch_idx}:")
    for class_idx in range(1, 3):
        while True:
            num_students = int(input(f"Nhập số học viên đi học của lớp {class_idx}: "))
            if num_students < 0:
                print("Số học viên không hợp lệ. Vui lòng nhập lại.")
            else:
                break 
        if num_students == 0:
            print(f"Chi nhánh {branch_idx} - Lớp {class_idx}: Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
        elif num_students < 20:
            print(f"Chi nhánh {branch_idx} - Lớp {class_idx}: Lớp cần được nhắc nhở theo dõi")
        else:
            print(f"Chi nhánh {branch_idx} - Lớp {class_idx}: Lớp học ổn định")