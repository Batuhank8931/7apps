import os
from pypdf import PdfReader  

TXT_SAVE_DIR = "saved_txt"

if not os.path.exists(TXT_SAVE_DIR):
    os.makedirs(TXT_SAVE_DIR)

def extract_text_from_pdf(pdf_path: str, pdf_id: str) -> str:

    reader = PdfReader(pdf_path)
    
    text_content = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            text_content += text

    txt_file_path = os.path.join(TXT_SAVE_DIR, f"{pdf_id}.txt")

    with open(txt_file_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text_content)
    
    return txt_file_path
