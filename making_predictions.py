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

list_of_images = np.expand_dims(image_to_test, axis=0)

results = model.predict(list_of_images)
single_result = results[0]

mostly_likely_class_index = int(np.argmax(single_result))
class_likelihood = single_result[mostly_likely_class_index]

class_label = class_labels[mostly_likely_class_index]
print('This is image is a {} - Likeihood: {:2f}'.format(class_label, class_likelihood))
