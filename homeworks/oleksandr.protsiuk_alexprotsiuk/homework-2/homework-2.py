#! usr/bin/env Python3

a_list_of_questions = ['What is your name?','How old are you?','Where are you from?']  #list with questions for user
a_list_of_keys = ['Name','Age','City'] # list with keys of dictionary
a_list_of_answers = [] # empty list for user answers
a_dict ={}   # emty dictionary. we will create user data in it
counter = [0, 1, 2]  # iterable list

for s in counter:   #in this block user have to answer the question.
    print (a_list_of_questions[s])
    a_list_of_answers.append(input())  # answers adding to a_list_of_answers
    a_dict[a_list_of_keys[s]] = a_list_of_answers[s]  # creating a dictionary with user-data

a_file = open('data.txt', 'w')  # open file to write user-data in it

for s in a_list_of_keys :  # writting data from a dictionary to txt-file
    print (s , a_dict[s] )
    line = (s + ':' + a_dict[s] + '\n')
    a_file.write(line)

a_file.close()

print('Data saved in data.txt file')
