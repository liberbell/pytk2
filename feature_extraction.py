from pathlib import Path
import numpy as np
import joblib
from keras.preprocessing import image
from keras.applications import vgg16


dog_path = Path('training_data') / 'dogs'
not_dog_path = Path('training_data') / 'not_dogs'
