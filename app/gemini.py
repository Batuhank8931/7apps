import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(pdf_content: str, user_query: str) -> str:
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Based on the following PDF content, {pdf_content}, answer the user's query: {user_query}"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error occurred: {str(e)}"
