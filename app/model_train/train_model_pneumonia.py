# filepath: /home/mahima/Desktop/AI-Powered-Early-Disease-Prediction-System/src/train_model_pneumonia.py
"""
Author: Patan Musthakheem
Date & Time: 2025-03-18 17:16
Description: This file contains the class for training the model for Pneumonia detection
"""

from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Flatten, Dropout
class TrainPneumoniaModel:
    def __init__(self, train_data_path, validation_data_path, epchos=10):
        self.train_data_path = train_data_path
        self.validation_data_path = validation_data_path
        self.epochs = epchos

    def load_data(self):
        """Load data from the directory"""
        train_datagen = self._train_data_generator()
        val_datagen = self._test_data_generator()

        self.train_generator = train_datagen.flow_from_directory(self.train_data_path, target_size=(224, 224), batch_size=32, class_mode='binary')
        self.val_generator = val_datagen.flow_from_directory(self.validation_data_path, target_size=(224, 224), batch_size=32, class_mode='binary')


    def _train_data_generator(self):
        """Rescaling the data and flipping to make it align to model"""
        return ImageDataGenerator(rescale=1./255,
                                rotation_range=15,
                                zoom_range=0.1,
                                horizontal_flip=True)

    def _test_data_generator(self):
        return ImageDataGenerator(rescale=1./255)

    def create_model(self):
        base_model = EfficientNetB0(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
        base_model.trainable = False  # Keep most layers frozen
        
        x = Flatten()(base_model.output)
        x = Dense(256, activation='relu')(x)
        x = Dropout(0.5)(x)
        x = Dense(1, activation='sigmoid')(x)  # Binary classification

        self.model = Model(inputs=base_model.input, outputs=x)
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        # Unfreeze last 20 layers after compiling
        for layer in base_model.layers[-20:]:
            layer.trainable = True
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

            

    def train_model(self):
        self.model.fit(self.train_generator, 
                       validation_data=self.val_generator, 
                       epochs=self.epochs)
    

    def save_model(self):
        self.model.save("xray_diagnosis_model.h5")


if __name__ == "__main__":
    train_data_dir = 'Dataset/train'
    validation_data_dir = 'Dataset/val'
    trainer = TrainPneumoniaModel(train_data_dir, validation_data_dir)
    trainer.load_data()
    trainer.create_model()
    trainer.train_model()
    trainer.save_model()
