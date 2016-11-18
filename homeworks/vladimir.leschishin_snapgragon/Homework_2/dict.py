
print ('--- ===  Dictionaries  === --- ')


name = input('Enter your name:')
last_name = input ("Enter your last name:")
age = input ('Enter  your age:')
city = input ('Where do you live?')

dict_inform = {
    'name': name,
    'last_name': last_name,
    'age': age,
    'city' : city
}
print (dict_inform)


results  = " Your name is %s . Your last name is %s. Your age is %s . You are from %s " %(name,last_name,age,city)
print(results)

file = open('results.txt', 'w')
file.write(results)
file.close()