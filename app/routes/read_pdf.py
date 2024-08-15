# app/routes/read_pdf.py

import os
from pypdf import PdfReader  # Updated import

# Define the path for the saved text files directory
TXT_SAVE_DIR = "saved_txt"

# Ensure the directory exists
if not os.path.exists(TXT_SAVE_DIR):
    os.makedirs(TXT_SAVE_DIR)

def extract_text_from_pdf(pdf_path: str, pdf_id: str) -> str:
    """
    Extract text from the given PDF and save it as a UTF-8 encoded text file.

    :param pdf_path: The path to the PDF file.
    :param pdf_id: The unique identifier for the PDF.
    :return: The path to the saved text file.
    """
    # Create a PdfReader object
    reader = PdfReader(pdf_path)
    
    # Extract text from each page
    text_content = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            text_content += text

    # Define the path for the text file
    txt_file_path = os.path.join(TXT_SAVE_DIR, f"{pdf_id}.txt")

    # Save the text content as a UTF-8 encoded text file
    with open(txt_file_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text_content)
    
    return txt_file_path
