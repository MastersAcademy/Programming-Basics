# Программа берет данные пользователя и сохраняет их

# Приветствие

print("Привет, ответь на несколько вопросов.")

# Переменные и ввод данных

name = input("Как тебя зовут?:")
surname = input("Напиши свою фамилию:")
age = int(input("В каком году ты родился? Например '1999':"))
hobby = input("Какое у тебя хобби?:")
date_of_birth = 2016 - age

# Вывод данных

data = "Я узнал что тебя зовут %s %s, тебе %i лет. Твое хобби %s." % (name, surname, date_of_birth, hobby)
print(data)
print("Спасибо за участие")

# Сохранение данных

file_info = open("info.txt", "w")
file_info.write(data)
file_info.close()
