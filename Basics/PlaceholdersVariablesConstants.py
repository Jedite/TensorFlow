import tensorflow as tf

x = tf.constant([1, 2, 3, 4, 5])

y = tf.constant([6, 7, 8, 9, 10])

result = tf.multiply(x, y)

with tf.Session() as sess:
    print(sess.run(result))

