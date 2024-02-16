n=int(input("enter the number"))
sum=1
while(n>0):
    i = n%10
    sum *= i
    n = n//10
    
print(sum)
