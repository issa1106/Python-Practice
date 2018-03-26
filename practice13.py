import pandas as pd
from sklearn import preprocessing, linear_model
from sklearn.feature_selection import f_regression

# 資料為老師雲端連結，Kaggle鐵達尼克號資料
url = "https://storage.googleapis.com/2017_ithome_ironman/data/kaggle_titanic_train.csv"  
titanic = pd.read_csv(url)
# 用Sex與Age，目的預測Survived

titanicd_age_label = titanic["Age"].notnull()  # 判斷年齡是否有遺失值
titanic_s = titanic[titanicd_age_label]
# 將Age有遺漏的資料不看:titanic_s

# 將Sex改為0, 1
label_encoder = preprocessing.LabelEncoder()
encoded_Sex = label_encoder.fit_transform(titanic_s["Sex"])

# 建立二元分類模型
X = pd.DataFrame([encoded_Sex, titanic_s["Age"]]).T
logistic_regr = linear_model.LogisticRegression()
logistic_regr.fit(X, titanic_s["Survived"])

print(logistic_regr.coef_)  # 印出係數
print(logistic_regr.intercept_)  # 印出截距
print(f_regression(X, titanic_s["Survived"])[1])  # p-value

# 計算預測準確度
survived_predicitons = logistic_regr.predict(X)
accuracy = logistic_regr.score(X, titanic_s["Survived"])

print(survived_predicitons)
print(accuracy)
