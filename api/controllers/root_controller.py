from utils.handle_error import handle_error
from app import app

# Función controladora
@app.route("/")
@handle_error
def root():
    return {
        "message":"welcome to Friends Recognition API"
    }

