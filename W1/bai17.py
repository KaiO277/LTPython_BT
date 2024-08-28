# Nhập nhiệt độ không khí (Ta) và tốc độ gió (V) từ người dùng
Ta = float(input("Nhập nhiệt độ không khí (°C): "))
V = float(input("Nhập tốc độ gió (km/h): "))

# Tính chỉ số gió lạnh (WCI) theo công thức
WCI = 13.12 + 0.6215 * Ta - 11.37 * (V ** 0.16) + 0.3965 * Ta * (V ** 0.16)

# Làm tròn chỉ số gió lạnh đến số nguyên gần nhất
WCI_rounded = round(WCI)

# Hiển thị chỉ số gió lạnh
print(f"Chỉ số gió lạnh (WCI) là: {WCI_rounded}")
