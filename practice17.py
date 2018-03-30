import tensorflow as tf
import numpy
import matplotlib.pyplot as plt

# 測試資料 y = 0.1x +0.3 已知係數
x_data = numpy.random.rand(100).astype(numpy.float32)
y_data = x_data * 0.1 + 0.3
plt.scatter(x_data, y_data)
plt.show()  # 將產生的資料圖像看看

W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))  # 係數 斜率=-1~1
b = tf.Variable(tf.zeros([1]))  # 截距
y = W * x_data + b  # 預測值

# 使loss(MSE)最小
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.5)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()  # 初始化

# 開始tensorflow
sess = tf.Session()
sess.run(init)
# 將迴歸線的係數與截距 每跑20印出來看看 越接近0.1 0.3
for step in range(201):
	sess.run(train)
	if step % 20 == 0:
		print(step, sess.run(W), sess.run(b))

sess.close()
