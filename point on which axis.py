x=float(input("enter the x coordinate point"))
y=float(input("enter the y coordinate point"))
if(x>0 and y>0):
    print("pint({},{}) in first quadrant".format(x,y))
elif(x<0 and y>0):
    print("point({},{}) in second quadrant".format(x,y))
elif(x<0 and y<0):
    print("point({},{}) in third quadrant".format(x,y))
elif(x>0 and y<0):
    print("point({},{}) in fourth quadrant".format(x,y))
elif(x==0 and y==0):
    print("point({},{}) is at origin".format(x,y))
if(x==0):
    print("point({},{}) is on Y-axis".format(x,y))
elif(y==0):
    print("point({},{}) is on X-axis".format(x,y))
