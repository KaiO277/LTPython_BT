def split_tuple(t):
    mid_index = len(t) // 2
    first_half = t[:mid_index]
    second_half = t[mid_index:]
    print("Phần tử nửa đầu:", first_half)
    print("Phần tử nửa sau:", second_half)

# Chạy chương trình
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
split_tuple(t)
