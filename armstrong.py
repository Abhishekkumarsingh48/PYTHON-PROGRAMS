n=int(input("enter number"))
m=n
count=0
sum1=0
while(n>0):
    n=n//10
    count=count+1
k=m
while(m>0):
    d=m%10
    m=m//10
    sum1=sum1+d**count
if(sum1==k):
    print("armstrong")
else:
    print("not")
