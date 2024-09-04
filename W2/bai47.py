def print_except_first_five_squares():
    square_list = [i ** 2 for i in range(1, 21)]
    print("Danh sách trừ 5 phần tử đầu tiên:", square_list[5:])

# Chạy chương trình
print_except_first_five_squares()
