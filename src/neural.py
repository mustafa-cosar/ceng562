import tensorflow as tf
from tensorflow import keras


def run_nn(training_data, training_labels, test_data, test_labels, prediction_set=None, epochs=10):

    input_count = training_data.shape[1]
    output_count = training_labels.shape[1]
    print(input_count, output_count)

    with tf.Session() as session:
        model = keras.Sequential([
            keras.layers.Dense(input_count),
            keras.layers.Dense(256, activation=tf.nn.relu),
            keras.layers.Dense(128, activation=tf.nn.relu),
            keras.layers.Dense(64, activation=tf.nn.relu),
            keras.layers.Dense(output_count, activation=None)
        ])

        model.compile(
            optimizer=tf.train.AdamOptimizer(), loss='mean_squared_error', metrics=['accuracy'])

        model.fit(training_data, training_labels, epochs=epochs)

        test_loss, test_accuracy = model.evaluate(test_data, test_labels)

        if prediction_set is not None:
            return model.predict(prediction_set)


        return model, test_loss, test_accuracy
