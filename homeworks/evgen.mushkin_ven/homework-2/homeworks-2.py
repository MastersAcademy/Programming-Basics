dict_a = {
    "first_name": "Evgen",
    "last_name": "Mushkin",
    "dob": "1989-09-05",
}

print(dict_a)

for k, v in dict_a.items():
    print(k + ": " + v)

dict_a['hobbis'] = ['fishing', 'studing']

dict_b = {
    'cat': {
        'name': 'Murzik',
        'color': 'whit',
        'age': '12'
    }
}
dict_a['pet'] = dict_b
print(dict_a)

print("=== *** manipulation set *** ===")
list_a = [1,2,3,4,4,4,'a',7,8,9,9,9,9,"hi"]
print(list_a)
print(set(list_a))
