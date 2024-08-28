# Hằng số nhiệt dung riêng của nước
C = 4.186  # J/g°C

# Nhập khối lượng nước và sự thay đổi nhiệt độ từ người dùng
M = float(input("Nhập khối lượng nước (gram): "))
delta_T = float(input("Nhập sự thay đổi nhiệt độ (ΔT) (°C): "))

# Tính năng lượng cần thiết (Q)
Q = M * C * delta_T

# Hiển thị năng lượng tính được
print(f"Năng lượng cần thiết để thay đổi nhiệt độ: {Q:.2f} Joules")

# Chi phí tính bằng kilowatt giờ (kWh)
kWh = Q * 2.777e-7  # Chuyển đổi từ Joules sang kWh

# Chi phí tính bằng cent
cost = kWh * 8.9  # Chi phí là 8.9 cent mỗi kWh

# Hiển thị chi phí
print(f"Chi phí để thay đổi nhiệt độ của nước: {cost:.4f} cent")
