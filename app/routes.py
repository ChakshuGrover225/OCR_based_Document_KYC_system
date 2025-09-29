from flask import request, jsonify, render_template
import os
from werkzeug.utils import secure_filename
from app import flask_app                   # updated import
from app.preprocessing import preprocess_image
from app.inference import run_inference




#UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploaded_images')
UPLOAD_FOLDER = os.path.join("", 'uploaded_images')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS






@flask_app.route('/')
def home():
    return render_template('homepage.html')






@flask_app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)  # temporarily save
        print(f"File saved to {file_path}")

        preprocess_image_path = preprocess_image(file_path)
        results = run_inference(preprocess_image_path)

        #os.remove(file_path)  # clean up temp file

        # Render new template with uploaded filename
        return render_template('predict.html', filename=file_path, inference_data="fake result")

    return "Invalid file type", 400
