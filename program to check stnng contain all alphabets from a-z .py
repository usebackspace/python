
import string

s = "The quick brown fox jumps over the lazy dog"

x = set(s.lower())
x.remove(" ")
print(x == set(string.ascii_lowercase))


print( string.ascii_lowercase)
print( set(string.ascii_lowercase))

