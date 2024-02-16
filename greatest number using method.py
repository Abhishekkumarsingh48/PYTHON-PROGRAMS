def great():
    x=int(input("enter value of x"))
    y=int(input("enter value of y"))
    z=int(input("enter value of z"))
    if(x>y):
        if(x>z):
            print("{} is greater".format(x))
    elif(y>z):
        print("{} is greater".format(y))
    else:
        print("{} is greater".format(z))
great()
