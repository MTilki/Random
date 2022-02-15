import tensorflow as tf

print("gpus avaliable:", len(tf.config.experimental.list_physical_devices('GPU')))
