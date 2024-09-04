# Nhập số cạnh từ người dùng
sides = int(input("Nhập số cạnh của hình dạng: "))

# Xác định và hiển thị tên của hình dạng
if sides == 3:
    print("Đó là hình tam giác.")
elif sides == 4:
    print("Đó là hình tứ giác.")
elif sides == 5:
    print("Đó là hình ngũ giác.")
elif sides == 6:
    print("Đó là hình lục giác.")
elif sides == 7:
    print("Đó là hình thất giác.")
elif sides == 8:
    print("Đó là hình bát giác.")
elif sides == 9:
    print("Đó là hình cửu giác.")
elif sides == 10:
    print("Đó là hình thập giác.")
else:
    print("Số cạnh không hợp lệ, vui lòng nhập số từ 3 đến 10.")
