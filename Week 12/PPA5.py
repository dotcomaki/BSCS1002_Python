'''
word is a string that contains one or more parentheses of the following types: "{ }", "[ ]", "( )". The string is said to be balanced if all the following conditions are satisfied.
When read from left to right:
(1) Number of opening parentheses of a given type is equal to the number of closing parentheses of the same type.
(2) An opening parenthesis cannot be immediately followed by a closing parenthesis of a different type.
(3) Every opening parenthesis should be eventually closed by a closing parenthesis of the same type.
Write a function named balanced that accepts the string word as argument. Return True if the string is balanced, and False otherwise. You can assume that the string doesn't contain any characters other than parentheses.
'''

def balanced(word):
    stack = []
    for char in word:
        if char in ['(', '{', '[']:
            stack.append(char)
        else:
            if not stack:
                return False
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return not stack
