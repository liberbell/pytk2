import numpy as np
from keras.preprocessing import image
from keras.applications import vgg16

model = vgg16.VGG16()

img = image.load_img('bay.jpg', target_size=(224, 224))

x = image.img_to_array(img)

x = np.expand_dims(x, axis=0)

x =

predictions =

predected_clases =

print('Top predictions for thsi images:')
