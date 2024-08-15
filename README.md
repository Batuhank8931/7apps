# SevenApps Project

## Overview

This project involves a FastAPI application with functionalities for PDF processing and Gemini API integration. It includes features for uploading PDFs, extracting text, and managing state.

## Prerequisites

- Python 3.12 or higher
- `pip` (Python package installer)

## Installation

### Clone the Repository

     git clone https://github.com/Batuhank8931/7apps.git
     cd 7apps

### Create and Activate a Virtual Environment

For Windows:

     python -m venv venv
     venv\Scripts\activate

For macOS/Linux:

     python3 -m venv venv
     source venv/bin/activate

### Install the Required Packages

     pip install -r requirements.txt

### Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

     GEMINI_API_KEY="your_gemini_key"
     DATABASE_URL=postgresql+asyncpg://username:password@localhost/database

### Create Database Tables

Run the following command to create the necessary tables in your PostgreSQL database:

     python app/create_tables.py

## Running the Application

### Start the FastAPI Server

     uvicorn app.main:app --reload

This command will start the FastAPI server in development mode. The application will be accessible at `http://localhost:8000`.

### Run Tests

     pytest

This command will run all the tests in the `tests/` directory.

## Making Requests

### Upload a PDF

**Request Method:** POST  
**Endpoint:** /v1/pdf  
**Description:** Endpoint for uploading and registering a PDF  
**Input:** Multipart form data containing the PDF file  
**Example:**

     curl -X POST "http://localhost:8000/v1/pdf" \
     -F "file=@/path/to/your/pdf/file.pdf"

**Output:** JSON response with the generated PDF ID  
**Example:**

     {
       "pdf_id": "unique_pdf_identifier"
     }

**Process:**

a. Validate the uploaded file (file type, size limits)  
b. Generate a unique identifier for the PDF  
c. Design a data structure to efficiently store PDFs  
d. Implement error handling to manage various PDF formats and potential parsing issues  
e. Store extracted text along with associated metadata (e.g., filename, document ID, page count) in a structured format  
f. Consider implementing text preprocessing techniques to enhance the quality of extracted content  

### Chat with PDF

**Request Method:** POST  
**Endpoint:** /v1/chat/{pdf_id}  
**Description:** Endpoint for interacting with a specific PDF  
**Input:** JSON body containing the user's message  
**Example:**

     {
       "message": "What is the main topic of this PDF?"
     }

**Output:** JSON response with the AI-generated answer  
**Example:**

     {
       "response": "The main topic of this PDF is..."
     }

**Process:**

- Use the unique PDF ID to locate the PDF and its associated text  
- Process the user's message to generate a relevant response using the Gemini API
