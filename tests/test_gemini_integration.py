from pypdf import PdfReader  
from pathlib import Path

def read_pdf(file_path):
    with open(file_path, "rb") as f:
        reader = PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def test_generate_response():
    pdf_path = Path(__file__).parent / 'data' / 'sample.pdf'
    pdf_content = read_pdf(pdf_path)
    