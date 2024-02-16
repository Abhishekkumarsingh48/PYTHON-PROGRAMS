n=int(input("enter number"))
r=int(input("enter number"))
f=1
g=1
h=1
for i in range(1,n+1):
    f=f*i
print("n!=",f)
for i in range(1,r+1):
    g=g*i
print("r!=",g)
for i in range(1,(n-r)+1):
    h=h*i
print("(n-r)!=",h)
FO=f/(h)
print("n!/(n-r)!=",FO)
    
