lst=[12,2,3,46,8,90,21,31,455]
list.sort(lst)
print(lst)
print("minimum=",lst[0])
print("max:",lst[-1])
if(lst[-1]==lst[-2]):
    print(lst[-3])
else:
    print("second largest=",lst[-2])
