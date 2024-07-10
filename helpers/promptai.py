import streamlit as st
import requests
import json

SYSTEM_PROMPT = "As an  LLM, your job is to generate detailed prompts that start with Create, for image generation models based on user input. Be descriptive and specific, but also make sure your prompts are clear, concise, and easy to understand. The more detailed your prompt, the better the model will be able to generate an image that matches your vision. Remember to include any relevant details, such as the subject, setting, and any other important elements you want to see in the image."
zephyr_7b_beta = st.secrets["AI_ENDPOINT"]
HEADERS = {"Authorization": st.secrets["API_KEY"]}

def build_input_prompt(message, chatbot, system_prompt):
    input_prompt = "<|system|>\n" + system_prompt + "</s>\n<|user|>\n"
    for interaction in chatbot:
        input_prompt = input_prompt + str(interaction[0]) + "</s>\n<|assistant|>\n" + str(interaction[1]) + "\n</s>\n<|user|>\n"

    input_prompt = input_prompt + str(message) + "</s>\n<|assistant|>"
    return input_prompt

def post_request_beta(payload):
    """
    Sends a POST request to the predefined Zephyr-7b-Beta URL and returns the JSON response.
    """
    response = requests.post(zephyr_7b_beta, headers=HEADERS, json=payload)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    return response.json()

def predict_beta(message, chatbot=[], system_prompt=""):
    input_prompt = build_input_prompt(message, chatbot, system_prompt)
    data = {
        "inputs": input_prompt
    }

    try:
        response_data = post_request_beta(data)
        json_obj = response_data[0]

        if 'generated_text' in json_obj and len(json_obj['generated_text']) > 0:
            bot_message = json_obj['generated_text']
            return bot_message
        elif 'error' in json_obj:
            print(json_obj['error'] + ' Please refresh and try again with smaller input prompt')
        else:
            print(f"Unexpected response: {json_obj}")
    except requests.HTTPError as e:
        print(f"Request failed with status code {e.response.status_code}")
    except json.JSONDecodeError as e:
        print(f"Failed to decode response as JSON: {str(e)}")

def prompt_improve(message, system_prompt=SYSTEM_PROMPT):
    response = predict_beta(message, [], system_prompt)
    text_start = response.rfind("<|assistant|>", ) + len("<|assistant|>")
    response = response[text_start:]
    return response.lstrip('\n')