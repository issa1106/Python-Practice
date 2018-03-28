# 整體學習:基本分類器投票機Bagging, AdaBoosting
# 隨機森林, 支持向量機(SVM)
import numpy
import pandas
from sklearn import cross_validation, ensemble
# This module will be removed in 0.20. (CV iterators)
from sklearn import svm, preprocessing, metrics


# 老師放雲端上的鐵達尼號 資料載入
url = "https://storage.googleapis.com/2017_ithome_ironman/data/kaggle_titanic_train.csv"
titanic = pandas.read_csv(url)

# 年齡的遺漏值填補平均年齡
age_median = numpy.nanmedian(titanic["Age"])
new_Age = numpy.where(titanic["Age"].isnull(), age_median, titanic["Age"])
titanic["Age"] = new_Age

# dummy variables 將性別轉為0, 1
label_encoder = preprocessing.LabelEncoder()
encoder_Sex = label_encoder.fit_transform(titanic["Sex"])

# 建立訓練與測試資料，用Pclass, Age, Sex 來預測 Survived
titanic_X = pandas.DataFrame([titanic["Pclass"],
				 encoder_Sex, titanic["Age"]]).T
titanic_y = titanic["Survived"]
train_X, test_X, train_y, test_y = cross_validation.train_test_split(
				titanic_X, titanic_y, test_size=0.3)

# 建立Bagging
bag = ensemble.BaggingClassifier(n_estimators=100)
bag_fit = bag.fit(train_X, train_y)

test_y_predicted = bag.predict(test_X)
print(test_y_predicted)

accuracy = metrics.accuracy_score(test_y, test_y_predicted)
print(accuracy)

# 建立AdaBoosting
boost = ensemble.AdaBoostClassifier(n_estimators=100)
boost_fit = boost.fit(train_X, train_y)

test_y_Adapredicted = boost.predict(test_X)
print(test_y_Adapredicted)

accuracy = metrics.accuracy_score(test_y, test_y_Adapredicted)
print(accuracy)

# 建立Random Forest
forest = ensemble.RandomForestClassifier(n_estimators=100)
forest_fit = forest.fit(train_X, train_y)

test_y_f_predicted = forest.predict(test_X)
print(test_y_f_predicted)

accuracy = metrics.accuracy_score(test_y, test_y_f_predicted)
print(accuracy)

# 建立SVC
svc = svm.SVC()
svc_fit = svc.fit(train_X, train_y)

test_y_svc_predicted = svc.predict(test_X)
print(test_y_svc_predicted)

accuracy = metrics.accuracy_score(test_y, test_y_svc_predicted)
print(accuracy)

# 另外的AUC績效
fpr, tpr, thresholds = metrics.roc_curve(test_y, test_y_f_predicted)
auc = metrics.auc(fpr, tpr)
print("隨機森林模型的AUC績效:", auc)

fpr, tpr, thresholds = metrics.roc_curve(test_y, test_y_svc_predicted)
auc = metrics.auc(fpr, tpr)
print("支持向量機模型的AUC績效:", auc)
