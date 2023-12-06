# Initialize an empty dictionary
dictionary = {}

# Get the number of key-value pairs the user wants to input
num = int(input("Enter the number of entries: "))

# Loop to take input for each key-value pair
for _ in range(num):
    key = input("Enter key: ")
    value = input("Enter value: ")

    # dictionary[key] = value
    dictionary.update({key:value})

print("User Dictionary:", dictionary)
