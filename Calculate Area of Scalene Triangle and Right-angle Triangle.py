'''8.	Write a program to Calculate Area of Scalene Triangle and Right-angle Triangle.'''
a=int(input("enter side1 value"))
b=int(input("enter side2 value"))
c=int(input("enter side3 value"))
d=int(input("enter hight"))
e=int(input("enter base"))
s=(a+b+c)/2
A=(s*(s-a)*(s-b)*(s-c))**1/2
Aa=1/2*d*e
print("area of saclen triangle is {}".format(A))
print("area of right-angle triangle is {}".format(Aa))
