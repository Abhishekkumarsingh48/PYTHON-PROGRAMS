n=int(input("enter a number"))
if(n>=0):
    if(n==0):
        print("niether negative nor positive")
    else:
        print("number is positive")
    if(n%2==0):
        print("num is even")
    else:
        print("num is odd")
else:
    print("num is negative")
