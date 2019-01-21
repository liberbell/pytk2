import numpy as np
from keras.preprocessing import image
from keras.applications import vgg16

model = vgg16.VGG16()

img = image.load_img('bay.jpg', target_size=(224, 224))

x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = vgg16.preprocess_input(x)

predictions = model.predict(x)
predected_clases = vgg16.decode_predictions(predictions, top=9)

print('Top predictions for thsi images:')

for imagenet_id, name, likehood in predected_clases[0]:
    print('Predicton: {} - {:2f}'.format(name, likehood))
