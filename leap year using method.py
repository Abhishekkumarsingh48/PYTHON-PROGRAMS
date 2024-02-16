def leap():
    y=int(input("enter any year"))
    if(y%100==0):
        if(y%400==0):
            print("leap")
    elif(y%4==0):
        print("leap")
    else:
        print("not leap")
leap()
