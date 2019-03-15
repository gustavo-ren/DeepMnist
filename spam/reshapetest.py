import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

sess = tf.InteractiveSession()

var1 = tf.Variable(initial_value=5)
var2 = tf.Variable(initial_value=6)

result = tf.multiply(x=var1, y=var2, name="blah")

x = tf.Variable([[1, 2, 3, 4], [5, 6, 7, 8]])
y = tf.reshape(tensor=x, shape=[4, 1, 2], name="ReshapeResult")

init = tf.global_variables_initializer()
sess.run(init)
# y = x.get_shape()
print(y.eval())
sess.close()
# print(x.shape())
# y = tf.reshape(x, [2, 2])
