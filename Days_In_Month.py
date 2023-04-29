def is_leap(year):
    """This Function is return the year is 
    leap year or not"""
    if year % 4 == 0 and(year % 400 == 0 or year % 100 != 0):
        return True
    else:
        return False

def days_in_month(year,month):
    if is_leap(year):
        month_days=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[month]
    else:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
        return month_days[month] 
    
    
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month-1)
print(days)