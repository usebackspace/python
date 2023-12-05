print('----- Coping of List Using "Copy" Method --------')
original_list = [1, [2, 3], 4]
shallow_copy = original_list.copy()
print('----- Modifying Nested List : Effect will reflect on both the list (original and shallow list) -----')

original_list[1][0] = 'X'
print(original_list)    
print(shallow_copy)     

print('----- Modifying List : Effect will reflect only on one list on which we have modified -----')

original_list[0] = 'Z'
shallow_copy[2] ='B'
print(original_list)    
print(shallow_copy)     

print()

#==========================================================================================================
print('----- Coping of List Using "Deepcopy" Method --------')
import copy

original_list = [1, [2, 3], 4]
deep_copy = copy.deepcopy(original_list)
print('---- In Deep Copy it changes values only in one list -----')

original_list[1][0] = 'X'
deep_copy[1][1] = 'Y'

print(original_list)    
print(deep_copy)        
