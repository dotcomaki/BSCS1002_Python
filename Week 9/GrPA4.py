'''
Write a function named num_to_words that accepts a square matrix of single digit numbers as argument.
Within the function, create a file named words.csv. Write the matrix to the file by replacing the digits with their corresponding words.
For example, num_to_words([[1, 2], [3, 4]]) should create the file words.csv with the following contents:
one,two
three,four
Note that the matrix will only have integers from
0
0 to
9
9, endpoints inclusive.

(1) You do not have to accept input from the user or print the output to the console.
You just have to write the function definition. However, within the function, you have to create a file named words.csv and write to it.

(2) The last line of the file should not end with a '\n'. The last character of every other line in the file should end with a '\n'.
This is a convention that we will be following in all questions that ask you to write to a file.
'''

def num_to_words(matrix):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    file = open('words.csv', 'w')
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            file.write(words[matrix[i][j]])
            if j != len(matrix[i]) - 1:
                file.write(',')
        if i != len(matrix) - 1:
            file.write('\n')
    file.close()
