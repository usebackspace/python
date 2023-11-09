
import string

s = "The quick brown fox jumps over the lazy dog"

x = set(s.lower())
x.remove(" ")
print(x == set(string.ascii_lowercase))


print( 'sting ascii',string.ascii_lowercase)
print( 'string set',set(string.ascii_lowercase))

