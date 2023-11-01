print('------ 1.Function Returning Another Function ------')
def create_machine():
    def machine():
        return("Machine Designed")
    print('Machine Blueprint')
    return machine

design = create_machine()
print(design())

print()

#====================================================================================
print('------ 2.Function Returning Another Function ------')
def create_machine(mach):
    print('Machine Blueprint 2')
    return mach

def machine():
    return("Machine Designed 2")

design = create_machine(machine)
print(design())

print()

#===================================================================================
print('------ 3.Function Returning Another Function ------')
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

# Create a function that multiplies by 2
multiply_by_2 = create_multiplier(2)

# Create a function that multiplies by 3
multiply_by_3 = create_multiplier(3)

# Use the created functions
result1 = multiply_by_2(5)  # This will return 10 (5 * 2)
result2 = multiply_by_3(7)  # This will return 21 (7 * 3)

print('multiply by 2:',result1)
print('multiply by 3:',result2)
