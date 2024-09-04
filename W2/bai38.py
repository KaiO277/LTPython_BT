def read_numbers():
    negative_numbers = []
    zero_numbers = []
    positive_numbers = []

    while True:
        user_input = input("Nhập số nguyên (nhấn Enter để kết thúc): ")
        if user_input == "":
            break
        number = int(user_input)
        if number < 0:
            negative_numbers.append(number)
        elif number == 0:
            zero_numbers.append(number)
        else:
            positive_numbers.append(number)

    return negative_numbers, zero_numbers, positive_numbers

def display_numbers(negative, zero, positive):
    print("Kết quả:")
    for number in negative:
        print(number, end=" ")
    for number in zero:
        print(number, end=" ")
    for number in positive:
        print(number, end=" ")
    print()

# Chạy chương trình
negatives, zeros, positives = read_numbers()
display_numbers(negatives, zeros, positives)
