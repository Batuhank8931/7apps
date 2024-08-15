# app/models.py

from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class PDFMetadata(Base):
    __tablename__ = "pdf_metadata"

    id = Column(Integer, primary_key=True, index=True)
    pdf_id = Column(String, unique=True, index=True, nullable=False)
    filename = Column(String, nullable=False)
    txt_file_path = Column(String, nullable=False)
    page_count = Column(Integer, nullable=False)
    file_content = Column(Text, nullable=False)
