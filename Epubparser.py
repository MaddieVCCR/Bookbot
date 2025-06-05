import zipfile
import sys
from html.parser import HTMLParser
import re
from collections import Counter

def main():
    epub_path = sys.argv[1]
    try:
        with zipfile.ZipFile(epub_path, "r") as epub:
            files = epub.namelist()
            print(f"contents of {epub_path}:")
            for file in files:
                print(file)
    except Exception as e:
        print(f"error: {e}")

def htmlremover()
    pass

main()
