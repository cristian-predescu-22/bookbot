def get_book_text(file_path: str) -> None:
    total_words = {}
    with open(file_path, encoding="utf-8") as f:
        file_content = f.read()
        a = file_content.split()
        for i in a:
            if i not in total_words:
                total_words[str(i)] = 1
            else:
                total_words[str(i)] += 1
        sorted_total_words: dict[str, int] = dict(
            sorted(total_words.items(), key=lambda x: x[1])
        )
        for i in sorted_total_words.keys():
            print(f"{sorted_total_words[i]} -> {i}")


def count(text):
    pass


def main():
    print(get_book_text("books/frankenstein.txt"))


main()
