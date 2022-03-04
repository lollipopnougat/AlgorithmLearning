import tensorflow as tf
from dataset import MnistDataset
from tensorflow.keras import models

model = models.load_model('./save/model.h5')

test_images, test_labels = MnistDataset.load_testing_data_oh('./mnist')

_, test_acc = model.evaluate(test_images, test_labels, batch_size=128, steps=78)
print("准确率: %.4f，共测试了%d张图片 " % (test_acc, len(test_labels)))