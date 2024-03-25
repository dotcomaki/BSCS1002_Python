'''
filename is a CSV file that has the following header:
Name,Country,Goals
The first five lines of a sample file are given below:
Name,Country,Goals
P1,Brazil,20
P2,Argentina,30
P3,Brazil,50
P4,Germany,30
Write a function named get_goals that accepts filename and the name of a country as arguments. It should return a tuple having two elements: (num_players, num_goals).
num_players is the number of players from this country that appear in this file, num_goals is the total number of goals scored by all the players who belong to this country. If the country is not present in the file, then return the tuple (-1, -1).
(1) filename is a string variable that holds the name of the file. For example, in the first test case, it is filename = 'public_1.csv'.
(2) Each player who represents a country has scored at least one goal. That is, the last column in the file will have only positive integers.
'''

def get_goals(filename, country):
    file = open(filename, 'r')
    num_players = 0
    num_goals = 0
    for line in file:
        fields = line.strip().split(',')
        if fields[1] == country:
            num_players += 1
            num_goals += int(fields[2])
    if num_players == 0:
        num_players = -1
        num_goals = -1
    file.close()
    return (num_players, num_goals)
