# Программа берет данные пользователя и сохраняет их

# Приветствие

print("Привет, ответь на несколько вопросов.")

# Переменные и ввод данных

n={}

n['name'] = input("Как тебя зовут?:")
n['surname'] = input("Напиши свою фамилию:")
n['age'] = int(input("В каком году ты родился? Например '1999':"))
n['hobby'] = input("Какое у тебя хобби?:")
n['date_of_birth'] = 2016 - n['age']

# Вывод данных

data = "Я узнал что тебя зовут %s %s, тебе %i лет. Твое хобби %s." % (n['name'], n['surname'], n['date_of_birth'], n['hobby'] )
print(data)
print("Спасибо за участие")

# Сохранение данных

file_info = open("info.txt", "w")
file_info.write(data)
file_info.close()



