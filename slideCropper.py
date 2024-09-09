import fitz  # PyMuPDF
import os  # To handle file paths and filenames

# Input PDF file path
input_pdf_path = "/Users/manuel/Downloads/Chapter 3 Lecture Notes - CHEM 1113 Broering.pdf"

# Extract the directory, base name, and file extension from the input path
input_dir = os.path.dirname(input_pdf_path)
input_base_name = os.path.basename(input_pdf_path)
input_name, input_ext = os.path.splitext(input_base_name)

# Create the output filename by adding the "CROPPED" prefix
output_pdf_name = f"CROPPED_{input_name}{input_ext}"
output_pdf_path = os.path.join(input_dir, output_pdf_name)

# Open the input PDF
pdf_document = fitz.open(input_pdf_path)

# Create a new PDF to store the cropped pages
output_pdf = fitz.open()

# Get the number of pages in the original PDF
num_pages = pdf_document.page_count

# Loop through all pages of the PDF
for page_num in range(num_pages):
    
    # Load the current page
    page = pdf_document.load_page(page_num)
    
    # Get the page dimensions (width and height)
    page_width, page_height = page.rect.width, page.rect.height

    # ======= FIRST IMAGE (TOP CROP) ======= #
    # Define the rectangle for the first crop (top section)
    rect1 = fitz.Rect(127, 90, page_width - 127, page_height - 434)

    # Crop the original page for the first section
    page.set_cropbox(rect1)

    # Add the cropped page to the new PDF
    output_pdf.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

    # Reload the same page to apply the second crop
    page = pdf_document.load_page(page_num)

    # ======= SECOND IMAGE (BOTTOM CROP) ======= #
    # Define the rectangle for the second crop (bottom section)
    rect2 = fitz.Rect(127, 434, page_width - 127, page_height - 90)

    # Crop the original page for the second section
    page.set_cropbox(rect2)

    # Add the cropped page to the new PDF
    output_pdf.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

# Save the new PDF with the "CROPPED_" prefix
output_pdf.save(output_pdf_path)
output_pdf.close()

print(f"Cropped PDF saved as '{output_pdf_path}'")
