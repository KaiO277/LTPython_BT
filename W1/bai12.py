# Nhập chi phí của bữa ăn từ người dùng
chi_phi_bua_an = float(input("Nhập chi phí của bữa ăn (VND): "))

# Tính thuế và tiền boa
thue = chi_phi_bua_an * 0.05
tien_boa = chi_phi_bua_an * 0.18
tong_tien = chi_phi_bua_an + thue + tien_boa

# Hiển thị kết quả
print(f"Chi phí bữa ăn: {chi_phi_bua_an:.2f} VND")
print(f"Tiền thuế: {thue:.2f} VND")
print(f"Tiền boa: {tien_boa:.2f} VND")
print(f"Tổng tiền: {tong_tien:.2f} VND")
