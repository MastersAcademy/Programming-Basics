import random

first_file = open('hello.txt', 'r')

second_file = open('results.txt', 'w')

hello_message = first_file.read()

for line in hello_message:
	print(line, end='')


name = input('What is your name? - ')

age = input('How old are you? - ')

desire = input('What are you want to buy? - ')


if int(age) > 18:
	age_answer = 'You are not schoolboy'
else:
	age_answer = 'Probably, you are schoolboy'


discount = random.randint(100, 1000)



full_answer = "Hello %s. %s as I see. If you want to buy a %s, here is your discount %i code" % (name, age_answer, desire, discount)


print('-------=============================-----------')
print(full_answer)
print('-------=============================-----------')

second_file.write(full_answer)

first_file.close()
second_file.close()