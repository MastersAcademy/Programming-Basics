
personal_info = {
    'name': 'Vadim',
    'surname': 'Perenesenko',
    'age': '19'
}

print(personal_info)
file = open("result.txt", "w")
file.write(str(personal_info))
file.close()

file = open("result.txt", "r")
print("*** Reading file ***")
print(file.read())
