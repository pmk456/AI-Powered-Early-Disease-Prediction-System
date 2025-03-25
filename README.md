# AI-Powered Early Disease Prediction System  

## Overview  
Designed specifically for healthcare professionals and researchers, our AI-Powered Early Disease Prediction System leverages state-of-the-art deep learning techniques—featuring the EfficientNetB0 architecture—to analyze patient symptoms and predict potential diseases at an early stage. This decision-support tool is intended to complement clinical judgment by providing timely, data-driven insights that can assist in early intervention and improve patient outcomes.


## Features  
- **AI-Powered Predictions** – Uses a deep learning model for accurate disease detection.  
- **Easy-to-Use Interface** – A simple web UI for entering symptoms.  
- **Multi-Disease Support** – Covers a variety of illnesses for early alerts.  
- **Fast & Efficient** – Quick results based on pre-trained models.  
- **Privacy-Focused** – No sensitive data storage or tracking.  

## Tech Stack  
- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **Machine Learning:** TensorFlow, Scikit-learn, **EfficientNetB0**  
- **APIs:** Custom API for disease prediction  

## How the AI Works  
We use **EfficientNetB0**, a lightweight yet powerful deep learning model, trained on medical datasets to predict diseases based on symptoms.  
**Key Training Details:**  
-  **Dataset:** NIH Chest X-Ray
-  **Preprocessing:** Normalization, augmentation  
-  **Evaluation Metrics:** Accuracy, Precision, Recall, F1-score  

## 📂 Project Structure  
### 🛠 Explanation:  
- **`model_train/`** → Training Files
- **`models/`** → Stores trained ML models.  
- **`static/`** → Contains CSS, JavaScript, and images for the frontend.  
- **`templates/`** → Holds HTML files for the user interface.  
- **`api.py`** → API for predicting disease from given X-Ray
- **`chat.py`** → LLM API
- **`requirements.txt`** → Lists dependencies.  
- **`.gitignore`** → Prevents unnecessary files from being committed.
- ** run ** → Starting Point

## Installation & Setup  
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/pmk456/AI-Powered-Early-Disease-Prediction-System.git
cd AI-Powered-Early-Disease-Prediction-System
```
## Create a Virtual Environment (Optional, But Recommended)
```bash
python -m venv venv
source venv/bin/activate
```
## Install all Required Dependencies
```bash
pip install -r requirements.txt
```
## Run the Application
```bash
export API_TOKEN=openai-token
python run.py
```
## Open in Browser
 **http://localhost:5000
