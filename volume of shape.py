a=int(input("enter length of side of cube"))
w=int(input("enter weidth of cuboid"))
h=int(input("enter length of cuboid"))
l=int(input("enter height of cuboid"))
r=int(input("enter redious of cylender"))
H=int(input("enter hight of cylender"))
v=a**3
Sa=6*a**2
cuv=w*h*l
csa=2*(l*w+l*h+h*w)
cyv=3.14*(r**2)*H
cysa=2*3.14*r*H+2*3.14*r**2
print("volume of cube is {}  and  surface area of cube is {}".format(v,Sa))
print("volume of cuboid is {} and surface area of cuboid is {}".format(cuv,csa))
print("volume of cylender is {} and surface area of cylender is {}".format(cyv,cysa))


