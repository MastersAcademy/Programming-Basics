name = input("What you name? ")
last_name = input("What is your last name? ")
age = int(input("How old are you? "))
country =input("Where do you live (country)? ")
city = input('Where do you live(city)? ')
birth = input("Enter your date of birth(date/month/year)? ")

print("Your name and last mane is %s %s,your birthday %s, your age is %s "
      "and you live in %s %s. Good!" % (name, last_name, birth, age, country, city))

result = 'name - %s, last_name - %s, age - %s, country-%s, city - %s, birth- %s  .'%(name, last_name, age, country, city, birth)
file = open('info.txt', 'w')
file.write(result)
file.close()
