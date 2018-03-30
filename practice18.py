# Tensorflow基本運作練習
import tensorflow as tf

# 距陣範例
matrix1 = tf.constant([[2, 2]])  # 1x2
martix2 = tf.constant([[1, 2, 3], [4, 5, 6]])  # 2x3
product = tf.matmul(matrix1, martix2)  # 矩陣乘法 shape=(1,3)

# 變數範例
state = tf.Variable(0, name="counter")

one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)  # 每次+1之後更新state

init_op = tf.global_variables_initializer()  # 初始化

# 資料輸入
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)

# 資料輸出
num1 = tf.constant([3])
num2 = tf.constant([5])
added = tf.add(num1, num2)
multiplied = tf.multiply(num1, num2)

# 執行運算
with tf.Session() as sess:
	# 印出矩陣範例
	result = sess.run(product)
	print(result)

 	# 印出變數範例
	sess.run(init_op)
	print(sess.run(state))
	for _ in range(3):
		sess.run(update)
		print(sess.run(state))

	# 執行時才將資料以dict輸入
	print(sess.run([output], feed_dict={input1: [7], input2: [5]}))

	# 直接輸出運算結果
	operation = sess.run([added, multiplied])
	print(operation)

sess.close()
