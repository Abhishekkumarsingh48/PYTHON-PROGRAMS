a=(input("enyter a value"))
b=(input("enter value of b"))
try:
    a=int(a)
    b=int(b)
    s=a/b
    print(s)
except ZeroDivisionError:
    print("by mistake")
except ValueError:
    print("enter correct value")
except TypeError:
    print("enter the correct type")
finally:
    print("completed")
