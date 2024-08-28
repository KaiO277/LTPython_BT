# Sử dụng giá trị cạnh tam giác từ Bài 8
a = float(input("Nhập cạnh tam giác đều (giá trị cạnh từ Bài 8): "))

# Tính diện tích tam giác đều bằng công thức S = 0.5 * a * b * sin(C)
S7 = 0.5 * a * a * math.sin(math.pi/3)

# Tính diện tích tam giác đều bằng định lý Heron từ Bài 8
S8 = (math.sqrt(3)/4) * a**2

# In kết quả so sánh
print(f"Diện tích tam giác đều tính theo Bài 7: {S7:.2f}")
print(f"Diện tích tam giác đều tính theo Bài 8: {S8:.2f}")

# Đánh giá kết quả
if math.isclose(S7, S8, rel_tol=1e-9):
    print("Kết quả của Bài 7 và Bài 8 là giống nhau.")
else:
    print("Kết quả của Bài 7 và Bài 8 là khác nhau.")
