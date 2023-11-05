print('--- Method 1----')
s = "It's not about how much we lost. It's about how much we have left."
ns = ""

for char in s:
	if char != " ":
		ns += char

print(ns)

print()

# Method 2
print('------- Method 2 --------')
print(s.replace(" ",""))