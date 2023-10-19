''' print following pattern
    1
    22
    333
    4444
    55555'''


for i in range(1,6):
    for j in range(i):
        print(i, end='')
    print()

print('-------------------------')

for i in range(5,0,-1):
    for j in range(i):
        print(i,end='')
    print()