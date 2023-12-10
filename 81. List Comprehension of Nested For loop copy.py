print('----- Nested For loop ----')

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

for i in list1:
    for j in list2:
        print(i,j)

print()

#===================================================================================================

print('----- Nested For loop Using List Comprehension ----')
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

pairs = [(x, y) for x in list1 for y in list2]

print(pairs)

print()

#===================================================================================================

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in l:
    for j in i:
        if j%2==0:
            print(j)

even_numbers = [j for i in l for j in i if j % 2 == 0]

print(even_numbers)
