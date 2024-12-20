# OCR Server using PaddleOCR

A simple Flask server that performs Optical Character Recognition (OCR) on uploaded images using PaddleOCR.

## Setup and Installation

1. Build the Docker image:
```bash
docker build -t paddle-ocr .
```

2. Run the container:
```bash
docker run -p 5000:5000 paddle-ocr
```

## Usage

The server exposes a single endpoint `/ocr` that accepts POST requests with image files.

### Making Requests

You can send requests using curl:
```bash
curl -X POST -F "image=@path/to/your/image.jpg" http://localhost:5000/ocr
```

Or using Python with requests:
```python
import requests

url = 'http://localhost:5000/ocr'
files = {'image': open('path/to/your/image.jpg', 'rb')}
response = requests.post(url, files=files)
print(response.json())
```

### Response Format

The server returns JSON responses in the following format:

Success response:
```json
{
    "status": "success",
    "results": [
        {
            "text": "extracted text",
            "confidence": 0.95
        }
    ]
}
```

Error response:
```json
{
    "status": "error",
    "message": "error description"
}
