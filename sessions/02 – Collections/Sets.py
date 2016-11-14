print '--- === *** LISTS *** === --- '
list_a = [1, 2, 3, 4, 5, 1, 6, 7, 2, 8, 9, 'a', 5, 7, 2, 3.14, 'hello']

print list_a
print set(list_a)

set_a = set(list_a)
print set_a
print set_a.__class__

list_from_set_a = list(set_a)
print list_from_set_a
print list_from_set_a.__class__
