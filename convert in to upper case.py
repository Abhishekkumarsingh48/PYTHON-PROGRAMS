s=input("enter a string")
S=""
for char in s:
    if('a'<=char<='z'):
        S+=chr(ord(char)-32)
    else:
        if('A'<=char<='Z'):
            S+=chr(ord(char)+32)
        else:
            S+=char
print("upper case string:",S)        
