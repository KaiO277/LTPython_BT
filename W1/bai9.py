import math

# Hàm tính diện tích tam giác theo công thức từ Bài 7
def tinh_dien_tich_tam_giac(a, b, C):
    return 0.5 * a * b * math.sin(C)

# Hàm tính diện tích tam giác đều theo định lý Heron từ Bài 8
def tinh_dien_tich_tam_giac_deu(a):
    return (math.sqrt(3) / 4) * a**2

# Nhập giá trị cạnh tam giác đều từ người dùng
a = float(input("Nhập cạnh tam giác đều: "))

# Góc của tam giác đều là 60 độ, tức là π/3 radian
goc_C = math.pi / 3

# Tính diện tích tam giác đều bằng hai cách
S7 = tinh_dien_tich_tam_giac(a, a, goc_C)
S8 = tinh_dien_tich_tam_giac_deu(a)

# Hiển thị kết quả diện tích tính theo hai cách
print(f"Diện tích tam giác đều tính theo Bài 7: {S7:.2f}")
print(f"Diện tích tam giác đều tính theo Bài 8: {S8:.2f}")

# So sánh kết quả và đánh giá
if math.isclose(S7, S8, rel_tol=1e-9):
    print("Kết quả của Bài 7 và Bài 8 là giống nhau.")
else:
    print("Kết quả của Bài 7 và Bài 8 là khác nhau.")
