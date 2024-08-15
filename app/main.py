import logging
from fastapi import FastAPI, HTTPException
from app.routes import pdf_upload, chat
from app.error_handlers import custom_http_exception_handler, generic_exception_handler

logging.basicConfig(
    level=logging.INFO,  
    format='%(asctime)s - %(levelname)s - %(message)s',  
    handlers=[
        logging.FileHandler("app.log"),  
        logging.StreamHandler() 
    ]
)

logger = logging.getLogger(__name__)

logger.info("Starting the 7apps FastAPI application")

app = FastAPI()

app.include_router(pdf_upload.router, prefix="/v1")
app.include_router(chat.router, prefix="/v1")

app.add_exception_handler(HTTPException, custom_http_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the 7apps API"}
