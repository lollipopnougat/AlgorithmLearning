import tensorflow as tf
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras import layers, models



class Bp:
    def __init__(self):
        model = models.Sequential()
        model.add(layers.Dense(32, activation='relu'))
        model.add(layers.Dense(16, activation='relu'))
        model.add(layers.Dense(10, activation='softmax'))
        #model.build(input_shape = [None, 784])
        #model.summary()
        self.model = model
    