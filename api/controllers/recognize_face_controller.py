from os import closerange
from utils.handle_error import handle_error
from app import app
from flask import request
import face_recognition
import base64
from PIL import Image
from io import BytesIO

# Función controladora
@app.route("/process-image", methods=['POST'])
@handle_error
def process_image():
    image = request.get_json().get('image').replace('data:image/png;base64,', '')
    print(image)
    print('*'*50)
    faces = get_faces(image)
    print(faces)
    return {
        "message":"welcome to Friends Recognition API"
    }


def get_faces(b64_image):
    with open("imageToSave.jpg", "wb") as fh:
        fh.write(base64.decodebytes(b64_image))
    image = face_recognition.load_image_file('imageToSave.jpg')
    print(image)
    # face_locations = face_recognition.face_locations(image)
    # faces = []
    # for i, face in enumerate(face_locations):
    #     top, right, bottom, left = face
    #     faces.append(image[top:bottom, left:right])
    # return faces