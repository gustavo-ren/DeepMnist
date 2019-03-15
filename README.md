ReLu is the activation function

tf.InteractiveSession(): creates an Interactive Session to run the tensorflow Operation objects and evaluate the Tensor objects, the only difference with normal Session is that the InteractiveSession puts itself as the default Session on construction. It can be used in interactive enviroments as a shell.

tf.placeholder(): placeholders are variables that don't have values assigned to it untill is needed, it is possible to define them program by what operations it will go through without having to know the actual data beforehand, but if you try to evaluate a placeholder it will produce an error, the values on a placeholder must be fed using the optional argument feed_dict on Session.runn(), Tensor.eval() or Operation.run(). Placeholders are not compatible with eager execution, that is a way to evaluate operations immediatly without building graphs on an imperative programming environment. Arguments -> dtype: type of the elements to be fed, shape: shape of the tensor if none is provided you can fed any tensor, name: name of the tensor. 

tf.reshape(): reshapes an tensor, for instance, it can transform an tensor [2, 4] as [[1, 2, 3, 4], [5, 6, 7, 8]] in a tensor with shape [4, 2], [2, 2, 2], [2, 1, 2], etc(apparently the multiplication of the dimensions must match the number of elements on the original tensor, look into it to be sure...)

tf.truncated_normal(initializers): this function outputs values from a truncated normal distribution, the generated values follow with specific mean and standard deviation, but values with more than 2 standard deviations from the mean are dropped and re-drawn. This is the recommended initializer for neural networks and filters

tf.nn.conv2d: computes a 2-D convolution given 4-D input and filter tensors

tf.nn.max_pool: performs a max_pooling on the tensor

tf.global_variables_initializer: initialize all variables, if you try to use any of them without this little guy be prepared to get some scary Exceptions(I've learned it on the hard way...)