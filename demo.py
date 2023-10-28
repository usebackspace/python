# Remove whitespace characters from the left of the string.
string = "   Hello, world!"
stripped_string = string.lstrip()
print(stripped_string)

# Output: Hello, world!

# Remove the leading characters "abc" from the string.
string = "abcHello, world!"
stripped_string = string.lstrip("abc")
print(stripped_string)

# Output: Hello, world!
