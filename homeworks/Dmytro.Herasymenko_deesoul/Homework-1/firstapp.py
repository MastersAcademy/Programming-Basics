# first block of questions
import time
first_name = input("What is your fist name?")
surname = input("What is your surname?")
age = int(input("How old are you?"))
study = input("Where are you study (or studied)?")

print("Ok. Your name is %s and your surname is %s. We know that "
      "your age is %i and you are study (or studied) in %s. It's very good, but we need more "
      "information about you. Please, give answers for few questions:)" % (first_name, surname, age, study))

gender = input("What is your gender?")
verify_gender = input("Are you sure?(YES/NO)")

# some joke addition
if verify_gender != "YES":
    print("Who are you, monster???")
if verify_gender != "NO":
    print("It's great!!!")

print("But let's continue!")

# second block of questions
adress = input("Where do you live?")
adress_term = int(input("How long you live there?(in years)"))
job = input("Where you want to work?")
payment = int(input("How much you want to earn per month?(in USD)"))
full_name = "%s %s" % (first_name, surname)
print("Nice job!!!")
print("Let's see you results:")

print("Your full name is %s,  your age is %i, you gender is %s (we hope so). You live in %s during %i years and study\
 (or studied) in %s. .)" % (full_name, age, gender, adress, adress_term, study))
print("Also we know that you want to work in %s, and you  want to get %i dollars per month" % (job, payment))

time.sleep(3)

print("Thank you for using this app. We made a short resume of you personal data.")
print("You can see that in RESUME.txt")

# info saving
resume = "Full name - %s. Gender - %s. Age - %i. Living place - %s. Wanted place of job - %s. Wanted payment - %i." \
         % (full_name, gender, age, adress, job, payment)

file = open("RESUME.txt", 'w')
file.write(resume)
file.close()

# start of info checking
time.sleep(5)
print("---===Wait for file checking===---")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

# info checking
print("Data content:")
content = open("RESUME.txt")
content_string = content.read()
print(content_string)

print("Good luck and see you later!!!")
