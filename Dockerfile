FROM python:3.9-slim

EXPOSE 8501

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

COPY .env .env

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]