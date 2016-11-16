

name = str(input (" What is your name? "))
surename = str(input(" Your Surename? "))
age = int(input (" Сколько вал лет? "))
country = str(input (" Гражданство? "))
print("Hello %s %s, you were born %i  years ago, you citizen of %s. Good" % (name, surename, age, country))
#
filename=name+'_'+surename+".txt"
f = open(filename, 'w')
data_to_write=name+";"+surename+";"+str(age)+";"+country+'\n'
f.write(data_to_write)
f.close