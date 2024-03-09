'''
para is a sequence of space-separated words. All words will be in lower case. There will be a single space between consecutive words. The string has no other special characters other than the space.
Write a function named exact_count that accepts the string para and a positive integer n as arguments. You have to return True if there is at least one word in para that occurs exactly n times, and False otherwise.
'''

def exact_count(para, n):
    words = para.split()
    for word in words:
        count = 0
        for other_word in words:
            if word == other_word:
                count += 1
        if count == n:
            return True
    return False
