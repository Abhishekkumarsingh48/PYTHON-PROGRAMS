'''def fun(num):
    print("hello")
    return fun("msg")
fun(5)'''
''' here two cases Base case and other one is recurcive case'''
'''def fact(x):
    if x==1 or x==0:
        return 1
    else:
        return(x*fact(x-1))
num=5
print(fact(num))'''
'''sum of natural number'''
'''def sum(x):
    if x==0:
        return 0
    else:
        return(x+sum(x-1))
num=5
print(sum(num))'''

'''fibbonacci'''
'''def fibbo(n):
    if n==1:#base case
        return 0
    elif n==2:
        return 1
    else:
        return(fibbo(n-1)+fibbo(n-2))#recursive case
n=int(input("enter number"))
for i in range(1,n+1):
    print(fibbo(i),end=" ")'''

'''sum of digit'''
'''def sum(n):
    if n<=0:
        return 0
    else:
        return(n%10+sum(n//10))
n=int(input("entere a number"))
print(sum(n))'''


'''even odd '''
'''def even(n):
    if n==0 or n==1:
        return "neither even nor odd"
    else:
        return(n%2==0)
n=int(input("enter number"))
print(even(n))'''

'''to find power'''

'''def power(x,y):
    if y==0:
        return 1
    else:
        return x*power(x,y-1)
x=int(input("enter value of x"))
y=int(input("enter value of y"))
print("result=",power(x,y))'''

'''wap to find the sum of list element'''
'''def sum_lst(lst):
    if len(lst)==0:
        return 0
    else:
        return(lst[0]+sum_lst(lst[1:]))
lst1=[12,23,43,22,12,47,90,32]
result=sum_lst(lst1)
print(result)'''

'''wap to chek wether a string is pallindrom or not'''

'''def pallindrom(x):
    if len(x)==0:
        return true
    else:
        return (x[1:]==x[: :-1])
x=input("eneter string")
print(pallindrom(x))'''













    

























        




























    














