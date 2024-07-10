# Image Generator with Prompt Improvement

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)

## Description

This project is a web application built using [Streamlit](https://streamlit.io/) that combines image generation with AI-assisted prompt improvement. The app leverages an external image generation API and a language model called Zephyr-7b-Beta to create detailed and imaginative images based on user input.

### Features

1. **User-friendly Interface:** The Streamlit app provides a simple and intuitive interface for users to enter their image prompts.
2. **Prompt Improvement:** The app enhances user prompts using the Zephyr-7b-Beta language model, ensuring more descriptive and specific inputs for the image generation model.
3. **Image Generation:** The improved prompt is sent to an AI image generation API, which returns a high-quality image that matches the enhanced description.
4. **Download and Refresh:** Users can download the generated image and refresh the app to start a new image generation session.

### Dependencies

- [Streamlit](https://streamlit.io/)
- [requests](https://docs.python-requests.org/en/master/)
- [datetime](https://docs.python.org/3/library/datetime.html)

### Usage

1. Clone the repository:
   ```
   git clone https://github.com/linuztx/imageine.git
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set your API keys and endpoint URLs in a `.secrets` file:
   ```
   AI_IMAGE_ENDPOINT=<your-image-generation-api-endpoint>
   API_KEY=<your-api-key>
   AI_ENDPOINT=<your-zephyr-7b-beta-api-endpoint>
   ```
4. Run the Streamlit app:
   ```
   streamlit run main.py
   ```
5. Open the app in your browser using the displayed URL
   ```
   Local URL: http://localhost:8501
   ```
