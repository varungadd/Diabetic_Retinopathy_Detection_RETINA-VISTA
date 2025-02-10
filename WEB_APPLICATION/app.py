from flask import Flask, request, render_template, url_for
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os

app = Flask(__name__, static_folder='static')



UPLOAD_FOLDER = r'C:\Users\spars\Desktop\SEM 5\AIOT\Diabetic_Retinopathy_Detection_Project\Diabetic_Retinopathy_Detection_RETINA-VISTA\WEB_APPLICATION\static\uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model_path = r'C:\Users\spars\Desktop\SEM 5\AIOT\Diabetic_Retinopathy_Detection_Project\Diabetic_Retinopathy_Detection_RETINA-VISTA\Models\Diabetic_retinopathy_cnn.keras'
model = load_model(model_path)

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            image = preprocess_image(file_path)
            predictions = model.predict(image)
            prediction = np.argmax(predictions, axis=1)[0]
            labels = ['No DR', 'Mild', 'Moderate', 'Proliferate DR', 'Severe']
            recommendation = get_recommendation(prediction)

            return render_template('result.html', image_url=url_for('static', filename='uploads/' + filename), prediction=labels[prediction], recommendation=recommendation)
    return render_template('upload.html')
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        # Process the feedback data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Here you can add code to save the feedback to a database or send an email
        return render_template('thank_you.html', name=name)  # Thank you page after submitting feedback
    return render_template('feedback.html')
@app.route('/methodology')
def methodology():
    return render_template('methodology.html')

def get_recommendation(prediction):
    recommendations = {
        0: "No diabetic retinopathy detected. Regular check-up advised.",
        1: "Mild diabetic retinopathy. Consider consulting an ophthalmologist.",
        2: "Moderate diabetic retinopathy. Medical attention recommended soon.",
        3: "Proliferative diabetic retinopathy. Seek immediate medical care.",
        4: "Severe diabetic retinopathy. Urgent medical treatment required."
    }
    return recommendations.get(prediction, "Check-up advised.")

if __name__ == '__main__':
    app.run(debug=True)
