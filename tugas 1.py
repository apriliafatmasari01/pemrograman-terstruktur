while True:
    x = int(input("enter a year:"))
    y = x
    x %= 4
    if x == 0:
        print("Year", y, "is a leap year")
    elif x != 0:
        print("Year", y, "is not a leap year")
