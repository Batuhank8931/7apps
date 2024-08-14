# app/routes/chat.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.models import PDFMetadata
from app.gemini import generate_response
import logging

router = APIRouter()

# Initialize logger
logger = logging.getLogger(__name__)

@router.post("/chat/{pdf_id}")
async def chat_with_pdf(pdf_id: str, user_query: dict, db: AsyncSession = Depends(get_db)):
    # Retrieve the PDF metadata from the database
    result = await db.execute(select(PDFMetadata).filter(PDFMetadata.pdf_id == pdf_id))
    pdf_metadata = result.scalars().first()

    if not pdf_metadata:
        logger.error(f"PDF with ID {pdf_id} not found.")
        raise HTTPException(status_code=404, detail="PDF not found")

    logger.info(f"Processing chat request for PDF ID {pdf_id}")

    # Extract the PDF content from the metadata
    pdf_content = pdf_metadata.file_content

    # Generate a response using the Gemini API
    response = generate_response(pdf_content, user_query["message"])

    logger.info(f"Generated response for PDF ID {pdf_id}")

    return {"response": response}
