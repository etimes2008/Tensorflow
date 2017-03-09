# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy
import math

print("hello world!", math.sin(1.2))

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
