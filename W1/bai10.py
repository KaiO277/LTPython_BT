# Nhập chiều rộng và chiều dài từ người dùng
chieu_rong = float(input("Nhập chiều rộng của căn phòng (m): "))
chieu_dai = float(input("Nhập chiều dài của căn phòng (m): "))

# Tính diện tích căn phòng
dien_tich = chieu_rong * chieu_dai

# Hiển thị kết quả
print(f"Diện tích của căn phòng là: {dien_tich:.2f} mét vuông")
