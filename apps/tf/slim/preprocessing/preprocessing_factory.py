# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Contains a factory for building various models."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf


# slim = tf.contrib.slim


def get_preprocessing(name, is_training=False):
  """Returns preprocessing_fn(image, height, width, **kwargs).

  Args:
    name: The name of the preprocessing function.
    is_training: `True` if the model is being used for training and `False`
      otherwise.

  Returns:
    preprocessing_fn: A function that preprocessing a single image (pre-batch).
      It has the following signature:
        image = preprocessing_fn(image, output_height, output_width, ...).

  Raises:
    ValueError: If Preprocessing `name` is not recognized.
  """
  preprocessing_fn_map = {
      'inception_v3': tf.keras.applications.inception_v3.preprocess_input,
      'inception_resnet_v2': tf.keras.applications.inception_resnet_v2.preprocess_input,
      'mobilenet': tf.keras.applications.mobilenet.preprocess_input,
      'nasnet': tf.keras.applications.nasnet.preprocess_input,
      'resnet_v1': tf.keras.applications.resnet.preprocess_input,
      'resnet_v2': tf.keras.applications.resnet_v2.preprocess_input,
      'vgg_16': tf.keras.applications.vgg16.preprocess_input,
      'vgg_19': tf.keras.applications.vgg19.preprocess_input,
  }

  if name not in preprocessing_fn_map.keys():
    return None

  return preprocessing_fn_map[name]#preprocessing_fn