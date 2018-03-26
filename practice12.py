from sklearn import datasets
import pandas
import numpy
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.feature_selection import f_regression

# LinearRegression說明:
# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

# 用sklern來讀取資料集iris
iris = datasets.load_iris()
print(type(iris.data))  # 讀入的資料為ndarray
iris_df = pandas.DataFrame(iris.data, columns=iris.feature_names)
print(iris_df.head(6))
print(iris.target_names)

# reshape 給定新的形狀但不改變資料內容
a = numpy.arange(6).reshape(3, 2)
print(a)

# 溫度與冰茶銷售的例子實作
temperatures = numpy.array(
	[29, 28, 34, 31, 25, 29, 32, 31, 24, 33, 25, 31, 26, 30])
iced_tea_sales = numpy.array(
	[77, 62, 93, 84, 59, 64, 80, 75, 58, 91, 51, 73, 65, 84])
# 線性迴歸 把資料轉置成(14,1)再fit進去lm模型
temperatures = numpy.reshape(temperatures, (len(temperatures), 1))
iced_tea_sales = numpy.reshape(iced_tea_sales, (len(iced_tea_sales), 1))
lm = LinearRegression()
lm.fit(temperatures, iced_tea_sales)
print(lm.coef_)  # 印出係數
print(lm.intercept_)  # 印出截距
# 預測氣溫30度時的銷售量
predicted = numpy.array([30])
predicted_sales = lm.predict(numpy.reshape(predicted, (len(predicted), 1)))
print(predicted_sales)

plt.scatter(temperatures, iced_tea_sales)
plt.plot(temperatures, lm.predict(numpy.reshape(temperatures,
	(len(temperatures), 1))))
plt.plot(predicted, predicted_sales, color="red", marker="^", markersize=10)
# plt.show() 

# 模型績效 計算估計子對應的參數的差平方 與score()
mse = numpy.mean((lm.predict(temperatures) - iced_tea_sales) **2)
print(mse)
r_squared = lm.score(temperatures, iced_tea_sales)
print(r_squared)

# 連鎖蛋糕店的例子X[店面積, 車站距離] y[分店銷售量]
X = numpy.array([
    [10, 80], [8, 0], [8, 200], [5, 200], [7, 300], 
    [8, 230], [7, 40], [9, 0], [6, 330], [9, 180]])
y = numpy.array([469, 366, 371, 208, 246, 297, 
			363, 436, 198, 364])
cakeshop_lm = LinearRegression()
cakeshop_lm.fit(X, y)
print(cakeshop_lm.coef_)
print(cakeshop_lm.intercept_)

# 預測新店面的銷售
cakeshop_predicted = numpy.array([[10, 110]])  # 兩個[]2維
ck_predicted_sales = cakeshop_lm.predict(cakeshop_predicted)
print(ck_predicted_sales)
# Mean squard error(MSE) 與 相關係數平方
mse = numpy.mean((cakeshop_lm.predict(X) - y) ** 2)
r_squared = cakeshop_lm.score(X, y)
adj_r_squard = r_squared - (1 - r_squared) * (X.shape[1] /
  				(X.shape[0] - X.shape[1] - 1))
print(mse)
print(r_squared)
print(adj_r_squard)
print(f_regression(X, y)[1])  # p-value
