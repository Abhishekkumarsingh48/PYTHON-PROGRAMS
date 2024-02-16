days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
day_num=int(input("enter a number between 1 and 7: "))
if(1<=day_num<=7):
    day_name=days[day_num-1]
    print("day:",day_name)
else:
    print("try again and enter valid number")
