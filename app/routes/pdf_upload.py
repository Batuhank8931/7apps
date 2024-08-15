import os
import logging
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from .read_pdf import extract_text_from_pdf
from app.database import get_db
from app.models import PDFMetadata
from pypdf import PdfReader  

router = APIRouter()

logger = logging.getLogger(__name__)

SAVE_DIR = "saved_files"

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

@router.post("/pdf")
async def upload_pdf(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    if file.content_type != "application/pdf":
        logger.warning(f"Invalid file type uploaded: {file.content_type}")
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDFs are allowed.")
    
    pdf_id = str(uuid4())
    file_path = os.path.join(SAVE_DIR, f"{pdf_id}.pdf")
    
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    
    logger.info(f"PDF uploaded successfully: {file.filename} with ID {pdf_id}")

    txt_file_path = extract_text_from_pdf(file_path, pdf_id)
    
    reader = PdfReader(file_path)  
    page_count = len(reader.pages)
    
    with open(txt_file_path, "r", encoding="utf-8", errors="ignore") as txt_file:
        file_content = txt_file.read()
    
    clean_text = file_content.encode('utf-8', 'ignore').decode('utf-8')  
    clean_text = clean_text.replace('\x00', '')  

    metadata = {
        "pdf_id": pdf_id,
        "filename": file.filename,
        "txt_file_path": txt_file_path,
        "page_count": page_count,
        "file_content": clean_text
    }

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
