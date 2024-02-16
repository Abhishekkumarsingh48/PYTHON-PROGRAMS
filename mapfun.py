'''list1=[1,2,3,4,5,6,7,8,99,9]
def square(x):
    return x**2
a=map(square,list1)
print("updated list:",list(a))
print("original:",list(list1))'''
'''list1=['a','c','b','r','e','t','p']
def vol(x):
    letters=['a','e','i','o','u']
    if x in letters:
        return True
    else:
        return False
num=filter(vol,list1)
for i in num:
    print(i)'''

ya=[2,4,5,7,6,10,14,9,17,20,19]
def odd(x):
    if x%2!=0:
        return True
    else:
        return False
num=filter(odd,ya)
x=list(num)
for i in num:
    print(i,end=" ")
def queue(x):
    return x**3
a=map(queue,x)
b=list(a)
print(list(b))
print(list(x))
















