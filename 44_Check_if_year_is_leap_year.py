yrs = int(input("Enter any years"))
if ((yrs%4 ==0 and yrs % 100!=0) or yrs%400 ==0):
    print("It is leap year",yrs)
else:
    print("It is not leap years")



















def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
