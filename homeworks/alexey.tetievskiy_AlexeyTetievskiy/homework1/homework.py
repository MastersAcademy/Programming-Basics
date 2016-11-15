name = input("Введите свое имя?")
age = int(input("Сколько вам лет?"))
city = input("Где вы живете?")

print("Ага, значит вас зовут %s, вам %i лет,"
      "и вы живете в %s. Ого!" % (name,age,city))

outputfile ="Data.txt"

datafile = open(outputfile, mode='w')

datafile.write("data:"+ " " + name + " " + str(age) + " "  + city )