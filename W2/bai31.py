def caesar_cipher(text):
    result = ""

    for char in text:
        if char.isalpha():  # Kiểm tra nếu ký tự là chữ cái
            shift = 3
            if char.islower():
                start = ord('a')
            elif char.isupper():
                start = ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char  # Giữ nguyên các ký tự không phải là chữ cái

    return result

# Nhập tin nhắn từ người dùng
message = input("Nhập tin nhắn cần mã hóa: ")
encrypted_message = caesar_cipher(message)
print("Tin nhắn đã được mã hóa:", encrypted_message)
