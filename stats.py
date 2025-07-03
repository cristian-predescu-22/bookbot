def get_num_words(text: str) -> str:
    a = text.split()
    count = 0
    for _ in a:
        count += 1
    new_text = f"{count} words found in the document"
    return new_text

def dict_count(text: str):
    new_dict = {}
    for i in text:
        a = i.lower()
        if a not in new_dict:
            new_dict[a] = 1
        else:
            new_dict[a] += 1

#print(count("hi Now let's see"))