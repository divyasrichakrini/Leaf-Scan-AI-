from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image
import pyttsx3

app = Flask(__name__)

# Load model
model = tf.keras.models.load_model("plant_model.h5")

# Disease Classes
class_names = [
    "Pepper__bell___Bacterial_spot",
    "Pepper__bell___healthy",
    "Potato___Early_blight",
    "Potato___healthy",
    "Potato___Late_blight",
    "Tomato_Target_Spot",
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_healthy",
    "Tomato_Late_blight"
]

# Disease Information
disease_info = {

    "Pepper__bell___Bacterial_spot": {
        "description": "Bacterial spot causes dark lesions on leaves and fruits.",
        "solution": "Remove infected leaves and use copper-based bactericides.",
        "severity": "Medium",
        "medicine": "Copper Fungicide Spray",
        "tip": "Avoid overhead watering and keep leaves dry."
    },

    "Pepper__bell___healthy": {
        "description": "The plant is healthy.",
        "solution": "Maintain proper watering and sunlight.",
        "severity": "Low",
        "medicine": "No medicine needed",
        "tip": "Continue regular monitoring for healthy growth."
    },

    "Potato___Early_blight": {
        "description": "Early blight is a fungal disease causing brown spots.",
        "solution": "Apply fungicides and remove affected leaves.",
        "severity": "Medium",
        "medicine": "Chlorothalonil Fungicide",
        "tip": "Ensure proper airflow around plants."
    },

    "Potato___healthy": {
        "description": "The potato plant is healthy.",
        "solution": "Maintain proper care and nutrition.",
        "severity": "Low",
        "medicine": "No medicine needed",
        "tip": "Keep soil nutrient-rich and monitor regularly."
    },

    "Potato___Late_blight": {
        "description": "Late blight spreads rapidly in cool and wet conditions.",
        "solution": "Remove infected plants immediately and apply fungicides.",
        "severity": "High",
        "medicine": "Mancozeb Fungicide",
        "tip": "Avoid excessive moisture around crops."
    },

    "Tomato_Target_Spot": {
        "description": "Target spot creates circular lesions on tomato leaves.",
        "solution": "Use suitable fungicides and prune affected leaves.",
        "severity": "Medium",
        "medicine": "Azoxystrobin Spray",
        "tip": "Maintain field cleanliness."
    },

    "Tomato_Bacterial_spot": {
        "description": "Bacterial spot causes dark water-soaked spots.",
        "solution": "Use copper sprays and remove infected leaves.",
        "severity": "Medium",
        "medicine": "Copper Bactericide",
        "tip": "Do not handle wet plants."
    },

    "Tomato_Early_blight": {
        "description": "Early blight affects older tomato leaves first.",
        "solution": "Use fungicides and remove infected parts.",
        "severity": "Medium",
        "medicine": "Neem Oil Spray",
        "tip": "Provide enough spacing between plants."
    },

    "Tomato_healthy": {
        "description": "The tomato plant is healthy.",
        "solution": "Continue regular maintenance.",
        "severity": "Low",
        "medicine": "No medicine needed",
        "tip": "Monitor plant growth regularly."
    },

    "Tomato_Late_blight": {
        "description": "Late blight causes dark lesions and rapid decay.",
        "solution": "Remove infected leaves and apply fungicides quickly.",
        "severity": "High",
        "medicine": "Metalaxyl Fungicide",
        "tip": "Reduce humidity and avoid overwatering."
    }
}

# Home Page
@app.route("/")
def home():
    return render_template("home.html")


# Detection Page
@app.route("/detect", methods=["GET", "POST"])
def detect():

    prediction = ""
    img_path = ""
    confidence = ""
    details = {}
    status = ""

    if request.method == "POST":

        file = request.files["file"]

        if file:

            img_path = "static/" + file.filename
            file.save(img_path)

            # Image Processing
            img = Image.open(img_path)
            img = img.resize((224, 224))
            img = np.array(img) / 255.0
            img = np.expand_dims(img, axis=0)

            # Prediction
            pred = model.predict(img)

            raw_prediction = class_names[np.argmax(pred)]

            prediction = raw_prediction.replace("___", " ").replace("__", " ").replace("_", " ")

            confidence = round(np.max(pred) * 100, 2)

            details = disease_info[raw_prediction]

            # Healthy or Diseased
            if "healthy" in raw_prediction.lower():
                status = "Healthy Plant"
            else:
                status = "Diseased Plant"

            # Voice Output
            try:
                engine = pyttsx3.init()
                engine.say(f"Detected disease is {prediction}")
                engine.runAndWait()
            except:
                pass

    return render_template(
        "detect.html",
        prediction=prediction,
        img_path=img_path,
        confidence=confidence,
        details=details,
        status=status
    )


if __name__ == "__main__":
    app.run(debug=True)