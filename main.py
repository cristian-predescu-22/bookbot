def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        file_content = f.read()
        return file_content


def count(text):
    pass


def main():
    print(get_book_text("books/frankenstein.txt"))


main()
