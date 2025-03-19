"""
Author: Patan Musthakheem
Date: 2021-10-10
Description: This file contains the class for loading the huge dataset of X-Ray images
             for Pneumonia Parallely by utilizing power of multiprocessing
"""

import os
import multiprocessing
import numpy as np

multiprocessing.set_start_method(method="fork", force=True) # Forcing to use fork


class LoadPneumoniaDataset:
    """Class for Loading the Huge X-Ray/MRI images for Pneumonia detection Paralley"""
    def __init__(self, path):
        self.path = os.path.abspath(path)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Path {path} does not exists")


    def _load_image(self, path):
        """Function for loading a image from the given path"""
        pass

    def _transform_image(self, image):
        """This is used to transform the image so it can be feeded to the EfficientNetb0 neural network"""
        pass

    def _load_labels(self, label):
        labels = np.array()
        # TODO: give labels for the disease 
        return labels

    def load_pneumonia_data(self):
        """Used to load the whole dataset from the given path"""
        pass

