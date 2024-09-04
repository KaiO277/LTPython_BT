# Nhập tên tháng từ người dùng
month = input("Nhập tên tháng: ").capitalize()

# Xác định và hiển thị số ngày trong tháng
if month in ("January", "March", "May", "July", "August", "October", "December"):
    print(f"{month} có 31 ngày.")
elif month in ("April", "June", "September", "November"):
    print(f"{month} có 30 ngày.")
elif month == "February":
    print(f"{month} có 28 hoặc 29 ngày.")
else:
    print("Tên tháng không hợp lệ.")
