print('--- === *** LISTS *** === --- ')
list_a = [1, 2, 3, 4, 5, 1, 6, 7, 2, 8, 9, 'a', 5, 7, 2, 3.14, 'hello']
print(list_a)
print(list_a[0])
print(list_a[4])
print(len(list_a))

print('--- === ***       *** === ---')
list_a.append('world')
print(list_a)
list_a.extend('extend')
print(list_a)

print('--- === ***       *** === ---')
print(list_a)
list_a.remove('a')
print(list_a)
del list_a[2]
print(list_a)
list_a.pop(2)
print(list_a)
list_a.pop()
print(list_a)

print('--- === ***       *** === ---')
print(list_a)
print(sorted(list_a))
print(sorted(list_a, reverse=True))
print(list_a)
list_a.sort()
print(list_a)
list_a.sort(reverse=True)
print(list_a)

print('--- === ***       *** === ---')
list_b = ['aye', 'aye', 'captain']
list_c = [list_a, list_b, 'hello']
print(list_c)
