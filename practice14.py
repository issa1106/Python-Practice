from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.cross_validation import train_test_split
# This module will be removed in 0.20 (CV iterators)
from sklearn import metrics
from sklearn import neighbors
import numpy
import matplotlib.pyplot as plt

# sklearn的資料集 取用iris的資料
iris = load_iris()
iris_X = iris.data
iris_y = iris.target

# 將資料分為訓練與測試
train_X, test_X, train_y, test_y = train_test_split(
	iris_X, iris_y, test_size=0.3)

# tree分類器
DTclassifier = tree.DecisionTreeClassifier()
iris_clf = DTclassifier.fit(train_X, train_y)
# 預測
test_y_predicted = iris_clf.predict(test_X)
print(test_y_predicted)
print(test_y)
# 精確度(45-E)/45
acc = metrics.accuracy_score(test_y, test_y_predicted)
print(acc)

# KNN分類器
KNclassifier = neighbors.KNeighborsClassifier()
iris_knclf = KNclassifier.fit(train_X, train_y)
# 預測
test_y_knpredicted = iris_knclf.predict(test_X)
print("PRE:", test_y_knpredicted)
print("ANS:", test_y)
# 績效
accuracy_kn = metrics.accuracy_score(test_y, test_y_knpredicted)
print(accuracy_kn)

# 選擇合適的K (n_neighbors預設為5)
range = numpy.arange(1, round(0.2 * train_X.shape[0]) + 1)
accuracies = []

for i in range:
	clf = neighbors.KNeighborsClassifier(n_neighbors=i)
	iris_dkclf = clf.fit(train_X, train_y)
	test_y_dkpredicted = iris_dkclf.predict(test_X)
	accuracy = metrics.accuracy_score(test_y, test_y_dkpredicted)
	accuracies.append(accuracy)

# 製圖
appr_k = accuracies.index(max(accuracies)) + 1
print(appr_k)
plt.scatter(range, accuracies)
plt.show()
