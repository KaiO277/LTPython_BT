import re

def is_good_password(password):
    # Kiểm tra độ dài mật khẩu
    if len(password) < 8:
        return False
    # Kiểm tra mật khẩu chứa ít nhất một chữ cái viết hoa, một chữ cái viết thường, và một số
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    
    return True

# Chạy chương trình
password = input("Nhập mật khẩu: ")

if is_good_password(password):
    print("Mật khẩu là tốt.")
else:
    print("Mật khẩu không tốt.")
