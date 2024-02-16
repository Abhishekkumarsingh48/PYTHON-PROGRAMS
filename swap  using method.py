x=int(input("enter a number"))
y=int(input("enter 2nd num"))
def swap(x,y):
    x=x+y
    y=x-y
    x=x-y
    print("after swap",x,y)
swap(x,y)
