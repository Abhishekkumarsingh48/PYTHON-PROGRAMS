list1=[1,2,3,4,5,6,7,8,911,23,5,678]
def even(x):
    if x%2==0:
        return True
    else:
        return False
a=sorted(filter(even,list1),reverse=True)
for i in a:
    print(i)
'''p=filter(lambda x:x%2==0,list1)
for i in p:
    print(i)'''
'''age=[24,32,61,17,21,4,78,9,29]
p=filter(lambda x: x>=18,age)
for i in p:
    print(i)'''
