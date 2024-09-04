def calculate_average(a, b, c):
    return (a + b + c) / 3

# Chạy chương trình
a = float(input("Nhập giá trị thứ nhất: "))
b = float(input("Nhập giá trị thứ hai: "))
c = float(input("Nhập giá trị thứ ba: "))

average = calculate_average(a, b, c)
print("Giá trị trung bình là:", average)
