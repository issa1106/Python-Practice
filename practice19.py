# 模組化寫法並視覺化呈現(改寫範例practice17.py的架構)
import tensorflow as tf
import numpy

# 增加層函數
def add_layer(inputs, input_tensors, output_tensors,n_layer, activation_funtion=None):
	layer_name = "layer%s" % n_layer
	with tf.name_scope("Layer"):  # 為每個運算元命名
		with tf.name_scope("Weights"):
			W = tf.Variable(tf.random_normal([input_tensors, output_tensors]))
			tf.summary.histogram(name=layer_name + "/Weights", values=W)
		with tf.name_scope("Biases"):
			b = tf.Variable(tf.zeros([1, output_tensors]))
			tf.summary.histogram(name=layer_name + "/Biases", values=b)
		with tf.name_scope("formula"):
			formula = tf.add(tf.matmul(inputs, W), b)
		if activation_funtion is None:
			outputs = formula
		else:
			outputs = activation_funtion(formula)
		return outputs


# 準備測試資料 y = 0.1x +0.3 已知係數
x_data = numpy.random.rand(100)
x_data = x_data.reshape(len(x_data), 1)
y_data = x_data * 0.1 + 0.3

# 建立Feeds
with tf.name_scope("Inputs"):
	x_feeds = tf.placeholder(tf.float32, shape=[None, 1], name="x_inputs")
	y_feeds = tf.placeholder(tf.float32, shape=[None, 1], name="y_inputs")

# 隱藏層
hidden_layer = add_layer(x_feeds, input_tensors=1,
		output_tensors=10, n_layer=1, activation_funtion=None)

# 輸出層
output_layer = add_layer(hidden_layer, input_tensors=10,
	 output_tensors=1, n_layer=2, activation_funtion=None)

# 使loss(MSE)最小
with tf.name_scope("Loss"):
	loss = tf.reduce_mean(tf.square(y_feeds - output_layer))
with tf.name_scope("Train"):
	optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
	train = optimizer.minimize(loss)

# 初始化Graph運算元
init = tf.global_variables_initializer()  # 全域變數初始化
sess = tf.Session()

# 視覺化輸出
merged = tf.summary.merge_all()
writer = tf.summary.FileWriter("TensorBoard/", graph=sess.graph)

# 執行運算
sess.run(init)
for step in range(201):
	sess.run(train, feed_dict={x_feeds:x_data, y_feeds:y_data})
	if step % 20 == 0:
		result = sess.run(merged, feed_dict={x_feeds: x_data, y_feeds: y_data})
		writer.add_summary(result, step)

sess.close()
