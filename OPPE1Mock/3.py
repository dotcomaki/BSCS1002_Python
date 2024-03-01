'''
Accept the date in MM/DD/YYYY format as input from the user and print the date in DD-MM-YY format, by retaining only the last two digits in a year, replacing the forward slash with a dash and swapping the order of month and date.
'''

date = input()
newdate = date[3:5] + '-' + date[0:2] + '-' + date[8:]
print(newdate)
