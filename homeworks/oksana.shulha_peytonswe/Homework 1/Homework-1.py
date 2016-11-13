name = input("What is your name? ")
surname = input("What is your surname? ")
gender = input("What is your gender? ")
year_of_birth = int(input("In what year were you born? "))
age = int(2016 - year_of_birth)
place_of_birth = input("Where you from? ")
nationality = input("What is your nationality? ")
address = str(input("What is your home address? "))
profession = input("What is your profession? ")
phone_number = str(input("What is your phone number? "))
email_address = str(input("What is your email address? "))


info = str("Well, your name is %s, you're a %s.\n"
       "You was born in %i and you're %i years old.\n"
       "You're from %s, your nationality is %s.\n"
       "You live at %s and your employment is %s.\n"
       "Your contact information: phone %s, email %s.\n"
           % (name + ' ' + surname, gender, year_of_birth,
              age, place_of_birth, nationality,
              address, profession, phone_number, email_address))

print (info) 

form = open('form.txt', 'w')
form.write (info)
form.close()
