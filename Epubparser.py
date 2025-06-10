import zipfile
import sys
from html.parser import HTMLParser
import re
from collections import Counter
from io import StringIO
import os
from os.path import expanduser, join


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 epubparser.py <epub_path>")
        return
    else:
        epub_path = sys.argv[1]
        output_base = expanduser("~/projects/Bookbot/books/temp") #expands ~ to home directory
        os.makedirs(output_base, exist_ok=True) #check if the path exists and make it if not
        try:
            with zipfile.ZipFile(epub_path, "r") as epub:
                print(f"contents of {epub_path}:")
                for file in epub.namelist(): #iterating through every epub file
                    if file.endswith(".xhtml"): #Here, we are taking every xhtml file, saving it as .txt file and then adding the path to a list
                        base,_ = os.path.splitext(file)
                        txt_file = os.path.basename(base) + ".txt" #getting just the file name
                        txt_path = join(output_base, f"{base}.txt")
                        print("test")
                        with epub.open(file) as infile:
                            content = infile.read().decode('utf-8')
                        with open(txt_path, "w", encoding="utf-8") as outfile:
                            outfile.write(content)
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
