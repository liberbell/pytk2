import keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
