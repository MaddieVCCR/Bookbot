import sys
from Epubparser import epupparser
import os

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    if book_path.endswith(".epub"):
        epupparser(book_path)
        epubfilelister = os.listdir("books/temp")
        epubfilepath = os.getcwd()
        totalwordcount = 0
        for file in epubfilelister:
            filepath = os.path.join("books/temp", file)
            text = get_book_text(filepath)
            num_words = get_num_words(text)
            print(f"Found {num_words} total words")
            totalwordcount += num_words
            if os.path.exists(filepath):
                os.remove(filepath)
        print(f"total words = {totalwordcount}")
            
    elif book_path.endswith(".txt"):  
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