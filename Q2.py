year=int(input("enter year"))
x=0
x=year%400
if x==0:
    print("it is a leap year")
elif year%100==0:
    print("it is not leap year")
elif year%4==0:
    print("it is a leap year")
else:
    print("it is not leap year")