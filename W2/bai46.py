def print_last_five_squares():
    square_list = [i ** 2 for i in range(1, 21)]
    print("5 phần tử cuối cùng của danh sách:", square_list[-5:])

# Chạy chương trình
print_last_five_squares()
