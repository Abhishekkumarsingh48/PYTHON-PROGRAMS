import math
try:
    a=int(input("enter a number"))
    print(math.sqrt(a))
except ValueError:
    print("enter correct value")
except KeyboardInterrupt:
    print("error:")
finally:
    print("completed")
