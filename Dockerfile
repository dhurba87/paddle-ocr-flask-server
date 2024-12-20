FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1-mesa-glx \
    patch \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install paddlepaddle
RUN pip install paddleocr opencv-python flask

COPY server.py .

EXPOSE 5000

CMD ["python", "server.py"]
