import numpy as np
from flask import Flask, request, jsonify, render_template, json
import cv2
from skimage.metrics import structural_similarity as ssim


app = Flask(__name__)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


@app.route('/')
def home():
    return jsonify({'message': 'Welcome to Flask Apis'})


@app.route('/image_Compare', methods=['POST'])
def predict():
    file1 = request.files['file1']
    file2 = request.files['file2']

    # Read the images using OpenCV
    img1 = cv2.imdecode(np.frombuffer(
        file1.read(), np.uint8), cv2.IMREAD_COLOR)
    img2 = cv2.imdecode(np.frombuffer(
        file2.read(), np.uint8), cv2.IMREAD_COLOR)

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


@app.route('/face_recognize', methods=['POST'])
def predictface():
    # Get the uploaded files from the request
    file1 = request.files['file1']
    file2 = request.files['file2']

   # Read the images using OpenCV directly from the request files
    img1 = cv2.imdecode(np.frombuffer(
        file1.read(), np.uint8), cv2.IMREAD_COLOR)
    img2 = cv2.imdecode(np.frombuffer(
        file2.read(), np.uint8), cv2.IMREAD_COLOR)

    # Convert the images to grayscale
    gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Detect faces in the images
    faces1 = face_cascade.detectMultiScale(
        gray_img1, scaleFactor=1.1, minNeighbors=5)
    faces2 = face_cascade.detectMultiScale(
        gray_img2, scaleFactor=1.1, minNeighbors=5)

    # Compare only the first detected face in each image
    if len(faces1) > 0 and len(faces2) > 0:
        x1, y1, w1, h1 = faces1[0]
        x2, y2, w2, h2 = faces2[0]

        # Extract the face regions from the images
        face1 = gray_img1[y1:y1+h1, x1:x1+w1]
        face2 = gray_img2[y2:y2+h2, x2:x2+w2]

        # Resize the face regions to the same dimensions
        resized_face1 = cv2.resize(face1, (face2.shape[1], face2.shape[0]))

        # Calculate the structural similarity index between the face regions
        score = ssim(resized_face1, face2, full=True)[0]

        # Convert the similarity score to a percentage
        similarity_percentage = score * 100

        # Return the similarity percentage in a JSON response
        return jsonify({'similarity_percentage': similarity_percentage})

    else:
        return jsonify({'similarity_percentage': 'Could not detect faces in both images.'})


@app.route('/face_recognize_from_Urls', methods=['POST'])
def predictface():
    data = request.json
    url1 = data['url1']
    # get URL of first image from form data
    url2 = data['url2']

    # Read the first image from URL using requests library
    img1 = cv2.imdecode(np.frombuffer(requests.get(
        url1).content, np.uint8), cv2.IMREAD_COLOR)

    # Download the second image from the URL
    with urllib.request.urlopen(url2) as url:
        s = url.read()
    img2 = cv2.imdecode(np.frombuffer(s, np.uint8), cv2.IMREAD_COLOR)

    # Convert the images to grayscale
    gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Detect faces in the images
    faces1 = face_cascade.detectMultiScale(
        gray_img1, scaleFactor=1.1, minNeighbors=5)
    faces2 = face_cascade.detectMultiScale(
        gray_img2, scaleFactor=1.1, minNeighbors=5)

    # Compare only the first detected face in each image
    if len(faces1) > 0 and len(faces2) > 0:
        x1, y1, w1, h1 = faces1[0]
        x2, y2, w2, h2 = faces2[0]

        # Extract the face regions from the images
        face1 = gray_img1[y1:y1+h1, x1:x1+w1]
        face2 = gray_img2[y2:y2+h2, x2:x2+w2]

        # Resize the face regions to the same dimensions
        resized_face1 = cv2.resize(face1, (face2.shape[1], face2.shape[0]))

        # Calculate the structural similarity index between the face regions
        score = ssim(resized_face1, face2, full=True)[0]

        # Convert the similarity score to a percentage
        similarity_percentage = score * 100

        # Return the similarity percentage in a JSON response
        return jsonify({'similarity_percentage': similarity_percentage})

    else:
        return jsonify({'similarity_percentage': 'Could not detect faces in both images.'})


if __name__ == '__main__':
    app.run(debug=False)
