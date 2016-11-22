print ('-=Приветствуем вас на нашем сайте,для продолжения работы заполните анкету=-')

name = input('Как вас зовут?\n')
surname = input('Какая ваша фамилия?\n')
age = input('Сколько вам лет?\n')
hobby = input('Какое ваше хобби?\n')
mail = input('Введите свой E-mail\n')
print ('Спасибо, давайте уточним информацию')

name='Сергей'
surname='Семиз'
age='21'
hobby='спорт,книги'
mail='80937588895@mail.ru'


dict = {
    'Ваше имя:': name,
    'Ваша фамилия:': surname,
    'Вам:': age,
    'Ваше хобби:':hobby,
    'Ваш e-mail:':mail,
    }


K=open('questionnaire_2.txt','w')
result=('имя: '+dict['Ваше имя:']+'\n'+'фамилия: '+dict['Ваша фамилия:']+'\n'+'Лет: '+(dict['Вам:'])+'\n'+'Хобби: '+dict['Ваше хобби:']+'\n'+'e-mail: '+dict['Ваш e-mail:'])
print(dict)
K.write(result)
K.close()
