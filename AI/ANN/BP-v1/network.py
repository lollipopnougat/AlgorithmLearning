import tensorflow as tf

import numpy as np

input_size = 784  # 输入大小
num_classes = 10  # 输出大小

class Network:
    def __init__(self, opt) -> None:
        with tf.variable_scope('input'):
            self.input_img = tf.placeholder(tf.float32, [None, input_size], 'img-input')
            self.input_label = tf.placeholder(tf.float32, [None, num_classes], 'label-input') 
        self.params = self.__build_net()
        with tf.variable_scope('loss'):
            #self.loss = -tf.reduce_sum(self.input_label * tf.log(self.output + 1e-10))
            self.loss = tf.reduce_mean(-tf.reduce_sum(self.input_label * tf.log(self.output + 1e-10), reduction_indices=[1]))
            #lossf = tf.nn.softmax_cross_entropy_with_logits(labels=self.input_label,logits=self.l4)
            #sub = tf.math.subtract(self.l3, self.input_label, name='sub')
            #self.loss = tf.reduce_mean(lossf)
            tf.summary.scalar("loss", self.loss)
        with tf.name_scope('local_grad'):
            #self.update_op = opt.minimize(self.loss)
            grads = tf.gradients(self.loss, self.params)
            self.update_op = opt.apply_gradients(zip(grads, self.params))
        with tf.name_scope('accuracy'):
            predict = tf.equal(tf.argmax(self.output, 1), tf.argmax(self.input_label, 1))
            # predict -> [true, true, true, false, false, true]
            # reduce_mean即求predict的平均数 即 正确个数 / 总数，即正确率
            self.accuracy = tf.reduce_mean(tf.cast(predict, "float"))
            tf.summary.scalar("accuracy", self.accuracy)
        self.merged_summary = tf.summary.merge_all()
        
    def __build_net(self):
        w_init = tf.random_normal_initializer(0., .1)
        with tf.variable_scope('net'):
            l1 = tf.layers.dense(self.input_img, 32, tf.nn.relu, kernel_initializer=w_init, name='Layer1')
            #l2 = tf.layers.dense(l1, 64, tf.nn.relu, kernel_initializer=w_init, name='Layer2')
            l3 = tf.layers.dense(l1, 16, tf.nn.relu, kernel_initializer=w_init, name='Layer2')
            self.output = tf.layers.dense(l3, num_classes, tf.nn.softmax, kernel_initializer=w_init, name='Layer3')
            #self.output = tf.nn.softmax(self.l4)
        params = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope='net')
        return params

    def train_one_step(self, sess, img, label):
        #lossval = sess.run(self.loss, {self.input_img: img, self.input_label: label})
        lossval, _, acc, ms = sess.run([self.loss, self.update_op, self.accuracy, self.merged_summary], {self.input_img: img, self.input_label: label})
        return lossval, acc, ms

    def get_output(self, sess, img):
        res = sess.run(self.output, {self.input_img: img})
        return np.argmax(res)

    



