n=int(input("enter number of terms"))
'''i=1
a=-1
b=1
while(i<=n):
    c=a+b
    a=b
    b=c
    i=i+1
    print(c,end="  ")'''
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
    
