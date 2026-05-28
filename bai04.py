# BÀI TẬP VẬN DỤNG CƠ BẢN 4
# [Phân tích] Hệ thống đánh giá sĩ số lớp học

# 1. Phân tích lỗi
# - Code gốc đặt điều kiện sai: so sánh sĩ số với ngưỡng nhưng dùng toán tử không phù hợp.
# - Ví dụ: sĩ số >= 40 thì đánh giá "Đủ", nhưng code lại viết ngược hoặc đặt sai vị trí.
# - Kết quả: lớp đông vẫn bị đánh giá thiếu, lớp ít lại bị đánh giá đủ.

# 2. Sửa lỗi

lop = {
    "Lớp A": 42,
    "Lớp B": 35,
    "Lớp C": 50
}

nguong = 40

print("=== ĐÁNH GIÁ SĨ SỐ LỚP HỌC ===")
for ten, si_so in lop.items():
    if si_so >= nguong:   # sửa lại điều kiện đúng
        print(f"{ten}: {si_so} học viên -> Đủ sĩ số")
    else:
        print(f"{ten}: {si_so} học viên -> Thiếu sĩ số")
