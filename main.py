def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    chars = get_char_count(text)
    sortedlist = sortlist(chars)
    for i in sortedlist:
        print(f"{i["char"]}: {i["num"]}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import get_num_words
from stats import get_char_count
from stats import sortlist
main()