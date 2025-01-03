import google.generativeai as genai
from api_data import api_key

def generate_response(question):
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(question)
        response_text = response.text
        print(response_text)
        return response_text
    except TypeError as e:
        print(f"Type Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

