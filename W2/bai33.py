def is_palindrome(s):
    s = s.lower()  # Chuyển chuỗi thành chữ thường để kiểm tra
    return s == s[::-1]  # So sánh chuỗi với chính nó khi đảo ngược

# Nhập chuỗi từ người dùng
input_str = input("Nhập chuỗi cần kiểm tra: ")

if is_palindrome(input_str):
    print(f"'{input_str}' là một Palindrom.")
else:
    print(f"'{input_str}' không phải là một Palindrom.")
