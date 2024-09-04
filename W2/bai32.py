def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():  # Kiểm tra nếu ký tự là chữ cái
            if char.islower():
                start = ord('a')
            elif char.isupper():
                start = ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char  # Giữ nguyên các ký tự không phải là chữ cái

    return result

# Chức năng chính
def main():
    choice = input("Bạn muốn mã hóa (nhập 'e') hay giải mã (nhập 'd') tin nhắn? ")
    message = input("Nhập tin nhắn của bạn: ")
    shift = int(input("Nhập số ký tự dịch chuyển: "))

    if choice == 'd':
        shift = -shift  # Đảo ngược dịch chuyển khi giải mã

    result = caesar_cipher(message, shift)
    print("Kết quả:", result)

# Chạy chương trình
main()
