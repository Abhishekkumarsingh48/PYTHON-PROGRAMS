def hello_fun():
    def hi():
        return "hi"
    return hi
hello=hello_fun()
print(hello())
