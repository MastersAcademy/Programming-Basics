personal_information = {
    "name": "Valik",
    "surname": "Pavlenko",
    "dob": "14-02-1999",
    "age": "17",
    "city": "Cherkasy",
    "school": "Chercasy №4"
}
for k, v in personal_information.items():
    print (k + ': ' + v)
personal_information['hobbies'] = ['computer games', 'reading are books']
print (personal_information)
