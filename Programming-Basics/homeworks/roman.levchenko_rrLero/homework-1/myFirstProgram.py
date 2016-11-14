# Homework 1
# by
# Roman Levchenko

f = open('output.txt')
f2 = open('data.txt', 'w')

print("What is your name? ")
name = f.readline()
print(name)


print("Why do you study PYTHON?")
answer_1 = f.readline()
print(answer_1)


print("How do you rate MasterAcademy (1-10)?")
answer_2 = int(f.readline())
print(answer_2)


print("What is your hobby?")
answer_3 = f.readline()
print(answer_3)


print("So mr. %s You study Python because %s" % (name, answer_1))
print("and you like", answer_3)
print("Your rating of Mater Academy is", answer_2, "Describe why?")

# Writing answer in data file
data = f2.write(input())
f.close()
f2.close()

# JOKE
# - How did you spent holidays?
# - was lying on the couch, then i tired and went sleep
