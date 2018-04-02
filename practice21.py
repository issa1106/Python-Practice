import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
x_train = mnist.train.images
y_train = mnist.train.labels
x_test = mnist.test.images
y_test = mnist.test.labels

# 設定參數
logs_path = 'TensorBoard/'
n_features = x_train.shape[1]
n_labels = y_train.shape[1]

# 啟動
sess = tf.InteractiveSession()
with tf.name_scope("Input"):
	x = tf.placeholder(tf.float32, shape=[None, n_features])
with tf.name_scope("Label"):
	y = tf.placeholder(tf.float32, shape=[None, n_labels])

# 自定義初始化權重的函數
def weight_variable(shape):
	initial = tf.truncated_normal(shape, stddev=0.1)
	return tf.Variable(initial)


def bias_variable(shape):
	initial = tf.constant(0.1, shape=shape)
	return tf.Variable(initial)


# 自訂 conv2d 與 max_pooling 函數
def convolution2d(x, W):
	return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding="SAME")


def max_pool_2x2(x):
	return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
	 strides=[1, 2, 2 ,1], padding="SAME")


# 第一層32個神經元
with tf.name_scope("FirstConvolutionLayer"):  # 用5x5的filter取出32個特徵
	W_cv1 = weight_variable([5, 5, 1, 32])
	b_cv1 = bias_variable([32])
	x_image = tf.reshape(x, [-1, 28, 28, 1])
	h_cv1 = tf.nn.relu(convolution2d(x_image, W_cv1) + b_cv1)
	h_pool1 = max_pool_2x2(h_cv1)  # 圖片降維成14X14
		
# 第二層64個神經元	取出64個特徵
with tf.name_scope("SecondConvolutionLayer"):
	W_cv2 = weight_variable([5, 5, 32, 64])
	b_cv2 = bias_variable([64])
	h_cv2 = tf.nn.relu(convolution2d(h_pool1, W_cv2) + b_cv2)
	h_pool2 = max_pool_2x2(h_cv2)  #圖片再降維

# 第三層1024個神經元 在視覺化看時特別粗
with tf.name_scope("DenselyConnectedLayer"):
	W_fc1 = weight_variable([7 * 7 * 64, 1024])
	b_fc1 = bias_variable([1024])
	h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
	h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# 避免Overfitting
with tf.name_scope("Dropout"):
	keep_prob = tf.placeholder(tf.float32)
	h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# 第四層 輸出層10神經元
with tf.name_scope("ReadoutLayer"):
	W_fc2 = weight_variable([1024, 10])
	b_fc2 = bias_variable([10])
	y_cv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2

# 訓練與模型效度
with tf.name_scope("CrossEntropy"):
	cross_entropy = tf.reduce_mean(
		tf.nn.softmax_cross_entropy_with_logits(logits=y_cv, labels=y))
	tf.summary.scalar("CrossEntropy", cross_entropy)
	train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
	correct_prediction = tf.equal(tf.argmax(y_cv, 1), tf.argmax(y, 1))

with tf.name_scope("Accuracy"):
	accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
	tf.summary.scalar("Accuracy", accuracy)

# 初始化
sess.run(tf.global_variables_initializer())

# 視覺化輸出
merged = tf.summary.merge_all()
writer = tf.summary.FileWriter(logs_path, graph=tf.get_default_graph())

for i in range(5000):  # 縮小迴圈 簡易實作時間 精確度可能下降
	batch = mnist.train.next_batch(50)
	if i%100 == 0:
		train_accuracy = accuracy.eval(feed_dict={x: batch[0], y:batch[1], keep_prob: 1.0})
		print("step %d, training accuracy %g"%(i, train_accuracy))
		summary = sess.run(merged, feed_dict={x: batch[0], y: batch[1], keep_prob: 1.0})
		writer.add_summary(summary, i)
		writer.flush()
	train_step.run(feed_dict={x: batch[0], y: batch[1], keep_prob: 0.5})

print("test accuracy %g"%accuracy.eval(feed_dict={x: x_test, y: y_test, keep_prob: 1.0}))

# 關閉
sess.close()
