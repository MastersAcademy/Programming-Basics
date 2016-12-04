#head of request

print("Please provide us with the following information")

#body of request

fullname = input("What is your full name? ")
country = input("What is your country of residence? ")
age = int(input("How old are You? "))
email = input("What is your email adress? ")

#result of request

result = ("Your full name is %s, You are %i years old, you live in %s, and we can contact you with %s. Thank you." % (fullname, age, country, email))
print (result)

#save to file

f= open ('following-information.txt', 'w')
f.write (result)
f.close ()
