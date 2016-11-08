# One line comment

"""
Multiline
comment.
"""

# Defining variables
hello_string = 'Hello'
world_string = 'World'
one_int = 1
two_int = 2
pi_float = 3.14
bool_true = True

# Printing
print('--- === Printing === ---')
print(hello_string)
print(hello_string[1])

# Data types
print('')
print('--- === Data types === ---')
print(hello_string.__class__)
print(one_int.__class__)
print(pi_float.__class__)
print(bool_true.__class__)

# Using variables
print('')
print('--- === Using variables === ---')
hello_world_one = hello_string + ' ' + world_string
hello_world_two = "%s %s" % (hello_string, world_string)
three_int = one_int + 2

print(hello_world_one)
print(hello_world_two)
print(three_int)
print(pi_float + three_int)
print(str(pi_float + three_int) + ' ' + str((pi_float + three_int).__class__))


# Reassignments
print("Hello world old: " + hello_world_one)
hello_world_one = "Hello World Reassigned"
print("Hello world new: " + hello_world_one)
hello_world_one = 125
print("Hello world integer: %i" % hello_world_one)
