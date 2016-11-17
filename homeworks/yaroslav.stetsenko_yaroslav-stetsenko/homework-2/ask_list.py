

name = str(input (" What is your name? "))
surename = str(input(" Your Surename? "))
age = int(input (" How old are you? "))
country = str(input (" What is your nationality? "))
print("Hello %s %s, you were born %i  years ago, you citizen of %s. Good" % (name, surename, age, country))

print("----Sets----")
list_ask = (name, surename, age, country)
print(list_ask)
print(set(list_ask))

print("----Lists----")

list_ask = (name, surename, age, country)
print(list_ask)
print(list_ask[3])
print(len(list_ask))

list_b = ['aye', 'aye', 'captain']
list_c = [list_ask, list_b, 'Human']
print(list_c)

print("----Dictionaries----")

dict_ask = {
    'name': (name),
    'surename': (surename),
    'age': (age),
    'country': (country)
}
print(dict_ask)

dict_ask['Dream'] = ['travelss', 'house', 'car']
print (dict_ask)


filename=name+'_'+surename+".txt"
f = open(filename, 'w')
data_to_write=name+";"+surename+";"+str(age)+";"+country+'\n'
f.write(data_to_write)
f.close