from stats import get_num_words, dict_count

def get_book_text(file_path: str) -> str:
    with open(file_path, encoding="utf-8") as f:
        file_content = f.read()
        count = get_num_words(file_content)
    return file_content

def get_book_text2(file_path: str) -> str:
    with open(file_path, encoding="utf-8") as f:
        file_content = f.read()
        dict_new = dict_count(file_content)
    return file_content



def main():
    file_path = "books/frankenstein.txt"
    print(get_num_words(file_path))
    print(get_book_text2(file_path))


main()