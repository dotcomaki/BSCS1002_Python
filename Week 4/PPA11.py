'''
Question's too long
'''

def solution(L):
    ### Enter your solution below this line
    ### Indent your entire code by one unit (4 spaces) to the right
    sorted_L = [ ]
    while L != [ ]:
        max_elem = L[0]
        for elem in L:
            if elem > max_elem:
                max_elem = elem
        L.remove(max_elem)
        sorted_L.append(max_elem)
    ### Enter your solution above this line
    return sorted_L
