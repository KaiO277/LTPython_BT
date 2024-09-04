def decimal_to_binary(n):
    return bin(n).replace("0b", "")  # Chuyển đổi và loại bỏ tiền tố '0b'

# Nhập số thập phân từ người dùng
decimal_number = int(input("Nhập số thập phân cần chuyển đổi: "))
binary_number = decimal_to_binary(decimal_number)

print(f"Số nhị phân tương ứng với {decimal_number} là: {binary_number}")
