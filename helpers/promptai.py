import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# System prompt remains the same but moved to a constant
SYSTEM_PROMPT = """As an LLM, your job is to generate detailed prompts that start with Create, 
for image generation models based on user input. Be descriptive and specific, but also make sure 
your prompts are clear, concise, and easy to understand. The more detailed your prompt, the better 
the model will be able to generate an image that matches your vision. Remember to include any 
relevant details, such as the subject, setting, and any other important elements you want to see 
in the image."""

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("AI_CHAT_API_KEY") or st.secrets["AI_CHAT_API_KEY"],
    base_url=os.getenv("AI_CHAT_ENDPOINT") or st.secrets["AI_CHAT_ENDPOINT"]
)

def prompt_improve(message, system_prompt=SYSTEM_PROMPT):
    try:
        response = client.chat.completions.create(
            model=os.getenv("AI_CHAT_MODEL", "gpt-4o-mini") or st.secrets["AI_CHAT_MODEL"],
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            temperature=0.7,    
            max_tokens=300
        )
        
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error in prompt improvement: {e}")
        return message  # Return original message if there's an error