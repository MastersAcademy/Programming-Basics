import random

first_file = open('hello.txt', 'r')

second_file = open('results.txt', 'w')

hello_message = first_file.read()

for line in hello_message:
	print(line, end='')

homework_dictionary = {

}

homework_dictionary['first_name'] = input('What is your name? - ')

homework_dictionary['age'] = int(input('How old are you? - '))

homework_dictionary['desire'] = input('What are you want to buy? - ')


if homework_dictionary['age'] > 18:
	age_answer = 'You are not a schoolboy'
else:
	age_answer = 'Probably, you are a schoolboy'


homework_dictionary['discount'] = random.randint(100, 1000)

full_answer = "Hello %s. %s as I see. If you want to buy a %s, here is your discount code %i" % (homework_dictionary['first_name'], age_answer, homework_dictionary['desire'],homework_dictionary['discount'])

print('-------=============================-----------')
print(full_answer)
print('-------=============================-----------')

second_file.write(full_answer)

first_file.close()
second_file.close()