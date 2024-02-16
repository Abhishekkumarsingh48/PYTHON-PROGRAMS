'''sum=lambda x:x+1
print(sum(3))'''
'''add=lambda x=10:(lambda y:x+y)
a=add()
print(a)
print(a(20))'''


'''returning lambda function'''
def add():
    y=20
    return(lambda x:x+y)
a=add()
print(a(10))
