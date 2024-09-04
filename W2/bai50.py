import random

def generate_random_password():
    length = random.randint(7, 10)
    password = ''.join(chr(random.randint(33, 126)) for _ in range(length))
    return password

# Chạy chương trình
random_password = generate_random_password()
print("Mật khẩu ngẫu nhiên là:", random_password)
