import tensorflow as tf
from dataset import MnistDataset
import matplotlib.pyplot as plt
# from tensorflow.python import pywrap_tensorflow
import numpy as np
saver = tf.train.import_meta_graph('save/model.ckpt.meta')
mnist_folder = './mnist'

# reader = pywrap_tensorflow.NewCheckpointReader('save/model.ckpt')
# var_to_shape_map = reader.get_variable_to_shape_map()
# for key in var_to_shape_map:
#     print('tensor_name: ', key)
#print(reader.get_tensor(key))
mnist = MnistDataset(mnist_folder)

with tf.Session() as sess:
    saver.restore(sess, './save/model.ckpt')
    graph = tf.get_default_graph()
    input_node = graph.get_tensor_by_name('input/img-input:0')
    output_node = graph.get_tensor_by_name('net/Layer3/Softmax:0')
    for i in range(10):
        timg, tlab = mnist.get_test_batch(10)
        raw_res = sess.run(output_node, {input_node: timg})
        r_res = tf.argmax(raw_res, 1)
        res = sess.run(r_res)
        predict = tf.equal(r_res, tlab)
        r_accuracy = tf.reduce_mean(tf.cast(predict, "float"))
        acc = sess.run(r_accuracy)
        fig, ax = plt.subplots(2, 5)
        ax = ax.flatten()
        for j in range(10):
            img = timg[j].reshape(28, 28)
            ax[j].imshow(img, cmap='Greys')
            ax[j].set_title(f'{res[j]}-{tlab[j]}')
        plt.tight_layout()
        """绘制画布"""
        plt.show()
        print(f'No.{i + 1} accuracy: {acc}')
    #input_node = graph.get_operation_by_name('input/img-input').outputss[0]