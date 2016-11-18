import time
print("Nice to meet you!")
time.sleep(2)
print("---===+++ Waiting for loading +++===---")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Loading complete")
time.sleep(1)

# block of questions
first_name = input("What is your fist name?")
surname = input("What is your surname?")
age = int(input("How old are you?"))
study = input("Where are you study (or studied)?")

print("Ok. Your name is %s and your surname is %s. We know that "
      "your age is %i and you are study (or studied) in %s. It's very good, but we need more "
      "information about you. Please, give answers for few questions:)" % (first_name, surname, age, study))

gender = input("What is your gender?")
address = input("Where do you live?")
address_term = int(input("How long you live there?(in years)"))
job = input("Where you want to work?")
payment = int(input("How much you want to earn per month?(in USD)"))
full_name = "%s %s" % (first_name, surname)
time.sleep(2)
print("Nice job!!!")
time.sleep(2)
print("Let's see you results:")
time.sleep(2)
print("Your full name is %s,  your age is %i, you gender is %s (we hope so). You live in %s during %i years and study\
 (or studied) in %s." % (full_name, age, gender, address, address_term, study))
print("Also we know that you want to work in %s, and you  want to get %i dollars per month" % (job, payment))

hobby = input("What hobbies you have?")
skill = input("What is your main skill?")

# add dictionaries
dict_1 = {'Student': {'Name': first_name,
                      'Last name': surname,
                      'Age': age,
                      'Gender': gender},
          'hobby': hobby,
          'skill': skill}

dict_2 = {"Address": address,
          'Living during': address_term,
          'Education': study}
print(dict_1)
dict_1['other'] = dict_2
time.sleep(3)
print(dict_1)

# add lists
print("***** Data list *****")
list_1 = [first_name, surname, gender]
print(list_1)
time.sleep(3)
print("Data list updating")
time.sleep(3)
list_1.append(age)
print(list_1)
time.sleep(3)
print("------- Loading addition data list ------")
list_2 = [address, study, job]
time.sleep(3)
print(list_2)
time.sleep(3)
print("Wait a moment. List is updating")
list_3 = [list_1, list_2, hobby, skill]
time.sleep(3)
print(list_3)
time.sleep(3)
print("_____ Formatting data_____")
list_2.remove(study)
list_2.remove(job)
time.sleep(2)
print(list_3)
time.sleep(2)
print("===== STREAMLINE DATA =====")
time.sleep(2)
list_3.sort()
print(list_3)
time.sleep(3)
list_3.sort(reverse=True)
time.sleep(3)
print("**** Creating unique data ****")
set_1 = set(list_3)
time.sleep(3)
print(set_1)
time.sleep(4)

# print("Thank you for using this app. We made a short resume of you personal data.")
# print("You can see that in RESUME.txt")

# info saving
# resume = "Full name - %s. Gender - %s. Age - %i. Living place - %s. Wanted place of job - %s. Wanted payment - %i." \
#          % (full_name, gender, age, address, job, payment)
#
# file = open("RESUME.txt", 'w')
# file.write(resume)
# file.close()
#
# # start of info checking
# time.sleep(5)
# print("---===Wait for file checking===---")
# print("5")
# time.sleep(1)
# print("4")
# time.sleep(1)
# print("3")
# time.sleep(1)
# print("2")
# time.sleep(1)
# print("1")
# time.sleep(1)
#
# # info checking
# print("Data content:")
# content = open("RESUME.txt")
# content_string = content.read()
# print(content_string)
#
# print("Good luck and see you later!!!")
