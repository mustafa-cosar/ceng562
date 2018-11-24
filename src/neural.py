import tensorflow as tf
from tensorflow import keras


def run(data_files, model_parameters):
    reader = tf.data.TextLineDataset(data_files)

    with tf.Session() as session:
        model = keras.Sequential([
            keras.layers.,
            keras.layers.Dense(128, activation=tf.nn.relu),
            keras.layers.Dense(128, activation=tf.nn.relu),
            keras.layers.Dense(6, activation=None)
        ])



