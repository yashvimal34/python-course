import fitz  # PyMuPDF

# Open the file with first 4 pages already removed
doc = fitz.open("input.pdf")

# Define the logo-only bounding box — tight to avoid the border
# Page size: A4 = 595 x 842 pts. Logo is at top-right, below top border line
x1, y1 = 480, 30    # just under the border line
x2, y2 = 580, 70    # width ~100, height ~40 (tightly fitted)

for page in doc:
    rect = fitz.Rect(x1, y1, x2, y2)
    page.draw_rect(rect, fill=(1, 1, 1), color=None, width=0)

# Save the cleaned output
doc.save("final_cleaned_preserve_border.pdf")
doc.close()
