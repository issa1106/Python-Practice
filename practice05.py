#巢狀函數練習
def my_mean(in_list):
	'計算平均數'
	def my_sum(in_list):
		'計算總合'
		temp_sum = 0
		for i in in_list:
			temp_sum += i
		return temp_sum
	def my_length(in_list):
		'計算長度'
		temp_length = 0
		for i in range(len(in_list)):
			temp_length += 1
		return temp_length
	try:
		return my_sum(in_list) / my_length(in_list)
	except:	
		print("please input List or Tuple!")
		

mlist = [11, 22, 33, 44, 20, 14]
print(my_mean(mlist))
print(my_mean("yee!"))  #測試錯誤訊息 try-except

#彈性參數 *args **kwargs (Keyword arguments)有帶鍵值
def show_score(**kwargs):
	'列出成績'
	for key in kwargs:
		print(key,":",kwargs[key])


show_score(chinese=86, english=85, homework=90)
