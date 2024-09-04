def filter_even_numbers(t):
    even_numbers = tuple(x for x in t if x % 2 == 0)
    return even_numbers

# Chạy chương trình
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result = filter_even_numbers(t)
print("Tuple chứa các số chẵn:", result)
