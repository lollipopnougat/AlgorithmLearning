import tensorflow as tf
from dataset import MnistDataset
from tensorflow.keras import models
import matplotlib.pyplot as plt

model = models.load_model('./save/model.h5')

test_images, test_labels = MnistDataset.load_testing_data_oh('./mnist')

mnist_folder = './mnist'
mnist = MnistDataset(mnist_folder)

timg, tlab = mnist.get_test_batch(10)

res = model.predict(timg, batch_size=10)
pre = tf.argmax(res, 1)

fig, ax = plt.subplots(2, 5)
ax = ax.flatten()

for j in range(10):
    img = timg[j].reshape(28, 28)
    ax[j].imshow(img, cmap='Greys')
    ax[j].set_title(f'p: {pre[j]}, r: {tlab[j]}')

plt.tight_layout()
plt.show()
