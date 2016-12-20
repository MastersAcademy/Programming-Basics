print ("Hello! We are glad to see you on our site! To create account please answer the following questions:")
name = str(input("Your name?"))
surname = str(input("Your surname?"))
age = int(input("Your age?"))
if age > 17 or age == 17:
    'pass'
elif age < 17:
    print('We are sorry, but we think you are not old enough to come to our party:(')
    exit()


if age > 99:
    print('We don`t think you`ve said truth.')
    exit()


job = str(input("Your job?"))
if job == 'programmer' or job == 'web-developer':
    print('Great!:)')
else:
    print('We think you know that our party is for programmers only...')
    exit()


phone = input("Your phone number?")
data = ("Name, surname: %s %s; age: %s; job: %s; phone number: %s."%(name, surname, age, job, phone))
print(data)
file = open ("data.txt", "w")
file.write(data)
file.close()

"""
I know this stuff is lack of sense,
but I'm too tired to think about something more logical.
Sorry...
"""


print('')
print('')


print("Ok. We need some products for our party. Everyone should bring something one day before it.")
question = input("Are you going to?")
print("If for sure it doesn't depend on your answer:) So here are some products to buy, and please check their freshness:")


print('')
print('')


print("---- ==== **** Product List **** ==== ----")
list_a = ['sugar', 'eggs', 'bread', 'salt', 'pepper', 'lemon', 'milk', 'cheese', 'sausage']
for i in list_a:
    print('* ' + str(i))

print('')
print('')



print ("---- ==== **** To Be More Precise **** ==== ----")
numbers_p = {
    'sugar': '4lb',
    'eggs': '30',
    'bread': '8',
    'salt': '1lb',
    'pepper': '2oz',
    'lemon': '3',
    'milk': '5quarts',
    'cheese': '5lb',
    'sausage': '6lb'

}
for k, v in numbers_p.items():
    print (k + ': ' + v)


print('')
print('')

print("We hope the bags won't be too heavy for you:) See you!")