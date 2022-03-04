import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, optimizers, Sequential, metrics

tf.enable_eager_execution()

#translate data type
def preprocess(x, y):
    x = tf.cast(x, dtype=tf.float32) / 255.
    y = tf.cast(y, dtype=tf.int32)
    return x, y


(x, y), (x_test, y_test) = keras.datasets.mnist.load_data()
batchsz = 128
db = tf.data.Dataset.from_tensor_slices((x, y))
db = db.map(preprocess).shuffle(10000).batch(batchsz)
db_test = tf.data.Dataset.from_tensor_slices((x_test, y_test))
db_test = db_test.map(preprocess).shuffle(10000).batch(batchsz)
model = Sequential([
    layers.Dense(256, activation=tf.nn.relu),
    layers.Dense(128, activation=tf.nn.relu),
    layers.Dense(64, activation=tf.nn.relu),
    layers.Dense(32, activation=tf.nn.relu),
    layers.Dense(10),
])
model.build(input_shape=[None, 28 * 28])
optimizer = optimizers.Adam(lr=1e-3)


def main():
    for epoch in range(30):
        for step, (x, y) in enumerate(db):
            x = tf.reshape(x, [-1, 28 * 28])
            with tf.GradientTape(persistent=True) as tape:
                logits = model(x)
                y_onehot = tf.one_hot(y, depth=10)
                #lose_mse = tf.reduce_mean(tf.losses.MSE(y_onehot, logits))
                lose_crossentropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_onehot,logits=logits))
            #grads1 = tape.gradient(lose_mse, model.trainable_variables)
            grads2 = tape.gradient(lose_crossentropy,
                                   model.trainable_variables)
            optimizer.apply_gradients(zip(grads2, model.trainable_variables))
            if step % 100 == 0:
                print(epoch, step, 'lose_ce:', float(lose_crossentropy))
        total_correct = 0
        total_num = 0
        for x, y in db_test:
            x = tf.reshape(x, [-1, 28 * 28])
            logits = model(x)
            prob = tf.nn.softmax(logits, axis=1)
            pred = tf.cast(tf.argmax(logits, axis=1), dtype=tf.int32)
            correct = tf.equal(pred, y)
            correct = tf.reduce_sum(tf.cast(correct, dtype=tf.int32))
            total_correct += int(correct)
            total_num += x.shape[0]
        acc = total_correct / total_num.value
        print(epoch, 'test accurracy:', acc)


if __name__ == '__main__':
    main()
