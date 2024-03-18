'''
You have a locker that has a finite number of coins in it. Each coin has some positive integer that is engraved on it. This denotes how valuable the coin is. You wish to draw a subset of coins from the locker whose total worth is s.
Your task is to determine if this can be done with the coins available in your locker.
Write a recursive function named subset_sum that accepts a list of positive integers L and a positive integer s as arguments. The list L represents the coins in your locker.
The integer s represents the total value of the coins that you need to withdraw. Return True if you can withdraw some subset of coins whose combined worth is s, return False otherwise.
'''

def subset_sum(L, s):
    if s == 0:
        return True
    if len(L) == 0:
        return False
    return subset_sum(L[1:], s) or subset_sum(L[1:], s - L[0])
