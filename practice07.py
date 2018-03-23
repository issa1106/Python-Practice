# 更多變數的應用，屬性與方法
import numpy
import pandas

FloatNum = 0.5
print(FloatNum.hex())
IntNum = 64
print(IntNum.bit_length())
print(IntNum.to_bytes(length=2, byteorder="big"))
complexNum = 2 + 2j
print(complexNum.real)  # 複數的實部
print(complexNum.imag)  # 複數得虛部
print(complexNum)
print(complexNum.conjugate())  # 共軛複數

print(numpy.zeros(6))  # 六個元素均為零的一維陣列
print(numpy.zeros((2, 3), dtype=numpy.int8))
print(numpy.arange(10))  # 0~9 1d array
print(numpy.arange(10).dtype)  # 查看資料類型
my_arange = numpy.arange(10)
my_arange2 = my_arange.astype(numpy.int8)  # 轉換為int 8
print(my_arange2.dtype)

my_2dA = numpy.array([numpy.arange(1, 6), numpy.arange(3, 8)])
print(my_2dA)
print(my_2dA[1, :])  # 第2列
print(my_2dA[:, 3])  # 第4欄
print(my_2dA.T)  # 轉置.T
print(numpy.where(my_2dA))  # condition [x,y] 流程控制

# 產生10組標準常態隨機變數(n=0,sigma=1)
normal_samples = numpy.random.normal(size=10)
print(normal_samples)
# 產生5組均勻分配的隨機變數(range=0~1)
uniform_samples = numpy.random.uniform(size=5)
print(uniform_samples)

# 更多DataFrame的應用
name = ["Anna", "Killy", "Troy", "Zoe", "Zac"]
score = [60, 81, 98, 43, 75]
gender = ["Female", numpy.nan, "Male", "Female", "Male"]
my_dict = {"name": name, "score": score, "gender": gender}
my_form = pandas.DataFrame(my_dict)
print(my_form)

my_form_dd = my_form.drop(2)  # 刪除資料
print(my_form_dd)
my_form_dc = my_form.drop("score", axis=1)  # 刪除欄位參數axis設為1
print(my_form_dc)

print(my_form.ix[:, "score"])  # 索引值.ix
print(my_form.ix[2])

print(my_form.sort_values(by="score"))  # 可用指定欄位排序
print(pandas.value_counts(my_form.gender))  # 統計相異質的個數
print(my_form.ix[:, "gender"].isnull())  # 判斷遺失值
remy_form = my_form.dropna()  # 刪除有遺失的觀測值
print(remy_form)
remy_form_fillna = my_form.fillna(0)  # 有遺失值的觀測值填補0
print(remy_form_fillna)
remy_form_filled = my_form.fillna({"gender": "Female"})  # 依欄位填補
print(remy_form_filled)
