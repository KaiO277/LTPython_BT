def is_perfect_number(n):
    divisors_sum = sum([i for i in range(1, n) if n % i == 0])
    return divisors_sum == n

# Chương trình chính để tìm các số hoàn hảo trong khoảng từ 1 đến 10,000
for num in range(1, 10001):
    if is_perfect_number(num):
        print(f"{num} là số hoàn hảo.")
