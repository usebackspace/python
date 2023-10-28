''' Write a Python program that prints the string s with the character curr_char replaced by the character new_char.

curr_char and new_char are variables that contain strings with a single character.

You may assume that new_char will not be an empty string.

The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).'''

x=input("Enter a string: ")
y=input("Enter a Character you want to replace: ")
z=input("Enter a character you want to replace with: ")

if(z==' '):
    print('we cannot replace a string with sapce')
else:
    result=x.replace(y,z)
    print(result)
