#ingredients to collections 結構
MyArray = ["ex1","ex2", "cat","dog"]  #建立list 中括號
print(MyArray[2])  #索引值從0開始
MyArray.insert(5,"fish") #用insert()新增

#無法新增、刪除、更新的資料結構tuple
MYtuplelist = tuple(MyArray)
MYnewtuple =("A","B","F","L")  #使用小括號
print(MYnewtuple)
print(MYtuplelist)

#帶有key值的資料結構 dictionay 大括號
myname = "Carrie"
myage = 25
is_sick = False
My_dictionary1 ={
	"name": myname,
	"age":myage,
	"status" :is_sick
}
print(My_dictionary1["age"]) #索引是key
