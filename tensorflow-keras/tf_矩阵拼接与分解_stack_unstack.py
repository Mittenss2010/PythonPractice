import tensorflow as tf

a = tf.constant([1,2,3])
b = tf.constant([4,5,6])
# 矩阵拼接
c = tf.stack([a, b], axis=0)  # 行拼接
c = tf.stack([a, b], axis=1)  # 对应列拼接

# 矩阵分解
d = tf.unstack(c, axis=0)  # 行，分解
e = tf.unstack(c, axis=1)  # 列，分解

# boxes = tf.stack([1, 2, 3, 4, 0], axis=1)

with tf.Session() as sess:
    print(sess.run(c))
    print(sess.run(d))
    print(sess.run(e))