import os

print("DEBUG: SQLALCHEMY_DATABASE_URI =", os.environ.get("SQLALCHEMY_DATABASE_URI"))

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "postgresql://postgres:natiss_natiss@localhost:5432/mdcan_bdm")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}

