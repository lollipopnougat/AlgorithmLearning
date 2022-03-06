import tensorflow as tf 
import numpy as np
import gym
from tensorflow.python import pywrap_tensorflow  
import os
import time


def downSample(s):
    """Preprocessing to the image of game state"""
    s = s[35:195]
    s = s[::2,::2, 0]
    s[s==144] = 0
    s[s==109] = 0
    s[s!=0] = 1
    return s[:,:,np.newaxis]

reader = pywrap_tensorflow.NewCheckpointReader('modellstm/model-lstm-yars/model.ckpt')  
var_to_shape_map = reader.get_variable_to_shape_map()  
for key in var_to_shape_map:
    print('tensor_name: ', key)  
    # print(reader.get_tensor(key))
    # if key.find('Global_Net/actor') != -1:
    #     print('tensor_name: ', key)  
    #     print(reader.get_tensor(key))

game_Name = 'PongDeterministic-v4'  
# game_Name = 'Pong-v0'  
saver = tf.train.import_meta_graph('modellstm/model-lstm-yars/model.ckpt.meta')#, clear_devices=True) 
graph_def = tf.get_default_graph().as_graph_def(add_shapes=True)
node_list = [n.name for n in graph_def.node]
for node in node_list:
    print('node_name', node) 
env = gym.make(game_Name)
s = env.reset()
s = downSample(s)
with tf.Session() as sess:  
    saver.restore(sess, 'modellstm/model-lstm-yars/model.ckpt.meta') # 注意路径写法  
    graph = tf.get_default_graph()
    
    # sp = graph.get_operation_by_name('s').outputs[0]#tf.placeholder(tf.float32, input_shape, 's')
    sp = graph.get_operation_by_name('s_1').outputs[0]#tf.placeholder(tf.float32, input_shape, 's')

    # res = graph.get_operation_by_name('Global_Net/actor/ap/Softmax').outputs[0]#graph.get_tensor_by_name("Global_Net/actor/ap/bias:0")
    res = graph.get_operation_by_name('W_0/actor/ap/Softmax').outputs[0]#graph.get_tensor_by_name("Global_Net/actor/ap/bias:0")
    frame = 0
    done = False
    rewards = 0
    env.render()
    input('wait key')
    while not done:
        frame += 1
        s = s[np.newaxis, :]
        prob_weights = sess.run(res, feed_dict={sp: s})
        a = np.random.choice(range(prob_weights.shape[1]),p=prob_weights.ravel())
        s, r, done, i = env.step(a)
        rewards += r
        env.render()
        time.sleep(0.005)
        s = downSample(s)
        print(f'{frame} frame: rewards: {r}')
    print(f'\nall rewards: {rewards}')
env.close()

