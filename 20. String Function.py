# Sample string
text = "Elsa is a good girl"
text1='Captain'
text2='      Avengers      '


# Basic String Functions
print(text+text1)
print(text1*5)
print("Length of string:", len(text))

print()

# String Methods
print('-------------String Methods------------')
text = "Elsa is a good girl"
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Casefold:", text.casefold()) # It also convert String into Lower case but in more Stronger Way
print("Capitalized:", text.capitalize()) # Captial Only First letter of the String, if space comes first after  that letter then it will not capital the word
print("Title Case:", text.title())  # Captial First Letter of each word

print()

# Strip Method
print('---------- Strip Methods----------')
text2='      Avengers      '
print("Stripped:", text2.strip())
print("Left Stripped:", text2.lstrip())
print("Right Stripped:", text2.rstrip())

# Remove the leading characters "abc" from the string.
string = "abcHello, world!"
stripped_string = string.lstrip("abc")
print(stripped_string)

# Output: Hello, world!

string = "abcHello, world!"
stripped_string = string.rstrip("ld!")
print(stripped_string)

# Output: Hello, wor

print()

print('---------Starting And Ending  And Replace String-------------')
text = "Elsa is a good girl"
print("Starts with 'Elsa':", text.startswith("Elsa"))
print("Ends with 'girl':", text.endswith("girl"))
print("Replaced 'Elsa' with 'Anna':", text.replace("Elsa", "Anna"))

print()

# String Slicing
print('---------- Slicing of String------------')
print("First 5 characters:", text[:3])
print("Last 6 characters:", text[-3:-1])


print()


# Count Method
print('--------- Count Method ----------')

print('----- Counting String-----')
text = "Hello, Hello, World"
count = text.count("Hello")
print(count)  # Output: 2
print(text.count("o"))  # Output: 2


print('-----Counting List------')
numbers = [1, 2, 3, 2, 4, 2, 5]
count = numbers.count(2)
print(count)  # Output: 3

print('------Counting Tuple ------')
fruits = ("apple", "banana", "apple", "cherry", "apple")
count = fruits.count("apple")
print(count)  # Output: 3


# Find Method
print('-------- find And index Method ---------')
text = "Hello, World! This is a sample text."
# Using the find and index method
fnd = text.find('l')
ind = text.index('l')
print("find method:",fnd)
print("index method:",ind)

# fnd = text.find('e')
# ind = text.index('e')
# print("find method:",fnd)
# print("index method:",ind)


# Using the find and index not available method
print('------- find and index not available -------')
text = "Hello, World! This is a sample text."
fn = text.find('z')
# nd = text.index('z')
print("find method:",fn)
# print("index method:",nd)


print()

# rfind Method
print('-------- rfind And rindex Method ---------')
text = "Hello, World!"
# Using the find and index method
rfnd = text.rfind('l')
rind = text.rindex('l')
print("find method:",rfnd)
print("index method:",rind)

# Using the find and index not available method
print('------- rfind and rindex not available -------')
rfnd = text.find('z')
# rind = text.index('z')
print("find method:",rfnd)
print("index method:",rind)

print()

# String Splitting
print('---------- String Spliting Method----------')
print('----- Splitting using default delimeter----')
text = "Hello, World! This - is a sample text." 
words = text.split()
print(words)
words = text.split("-")
print("Spliting using space:", words)

print()

print('------ Spliting using ","------')
data = "apple,banana,orange,grape"
fruits = data.split(',')
print(fruits)

print()

print('----- Specifying a maximum number of split ------')
sentence = "This is a sample sentence with many words."
words = sentence.split(" ",3)
print(words)

print()

# String Join method
print('----------String Join Method---------')
words = ["Hello", "World", "Python"]
# separator = " "
# result = separator.join(words)
result = " 420 ".join(words)
print(result)

print()

text = "Hello how are you"
separator = "*"
result = separator.join(text)
# result = "+".join(text)
print(result)


# String Checks
print('---------String Check Methods-------------')
text='123456'
text1='Avengers'
text3='Avengers123'
text4='avenger'
text5='AVENGERS'
text6='١٢٣१२३⅒½'
print("Is it isdigit?", text.isdigit())
print("Is it alphabetic?", text1.isalpha())
print("Is it alphanumeric?", text3.isalnum())
print("Is it in lowercase?", text4.islower())
print("Is it in uppercase?", text5.isupper())
print("Is it numeric?", text6.isnumeric())
print("Is it digit?", text6.isdigit())


print()

print('----- Swapcase ------')
text = "Hello, World!"
swapped_text = text.swapcase()
print(swapped_text)


