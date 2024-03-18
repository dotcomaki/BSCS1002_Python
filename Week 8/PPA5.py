'''
Write a recursive function named palindrome that accepts a string word as argument and returns True if it is a palindrome and False otherwise.
'''

def palindrome(word):
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[-1]:
            return palindrome(word[1:-1])
        else:
            return False
