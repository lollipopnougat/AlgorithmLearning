import multiprocessing
import threading
import tensorflow as tf
import numpy as np
import gym
import os
import shutil
import matplotlib.pyplot as plt
import envs

import cv2
from tensorflow.python.tools import freeze_graph 
from tensorflow.python.platform import gfile

from envs import create_atari_env

class AC_CONV(object):
    """the structure of core net"""
    
    def __init__(self, scope, input, classNum, sess):
        """Initialize the core net
        Args:
            scope: scope name
            input: input node
            classNum: the number of actions
            sess: the activated session
        """
        self.sess = sess
        self.input = input
        
        with tf.variable_scope(scope):
            self._build_net(scope, classNum)
            
    def _build_net(self, scope, classNum):
        """The detailed structure of core net"""
        w_init = tf.random_normal_initializer(0., .1)
        self.conv1 = tf.layers.conv2d(self.input, filters=32, kernel_size=3, strides=2, padding='VALID', activation=tf.nn.relu, name = 'conv1')
        self.conv2 = tf.layers.conv2d(self.conv1, filters=32, kernel_size=3, strides=2, padding='VALID', activation=tf.nn.relu, name = 'conv2')
        self.conv3 = tf.layers.conv2d(self.conv2, filters=32, kernel_size=3, strides=2, padding='VALID', activation=tf.nn.relu, name = 'conv3')
        
        self.flat = tf.layers.flatten(self.conv3, name='flat')
        
        #define the actor
        with tf.variable_scope('actor'):
            self.a_dense = tf.layers.dense(self.flat, 256, tf.nn.relu6, kernel_initializer=w_init, name='la')
            self.a_prob = tf.layers.dense(self.a_dense, classNum, tf.nn.softmax, kernel_initializer=w_init, name='ap')
    
    def output(self, s):
        prob_weights = self.sess.run(self.a_prob, 
                                      feed_dict={self.input: s})
        return prob_weights

class AC_LSTM(object):
    """the structure of core net"""
    
    def __init__(self, scope, input, classNum, sess):
        
        self.sess = sess
        self.input = input
        
        with tf.variable_scope(scope):
            self._build_net(scope, classNum)
            
    def _build_net(self, scope, classNum):
        """The detailed structure of core net"""

        #define the actor
        with tf.variable_scope('actor'):
            w_init = tf.random_normal_initializer(0., .1)
            self.conv1 = tf.layers.conv2d(self.input, filters=32, kernel_size=3, strides=2, padding='VALID', activation=tf.nn.relu, name = 'conv1')
            self.conv2 = tf.layers.conv2d(self.conv1, filters=32, kernel_size=3, strides=2, padding='VALID', activation=tf.nn.relu, name = 'conv2')
            self.conv3 = tf.layers.conv2d(self.conv2, filters=32, kernel_size=3, strides=2, padding='VALID', activation=tf.nn.relu, name = 'conv3')
            
            flat = tf.layers.flatten(self.conv3, name='flat0')
            lstm_cell = tf.contrib.rnn.BasicLSTMCell(256, state_is_tuple=True, name='lstm_cell')
            c_init = np.zeros((1, lstm_cell.state_size.c), np.float32)
            h_init = np.zeros((1, lstm_cell.state_size.h), np.float32)
            self.state_init = [c_init, h_init]
            
            self.c_in = tf.placeholder(tf.float32, [1, lstm_cell.state_size.c], name='c_in')
            self.h_in = tf.placeholder(tf.float32, [1, lstm_cell.state_size.h], name='h_in')
                
            rnn_in = tf.expand_dims(flat, [0], name='flat_exp')
            state_in = tf.contrib.rnn.LSTMStateTuple(self.c_in, self.h_in)
            lstm_outputs, lstm_state = tf.nn.dynamic_rnn(
                    lstm_cell, rnn_in,
                    initial_state=state_in,
                    time_major=False)
            lstm_c, lstm_h = lstm_state
            self.state_out = (lstm_c[:1, :], lstm_h[:1, :])
            self.rnn_out = tf.reshape(lstm_outputs, [-1, 256], name='reshape')
            
            self.flat = tf.layers.flatten(self.rnn_out, name='flat')
            
            self.a_prob = tf.layers.dense(self.flat, classNum, tf.nn.softmax, kernel_initializer=w_init, name='ap')
        
    #get the output node of core net
    #the probability of actions
    def output(self, s, lstm_state):
        prob_weights, state_out = self.sess.run([self.a_prob, self.state_out], 
                                      feed_dict={self.input: s, 
                                                 self.c_in: lstm_state[0],
                                                 self.h_in: lstm_state[1]})
        return prob_weights, state_out
        
def cal_score_lstm(env, model):
    s = env.reset()
    score = 0
    frame = 0
    lstm_state = model.state_init
    while True:
        s = np.squeeze(s)[np.newaxis, :, :, np.newaxis]
        ap, lstm_state = model.output(s, lstm_state)
        a = int(np.argmax(ap))
        s_, r, done, info = env.step(a)
        
        score += r
        frame += 1
        s = s_
        if done:
            break
    return score, frame

def cal_score(env, infer):
    s = env.reset()
    score = 0
    frame = 0
    while True:
        s = np.squeeze(s)[np.newaxis, :, :, np.newaxis]
        ap = model.output(s)
        a = int(np.argmax(ap))
        s_, r, done, info = env.step(a)
        
        score += r
        frame += 1
        s = s_
        if done:
            break
    return score, frame

        
#game_Name = 'PongDeterministic-v4'
#game_Name = 'AlienDeterministic-v4'
game_Name = 'YarsRevengeDeterministic-v4'
env = create_atari_env(game_Name)
shape = env.observation_space.shape
N_A = env.action_space.n

# saver = tf.train.import_meta_graph('modellstm/model/model.ckpt.meta')
SESS = tf.Session()
# saver.restore(SESS, "./model15k/model.ckpt") # 注意路径写法  
# graph = tf.get_default_graph()
ckpt_path = "./modellstm/model/model.ckpt"
input = tf.placeholder(tf.float32, [1, 42, 42, 1], 's')#graph.get_operation_by_name('s_1').outputs[0]#

# var_to_shape_map = reader.get_variable_to_shape_map()  
# for key in var_to_shape_map:
#     if key.find('Global_Net/actor') != -1:
#         print("tensor_name: ", key)  
#         print(reader.get_tensor(key))
model = AC_LSTM("W_0", input, N_A, SESS)
# model = AC_CONV("W_0", input, N_A, SESS)
flow = model.a_prob
flow = tf.argmax(flow, axis=1, output_type=tf.int32, name='out_a')

var = tf.global_variables()
saver = tf.train.Saver(var)
SESS.run(tf.global_variables_initializer())

saver.restore(SESS, ckpt_path)

env.seed(2)
re, fr = cal_score_lstm(env, flow)
print(f'reward: {re}, frame: {fr}')