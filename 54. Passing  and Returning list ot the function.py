print('---- Passing List To The Function ----')
def passing_list(l):
    for i in l:
        print(i)

list = [1, 2, 3, 4, 5]
passing_list(list)

print()

print('---- Returning List From The Function ----')
def even_numbers_list(n):
    result = []
    for i in range(2, n + 1, 2):
        result.append(i)
    return result

even_list = even_numbers_list(10)
print(even_list)
