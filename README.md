# 🌱 LeafScan AI – Plant Disease Detection System

An AI-powered plant disease detection web application that uses a Convolutional Neural Network (CNN) to identify plant diseases from leaf images.

## 🚀 Features

- 🌿 Plant disease detection from leaf images
- 🤖 CNN-based image classification
- 📊 Prediction confidence score
- 🩺 Disease severity classification
- 💊 Recommended treatment/medicine
- 🌱 Farmer care tips
- 🔊 Voice output for detected disease
- 🖥️ Flask-based web application

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- Convolutional Neural Network (CNN)
- Flask
- NumPy
- Pillow
- pyttsx3
- HTML
- CSS

## 🌿 Supported Plant Conditions

The model supports classification of:

- Pepper Bell – Bacterial Spot
- Pepper Bell – Healthy
- Potato – Early Blight
- Potato – Healthy
- Potato – Late Blight
- Tomato – Target Spot
- Tomato – Bacterial Spot
- Tomato – Early Blight
- Tomato – Healthy
- Tomato – Late Blight

## 📂 Project Structure

```text
Leaf-Scan-AI/
│
├── static/
├── templates/
│   ├── home.html
│   ├── detect.html
│   ├── index.html
│   └── show_image.html
│
├── app.py
├── train.py
├── requirements.txt
├── README.md
└── .gitignore
