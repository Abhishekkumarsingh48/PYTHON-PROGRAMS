n=int(input("enter the number"))
sum=0
while(n>0):
    i = n%10
    sum += i
    n = n//10
    
print(sum)
