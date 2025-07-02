def count(text: str) -> str:
    total_words = []
    a = text.split()
    b = dict_convert(a)
    return b


def dict_convert(text: str) -> str:
    dict_list = {}
    for i in a:
        i = i.lower()
        if i not in total_words:
            total_words[str(i)] = 1
        else:
            total_words[str(i)] += 1
    sorted_total_words: dict[str, int] = dict(
        sorted(total_words.items(), key=lambda x: x[1])
    )
    for i in sorted_total_words.keys():
        print(f"{sorted_total_words[i]} -> {i}")
