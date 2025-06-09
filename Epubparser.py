import zipfile
import sys
from html.parser import HTMLParser
import re
from collections import Counter

def main():
    epub_path = sys.argv[1]
    xhtmllist = []
    try:
        with zipfile.ZipFile(epub_path, "r") as epub:
            files = epub.namelist()  #Epub.namelist is a list of every file in the epub., we are creating a new list to run through
            print(f"contents of {epub_path}:")
            for file in files:
                if file.endswith(".xhtml"):
                    newfile = file.replace(".xhtml",".txt")
                    xhtmllist.append(newfile)
                    print(newfile)
    except Exception as e:
        print(f"error: {e}")

def htmlremover():
    pass

main()
