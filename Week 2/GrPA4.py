'''
You are given the dates of birth of two persons, not necessarily from the same family. Your task is to find the younger of the two.
If both of them share the same date of birth, then the younger of the two is assumed to be that person whose name comes first in alphabetical order (names will follow Python's capitalize case format).
The input will have four lines. The first two lines correspond to the first person, while the last two lines correspond to the second person.
For each person, the first line corresponds to the name and the second line corresponds to the date of birth in DD-MM-YYYY format. Your output should be the name of the younger of the two.
'''

name1 = input()
dob1 = input()
name2 = input()
dob2 = input()

# Convert string slices to integers for comparison
year1, month1, day1 = int(dob1[6:]), int(dob1[3:5]), int(dob1[0:2])
year2, month2, day2 = int(dob2[6:]), int(dob2[3:5]), int(dob2[0:2])

if year1 > year2:
    print(name1)
elif year2 > year1:
    print(name2)
elif month1 > month2:  # If years are equal
    print(name1)
elif month2 > month1:
    print(name2)
elif day1 > day2:  # If months are also equal
    print(name1)
elif day2 > day1:
    print(name2)
else:  # If dates are equal, compare names
    if name1 > name2:
        print(name2)
    elif name2 > name1:
        print(name1)
    else:
        print("Both have the same name and date of birth.")
