'''this is for split() function'''
file=open("myfile.txt","r")
data=file.readlines()
for line in data:
    word=line.split()
    print(word)



    
    ''' this code is for writing the line with creating new file


lines=["hello world","welcome to niet","enjoy python"]
f.writelines(lines)
f.close()
print("data written to file:")
'''
