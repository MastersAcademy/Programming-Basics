# Homework 1
# by
# Roman Levchenko

f = open('output.txt')
f2 = open('data.txt','w')

print("What is your name? ")
name = f.readline()
print(name)
print()

print("Why do you study PYTHON?")
answer_1 = f.readline()
print(answer_1)
print()

print("How do you rate MasterAcademy (1-10)?")
answer_2 = f.readline()
print(answer_2)
print()

print("What is your hobby?")
answer_3 = f.readline()
print(answer_3)
print()

print("So mr.",name,"You study Python because",answer_1)

print("and you like", answer_3)

print("Your rating of Mater Academy is", answer_2, "Describe why?")

#Записываем ответ в файл дата и сохраняем для статистики
data = f2.write(input())
f.close()
f2.close()

# JOKE
#- How did you spent holidays?
#- was lying on the couch, then i tired and went sleep