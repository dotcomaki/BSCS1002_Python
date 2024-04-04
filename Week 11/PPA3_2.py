'''
Write a function named longest_words that accepts a list of words as argument and returns the sub-list of the longest words. Use list comprehension and built-in functions.
'''

def longest_words(words):
    max_len = max(len(word) for word in words)
    return [word for word in words if len(word) == max_len]
  
