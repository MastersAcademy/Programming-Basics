print '--- === *** Dictionaries *** === --- '

dict_a = {
    'first_name': 'Dmitry',
    'last_name': 'Zhuk',
    'dob': '1987-04-11'
}
print dict_a
print dict_a['first_name']

for k, v in dict_a.items():
    print k + ': ' + v

dict_a['hobbies'] = ['computer games', 'reading', 'studying']
print dict_a

dict_b = {
    'cat': {
        'name': 'Hort',
        'color': 'black',
        'age': '3'
    },
    'dog': {
        'name': 'Bars',
        'color': 'white',
        'age': '11'
    }
}

dict_a['pet'] = dict_b
print dict_a

