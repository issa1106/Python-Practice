import numpy #Anaconda中的套件 np
import pandas #Anaconda中的套件 pd

vlist = numpy.array([2,15,3,70,10]) #轉成numpy.ndarray資料結構
print(vlist * 2)  #向量乘上係數積的運算
print(vlist ** 2) #平方運算
print(vlist > 12)      #篩選資料以布林呈現
print(vlist[vlist>12]) #印出>12的資料

mlist = numpy.array([[1,2,3],[4,5,6]]) #矩陣結構
print(mlist)
print(mlist.size) 
print(mlist.shape) #矩陣規模

#用dictionary建表格 用法pandas.DataFrame
stuname = ["Killy","Troy","Zoe","Zac"]
mathsor = [60,98,43,75]
myform = {"name":stuname,"score":mathsor}
buildform=pandas.DataFrame(myform)
print(buildform)

martixtoframe = pandas.DataFrame(mlist,["Row1","Row2"],["C1","C2","C3"])
print(martixtoframe.iloc[0:1,:]) #使用.iloc列出想要的元素

print(buildform[buildform.loc[:,"score"]>60]) #選出分數大於60的資料表
print(buildform.describe()) #描述性統計
print(buildform.columns) #欄位名稱
print(buildform.index) 
#建立category資料結構
Mycategorical = pandas.Categorical(["A","B","C"])
print(Mycategorical)
