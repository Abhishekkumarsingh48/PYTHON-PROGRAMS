x=10
def outer():
    x=12
    def inner():
        x=7
        print("inside the inner function",x)
    inner()
    print("inside outer function",x)
outer()
print("outside function difination",x)
