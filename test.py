print("Hello World by Python!")
print(2+3)
print(2-5)
print(4*4)
print(10/2)
print(3 ** 2) # R 語言使用 3 ^ 2 指數
print(10%4)   # R 語言使用 10 %% 4 求餘

print(type(5))    #顯示基本變數類型
print(type(3.2))
print(type(3+2j))  #j是複數
print(type(True))
print(type("2018 start GitHub")) 

print(1.0 == True)
print(0 == False)
print(1.2 + True) #布林值的彈性應用 +合併 *複製
print(3+True * 2) #5
print("It's time to rocks"+" and rolls!") #可以進行字串+組合

days = 30
days -= 29  # d = d + 5 簡潔的運算子+= -= *= /= %/
print(days)
print("Today is "+ str(days) +"天在練習Python!" ) 
#變數類型轉換 　才可印出↖   而非 +days+

test_bool = True
print(float(test_bool))
print(complex(test_bool))

