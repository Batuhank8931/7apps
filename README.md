# SevenApps Project

## 1. Overview

This project involves a FastAPI application with functionalities for PDF processing and Gemini API integration. It includes features for uploading PDFs, extracting text, and managing state.

## 2. Prerequisites

- Python 3.12 or higher
- `pip` (Python package installer)

## 3. Installation

### 3.1 Clone the Repository

     git clone https://github.com/Batuhank8931/7apps.git
     cd 7apps

### 3.2 Create and Activate a Virtual Environment

For Windows:

     python -m venv venv
     venv\Scripts\activate

For macOS/Linux:

     python3 -m venv venv
     source venv/bin/activate

### 3.3 Install the Required Packages

     pip install -r requirements.txt

### 3.4 Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

     GEMINI_API_KEY="your_gemini_key"
     DATABASE_URL=postgresql+asyncpg://username:password@localhost/database

### 3.5 Create Database Tables

Run the following command to create the necessary tables in your PostgreSQL database:

     python create_tables.py

## 4. Running the Application

### 4.1 Start the FastAPI Server

     uvicorn app.main:app --reload

This command will start the FastAPI server in development mode. The application will be accessible at `http://localhost:8000`.

### 4.2 Run Tests

     pytest

This command will run all the tests in the `tests/` directory.

## 5. Making Requests

### 5.1 Upload a PDF

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
         "pdf_id": "144fe247-24eb-4a06-bfda-24073229a08e",
         "filename": "deneme.pdf",
         "txt_file_path": "saved_txt\\144fe247-24eb-4a06-bfda-24073229a08e.txt",
         "page_count": 1,
         "file_content": "Örnek Deneme İçeriği"
     }

**Process:**

a. Validate the uploaded file (file type, size limits)  
b. Generate a unique identifier for the PDF  
c. Design a data structure to efficiently store PDFs  
d. Implement error handling to manage various PDF formats and potential parsing issues  
e. Store extracted text along with associated metadata (e.g., filename, document ID, page count) in a structured format  
f. Consider implementing text preprocessing techniques to enhance the quality of extracted content  

### 5.2 Chat with PDF

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

## 6. Logging

In the project folder, the app.log file holds the log data for all requests and errors 

     2024-08-15 14:21:37,980 - INFO - Starting the 7apps FastAPI application
     2024-08-15 14:21:42,220 - INFO - PDF uploaded successfully: deneme.pdf with ID 144fe247-24eb-4a06-bfda-24073229a08e
     2024-08-15 14:21:42,284 - INFO - Metadata stored successfully for PDF ID 144fe247-24eb-4a06-bfda-24073229a08e
     2024-08-15 14:21:48,201 - INFO - Processing chat request for PDF ID 33c6ec50-c35f-4cf6-8167-b2e86b2b4204
     2024-08-15 14:21:50,624 - INFO - Generated response for PDF ID 33c6ec50-c35f-4cf6-8167-b2e86b2b4204
     2024-08-15 14:27:11,222 - ERROR - PDF with ID 0d3aadbc-4ed6-4884-8593-0ed979ddcf0 not found.
     2024-08-15 14:27:11,222 - ERROR - HTTP exception occurred: PDF not found
     2024-08-15 14:27:21,306 - WARNING - Invalid file type uploaded: application/octet-stream
     2024-08-15 14:27:21,306 - ERROR - HTTP exception occurred: Invalid file type. Only PDFs are allowed.
