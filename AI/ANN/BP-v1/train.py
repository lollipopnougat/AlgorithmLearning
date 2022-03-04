import numpy as np
import matplotlib.pyplot as plt
import gzip
import tensorflow as tf
from network import Network
from dataset import MnistDataset

train_images_file_name = 't10k-images-idx3-ubyte.gz'
train_labels_file_name = 't10k-labels-idx1-ubyte.gz'

lr = 0.001
batch_size = 128




mnist_folder = './mnist'

#mnist = input_data.read_data_sets(mnist_folder, one_hot=True)

mnist = MnistDataset(mnist_folder)

#train_images, train_labels = load_data(mnist_folder)

# train_nums = mnist.train.num_examples
# validation_nums = mnist.validation.num_examples
# test_nums = mnist.test.num_examples
# print(f'MNIST训练数据集个数 {train_nums}')
# print(f'MNIST验证数据集个数 {validation_nums}')
# print(f'MNIST测试数据集个数 {test_nums}')

#print(f'images shape = {train_images.shape}, labels shape = {train_labels.shape}')

#print(train_labels[0])
#img1 = train_images[0].reshape(28, 28)
#plt.imshow(img1)
#plt.show()

OPT = tf.train.RMSPropOptimizer(lr, name='RMSProp')
net = Network(OPT)
sess = tf.Session()
writer = tf.summary.FileWriter("logs/", sess.graph)
sess.run(tf.global_variables_initializer())
sess.run(tf.local_variables_initializer())
saver = tf.train.Saver() 
for i in range(3000):
    rimg, rlabel = mnist.next_batch(batch_size)
    _label = tf.one_hot(rlabel, depth=10, dtype=tf.uint8)
    label = sess.run(_label)
    loss, acc, ms = net.train_one_step(
        sess, rimg, label)
    writer.add_summary(ms, i)
    if i % 100 == 0:
        print(f'No.{i} loss = {loss}, accuracy = {acc}')

saver.save(sess, 'save/model.ckpt')
te_img, te_lab = mnist.get_test_batch(batch_size)
#te_label = tf.one_hot(te_lab, depth=10, dtype=tf.uint8)
label = sess.run(_label)
res = net.get_output(sess, te_img)
predict = np.equal(res, te_lab)
            # reduce_mean即求predict的平均数 即 正确个数 / 总数，即正确率
accuracy = np.mean(predict.astype(np.int))
print(f'test accuracy = {accuracy}')
sess.close()