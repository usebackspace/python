def length_of_string(string):
    count = 0
    for _ in string:
        count = count + 1
    return "The length of string is "+ string + " "+ str(count)

print(length_of_string("OMKAR"))