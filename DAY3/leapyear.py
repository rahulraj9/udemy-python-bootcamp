year = int(input("Enter the year you want to check is it leap or not:-"))
if year % 4 == 0 and year % 100 != 0 or year %400 == 0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")