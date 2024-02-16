n=int(input("enter number"))
r=int(input("enter number"))
f = g =h =1
def pnr(n,r):
    global f,g,h
    for i in range(1,n+1):
         f=f*i
    print("n!=",f)
    for i in range(1,r+1):
         g=g*i
    print("r!=",g)
    for i in range(1,(n-r)+1):
         h=h*i
    print("(n-r)!=",h)
    print("n!/(n-r)!=",f/h)
pnr(n,r)
#FO=f/(h)


