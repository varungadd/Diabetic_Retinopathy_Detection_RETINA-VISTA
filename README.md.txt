# Diabetic Retinopathy Detection

## Overview
This project aims to develop a robust diabetic retinopathy detection system by utilizing deep learning models. We've created four Jupyter notebooks (V1, V2, V3, V4) during the development phase, with V4 being identified as the most effective.

## Notebooks
- **V1**: Initial experiments with basic model architectures.
- **V2**: Introduction of more complex model structures and initial preprocessing techniques.
- **V3**: Enhancement with advanced image preprocessing.
- **V4**: Comprehensive application of preprocessing techniques such as normal preprocessing, green channel extraction, vessel segmentation, and a combined approach. This version has shown to be the most effective in identifying diabetic retinopathy.

## Models
The project includes multiple trained models to handle different aspects of image analysis:
- **CNN**: A convolutional neural network that serves as the baseline model.
- **Green Channel Model**: A model that specifically processes the green channel of retinal images to highlight certain features.
- **Vessel Model**: Focuses on extracting blood vessels from retinal images for detailed analysis.
- **Combined Model**: Integrates inputs from multiple preprocessing methods for a comprehensive analysis.

## Dataset
The dataset used in this project can be accessed [here](#dataset-source-link).

## Running the Application
The project also features a web application that allows users to upload retinal images and receive immediate predictions. Follow the instructions below to set up and run the application on your local machine:
1. Clone the repository: `git clone <repository-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`

Visit `http://127.0.0.1:5000` in your web browser to interact with the application.

## Contribution
Feel free to contribute to this project by making a pull request or suggesting improvements via issues.
