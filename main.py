import sys
from stats import get_num_words, dict_count, sorted_dict


def get_book_text(file_path: str) -> str:
    with open(file_path, encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = get_book_text(file_path)


    word_count = get_num_words(text)
    char_counts = dict_count(text)
    sorted_chars = sorted_dict(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
