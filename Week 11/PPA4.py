'''
Write a function named sort_by_len that accepts a list of strings as arguments and sorts the list based on the lengths of the strings in ascending order. If multiple strings have the same length, their original ordering in the unsorted list must be maintained. Refer to the idea of "stable sorting" for more details. Use built-in functions.
'''

def sort_by_len(lst):
    return sorted(lst, key=len)
