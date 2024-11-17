<div align="center">

# 🎨 AI Image Generator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)](https://openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Transform your text descriptions into stunning visuals using AI technology.

![imageine](https://github.com/user-attachments/assets/fea57fac-8586-4f25-aaae-058e414fe685)

</div>

## 🚀 Demo

Visit live demo at: [AI Image Generator Demo](https://imageine.streamlit.app/)

## ✨ Features

### 🎯 Core Features
- **AI-Powered Image Generation**: Create stunning visuals using any OpenAI Compatible image model
- **Smart Prompt Enhancement**: Improve your prompts with any OpenAI Compatible chat model
- **Real-time Processing**: Watch your ideas come to life instantly

### 💫 User Experience
- **Intuitive Interface**: Clean, modern design with responsive layout
- **Progress Tracking**: Real-time generation progress indicators
- **Quick Actions**: One-click download and regeneration options

### 🛠️ Technical Features
- **OpenAI Integration**: Leverages latest AI models
- **Docker Support**: Easy deployment with containerization

## 📦 Installation

### Prerequisites
- Python 3.9+
- OpenAI API key
- Docker (optional)

### Quick Start
```bash
# Clone the repository
git clone https://github.com/linuztx/imageine.git

# Navigate to project directory
cd imageine

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# Run the application
streamlit run main.py
```

### 🐳 Docker Installation
```bash
# Build the image
docker build -t imageine .

# Run the container
docker run -p 8501:8501 imageine
```

## 🎯 Usage

### Basic Usage
1. Enter your image description
2. (Optional) Enable prompt enhancement
3. Click "Generate Image"
4. Download or regenerate as needed

### 🎨 Writing Effective Prompts
- Be specific about desired elements
- Include style preferences
- Mention lighting and composition
- Reference artistic influences

### ⚙️ Configuration
```env
# Chat Generation API
AI_CHAT_ENDPOINT=your-chat-generation-endpoint
AI_CHAT_API_KEY=your-chat-api-key

# Image Generation API
AI_IMAGE_ENDPOINT=your-image-generation-endpoint
AI_IMAGE_API_KEY=your-image-api-key 

# Model
AI_CHAT_MODEL=your-model-here
AI_IMAGE_MODEL=your-image-model-here
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💝 Donations

If you find this project useful, consider supporting my work by making a donation. Every contribution helps me continue developing and maintaining this project.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/linuztx)


---

<div align="center">
Made with ❤️ using Streamlit | © 2024 AI Image Generator
</div>
