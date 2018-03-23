import pandas
import math

stu_name = ["Killy", "Troy", "Zoe", "Zac"]
math_score = [60, 98, 43, 75]
score_dict = {"name": stu_name, "score": math_score}

buildform = pandas.DataFrame(score_dict)  #建立表格
print(buildform.head(n=2))  #列出前 2 row 物件的方法Method
print(buildform.dtypes)  #列出變數類型 物件的屬性Attribute


#物件導向 Object
class MyBall(object):
	"""myBall 是描述 球 的類別
	   radius為半徑, color為球的顏色"""
	def __init__(self,radius,color):
		self.radius = radius
		self.color = color
	def volume(self):
		volume = 4 / 3 * math.pi *  self.radius ** 3
		return volume


#物件繼承Inheritance
class newBall(MyBall):
	"""繼承自MyBall類別
	   新增了print_color直接印出顏色
	   fixable為是否固定不變
	   volume被改寫為直接列印"""
	def __init__(self, radius, color, fixable): #若不建立新的參數可不要這段
		super().__init__(radius,color)  #super()來繼承原始參數
		self.fixable = fixable  #並建立新的參數
	def print_color(self):
		print(self.color)
	# 改寫Override volume 
	def volume(self):
		print(self.radius ** 3 * math.pi * 4 / 3, "Overrided!")
		

Ball_A = MyBall(20, "red")  #建立一個物件
Ball_B = newBall(10,"white",True)  #可用繼承後的類別建立物件
print("What's color? ", Ball_A.color)  #呼叫物件的屬性
print("What's size? ",Ball_A.volume())  #呼叫物件的方法
Ball_B.print_color()
Ball_B.volume()
