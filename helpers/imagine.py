import streamlit as st
import requests
import datetime
import os

API_URL = st.secrets["AI_IMAGE_ENDPOINT"]
headers = {"Authorization": st.secrets["API_KEY"]}

# Use the current time as 
current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def imageine(query: str):
    try:
        prompt = {"inputs": query}
        response = requests.post(API_URL, headers=headers, json=prompt)
        image_base64 = response.content
        # print(image_base64)
        file_name = f"generated_image_{current_time}.png"
        with open(file_name, "wb") as f:
            f.write(image_base64)
        return file_name
    except Exception as e:
        print(f"Error: {e}")
        with open("error.txt", "a") as f:
            f.write(f"Error generating image: {e}\n")
