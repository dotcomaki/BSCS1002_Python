'''
Question's too long
'''

def is_perfect(word):
    is_perfect = True

    if 'a' not in word or 'e' not in word or 'i' not in word or 'o' not in word or 'u' not in word:
        is_perfect = False

    else:
        if word.index('e') < word.index('a') or word.index('i') < word.index('e') or word.index('o') < word.index(
                'i') or word.index('u') < word.index('o'):
            is_perfect = False

        else:
            count_a = word.count('a')
            count_e = word.count('e')
            count_i = word.count('i')
            count_o = word.count('o')
            count_u = word.count('u')

            if count_a < count_e or count_e < count_i or count_i < count_o or count_o < count_u:
                is_perfect = False

    return is_perfect

string = input()
if is_perfect(string) == True:
    print("It is a perfect word")
else:
    print("It is not a perfect word")
    
