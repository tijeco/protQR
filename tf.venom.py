#!/usr/bin/env python

# conda execute
# env:
#  - python >=3
#  - numpy
#  - tensorflow



import os
import urllib.request

import numpy as np
import tensorflow as tf
training_data = "venom.binary.train.csv"
test_data = "venom.binary.test.csv"


training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
    filename=training_data,
    target_dtype=np.int,
    features_dtype=np.float32)
test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
    filename=test_data,
    target_dtype=np.int,
    features_dtype=np.float32)
feature_columns = [tf.feature_column.numeric_column("x", shape=[6])]
print(feature_columns)
classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns,
                                  hidden_units=[500,500,500,500],
                                      n_classes=2,
                                      model_dir="tmp/venom_model",
                                      optimizer="SGD"
                                      )
                                      #Adagrad', 'Adam', 'Ftrl', 'RMSProp', 'SGD'

train_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"x": np.array(training_set.data)},
    y=np.array(training_set.target),
    num_epochs=None,
    shuffle=True)
classifier.train(input_fn=train_input_fn, steps=20000)

test_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"x": np.array(test_set.data)},
    y=np.array(test_set.target),
    num_epochs=1,
    shuffle=False)
accuracy_score = classifier.evaluate(input_fn=test_input_fn)["accuracy"]

print("\nTest Accuracy: {0:f}\n".format(accuracy_score))


"""
49044 venom.train.csv
21020 venom.test.csv
120,4,setosa,versicolor,virginica

"""
