import pandas

# 載入資料可從雲端或電腦中
# 老師雲端上的檔案，用網址
iriscsv = "https://storage.googleapis.com/2017_ithome_ironman/data/iris.csv"
iris_df = pandas.read_csv(iriscsv)  # 載入資料(逗號)
print(iris_df.head(8))

# 空白分隔資料，用sep指定分隔符號
# 電腦中檔案位置(~\Documents\Python-Practice\S10619A.prn)與py檔同位置
studentscore = "S10619A.prn"
studentscore_df = pandas.read_table(studentscore, sep="\s+")
print(studentscore_df.head(6))

xlsx = "S10619A.xlsx"  # excel 表格與py檔同位置
score_df = pandas.read_excel(xlsx)
print(score_df.head(3))
