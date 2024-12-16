import re

from pdfminer.high_level import extract_text

# Extract text from the PDF
text = extract_text("Sample.pdf")

# Update the regex to match emails in the entire text
pattern = re.compile(r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+")

# Find all matches
matches = pattern.findall(text)
print(matches)

# for page_layout in extract_pages("./Sample.pdf"):
#     for element in page_layout:
#         print(element)
