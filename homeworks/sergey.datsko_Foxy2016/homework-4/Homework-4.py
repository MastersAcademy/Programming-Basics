print("Hello, you can reply to questions? Press 'Yes' or 'No'. ")
answ = input()
if answ == 'no' or answ =='No' or answ=='NO' or answ =='n' or answ =='N':
        print ("Sadly, you can go back to the beginning and the answer is yes?")
if answ == 'yes' or answ =='Yes' or answ =='YES' or answ =='y' or answ =='Y':
	Name = input("What is your name?: ")
	Age = input("How old are you: ")
	Hooby = input("What is your hobby?: ")

	dict_data = {
    	'Name': Name,
    	'Age':Age,
    	'Hooby': Hooby
	}

	print('Thanks for responding, entries lower:')
	for i in dict_data:
		print(i+': '+dict_data[i])
else:
	print('Bye!)')
