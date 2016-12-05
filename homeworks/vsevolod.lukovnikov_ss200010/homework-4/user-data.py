age = input("How old are you?")

while int(age) <= 0 :
    print("Wrong value. Enter number more than 0, please!")
    age = input("|- How old are you?")
else:
    if int(age) in range (1,17):
        print("|- Access denied!!!")
    else:
        print("|- Access opened!!!" )


list_cars = []
while len(list_cars) < 4:
    list_cars.append(input("Enter car brand"))


for elem in list_cars:
    if elem.lower() != "ford":
        print("|-" + elem + " " + "is not my car")
    else:
        print("|- My favorite car brand is"+" "+ elem)
        break


birth_year = input("Enter year of your's birth")
current_year = input("Enter current year")

list_year = [i for i in range(int(birth_year),int(current_year)+1)]
for elem in list_year:
    if elem % 2 == 0:
        continue
    print(elem)


print("---=====---")

list_reverse = reversed( list_year)
for elem in list_reverse:
    if elem % 2 == 0:
        pass
    print(elem)








