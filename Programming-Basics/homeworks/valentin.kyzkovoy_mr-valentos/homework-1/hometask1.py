print("______________________Welcome________________________")
print("If you want to find a job, please fill in the form!!!")

file_info = open("finfo.txt", "w")

name = input("What is your name? ")
surname = input("What is your surname ")
age = int(input("How old are you? "))
city = input("Where do you live? ")
previous_job = input("Where did you work? ")
experience = input("What is your work experience? ")
name_surname = name + ' ' + surname


info = "Thank you %s, your age is %i. \n We will try to find work in the city %s." \
       " \n Job vacancy - %s \n Experience - %s" % (name_surname, age, city, previous_job, experience)

print(info)
print("We will send you letter, check your postbox.")

file_info.write(info)
file_info.close()