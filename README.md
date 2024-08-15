# SevenApps Project

## Overview

This project involves a FastAPI application with functionalities for PDF processing and Gemini API integration. It includes features for uploading PDFs, extracting text, and managing state.

## Prerequisites

- Python 3.12 or higher
- `pip` (Python package installer)

## Installation

### Clone the Repository

git clone https://github.com/yourusername/your-repo.git
cd your-repo

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

DATABASE_URL=postgresql+asyncpg://postgres:101010@localhost/sevenapps

## Running the Application

### Start the FastAPI Server

uvicorn app.main:app --reload

This command will start the FastAPI server in development mode. The application will be accessible at `http://localhost:8000`.

### Run Tests

pytest

This command will run all the tests in the `tests/` directory.

## Making Requests

### Upload a PDF

You can use tools like `curl` or Postman to test the PDF upload endpoint. Here's an example `curl` command:

curl -X POST "http://localhost:8000/upload_pdf" \
-H "Content-Type: multipart/form-data" \
-F "file=@path/to/your/sample.pdf"

Replace `path/to/your/sample.pdf` with the actual path to the PDF file you want to upload.

### Generate a Response

For endpoints like generating responses from the Gemini API, you can use `curl` or Postman to send POST requests with the necessary payload.

curl -X POST "http://localhost:8000/generate_response" \
-H "Content-Type: application/json" \
-d '{"prompt": "Your prompt here"}'

Replace `"Your prompt here"` with the actual prompt for the Gemini API.

For more details on the API endpoints, refer to the FastAPI documentation provided by the application.
