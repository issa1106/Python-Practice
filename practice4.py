import math
import random

#函數練習
A_length=[23, 25, 22, 26, 18, 27]
print(max(A_length))
print(min(A_length))
print(len(A_length))  #list長度
print(sorted(A_length))  #遞增排序
print(sorted(A_length, reverse=True))  #遞減排序

#自定義函數計算圓面積和周長 回傳多值為tuple
def circle_calculate(radius):
	'輸入半徑得到面積和周長'
	circle_area = math.pi * radius**2
	circle_circum = 2 * math.pi * radius
	return circle_area, circle_circum


my_radius = 10
print(circle_calculate(my_radius))  #回傳是tuple
print(type(circle_calculate(my_radius)))
getarea, getcircum = circle_calculate(my_radius)
print("circum=", getcircum, ", area=", getarea)


#exchange sort
def exchange_sort(in_list,reverse = False):
	"""輸入list用交換排序法排序，
	reverse參數可False遞增排序,
	True 遞減排序"""
	
	in_list_cloned = in_list #複製list
	if reverse ==False: #遞增
		for i in range(len(in_list)):
			for j in range(i+1,len(in_list)):
				#如果前一個數字比後一個數字大則交換
				if in_list_cloned[i]>in_list_cloned[j]:
					temp = in_list_cloned[i]
					in_list_cloned[i]=in_list_cloned[j]
					in_list_cloned[j]= temp
	else: #遞減排序
		for i in range(len(in_list)):
			for j in range(i+1,len(in_list)):
			#如果前一個數字比後一個數字小則交換
				if in_list_cloned[i]<in_list_cloned[j]:
					temp = in_list_cloned[i]	
					in_list_cloned[i]= in_list_cloned[j]
					in_list_cloned[j]= temp
	return in_list_cloned
	pass


print("origin:", A_length)
print(exchange_sort(A_length))
print(exchange_sort(A_length, reverse=True))
