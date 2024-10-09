import streamlit as st
from openai import OpenAI

# Access the secret API key from the 'default' section in st.secrets
api_key = st.secrets["default"]["OPENAI_API_KEY"]

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

st.title("MedPatch")
user_content = st.text_area("Please enter your vital signs data here (e.g., heart rate, respiratory rate, oxygen saturation, blood pressure, temperature, etc.). This information will help us prioritize your care in the emergency room.", "Help us assess the urgency of your condition, please provide the following information for re-evaluation in the emergency room.")
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant, tasked with optimizing patient prioritization in an emergency room (ER) waiting room using a five-category triage system. The categories range from non-urgent to immediate life-threatening cases. Your role is to re-evaluate patient information in real-time, identify the most urgent cases based on symptoms, vital signs, and medical history, and assign them to the appropriate triage category. Provide accurate diagnoses and recommendations to the attending physician, ensuring timely and effective care while improving the workflow and patient safety in the ER."},
        {"role": "user", "content": user_content}
    ]
)

st.write(completion.choices[0].message.content)