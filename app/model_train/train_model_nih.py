import os
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import EfficientNetB0

# Configurations
BATCH_SIZE = 64 
EPOCHS = 25
IMG_SIZE = (224, 224)
MODEL_PATH = "chest_xray_model.keras"
CSV_FILE = "Data_Entry_2017.csv"
IMG_DIR = "NIH_CHEST_XRAY"

# Load Data
df = pd.read_csv(CSV_FILE).iloc[:30000]
df["Image Index"] = df["Image Index"].apply(lambda x: os.path.join(IMG_DIR, x))

# Handle labels
all_labels = df["Finding Labels"].str.split("|").explode().unique()
all_labels = [label for label in all_labels if label != "No Finding"]
label_map = {label: i for i, label in enumerate(sorted(all_labels))}
df["Target"] = df["Finding Labels"].apply(lambda labels: np.array([1.0 if lbl in labels.split("|") else 0.0 for lbl in label_map]))

# Remove missing images
df = df[df["Image Index"].apply(os.path.exists)]

# Create Dataset
def load_image(path, label):
    img = tf.io.read_file(path)
    img = tf.image.decode_jpeg(img, channels=3)
    img = tf.image.resize(img, IMG_SIZE)
    img = tf.keras.applications.efficientnet.preprocess_input(img)
    return img, label

dataset = tf.data.Dataset.from_tensor_slices((df["Image Index"].values, np.stack(df["Target"].values)))
dataset = dataset.map(load_image, num_parallel_calls=tf.data.AUTOTUNE)
dataset = dataset.shuffle(30000).batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)

train_size = int(0.8 * len(df))
train_ds = dataset.take(train_size)
val_ds = dataset.skip(train_size)

# Build Model
def create_model():
    base_model = EfficientNetB0(include_top=False, input_shape=(224, 224, 3), weights="imagenet")
    base_model.trainable = False  # Freeze first for faster training

    x = layers.GlobalAveragePooling2D()(base_model.output)
    x = layers.Dense(256, activation="relu")(x)
    x = layers.Dropout(0.3)(x)
    output = layers.Dense(len(label_map), activation="sigmoid")(x)

    model = models.Model(inputs=base_model.input, outputs=output)
    model.compile(optimizer=tf.keras.optimizers.AdamW(learning_rate=1e-4),  # AdamW for speed
                  loss="binary_crossentropy",
                  metrics=[tf.keras.metrics.AUC(name="AUC")])
    return model

if os.path.exists(MODEL_PATH):
    print("Loading saved model...")
    model = tf.keras.models.load_model(MODEL_PATH)
else:
    model = create_model()

# Train (Warm-up)
model.fit(train_ds, validation_data=val_ds, epochs=5)

# Fine-tune (Unfreeze EfficientNet)
model.trainable = True
model.compile(optimizer=tf.keras.optimizers.AdamW(learning_rate=1e-5), loss="binary_crossentropy", metrics=["accuracy", tf.keras.metrics.AUC(name="AUC")])
model.fit(train_ds, validation_data=val_ds, epochs=20)

# Save Model
model.save(MODEL_PATH)