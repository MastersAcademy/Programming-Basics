print("Hello, may you answer on a quiz?")
answ = input()
if answ == 'yes' or answ =='Y' or answ =='Yes' or answ =='y' or answ =='YES':
	name = input("Please enter your name:")
	last_name = input("Please enter you last name:")
	age = input("Please enter your age:")

	dict_data = {
    	'name': name,
    	'last_name':last_name,
    	'age': age
	}

	print('Thanks for responding! You have entered next data:')
	for i in dict_data:
		print(i+': '+dict_data[i])

else:
	print('Goodbye!')
