from pathlib import Path
import numpy as np
import joblib
from keras.preprocessing import image
from keras.applications import vgg16


dog_path = Path('training_data') / 'dogs'
not_dog_path = Path('training_data') / 'not_dogs'

images = []
labels = []

for img in not_dog_path.glob('*.ong'):
    img = image.load_img(img)

    image_array = image.img_to_array(img)
    images.append(image_array)

    labels.append(0)

for img in dog_path.glob('*.png'):
    img = image.load_img(img)
