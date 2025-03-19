"""
Author: Patan Musthakheem
Date: 2021-10-10
Description: This file contains the class for loading the huge dataset of NIH X-Ray images
             for 14 diseases Parallely by utilizing power of multiprocessing 
"""

import os
import multiprocessing.pool
import numpy as np

class LoadPneumoniaDataset:
    """Class for Loading the Huge X-Ray/MRI images for NIH data parallely"""
    def __init__(self):
        pass

    def _load_image(self, path):
        """Function for loading a image from the given path"""
        pass

    def _transform_image(self, image):
        """This is used to transform the image so it can be feeded to the EfficientNetb0 neural network"""
        pass

    

    def load_nih_data(self):
        """Used to load the whole dataset from the given path"""
        pass

