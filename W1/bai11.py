# Hằng số chuyển đổi từ mét vuông sang Mẫu Anh
MOT_MAU_ANH = 43560

# Nhập chiều rộng và chiều dài từ người dùng
chieu_rong = float(input("Nhập chiều rộng của cánh đồng (m): "))
chieu_dai = float(input("Nhập chiều dài của cánh đồng (m): "))

# Tính diện tích cánh đồng theo mét vuông
dien_tich_met_vuong = chieu_rong * chieu_dai

# Chuyển đổi diện tích sang Mẫu Anh
dien_tich_mau_anh = dien_tich_met_vuong / MOT_MAU_ANH

# Hiển thị kết quả
print(f"Diện tích của cánh đồng là: {dien_tich_mau_anh:.2f} Mẫu Anh")
