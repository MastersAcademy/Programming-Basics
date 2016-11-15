# the variable is assigned a demo file
fileName = 'demo.txt'
# It opens the file for writing only. Index stands at the beginning of
# the file. Creates a file with the filename, if such does not exist.
accessMode = 'w'
# Collections(Dictionaries)
user_info = {
    'user_name': str(input('What is your name? ')),
    'user_surname': str(input('What is your surname? ')),
    'age': int(input('How old are you? ')),
    'user_car': {
        'car_make': str(input('what brand of your car? ')),
        'color': str(input('What color car? '))
    }
}
all_info = (
' I %s %s, \n I am %s, \n mark my car %s, \n car color %s' % (user_info['user_name'], user_info['user_surname'],user_info['age'], user_info['user_car']['car_make'],user_info['user_car']['color']))
print(all_info)

myFile = open(fileName, accessMode)
myFile.write(all_info)
myFile.close()
