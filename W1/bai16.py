import math

# Hằng số gia tốc trọng trường
g = 9.8  # m/s^2

# Nhập chiều cao từ người dùng
d = float(input("Nhập chiều cao (m): "))

# Tốc độ ban đầu của vật
v_i = 0  # m/s

# Tính tốc độ cuối cùng của vật khi chạm đất
v_f = math.sqrt(v_i**2 + 2 * g * d)

# Hiển thị tốc độ cuối cùng
print(f"Tốc độ của vật khi chạm đất: {v_f:.2f} m/s")
