# app/gemini.py

import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Function to generate content based on PDF text and user query
def generate_response(pdf_content: str, user_query: str) -> str:
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Based on the following PDF content, {pdf_content}, answer the user's query: {user_query}"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Handle API errors
        return f"Error occurred: {str(e)}"
