# Initialize an empty set
set_data = set()

# Get the number of elements in the set from the user
num = int(input("Enter the number of elements in the set: "))

for i in range(num):
    x = input(f"Enter element {i + 1}: ")
    set_data.add(x)

print("User's set:", set_data)
