print('---- 1.Union (| or union()) ----')

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union_set = set1 | set2
union_set = set1.union(set2)

print(union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

print()

#================================================================================================================

print('---- 2. Intersection (& or intersection())----')

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# intersection_set = set1 & set2
intersection_set = set1.intersection(set2)

print(intersection_set)  # Output: {4, 5}
print(set1)

print('---- 2.1 Intersetion Update ---')
set1.intersection_update(set2)
print(set1) 
print()

#================================================================================================================

print('---- 3. Difference (- or difference())----')

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# difference_set = set1 - set2
difference_set = set1.difference(set2)

print(difference_set)  # Output: {1, 2, 3}

print(set1)

print()

print('----3.1 Difference Update ----')
# Example sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Using difference_update to remove 
# elements common to both sets from set1
set1.difference_update(set2)
s=set1.difference_update(set2)
print(set1)
print(s)

print()

#================================================================================================================

print('---- 4. Symmetric Difference (^ or `symmetric_difference()`) ----')

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# symmetric_difference_set = set1 ^ set2
symmetric_difference_set = set1.symmetric_difference(set2)

print(symmetric_difference_set)  # Output: {1, 2, 3, 6, 7, 8}

print()

print('---- 4.1 Symmetric diffrence Update ----')


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set1.symmetric_difference_update(set2)
s=set1.symmetric_difference_update(set2)

print(set1)
print(s)

#==================================================================================================================

print('----5. Subset (issubset())----')

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

is_subset = set1.issubset(set2)
print(is_subset)  # Output: True

print()

#==================================================================================================================

print('----6. Superset (issuperset())----')

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

is_superset = set1.issuperset(set2)
print(is_superset)  # Output: True

print()

#==================================================================================================================

print('----7. Disjoint Sets----')
set1 = {1, 2, 3}
set2 = {4, 5, 6}

are_disjoint = set1.isdisjoint(set2)
print(are_disjoint)  # Output: True

print()

