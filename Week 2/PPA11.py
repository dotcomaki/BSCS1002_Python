'''
A class teacher has decided to split her entire class into four groups, namely Sapphire, Peridot, Ruby, and Emerald for sports competitions. For dividing the students into these four groups, she has followed the pattern given below:
Group							
Sapphire	1	5	9	13	17	21	...
Peridot	2	6	10	14	18	22	...
Ruby	3	7	11	15	19	23	...
Emerald	4	8	12	16	20	24	...
All the students are represented by their roll numbers. Based on the above pattern, given the roll number as input, print the group the student belongs to as output.
'''

roll = int(input())

while roll != 0:
    temp = roll % 4
    if roll == 1 or temp == 1:
        print("Sapphire")
        break
    elif roll == 2 or temp == 2:
        print("Peridot")
        break
    elif roll == 3 or temp == 3:
        print("Ruby")
        break
    elif roll == 4 or temp == 0:
        print("Emerald")
        break
    roll %= 4
