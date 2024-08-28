import math

# Nhập cạnh tam giác đều từ bàn phím
a = float(input("Nhập cạnh tam giác đều: "))

# Tính diện tích tam giác đều theo định lý Heron
S = (math.sqrt(3)/4) * a**2

# In kết quả
print(f"Diện tích của tam giác đều là: {S:.2f}")
