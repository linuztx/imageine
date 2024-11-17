import streamlit as st
import os
from helpers.imagine import imageine
from helpers.promptai import prompt_improve

# Set the page configuration
st.set_page_config(
    layout="wide",
    page_title="AI Image Generator",
    page_icon="🎨",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    /* Main container styling */
    .main {
        padding: 2rem;
        border-radius: 10px;
        background-color: rgba(255, 255, 255, 0.95);
    }
    
    /* Input container styling */
    .input-container {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Button styling */
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3rem;
        font-weight: bold;
        margin-top: 1rem;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Image display styling */
    .image-container {
        display: flex;
        justify-content: center;
        margin-top: 2rem;
    }
    
    /* Progress bar styling - Option 1: Hide it completely */
    .stProgress {
        display: none;
    }
    
    /* OR Option 2: Make it more subtle with a different color */
    .stProgress > div > div > div > div {
        background-color: rgba(255, 255, 255, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# Background image
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1516557070061-c3d1653fa646?ixlib=rb-4.0.3");
        background-attachment: fixed;
        background-size: cover;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## About")
    st.markdown("""
    This AI Image Generator combines the power of:
    - 🤖 Advanced Language Models
    - 🎨 State-of-the-art Image Generation
    - ✨ Prompt Enhancement Technology
    """)
    
    st.markdown("---")
    st.markdown("## Tips for Better Results")
    st.markdown("""
    1. Be specific about what you want
    2. Include details about style and mood
    3. Mention lighting and composition
    4. Specify any particular artistic influences
    """)
    
    st.markdown("---")
    st.markdown("### 👨‍💻 Created by [LinuzTX](https://github.com/linuztx)")

# Main content
st.markdown('<div class="title-container">', unsafe_allow_html=True)
st.markdown("# 🎨 **AI** Image Generator")
st.markdown("- Transform your ideas into stunning visuals, with a simple prompt.")
st.markdown('</div>', unsafe_allow_html=True)

# Create columns for layout
col1, col2 = st.columns([2, 1])

with col1:
    prompt_input = st.text_area(
        "Describe your image:",
        placeholder="Example: A serene Japanese garden at sunset with cherry blossoms falling, painted in watercolor style",
        height=100
    )

with col2:
    st.markdown("### Generation Settings")
    enhance_prompt = st.checkbox("Enhance prompt", value=False)

# Always show the Generate button, but disable it if there's no input
generate_button = st.button(
    "🚀 Generate Image",
    disabled=not bool(prompt_input),  # Disable button if prompt_input is empty
    use_container_width=True
)

if generate_button and prompt_input:  # Check both button click and input existence
    final_prompt = prompt_input
    
    if enhance_prompt:
        with st.spinner("🤔 Enhancing your prompt..."):
            final_prompt = prompt_improve(prompt_input)
            st.info(f"Enhanced prompt:\n\n{final_prompt}")
    
    with st.spinner("🎨 Creating your masterpiece..."):
        progress_bar = st.progress(0)
        for i in range(100):
            progress_bar.progress(i + 1)
        image_output = imageine(final_prompt)
        
        if image_output:
            st.success("✨ Image generated successfully!")
            st.balloons()
            
            # Display image in a container
            st.markdown('<div class="image-container">', unsafe_allow_html=True)
            st.image(
                image_output, 
                caption="Generated Image", 
                use_container_width=True
            )
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Create a container for buttons with consistent styling
            st.markdown("""
                <style>
                .button-container {
                    display: flex;
                    gap: 1rem;
                    margin-top: 1rem;
                    align-items: stretch;
                }
                .button-container > div {
                    flex: 1;
                    display: flex;
                }
                .button-container > div > div {
                    width: 100%;
                }
                .stButton, .stDownloadButton {
                    width: 100%;
                    height: 100%;
                }
                .stButton > button, .stDownloadButton > button {
                    height: 100% !important;
                    margin-top: 0 !important;
                }
                </style>
            """, unsafe_allow_html=True)
            
            # Button container
            st.markdown('<div class="button-container">', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            
            with col1:
                with open(image_output, 'rb') as file:
                    st.download_button(
                        "⬇️ Download Image",
                        data=file,
                        file_name=image_output,
                        mime="image/png",
                        use_container_width=True,
                        key="download_button"
                    )
            with col2:
                if st.button(
                    "🔄 Generate Another",
                    use_container_width=True,
                    key="regenerate_button"
                ):
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Cleanup
            os.remove(image_output)
        else:
            st.error("❌ Failed to generate image. Please try again.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: rgba(255,255,255,0.7);'>
    <p>Made with ❤️ using Streamlit | © 2024 AI Image Generator</p>
</div>
""", unsafe_allow_html=True)