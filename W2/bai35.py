def filter_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

# Nhập các số từ người dùng và chuyển thành danh sách số nguyên
input_numbers = list(map(int, input("Nhập các số, cách nhau bằng dấu phẩy: ").split(',')))
odd_numbers = filter_odd_numbers(input_numbers)

print("Các số lẻ là:", odd_numbers)
