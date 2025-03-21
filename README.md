# 🏥 AI-Powered Early Disease Prediction System  

## 🚀 Overview  
Ever wondered if AI could give you early insights into your health? This **AI-Powered Early Disease Prediction System** does exactly that! Using **EfficientNetB0** and machine learning, it analyzes symptoms and predicts potential diseases—helping you take early action before visiting a doctor.  

## 🔥 Features  
- ✅ **AI-Powered Predictions** – Uses a deep learning model for accurate disease detection.  
- 🎨 **Easy-to-Use Interface** – A simple web UI for entering symptoms.  
- 🌍 **Multi-Disease Support** – Covers a variety of illnesses for early alerts.  
- ⚡ **Fast & Efficient** – Quick results based on pre-trained models.  
- 🔐 **Privacy-Focused** – No sensitive data storage or tracking.  

## 🏗️ Tech Stack  
- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **Machine Learning:** TensorFlow, Scikit-learn, **EfficientNetB0**  
- **APIs:** Custom API for disease prediction  

## 🤖 How the AI Works  
We use **EfficientNetB0**, a lightweight yet powerful deep learning model, trained on medical datasets to predict diseases based on symptoms.  
**Key Training Details:**  
- 📊 **Dataset:** Medical records & symptom-based data  
- 🔧 **Preprocessing:** Normalization, augmentation  
- 🎯 **Evaluation Metrics:** Accuracy, Precision, Recall, F1-score  

## 📂 Project Structure  
### 🛠 Explanation:  
- **`data/`** → Holds the dataset for training.  
- **`models/`** → Stores trained ML models.  
- **`static/`** → Contains CSS, JavaScript, and images for the frontend.  
- **`templates/`** → Holds HTML files for the user interface.  
- **`app/`** → Core application logic, including:  
  - `app.py` → Main Flask application.  
  - `model.py` → Defines and loads the ML model. 
  - `routes.py` → API endpoints and Flask routes.  
- **`requirements.txt`** → Lists dependencies.  
- **`.gitignore`** → Prevents unnecessary files from being committed.  
- ** run ** → Starting Point

## 🛠️ Installation & Setup  
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
python run.py
```
## Open in Browser
 ** http://localhost:5000
