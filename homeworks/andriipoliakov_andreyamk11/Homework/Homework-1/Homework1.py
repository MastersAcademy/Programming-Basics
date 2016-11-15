print("Введите данные для анкеты\n")
name = input("Как тебя зовут?\n")
surname = input("Какая у тебя фамилия?\n")
age = int(input("Сколько тебе лет?\n"))
country = input ("В какой стране ты живешь?\n")
city = input("В каком городе ты живешь?\n")
hobby = input("Какое у тебя хобби?\n")
print ("Анкета\n Имя: %s\n Фамилия: %s\n Возраст: %i\n Адрес: %s %s\n Хобби: %s\n" %(name, surname, age, country, city, hobby))

f = open('anketa.txt', 'w', encoding='utf-8')
f.write("Анкета\n Имя: %s\n Фамилия: %s\n Возраст: %i\n Адрес: %s %s\n Хобби: %s\n" %(name, surname, age, country, city, hobby))
f.close()

print ("Данные записаны в файл anketa.txt")
