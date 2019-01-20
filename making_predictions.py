from keras.models import model_from_json
from pathlib import Path
from keras.preprocessing import image
import numpy as np

class_labels = [
    'Plane',
    'Car',
    'Bird',
    'Cat',
    'Deer',
    'Dog',
    'Frog',
    'Horse',
    'Boat',
    'Truck'
]
