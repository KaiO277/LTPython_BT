def read_words():
    words = []
    seen_words = set()

    while True:
        word = input("Nhập từ (nhấn Enter để kết thúc): ")
        if word == "":
            break
        if word not in seen_words:
            words.append(word)
            seen_words.add(word)

    return words

def display_words(words):
    print("Các từ đã nhập (sau khi loại bỏ từ bị trùng):")
    for word in words:
        print(word)

# Chạy chương trình
words_list = read_words()
display_words(words_list)
