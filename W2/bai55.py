import zipfile
import os

def compress_file(file_name):
    with zipfile.ZipFile(file_name + '.zip', 'w') as zipf:
        zipf.write(file_name, os.path.basename(file_name))
    print(f"Tệp {file_name} đã được nén thành {file_name}.zip")

def decompress_file(zip_file_name):
    with zipfile.ZipFile(zip_file_name, 'r') as zipf:
        zipf.extractall()
    print(f"Tệp {zip_file_name} đã được giải nén.")

# Chương trình chính
def main():
    while True:
        action = input("Nhập 'c' để nén tệp, 'd' để giải nén tệp, hoặc 'q' để thoát: ").lower()
        if action == 'c':
            file_name = input("Nhập tên tệp cần nén (bao gồm đuôi tệp, ví dụ: file.txt): ")
            compress_file(file_name)
        elif action == 'd':
            zip_file_name = input("Nhập tên tệp zip cần giải nén (ví dụ: file.zip): ")
            decompress_file(zip_file_name)
        elif action == 'q':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

if __name__ == "__main__":
    main()
