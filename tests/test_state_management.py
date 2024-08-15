# tests/test_state_management.py

from app.state import StateManager
from pathlib import Path
from pypdf import PdfReader  # Updated import

def read_pdf(file_path):
    with open(file_path, "rb") as f:
        reader = PdfReader(f)  # Updated to PdfReader
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def test_state_management():
    state_manager = StateManager()
    pdf_path = Path(__file__).parent / 'data' / 'sample.pdf'
    pdf_content = read_pdf(pdf_path)
    
    pdf_id = "12345"
    state_manager.add_pdf(pdf_id, pdf_content)
    
    retrieved_content = state_manager.get_pdf(pdf_id)
    
    assert retrieved_content == pdf_content
