print('===========================================')
print("Hello. Fill next fields:")
print('===========================================')
while True:
    f1 = input('What is you name? (1/4) ')
    while True:
        if not f1 or f1.isspace():
            print("Value can't be empty")
            f1 = input('Type you name? (1/4) ')
        else:
            break
    f2 = input('What is you surname? (2/4) ')
    while True:
        if not f2 or f2.isspace():
            print("Value can't be empty")
            f2 = input('Type you surname? (2/4) ')
        else:
            break
    f3 = input("Your age? (3/4) ")
    while True:
        try:
            f3 = int(f3)
            while True:
                if f3 >= 110 or f3 <= 6:
                    f3 = input('Are you seriously? ')
                    while True:
                        try:
                            f3 = int(f3)
                            break
                        except ValueError:
                            f3 = input('Value must be integer!!: ')
                else:
                    break
            break
        except ValueError:
            f3 = input('Value must be integer!: ')
    f4 = input("Why do you start study this language? (4/4) ")
    info = '\nDo you know that your name and surname together have ' + \
          str(len(list(f1+f2))) + ' symbols and ' + str(len(set((f1+f2)))) + ' non repeat symbols?\n'
    print(info)
    print('===========================================')
    answers = {'name': f1, 'surname': f2, 'age': f3, 'opinion': f4}
    out = "Your answers was: \n" + answers['name'] + ' ' + answers['surname'] + '\n' + str(answers['age']) + '\n' +\
          answers['opinion']
    print(out)
    print('===========================================')
    f5 = input('Thank you. Do you want add new user? [Yes/No] (Yes) ')
    no = ['No', 'N', 'n', 'no']
    print('===========================================')
    stdout = open('log.txt', 'a')
    stdout.write('\n###########################\n' + out + '\n###########################\n')
    if f5 in no:
        stdout.close()
        print('Bye')
        break
