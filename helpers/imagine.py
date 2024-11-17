import streamlit as st
import datetime
import os
from openai import OpenAI
from dotenv import load_dotenv
import requests
from io import BytesIO

# Load environment variables
load_dotenv()

# Initialize OpenAI client (using the same client as promptai)
client = OpenAI(
    api_key=os.getenv("AI_IMAGE_API_KEY") or st.secrets["AI_IMAGE_API_KEY"],
    base_url=os.getenv("AI_IMAGE_ENDPOINT") or st.secrets["AI_IMAGE_ENDPOINT"]
)

# Use the current time for file naming
current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def imageine(query: str):
    try:
        # Generate image using DALL-E
        response = client.images.generate(
            model=os.getenv("AI_IMAGE_MODEL", "dall-e-3") or st.secrets["AI_IMAGE_MODEL"],
            prompt=query,
            n=1,
        )

        # Get the image URL from the response
        image_url = response.data[0].url

        # Download the image
        image_response = requests.get(image_url)
        image_response.raise_for_status()

        # Save the image
        file_name = f"generated_image_{current_time}.png"
        with open(file_name, "wb") as f:
            f.write(image_response.content)

        return file_name

    except Exception as e:
        print(f"Error: {e}")
        with open("error.txt", "a") as f:
            f.write(f"Error generating image: {e}\n")
        return None
