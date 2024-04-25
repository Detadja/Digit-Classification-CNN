import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
print("Train: x = %s, y = %s" % (x_train, y_train))
print("test: x = %s, y = %s" % (x_test, y_test))

