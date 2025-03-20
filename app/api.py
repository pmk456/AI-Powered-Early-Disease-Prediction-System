import tensorflow as tf
from PIL import Image
from io import BytesIO
import numpy as np

IMG_SIZE = (224, 224)

MODEL_PATH = "app/models/chest_xray_model.keras"

class XRayPredictor:
    def __init__(self):
        self.model = tf.keras.models.load_model(MODEL_PATH)

    def predict(self, image_bytes):
        transformed_image = self._transform_image(image_bytes)
        if transformed_image is None:
            return {"error": "Error processing image"}

        predictions = self.model.predict(transformed_image)[0]  # Get first (and only) prediction
        all_labels = [
            "Atelectasis", "Cardiomegaly", "Consolidation", "Edema", "Effusion",
            "Emphysema", "Fibrosis", "Hernia", "Infiltration", "Mass",
            "Nodule", "Pleural_Thickening", "Pneumonia", "Pneumothorax"
        ]
        predicted_labels = [all_labels[i] for i in np.where(predictions > 0.5)[0]]

        return {
            "prediction": predicted_labels if predicted_labels else ["No Disease Detected"]
        }

    def _transform_image(self, image_bytes):
        try:
            img = Image.open(BytesIO(image_bytes)).convert("RGB")  # Convert to RGB
            img = img.resize(IMG_SIZE)  # Resize to match model input
            img_array = np.array(img, dtype=np.float32)
            img_array = tf.keras.applications.efficientnet.preprocess_input(img_array)  # Normalize
            img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
            return img_array
        except Exception as e:
            print(f"Error processing image: {e}")
            return None

if __name__ == "__main__":
    predictor = XRayPredictor()
    image_bytes = open("model_train/NIH_CHEST_XRAY/00000001_002.png", "rb").read()
    result = predictor.predict(image_bytes)
    print("Prediction:", result)
