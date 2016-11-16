# notice before start
print('Notice:\n to record your answer file will be created results.txt'
      '\n it will be saved in the current folder'
      '\n if a file with that name exists it will be overwritten')
import os
print('\n Current folder:'+ os.getcwd())

# user's profile
import collections
profile=collections.OrderedDict()
profile['first_name']=str(input('What is your first name? '))
profile['last_name']=str(input('What is your last name? '))
profile['city'] = str(input('Where do you live?(name of the city or village) '))
while True:
    try:
        profile['age']=int(input('How old are you? '))
        print('Good!')
        break
    except (TypeError,ValueError):
        print('Write again ')

# output to the screen
print('\n Check:')
for k, v in profile.items():
    print (k,'->', v)
print('Nice to meet you %s %s, who lives in %s.' % (profile['last_name'], profile['first_name'], profile['city']))

# write the results to a file
file = open('results.txt', 'w')
file.write(str(profile))
file.close()
