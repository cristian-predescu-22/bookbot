def get_num_words(text: str) -> str:
    count = len(text.split())
    return f"Found {count} total words"


def dict_count(text: str):
    new_dict = {}
    for i in text:
        a = i.lower()
        if a not in new_dict:
            new_dict[a] = 1
        else:
            new_dict[a] += 1
    return new_dict

def sorted_dict(dict):
    new_list = []
    for a, b in dict.items():
        if a.isalpha():
            new_list.append({"char": a, "num": b})


    new_list.sort(reverse=True, key=sort_on)
    return new_list

def sort_on(item):
    return item["num"]