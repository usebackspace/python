print('----- Nested For loop ----')

set1 = {1, 2, 3}
set2 = {'a', 'b', 'c'}

for i in set1:
    for j in set2:
        print(i,j)

print()

#===================================================================================================

print('----- Nested For loop Using set Comprehension ----')
set1 = {1, 2, 3}
set2 = {'a', 'b', 'c'}

pairs = {(x, y) for x in set1 for y in set2}

print(pairs)

print()

#===================================================================================================

