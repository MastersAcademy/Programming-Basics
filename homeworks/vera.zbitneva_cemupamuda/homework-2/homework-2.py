#Create dictionaries
dict_q = {
    'name' : str(input("Enter your name: ")),
    'surname':str(input("Enter youre surname: ")),
    'age':int(input("How old are you? ")),
    'city':str(input("Where do you live? ")),
    'game':str(input("Enter your favorite game: "))
}

#output on display dictionaries
print (dict_q)
print ('--------*********--------')
print (dict_q['city'])

#lists
list_name = ['Nick', 'Dasha', 'Masha']
print (list_name)
list_name.sort()
print (list_name)
list_n = [list_name, dict_q]
print (list_n)
#output on display
n = "Name: %s \n"%(dict_q['name'])
s = "Surname: %s \n"%(dict_q['surname'])
a = "Age: %i \n" %(dict_q['age'])
c = "City: %s \n" %(dict_q['city'])
g = "Game: %s \n" %(dict_q['game'])
symb = "------------------------*********------------------------ \n"
print(n)
print(s)
print(a)
print(c)
print(g)
print ('--------Thank you!--------')

#Pause in console
import time
time.sleep(5)

#create file
file = open('new.txt', 'w')
file.write(symb)
file.write(n)
file.write(s)
file.write(a)
file.write(c)
file.write(g)
file.write(symb)
file.close()




