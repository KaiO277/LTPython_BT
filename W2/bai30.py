# Nhập một năm từ người dùng
year = int(input("Nhập một năm: "))

# Kiểm tra và hiển thị thông báo xem năm đó có phải là năm nhuận hay không
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(f"{year} là năm nhuận.")
else:
    print(f"{year} không phải là năm nhuận.")
