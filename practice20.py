from tensorflow.examples.tutorials.mnist import input_data
import numpy
import matplotlib.pyplot as plt
import tensorflow as tf

# 讀入手寫數字辨識資料 會下載gz檔
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
x_train = mnist.train.images
y_train = mnist.train.labels
x_test = mnist.test.images
y_test = mnist.test.labels

print(x_train.shape)  # 55000張 28x28=784像素的圖片

# 印出圖片看看 第54999張=最後一張
last_train_img = numpy.reshape(x_train[54999, :], (28,28))
plt.matshow(last_train_img, cmap=plt.get_cmap('gray'))
plt.show()

# 設定參數
learning_rate = 0.5
training_steps = 1000
batch_size = 100
logs_path = 'TensorBoard/'
n_features = x_train.shape[1]
n_labels = y_train.shape[1]

# 建立Feeds
with tf.name_scope("Inputs"):
	x = tf.placeholder(tf.float32, [None, n_features], name="Input_Data")
with tf.name_scope("Labels"):
	y = tf.placeholder(tf.float32, [None, n_labels], name="Labe_Data")

# 建立 Variables
with tf.name_scope("ModelParameters"):
	W = tf.Variable(tf.zeros([n_features, n_labels]), name="Weights")
	b = tf.Variable(tf.zeros([n_labels]), name="Biases")

# 深度學習模型
with tf.name_scope("Model"):
	prediction = tf.nn.softmax(tf.matmul(x, W) + b)
with tf.name_scope("Cross_Entropy"):  # 定義Loss
	loss = tf.reduce_mean(-tf.reduce_sum(y * tf.log(prediction),
		reduction_indices=1))
	tf.summary.scalar("Loss", loss)
with tf.name_scope("Gradient_Descent"):  # 優化Optimization 梯度下降
	optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
with tf.name_scope("Accuracy"):  # 準確度
	correct_prediction = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
	acc = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
	tf.summary.scalar("Accuracy", acc)

# 初始化
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

merged = tf.summary.merge_all()
writer = tf.summary.FileWriter(logs_path, graph=tf.get_default_graph())

for step in range(training_steps):
	batch_xs, batch_ys = mnist.train.next_batch(batch_size)
	sess.run(optimizer, feed_dict={x: batch_xs, y: batch_ys})
	if step % 50 == 0:
		print(sess.run(loss, feed_dict={x: batch_xs, y: batch_ys}))
		summary = sess.run(merged, feed_dict={x:batch_xs, y: batch_ys})
		writer.add_summary(summary, step)

print("Accuracy:", sess.run(acc, feed_dict={x: x_test, y: y_test}))

sess.close()
