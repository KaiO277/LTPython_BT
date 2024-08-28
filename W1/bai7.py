import math

# Nhập vào 3 cạnh và 3 góc (radian) từ bàn phím
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
A = float(input("Nhập góc A (radian): "))
B = float(input("Nhập góc B (radian): "))
C = float(input("Nhập góc C (radian): "))

# Tính diện tích tam giác theo công thức S = 0.5 * a * b * sin(C)
S = 0.5 * a * b * math.sin(C)

# In kết quả
print(f"Diện tích của tam giác là: {S:.2f}")
