# Install necessary libraries
from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

# Load API key from environment variables
load_dotenv()
gemini_api_key = os.environ.get('gemini_api_key')

genai.configure(api_key=gemini_api_key)  # Replace with your API key

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def generate_itr_advice(income_sources, deductions):
    """
    Generate ITR filing advice using Gemini AI.
    """
    prompt = f"""
    You are a supreme absolute tax assistant helping users determine the correct ITR form and tax-saving options.
    The user has the following income sources: {income_sources}.
    They are considering deductions under: {deductions}.
    
    Recommend the appropriate ITR form and suggest possible tax-saving investments.
    Keep the response concise and easy to understand also don't say consult a professional.
    """
    
    response = model.generate_content(prompt)
    
    if response.candidates:
        return response.candidates[0].content.parts[0].text
    else:
        return "No response generated."

# Streamlit UI
st.title("Smart ITR Filing Chatbot")
st.write("Get AI-powered recommendations for selecting the right ITR form and maximizing tax savings!")

# User inputs
income_sources = st.text_input("Enter your income sources (e.g., Salary, Business, Rental, Capital Gains)")
deductions = st.text_input("Enter deductions considered (e.g., 80C, 80D, Home Loan, NPS)")

if st.button("Get Advice"):
    if income_sources and deductions:
        advice = generate_itr_advice(income_sources, deductions)
        st.write("### AI Advice:")
        st.write(advice)
    else:
        st.warning("Please enter both income sources and deductions.")
