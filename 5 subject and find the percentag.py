'''write a program that accepts the marks of 5 subject and find the percentage marks obtain by the student.it also prints grade according to the followingcriteria
between 91-100----print'A'
81-90-----print'B'
61-80-----print'C'
51-60------print'D'
41-50------print'E'
40% below ----print'f'''
math=int(input("enter marks os math"))
eng=int(input("enter marks of english"))
history=int(input("enter marks of history"))
hindi=int(input("enter marks of hindi"))
sanskrit=int(input("enyter marks of sanskrit"))

tm=(math+eng+history+hindi+sanskrit)/5
print("percentage:",tm)
if(tm>=91):
    print("A grade")
elif(tm>=81 and tm<91):
    print("B grade")
elif(tm>=61 and tm<81):
    print("C grade")
elif(tm>=51 and tm<61):
    print("D grade")
elif(tm>=40 and tm<51):
    print("E grade")
else:
    print("F grade")
