import math

# Nhập bán kính r và chiều cao h từ bàn phím
r = float(input("Nhập bán kính r của mặt đáy: "))
h = float(input("Nhập chiều cao h của hình trụ: "))

# Tính thể tích hình trụ
V = math.pi * r**2 * h

# In kết quả
print(f"Thể tích của hình trụ là: {V:.2f}")
