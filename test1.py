import numpy as np
import pandas as pd
import sklearn as sk
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import torch as tt
import numpy as np
import torchvision as tv
#import time as t
import os
import matplotlib as mb
from tensorflow.python import time


# Check for TensorFlow GPU access
print(f"TensorFlow has access to the following devices:\n{tf.config.list_physical_devices()}")

# See TensorFlow version
print(f"TensorFlow version: {tf.__version__}")
print(f"sklearn version: {sk.__version__}")
print(f"numpy version: {np.__version__}")
print(f"pandas version: {pd.__version__}")
print(f"cv2 version: {cv2.__version__}")
print(f"pytorch versiuon{tt.__version__}")
print(f"numpy version : {np.__version__}")
print(f"torchvision version : {tv.__version__}")
print(f"matplotlib version : {mb.__version__}")
#print(f"os version: {os.__version__}")
#print(f"time as t version : {t.__version__}")
print(f"time as t version : {t.__version__}")