import zipfile
import sys
from html.parser import HTMLParser
import re
from collections import Counter
from io import StringIO
import os
from os.path import expanduser, join
from bs4 import BeautifulSoup

def htmlremover(txt_path):
    with open(txt_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
    
    # Remove script/style tags
    for tag in soup(['script', 'style']):
        tag.decompose()
    
    # Get clean text
    text = soup.get_text(separator=' ', strip=True)
    
    return StringIO(text)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 epubparser.py <epub_path>")
        return

    epub_path = sys.argv[1]
    output_base = expanduser("~/projects/Bookbot/books/temp")
    os.makedirs(output_base, exist_ok=True)

    try:
        with zipfile.ZipFile(epub_path, "r") as epub:
            print(f"Contents of {epub_path}:")
            for file in epub.namelist():
                if file.endswith(".xhtml"):
                    # Get base filename without extension
                    base = os.path.splitext(os.path.basename(file))[0]
                    
                    # Create output path
                    txt_path = join(output_base, f"{base}.txt")
                    
                    print(f"Processing: {file} -> {txt_path}")  # Better debug output
                    
                    # Read and write content
                    with epub.open(file) as infile:
                        content = infile.read().decode('utf-8')
                    
                    with open(txt_path, "w", encoding="utf-8") as outfile:
                        outfile.write(content)
                        print(f"Created: {txt_path}")  # Fixed variable name

                    cleaned_content = htmlremover(txt_path)
                    with open(txt_path, "w", encoding="utf-8") as outfile:
                        outfile.write(cleaned_content.read())




    except zipfile.BadZipFile:
        print(f"Error: {epub_path} is not a valid EPUB file")
    except Exception as e:
        print(f"Error: {str(e)}")



main()
