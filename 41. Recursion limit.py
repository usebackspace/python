
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(10)  # Setting recursion limit to the 10

i=0
def sum():
    global i
    print('sum',i)
    i+=1
    sum()
sum()

