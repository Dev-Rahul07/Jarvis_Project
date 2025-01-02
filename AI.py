import google.generativeai as genai
from api_data import api_key
def generate_response(question):
        genai.configure(api_key = api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(question,generation_config = genai.GenerationConfig(
        max_output_tokens=100,
        temperature=0.1) 
        )
        print(response.text)

        return response