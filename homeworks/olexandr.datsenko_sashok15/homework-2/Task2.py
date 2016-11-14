personal_information = {
    'name': 'Sashka',
    'surname': 'Datsenko',
    'age': '19',
    'city': 'Poltava',
    'university': 'CHDTU'
}

print(personal_information)
f = open('homework-2.txt', 'r')
f = open('homework-2.txt', 'w')
f.write(str(personal_information))
f.close()
