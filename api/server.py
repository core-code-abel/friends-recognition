from app import app
import os

PORT = os.getenv('PORT', 5000)

import controllers.root_controller
import controllers.recognize_face_controller

app.run("0.0.0.0", PORT)