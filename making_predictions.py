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
model.load_weight('model_weights.h5')

img = image.load_img('cat.png', target_size=(32, 32))
image_to_test = image.image_to_array(img)
