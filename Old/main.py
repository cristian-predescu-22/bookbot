from stats import count


def get_book_text(file_path: str) -> str:
    with open(file_path, encoding="utf-8") as f:
        file_content = f.read()
        a = count(file_content)
    return a


def main():
    print(get_book_text("books/frankenstein.txt"))


main()
