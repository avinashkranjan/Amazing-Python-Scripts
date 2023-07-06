import numpy as np
from flask import Flask, request, jsonify, render_template,json
import cv2
from skimage.metrics import structural_similarity as ssim



app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message':'Welcome to Flask Apis'})

@app.route('/img',methods=['POST'])
def predict():
    file1 = request.files['file1']
    file2 = request.files['file2']

    # Read the images using OpenCV
    img1 = cv2.imdecode(np.frombuffer(file1.read(), np.uint8), cv2.IMREAD_COLOR)
    img2 = cv2.imdecode(np.frombuffer(file2.read(), np.uint8), cv2.IMREAD_COLOR)

    # Resize the images to 256x256 pixels
    img1 = cv2.resize(img1, (256, 256))
    img2 = cv2.resize(img2, (256, 256))

    # Convert the images to grayscale
    gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Calculate the structural similarity index between the images
    score = ssim(gray_img1, gray_img2, full=True)[0]

    # Convert the similarity score to a percentage
    similarity_percentage = score * 100

    # Return the similarity percentage in a JSON response
    return jsonify({'similarity_percentage': similarity_percentage})    


if __name__ == '__main__':
    app.run(debug=True)