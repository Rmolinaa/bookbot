import sys

from stats import count_characters, get_num_words, sort_items


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    num_char = count_characters(book_text)
    sorted = sort_items(num_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted:
        print(f"{item['char']}: {item['num']}")


main()
