'''
Question's too long
'''

def encrypt_string(s):
    encrypted_string = ''
    for char in s:
        if char.islower():
            encrypted_string += chr(219 - ord(char))
        else:
            encrypted_string += char
    print(encrypted_string)

s = input()
encrypt_string(s)
