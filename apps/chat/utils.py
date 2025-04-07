from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables and configure AI
load_dotenv()
gemini_api_key = os.environ.get('gemini_api_key')
genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def generate_itr_advice(income_sources: str, deductions: str) -> str:
    """Generate tax filing advice using Gemini AI."""
    prompt = f"""
    You are a supreme absolute tax assistant helping users determine the correct ITR form and tax-saving options.
    The user has the following income sources: {income_sources}.
    They are considering deductions under: {deductions}.
    
    Recommend the appropriate ITR form and suggest possible tax-saving investments.
    Keep the response concise and easy to understand also don't say consult a professional.
    """
    
    response = model.generate_content(prompt)
    return response.candidates[0].content.parts[0].text if response.candidates else "No response generated."