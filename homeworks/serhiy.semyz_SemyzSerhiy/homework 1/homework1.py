print ('Приветствуем вас на нашем сайте,для продолжения работы заполните анкету')

name = input('Как вас зовут?\n')
surname = input('Какая ваша фамилия?\n')
age = input('Сколько вам лет?\n')
hobby = input('Какое ваше хобби?\n')
mail = input('Введите свой E-mail\n')
print ('Спасибо, можете продолжить работу')



#Working with files and output to the screen
f=open('questionnaire.txt','w')
result=' name: %s \nsurname: %s \nAge: %s \nhobby: %s \ne-mail: %s\n'\
       %(name,surname,age,hobby,mail)
print(result)
f.write(result)
f.close()
