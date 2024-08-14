# app/routes/pdf_upload.py

import os
import re
import logging
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from .read_pdf import extract_text_from_pdf
from app.database import get_db
from app.models import PDFMetadata
from PyPDF2 import PdfReader

router = APIRouter()

# Initialize logger
logger = logging.getLogger(__name__)

# Define the path for the saved files directory
SAVE_DIR = "saved_files"

# Ensure the directory exists
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

@router.post("/pdf")
async def upload_pdf(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    if file.content_type != "application/pdf":
        logger.warning(f"Invalid file type uploaded: {file.content_type}")
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDFs are allowed.")
    
    # Generate a unique filename for the PDF to avoid collisions
    pdf_id = str(uuid4())
    file_path = os.path.join(SAVE_DIR, f"{pdf_id}.pdf")
    
    # Save the file to the specified directory
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    
    logger.info(f"PDF uploaded successfully: {file.filename} with ID {pdf_id}")

    # Extract text from the saved PDF and save it as a text file
    txt_file_path = extract_text_from_pdf(file_path, pdf_id)
    
    # Read the PDF again to get the number of pages
    reader = PdfReader(file_path)
    page_count = len(reader.pages)
    
    # Read the content from the text file
    with open(txt_file_path, "r", encoding="utf-8", errors="ignore") as txt_file:
        file_content = txt_file.read()
    
    # Clean the extracted text to remove extra lines, spaces, and non-printable characters
    clean_text = file_content.encode('utf-8', 'ignore').decode('utf-8')  # Ensure UTF-8 encoding
    clean_text = clean_text.replace('\x00', '')  # Remove any null bytes

    # Further clean up text to remove non-printable characters (Uncomment if needed)
    # clean_text = re.sub(r'[\x00-\x1F\x7F-\x9F]', ' ', clean_text)  # Remove non-printable characters
    # clean_text = re.sub(r'[\n\r]+', ' ', clean_text)  # Replace newlines and carriage returns with a single space
    # clean_text = re.sub(r'\s+', ' ', clean_text).strip()  # Replace multiple spaces with a single space and trim

    # Prepare the metadata
    metadata = {
        "pdf_id": pdf_id,
        "filename": file.filename,
        "txt_file_path": txt_file_path,
        "page_count": page_count,
        "file_content": clean_text
    }

    # Insert the metadata into the database
    new_metadata = PDFMetadata(
        pdf_id=metadata["pdf_id"],
        filename=metadata["filename"],
        txt_file_path=metadata["txt_file_path"],
        page_count=metadata["page_count"],
        file_content=metadata["file_content"]
    )
    
    db.add(new_metadata)
    await db.commit()
    await db.refresh(new_metadata)

    logger.info(f"Metadata stored successfully for PDF ID {pdf_id}")

    return metadata
