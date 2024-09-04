def compare_strings(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    if len_s1 > len_s2:
        print(s1)
    elif len_s1 < len_s2:
        print(s2)
    else:
        print(s1)
        print(s2)

# Chạy chương trình
s1 = input("Nhập chuỗi thứ nhất: ")
s2 = input("Nhập chuỗi thứ hai: ")
compare_strings(s1, s2)
