def create_dictionary(n):
    dictionary = {i: i * i for i in range(1, n + 1)}
    return dictionary

# Chạy chương trình
n = int(input("Nhập số nguyên n: "))
result = create_dictionary(n)
print("Dictionary:", result)
