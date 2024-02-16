a=float(input("enter unit"))
if(a<=150):
    print("you have not to pay any cost 660")
elif(a>150 and a<=200):
    cost=(a-150)*5.50+660+30
    print("cost=",cost)
elif(a>200 and a<=300):
    cost=(a-150)*5.50+(a-200)*6+660+40
    print("cost=",cost)
elif(a>300 and a<=400):
    cost=(a-150)*5.50+(a-200)*6+660+(a-300)*6.50+60
    print("cost=",cost)
elif(a>400 and a<=500):
    cost=(a-150)*5.50+(a-200)*6+660+(a-300)*6.50+(a-400)*7+80
    print("cost=",cost)
else:
    cost=(a-150)*5.50+(a-200)*6+660+(a-300)*6.50+(a-400)*7+(a-500)*7.50+100
    print("cost=",cost)
    
