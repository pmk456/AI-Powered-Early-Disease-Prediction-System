import flask, os
from flask import request
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
app = flask.Flask("app")

@app.route("/upload-xray", methods=["POST"])
def process_xray():
    image_file = request.files['file']
    file_name = image_file.filename
    image_file.save(file_name)
    return predict(file_name)

def load_image(path):
    img = image.load_img(path, target_size=(224, 224), color_mode='rgb')
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def predict(path):
    transformed_image = load_image(path)
    model = load_model("xray_diagnosis_model.h5")
    pred = model.predict(transformed_image)[0][0]
    if pred > 0.5:
        return "Pneumonia"
    else:
        return "Normal"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1234)
