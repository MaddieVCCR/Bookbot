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

    except zipfile.BadZipFile:
        print(f"Error: {epub_path} is not a valid EPUB file")
    except Exception as e:
        print(f"Error: {str(e)}")

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
