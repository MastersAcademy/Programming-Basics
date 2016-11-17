#head of request

print("Please provide us with the following information")

#body of request

fullname = input("What is your full name?\n")
country = input("What is your country of residence?\n")
age = int(input("How old are You?\n"))
email = input("What is your email address?\n")

#result of request

result = ("Your full name is %s, You are %i years old, you live in %s, and we can contact you with %s. Thank you.\n\n" % (fullname, age, country, email))
print(result)

#additional information

print("Please provide us with the additional information")

hobby = input("What is your hobby?\n")
book = input("What is your favorite book\n")
dream = input("What is your dream\n")

#dictionaries

dict_a = {
    'Name': fullname,
    'Country': country,
    'Age': age,
    'Email': email
    }
dict_a['profession'] = ['teacher']

dict_b = {
    'Hobby': hobby,
    'Book': book,
    'Dream': dream
}
dict_a['additional information'] = dict_b

print(dict_a)

#save to file

f = open('following-information.txt', 'w')
f.write(result)
f.close()
