
def get_book_text(path_to_book):
    with open(path_to_book)as b:
        return b.read()
    
def get_word_count(path_to_book):
    count = get_book_text(path_to_book).split()
    return count.__len__()


def get_char_count(path_to_book):
    splits = get_book_text(path_to_book).lower().split()
    text = ""
    for s in splits:
        text += s
    result = {}
    for c in text:
        if c not in result:
            result[c] = 0
        result[c] +=1
    return result


def sort_char_count(path_to_book):
    chars = get_char_count(path_to_book)
    result = []
    for c in chars:
        result.append({"char":c, "num": chars[c]})
    result.sort(reverse= True, key= sort_on)
    return result

def sort_on(item):
    return item["num"]
