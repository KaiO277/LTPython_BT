def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Chạy chương trình
n = int(input("Nhập một số nguyên: "))
result = factorial(n)
print("Giai thừa của {} là: {}".format(n, result))
