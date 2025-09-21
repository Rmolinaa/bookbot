def get_num_words(text):
    return len(text.split())


def count_characters(text):
    words = "".join(text.split()).lower()
    chars_count = {}
    for char in words:
        if char in chars_count:
            continue
        chars_count[char] = words.count(char)
    return chars_count


def sort_on(items):
    return items["num"]


def sort_items(items):
    chars = []
    for char in items:
        if char.isalpha():
            chars.append({"char": char, "num": items[char]})
    chars.sort(reverse=True, key=sort_on)
    return chars
