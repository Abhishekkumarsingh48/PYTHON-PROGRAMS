'''WAP to chek number is prime or not'''
a=int(input("enter a number"))
i=1
count=0
while(i<=a):
    if(a%i==0):
        count=count+1
    i=i+1
if(count==2):
    print("num is prime")
else:
    print("not prime")
        
     
