import pdfplumber
import os
import json

page_start_delimiters = ["Rich Dad Poor Dad", "Free eBooks at Planet eBook.com"]

chapter_number = 0
pages = []
current_page = ""
page_number = 0

text_file_path = r"C:\Users\hp\PycharmProjects\pythonProject15\rich-dad-poor-dad.txt"


with open(text_file_path, "r", encoding="utf-8") as f:
    text = f.readlines()

for line in text:
    line = line.strip()
    # Check if the line matches any of the chapter delimiters
    if "chapter" in line.lower():
        # If so, increment the chapter number
        chapter_number += 1
        continue
    # Check if the line matches any of the start delimiters
    if any(start in line for start in page_start_delimiters):
        # If so, append the current page to the list of pages and start a new page
        if current_page:
            page_number += 1
            pages.append({
                "chapter": chapter_number,
                "page": current_page,
                "page_number": page_number
            })
            current_page = ""
        continue
    # Append the current line to the current page
    current_page += line + "\n"

# Append the final page if there is any remaining text
if current_page:
    page_number += 1
    pages.append({
        "chapter": chapter_number,
        "page": current_page,
        "page_number": page_number
    })

# Convert pages list to JSON string without escape sequences
pages_json = json.dumps(pages, indent=4, ensure_ascii=False)
print(pages_json)
