score = [55,89,76,66,42,95,71]
print(len(score)) #list的長度
print(range(len(score))) #製造全距range
print(list(range(len(score)))) #產生0到7的list
for index in list(range(len(score))): #索引值for迴圈
	print(score[index])
print(index) #印出最後index的值

for score in score: #不用索引值
	print(score)
print(type(score)) #資料型態變成int
print(score) #印出後的score值

mylist = [2,3,4,5,10,8]  
ind = 0
while ind <len(mylist):  #While迴圈
	print(mylist[ind])
	ind +=1
	
my_seq =list(range(1,11))
for i in my_seq:               #if else
	if(i % 2 ==0):
		print(i,"is even")
	else:
		print(i,"is odd")
for a in my_seq:                #三段式條件 elif
	if(a % 3 ==0):
		print(a, "can be divided by 3")
	elif(a%3 ==1):
		print(a,"mod 3 = 1")
	else:
		print(a,"mod 3 = 2")

#流程控制break continue
Blist = [12,23,45,10,50]
for Blist in Blist:
	if(Blist >30):          #if大於30就break結束迴圈
		break
	else:
		print(Blist)

print("fin_index=",Blist)

Clist = [12,23,45,10,50]
for Clist in Clist:
	if(Clist>30):       #if大於30跳過它繼續執行countinue
		continue
	else:
		print(Clist)

print("fin_index=",Clist)