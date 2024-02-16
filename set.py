lst=[1,2,3,4,5,6,7,8,8,8,7,9,7,8,9,0]
m=set(lst)
print(m)
n=list(m)
print(n)
n.sort()
print(n[-2])
x=[]
for i in range(1,21):
    if i%2==0:
        x.append(i)
print(x)
