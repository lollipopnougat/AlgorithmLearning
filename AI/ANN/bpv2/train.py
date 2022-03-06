import tensorflow as tf
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras import callbacks
from dataset import MnistDataset
from model import Bp

Lr = 0.001


class Train:
    def __init__(self):
        self.nn = Bp()
        self.train_images, self.train_labels = MnistDataset.load_training_data_oh(
            './mnist')
        self.test_images, self.test_labels = MnistDataset.load_testing_data_oh(
            './mnist')

    def train(self):
        check_path = './save/model-{epoch:04d}.ckpt'
        # period 每隔10epoch保存一次
        #save_model_cb = callbacks.ModelCheckpoint(check_path, save_weights_only=True, verbose=1, period=10)
        tensorboard_callback = callbacks.TensorBoard(log_dir='logs/',
                                                     histogram_freq=1)
        self.nn.model.compile(optimizer='adam',
                            # 此损失函数要求one_hot
                              loss='categorical_crossentropy', 
                              metrics=['accuracy'])
        self.nn.model.fit(self.train_images,
                          self.train_labels,
                          batch_size=128,
                          epochs=50,
                          steps_per_epoch=468,
                          callbacks=[tensorboard_callback])

    def test(self):
        test_loss, test_acc = self.nn.model.evaluate(self.test_images,
                                                     self.test_labels)
        print("准确率: %.4f，共测试了%d张图片 " % (test_acc, len(self.test_labels)))

    def save(self, filename: str):
        self.nn.model.save(filename)
        print(f'模型存储位置: {filename}')


if __name__ == "__main__":
    app = Train()
    app.train()
    app.test()
    app.save('./save/model.h5')