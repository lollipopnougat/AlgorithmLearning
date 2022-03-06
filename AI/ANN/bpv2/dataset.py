import numpy as np
import gzip
import tensorflow as tf

train_images_file_name = 'train-images-idx3-ubyte.gz'
train_labels_file_name = 'train-labels-idx1-ubyte.gz'
test_images_file_name = 't10k-images-idx3-ubyte.gz'
test_labels_file_name = 't10k-labels-idx1-ubyte.gz'


class MnistDataset:
    def __init__(self, folder: str) -> None:
        self.tr_images, self.tr_labels = MnistDataset.load_training_data(
            folder)
        self.te_images, self.te_labels = MnistDataset.load_testing_data(folder)

    @staticmethod
    def load_training_data(folder: str):
        with gzip.open(f'{folder}/{train_labels_file_name}', 'rb') as lbpath:
            train_labels = np.frombuffer(lbpath.read(), np.uint8, offset=8)
        with gzip.open(f'{folder}/{train_images_file_name}', 'rb') as imgpath:
            train_images = np.frombuffer(imgpath.read(), np.uint8,
                                         offset=16).reshape(
                                             len(train_labels), 784)
        return train_images, train_labels

    @staticmethod
    def load_testing_data(folder: str):
        with gzip.open(f'{folder}/{test_labels_file_name}', 'rb') as lbpath:
            test_labels = np.frombuffer(lbpath.read(), np.uint8, offset=8)
        with gzip.open(f'{folder}/{test_images_file_name}', 'rb') as imgpath:
            test_images = np.frombuffer(imgpath.read(), np.uint8,
                                        offset=16).reshape(
                                            len(test_labels), 784)
        return test_images, test_labels

    @staticmethod
    def load_training_data_oh(folder: str):
        with gzip.open(f'{folder}/{train_labels_file_name}', 'rb') as lbpath:
            train_labels = np.frombuffer(lbpath.read(), np.uint8, offset=8)
        with gzip.open(f'{folder}/{train_images_file_name}', 'rb') as imgpath:
            train_images = np.frombuffer(imgpath.read(), np.uint8,
                                         offset=16).reshape(
                                             len(train_labels), 784)
        return train_images, tf.one_hot(train_labels, 10, dtype=tf.uint8)

    @staticmethod
    def load_testing_data_oh(folder: str):
        with gzip.open(f'{folder}/{test_labels_file_name}', 'rb') as lbpath:
            test_labels = np.frombuffer(lbpath.read(), np.uint8, offset=8)
        with gzip.open(f'{folder}/{test_images_file_name}', 'rb') as imgpath:
            test_images = np.frombuffer(imgpath.read(), np.uint8,
                                        offset=16).reshape(
                                            len(test_labels), 784)
        return test_images, tf.one_hot(test_labels, 10, dtype=tf.uint8)

    def next_batch(self, batch_sz):
        rand = np.random.randint(0, 60000, batch_sz)
        return self.tr_images[rand], self.tr_labels[rand]

    def get_test_batch(self, batch_sz):
        rand = np.random.randint(0, 10000, batch_sz)
        return self.te_images[rand], self.te_labels[rand]