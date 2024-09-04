def format_word_list(words):
    # Kiểm tra độ dài danh sách để xử lý các trường hợp khác nhau
    if len(words) == 0:
        return ""
    elif len(words) == 1:
        return words[0]
    elif len(words) == 2:
        return f"{words[0]} and {words[1]}"
    else:
        return ", ".join(words[:-1]) + " and " + words[-1]

# Chương trình chính
def main():
    # Nhập vào một danh sách từ từ người dùng
    user_input = input("Nhập các từ, cách nhau bằng dấu phẩy: ")
    word_list = [word.strip() for word in user_input.split(",")]
    
    # Định dạng danh sách từ
    formatted_list = format_word_list(word_list)
    
    # Hiển thị kết quả
    print("Danh sách đã được định dạng: " + formatted_list)

if __name__ == "__main__":
    main()
