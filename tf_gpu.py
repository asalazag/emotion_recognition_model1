# import tensorflow as tf

# # Check if TensorFlow detects the GPU
# physical_devices = tf.config.list_physical_devices('GPU')
# if len(physical_devices) > 0:
#     print("GPU available for TensorFlow:", physical_devices)
# else:
#     print("No GPU available for TensorFlow.")

import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))