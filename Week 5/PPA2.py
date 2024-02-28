'''
Write a function named check_leap_year that accepts a year between 1600 and 9999 as argument. It should return True if the year is a leap year and False otherwise.
'''

def check_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 100 != 0:
        if year % 4 == 0:
            return True
        else:
            return False
