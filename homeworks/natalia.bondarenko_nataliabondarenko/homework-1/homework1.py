# notice before start
print('Notice:\n to record your answer file will be created results.txt'
      '\n it will be saved in the current folder'
      '\n if a file with that name exists it will be overwritten')
import os
print('\n Current folder:'+ os.getcwd())

# user's profile    
first_name=str(input('What is your first name? '))
last_name=str(input('What is your last name? '))
city = str(input('Where do you live?(name of the city or village) '))
while True:
    try:
        age=int(input('How old are you? '))
        print('Good!')
        break
    except (TypeError,ValueError):
        print('Write again ')

# output to the screen       
print('Check: '+'Your name '+first_name+' '+last_name+ '.'' You live in '+city+ '.')
print('Your age is', age)
print('Nice to meet you %s %s, who lives in %s.' % (last_name, first_name, city))

# write the results to a file
result='first name - %s, last name - %s, city - %s, age - %i.'%(first_name, last_name, city, age)
file = open('results.txt', 'w')
file.write(result)
file.close()

