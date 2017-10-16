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

# Data sets
IRIS_TRAINING = "iris_training.csv"
IRIS_TRAINING_URL = "http://download.tensorflow.org/data/iris_training.csv"

IRIS_TEST = "iris_test.csv"
IRIS_TEST_URL = "http://download.tensorflow.org/data/iris_test.csv"


# If the training and test sets aren't stored locally, download them.
if not os.path.exists(IRIS_TRAINING):
  raw = urllib.request.urlopen(IRIS_TRAINING_URL).read()
  with open(IRIS_TRAINING, "w") as f:
    f.write(raw)

if not os.path.exists(IRIS_TEST):
  raw = urllib.request.urlopen(IRIS_TEST_URL).read()
  with open(IRIS_TEST, "w") as f:
    f.write(raw)
  # Load datasets.

training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
    filename=IRIS_TRAINING,
    target_dtype=np.int,
    features_dtype=np.float32)
test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
    filename=IRIS_TEST,
    target_dtype=np.int,
    features_dtype=np.float32)
# Specify that all features have real-value data
# Specify that all features have real-value data
# Specify that all features have real-value data
feature_columns = [tf.feature_column.numeric_column("x", shape=[4])]
print(feature_columns)

# Build 3 layer DNN with 10, 20, 10 units respectively.
classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns,
                                      hidden_units=[10, 20, 10],
                                      n_classes=3,
                                      model_dir="/tmp/iris_model")
