import tensorflow as tf

for device in tf.config.list_physical_devices():
    print(device.name)