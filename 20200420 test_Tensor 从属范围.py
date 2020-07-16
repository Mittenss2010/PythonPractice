import tensorflow as tf

input_data_0 = tf.placeholder(dtype=tf.float32, name='input_data')

with tf.name_scope('define_input'):
    input_data   = tf.placeholder(dtype=tf.float32, name='input_data')

## 不同变量，tensor名称一样，但是从属的范围不一样
print(input_data_0)     ## Tensor("input_data:0", dtype=float32)
print(input_data)       ## Tensor("define_input/input_data:0", dtype=float32)

