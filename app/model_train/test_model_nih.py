import os
import numpy as np
import tensorflow as tf
import pandas as pd

# Configurations
MODEL_PATH = "../models/chest_xray_model.keras"
IMG_SIZE = (224, 224)

# Load the saved model
model = tf.keras.models.load_model(MODEL_PATH)
print("✅ Model Loaded Successfully!")

# Load Global Labels to avoid mapping errors
all_labels = pd.read_csv("Data_Entry_2017.csv")["Finding Labels"].str.split("|").explode().unique()
all_labels = [label for label in all_labels if label != "No Finding"]
label_map = {i: label for i, label in enumerate(sorted(all_labels))}

# Load Test Data
df = pd.read_csv("Data_Entry_2017.csv").iloc[0:2000]
df["Image Index"] = df["Image Index"].apply(lambda x: os.path.join("NIH_CHEST_XRAY", x))
df = df[df["Image Index"].apply(os.path.exists)]  # Remove missing files

# Ensure valid test dataset
if df.empty:
    raise ValueError("❌ No valid test images found! Check dataset paths.")

# Function to preprocess images safely
def preprocess_image(img_path):
    try:
        img = tf.io.read_file(img_path)
        img = tf.image.decode_jpeg(img, channels=3)
        img = tf.image.resize(img, IMG_SIZE)
        img = tf.keras.applications.efficientnet.preprocess_input(tf.cast(img, tf.float32))
        return img.numpy()
    except Exception as e:
        print(f"❌ Error processing {img_path}: {e}")
        return np.zeros((*IMG_SIZE, 3), dtype=np.float32)  # Blank image for safety

# Prepare dataset
test_images = np.array([preprocess_image(img_path) for img_path in df["Image Index"]], dtype=np.float32)

# Validate image shape before prediction
if test_images.shape[1:] != (224, 224, 3):
    raise ValueError(f"❌ Image shape mismatch! Expected (224, 224, 3), got {test_images.shape[1:]}")

# Make predictions
predictions = model.predict(test_images)

# Interpret results
for i, pred in enumerate(predictions):
    predicted_labels = [label_map[j] for j in np.where(pred > 0.5)[0]]
    print(f"🩻 Image {df.iloc[i]['Image Index']} --> Predicted: {predicted_labels if predicted_labels else 'No Disease Detected'}")
