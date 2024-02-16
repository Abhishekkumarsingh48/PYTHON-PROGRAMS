from functools import reduce as r
def add (x,y):
    return x+y
def even(x):
    if x%2==0:
        return True
    else:
        return False

list1=[2,5,7,6,13,15,10,21,24]
b=filter(even,list1)
a=r(add,b)
print(a)

