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

f = Path('model_structure.json')
model_structure= f.read_text()

model = model_from_json(model_structure)
