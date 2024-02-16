c=input("enter a character")
if(len(c)==1 and'A'<=c<='Z'):
    if c=='A'or c=='E'or c=='I'or c=='O'or c=='U':
        print("{} is a vowel".format(c))
    else:
        print("{} is a consonant".format(c))
elif(len(c)==1 and'a'<=c<='z'):
    if c=='a' or c=='e'or c=='i'or c=='o'or c=='u':
        print("{} is a vowel".format(c))
    else:
        print("{} is a consonant".format(c))
else:
    print("{} is an invalid character".format(c))
