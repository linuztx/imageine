import streamlit as st
import os
from helpers.imagine import imageine
from helpers.promptai import prompt_improve

# Set the page headers
st.set_page_config(layout="wide", page_title="Image Generator")

hide_streamlit_style = """

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

"""
# Set the background image aesthetic
st.markdown(f"""
            <style>
            .stApp {{background-image: url("https://images.unsplash.com/photo-1516557070061-c3d1653fa646?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80"); 
                     background-attachment: fixed;
                     background-size: cover}}
            
            {hide_streamlit_style}
            
         </style>
         """, unsafe_allow_html=True)

# Page title
st.write("# :art: Image Generator")

# Page description
st.write("""- Welcome to Image Generator Web App Powered by Stable Diffusion X1 and Zephyr-7B-Beta, 
         Developed, Enhance and Created by [linuztx](https://github.com/linuztx). :man: :wrench:
         """)
st.write("- Stable Diffusion X1 brings your ideas to vivid detail, creating amazing images. :zap: Zephyr-7B-Beta enhances your prompts for even more striking and imaginative results. :tornado: :stars:")

prompt_input = st.text_input("Enter your prompt here:", placeholder=' Example: A cute cat playing chess')
if prompt_input is not None:
    if st.button("Generate Image"):
        # print(prompt_input)
        st.info("Improving prompt...")
        improve_prompt = prompt_improve(prompt_input)
        st.info("Generating image...")
        image_output = imageine(improve_prompt)
        st.success("Image Generated Successfully")
        st.balloons()
        st.image(image_output, caption=improve_prompt)
        with open(image_output, 'rb') as file:
          st.download_button("Download image", data=file, file_name=image_output, mime="image/png")
        os.remove(image_output)
        if st.button("Refresh"):
            st.session_state.clear()
            st.rerun()