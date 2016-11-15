# Homework_1

name = input("What is your name?")
city = input("Where do you live?")
age = input("How old are you?")
street = input("Write your street")

all_answers = (
    'Your name is: %s \n You live in: %s \n You are: %s \n Your street is named: %s' % (name, city, age, street))

doFile = open('Answers.txt', "w")
doFile.write(all_answers)
doFile.close()

# Homework_2

print("Delete the jobs that you don't like:")

listOfJobs = ['accountant', 'cleaner', 'teacher', 'software developer', 'web developer']
print(listOfJobs)
del listOfJobs[0]
listOfJobs.remove("cleaner")
listOfJobs.pop(0)
print("So, you like the jobs:")
print(listOfJobs)

print("Add jobs that you like to the remaining ones:")
listOfJobs.append('Python developer')
listOfJobs.append('Ruby developer')
print(listOfJobs)

jobPreferences = {
    'First_job': 'software developer',
    'Second_job': 'web developer',
    'Third_job': 'Python developer',
    'Fourth_job': 'Ruby developer',
}

for k, v in jobPreferences.items():
    print(k + ':' + v)
print(jobPreferences)
yourList = ('Your job preferences are: %s' % listOfJobs)

doFile = open('Answers.txt', "a")
doFile.write('\n' + str(yourList))
doFile.close()
