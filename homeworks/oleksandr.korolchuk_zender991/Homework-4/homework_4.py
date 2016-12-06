print('Hello, young padawan')

answer = 'Y'

full_dictionary = {}
homework_dictionary = {}
counter = 0

while answer == 'Y':
    print('--- ===== **** ==== ----')
    homework_dictionary['age'] = input('How old are you? - ')


    homework_dictionary['name'] = str(input('What is your name? - '))

    if homework_dictionary['name'] == 'Justin Bieber':
        print ('No, Justin Bieber, go home!')
        continue


    homework_dictionary['country'] = str(input('Where are you from? - '))

    if homework_dictionary['country'] == 'Russia':
        print('Moskaliaku na giliaku!')
        continue
    elif homework_dictionary['country'] == 'Ukraine':
        print('Slava Ukraini')



    full_dictionary[counter] = homework_dictionary
    counter += 1

    homework_dictionary = {}
    answer = str(input('Do you want to continue (Y or N)? - '))

print('--- ===== **** ==== ----')
print('All records:')

for k,v in full_dictionary.items():
    print('| - ' + str(k) + '  --  ' + str(v))
    print()

print('--- ===== **** ==== ----')
print('Enter number and see list of users depends of age: -')
print('1. Children')
print('2. Teenagers')
print('3. Normal')
print('4. Old')
choose_list = int(input('What are you want? - '))


temp_list = []
if choose_list == 1:

    for k, v in full_dictionary.items():
        for q, w in v.items():
            if q == 'age' and int(w) in range(0,14):
                get_name = v.get('name')
                temp_list.append(get_name)
    print('List of children:' + '\n' + str(temp_list))

if choose_list == 2:

    for k, v in full_dictionary.items():
        for q, w in v.items():
            if q == 'age' and int(w) in range(14,20):
                get_name = v.get('name')
                temp_list.append(get_name)
    print('List of teenagers:' + '\n' + str(temp_list))

if choose_list == 3:

    for k, v in full_dictionary.items():
        for q, w in v.items():
            if q == 'age' and int(w) in range(20,55):
                get_name = v.get('name')
                temp_list.append(get_name)
    print('List of normal:' + '\n' + str(temp_list))


if choose_list == 4:

    for k, v in full_dictionary.items():
        for q, w in v.items():
            if q == 'age' and int(w) in range(55,100):
                get_name = v.get('name')
                temp_list.append(get_name)
    print('List of old:' + '\n' + str(temp_list))