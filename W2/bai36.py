def read_and_sort_numbers():
    numbers = []

    while True:
        number = int(input("Nhập một số nguyên (nhập 0 để dừng): "))
        if number == 0:
            break
        numbers.append(number)

    # Sắp xếp danh sách theo thứ tự tăng dần
    numbers.sort()

    print("Các số đã nhập theo thứ tự tăng dần:")
    for num in numbers:
        print(num)

# Chạy chương trình
read_and_sort_numbers()
