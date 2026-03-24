from flask import Flask, request, jsonify
import requests
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/read-image', methods=['POST'])
def read_image():
    data = request.get_json()
    image_url = data.get('image_url')

    try:
        # Fetch image from URL
        response = requests.get(image_url)
        response.raise_for_status()

        # Open image using PIL
        img = Image.open(BytesIO(response.content))

        # Example: get image details
        width, height = img.size
        format = img.format

        return jsonify({
            "message": "Image fetched successfully",
            "width": width,
            "height": height,
            "format": format
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)