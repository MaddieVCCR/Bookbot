import zipfile
import sys
from html.parser import HTMLParser
import re
from collections import Counter
from io import StringIO
import os

def main():
    epub_path = sys.argv[1]
    xhtmllist = []
    try:
        with zipfile.ZipFile(epub_path, "r") as epub:
            files = epub.namelist()  #Epub.namelist is a list of every file in the epub., we are creating a new list to run through
            print(f"contents of {epub_path}:")
            for file in files:
                if file.endswith(".xhtml"): #Here, we are taking every xhtml file, saving it as .txt file and then adding the path to a list
                    base,_ = os.path.splitext(file)
                    txt_path = "~/projects/Bookbot/books/temp" + base + ".txt"
                    with open(file, "r", encoding="utf-8") as infile:
                        content = infile.read()
                    with open(txt_path, "w", encoding="utf-8") as outfile:
                        outfile.write(content)
                    newfile = txt_path
                    print(newfile)
    except Exception as e:
        print(f"error: {e}")

def htmlremover(txt):
    print(f"{txt} this is part of htmlremvor")
    with open(txt, "r", encoding="utf-8") as file:
        content = file.read()

    content = re.sub(r'<[^>]+>.*?</[^>]+>', '', content, flags=re.DOTALL)
    content = re.sub(r'<[^>]+/>', '', content)
    content = re.sub(r'<[^>]+>', '', content)

    cleaned_file_obj = StringIO(content)
    cleaned_file_obj.seek(0)

    return cleaned_file_obj



main()
