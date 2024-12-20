from flask import Flask, request, jsonify
from paddleocr import PaddleOCR
import cv2
import numpy as np
import os

app = Flask(__name__)
ocr = PaddleOCR(use_angle_cls=True, lang='en')

@app.route('/ocr', methods=['POST'])
def perform_ocr():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Read image file
    in_memory_file = file.read()
    nparr = np.frombuffer(in_memory_file, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    try:
        # Perform OCR
        result = ocr.ocr(image)

        # Extract text from results
        extracted_text = []
        if result[0]:  # Check if any text was detected
            for line in result[0]:
                text = line[1][0]  # Get the text content
                confidence = line[1][1]  # Get the confidence score
                extracted_text.append({
                    'text': text,
                    'confidence': float(confidence)
                })

        return jsonify({
            'status': 'success',
            'results': extracted_text
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
