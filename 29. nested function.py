
print('------Nested Function------')
def outer_function():
    def inner_function():
        print('Innner Function')
    print('Outer Function')
    inner_function()
# Call the outer function
outer_function()

print()

#===================================================================================

print('------ Nested Function With Return Statement-----------')
def outer_function():
    def inner_function():
        return ('Innner Function')
    return inner_function() + '  ' + 'Outer Function'
# Call the outer function
print(outer_function())

print()

#====================================================================================

print('-----Returning Nested Function To The Variable----')
def outer_function():
    def inner_function():
        return ('Innner Function')
    final_result= inner_function() + '  ' + 'Outer Function'
    return final_result
# Call the outer function
x=outer_function()
print(x)
