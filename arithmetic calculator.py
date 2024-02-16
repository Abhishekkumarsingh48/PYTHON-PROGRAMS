'''write a program to simulate arithmetic calculator'''
a=int(input("enter first number"))
b=int(input("enter 2nd number"))
print("enter operater")
print("Addition:+")
print("substract:-")
print("multiply:*")
print("division:/")
print("reminder:%")
print("exponant:**")
op=input()
if(op=='+'):
    print("sum:",a+b)
elif(op=='-'):
    print("sub",a-b)
elif(op=='*'):
    print("mul:",a*b)
elif(op=='/'):
    print("div:",a/b)
elif(op=='%'):
    print("reminder:",a%b)
elif(op=='**'):
    print("expo:",a**b)
else:
    print("invalid operater")
    
            
