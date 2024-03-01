'''
p and q are called twin primes if both p and q are primes and ∣p−q∣=2. Write a function named twin_primes that accepts two integers p and q as arguments. It should return True if the arguments are twin primes and False otherwise.
'''

def twin_primes(p, q):
    count_p = 0
    for i in range(1, p+1):
        if p % i == 0:
            count_p += 1
    count_q = 0
    for j in range(1, q+1):
        if q % j == 0:
            count_q += 1

    if p > q:
        diff = p - q
    elif q > p:
        diff = q - p

    if count_p == 2 and count_q == 2 and diff == 2:
        return True
    else:
        return False
