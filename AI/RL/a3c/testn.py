import tensorflow as tf 
import numpy as np
import gym
import os
import time
import sys

from skimage.color import rgb2gray
from skimage.transform import resize

def preprocess_image(image, height, width):
    """Change the color of the image from rgb to gray
       and then modify the size of image"""
    image = np.uint8(
        resize(rgb2gray(image), [height, width], mode='constant')*255)
    image = np.reshape(image, [height, width, 1])/255.
    return image

def downSample(s):
    s = s[35:195]
    s = s[::2,::2, 0]
    s[s==144] = 0
    s[s==109] = 0
    s[s!=0] = 1
    return s[:,:,np.newaxis]



def main():
    game_Name = 'YarsRevengeDeterministic-v4'
    model_path = 'modely2k/model.ckpt'
    if len(sys.argv) > 1:
        model_path = f'{sys.argv[1]}/model.ckpt'
    saver = tf.train.import_meta_graph(model_path +'.meta')
    env = gym.make(game_Name)
    s = env.reset()
    s = preprocess_image(s, 42, 42)
    # s = downSample(s)
    with tf.Session() as sess:  
        saver.restore(sess, './' + model_path)
        graph = tf.get_default_graph()
        sp = graph.get_operation_by_name('s').outputs[0]
        res = graph.get_operation_by_name('Global_Net/actor/ap/Softmax').outputs[0]
        frame = 0
        done = False
        count = 0
        rewards = 0
        while count < 10:
            frame += 1
            s = s[np.newaxis, :]
            prob_weights = sess.run(res, feed_dict={sp: s})
            a = np.random.choice(range(prob_weights.shape[1]),p=prob_weights.ravel())
            s, r, done, i = env.step(a)
            if done:
                count += 1
                s = env.reset()
                print(f'\nall rewards: {rewards} frame: {frame}')
                rewards = 0
                frame = 0
            rewards += r
            #env.render()
            #time.sleep(0.005)
            s = preprocess_image(s,42,42)
            # s = downSample(s)
            #print(f'{frame} frame: rewards: {r}')
        #print(f'\nall rewards: {rewards} frame: {frame}')
    env.close()

if __name__ == "__main__":
    main()