import math

# Nhập hai số nguyên từ người dùng
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Tính toán các giá trị theo yêu cầu
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b if b != 0 else "Không thể chia cho 0"
phan_du = a % b if b != 0 else "Không thể chia cho 0"
log_a = math.log10(a) if a > 0 else "Không tồn tại logarit của số không hoặc số âm"
a_mu_b = a ** b

# Hiển thị kết quả
print(f"Tổng của {a} và {b} là: {tong}")
print(f"Hiệu của {a} và {b} là: {hieu}")
print(f"Tích của {a} và {b} là: {tich}")
print(f"Thương của {a} chia cho {b} là: {thuong}")
print(f"Phần còn lại khi {a} được chia cho {b} là: {phan_du}")
print(f"Kết quả của log_10({a}) là: {log_a}")
print(f"Kết quả của {a}^({b}) là: {a_mu_b}")
