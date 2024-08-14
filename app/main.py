# app/main.py

import logging
from fastapi import FastAPI, HTTPException
from app.routes import pdf_upload, chat
from app.error_handlers import custom_http_exception_handler, generic_exception_handler

# Set up logging
logging.basicConfig(
    level=logging.INFO,  # Set log level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format with timestamp, log level, and message
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file named 'app.log'
        logging.StreamHandler()  # Also log to the console
    ]
)

# Create a logger instance
logger = logging.getLogger(__name__)

# Log a message indicating the application is starting
logger.info("Starting the 7apps FastAPI application")

app = FastAPI()

# Include the routers
app.include_router(pdf_upload.router, prefix="/v1")
app.include_router(chat.router, prefix="/v1")

# Add custom error handlers
app.add_exception_handler(HTTPException, custom_http_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the 7apps API"}
