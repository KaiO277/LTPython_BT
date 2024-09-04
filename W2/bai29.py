# Nhập độ dài của ba cạnh từ người dùng
a = float(input("Nhập độ dài cạnh thứ nhất: "))
b = float(input("Nhập độ dài cạnh thứ hai: "))
c = float(input("Nhập độ dài cạnh thứ ba: "))

# Phân loại tam giác dựa trên độ dài các cạnh
if a == b == c:
    print("Đây là tam giác đều.")
elif a == b or b == c or a == c:
    print("Đây là tam giác cân.")
else:
    print("Đây là tam giác thường.")
