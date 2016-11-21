print('===========================================')
print("Hello. Fill next fields:")
print('===========================================')
f1 = input('What is you name? (1/4) ')
f2 = input('What is you surname? (2/4) ')
f3 = input("Your age? (3/4) ")
f4 = input("Why do you start study this language? (4/4) ")
info = '\nDo you know that your name and surname together have ' + \
      str(len(list(f1+f2))) + ' symbols and ' + str(len(set((f1+f2)))) + ' non repeat symbols?\n'
print(info)
print('===========================================')
answers = {'name': f1, 'surname': f2, 'age': f3, 'opinion': f4}
out = "Your answers was: \n" + answers['name'] + ' ' + answers['surname'] + '\n' + answers['age'] + '\n' + answers['opinion']
print(out)
print('===========================================')
print('Thank you. Bye')
print('===========================================')
stdout = open('log.txt', 'a')
stdout.write(out)
stdout.close()
