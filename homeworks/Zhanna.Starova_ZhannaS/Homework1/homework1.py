name=str(input("What is your name? "))
surname=str(input("What is your surname? "))
year_of_birth=int(input("Enter your year of birth? "))
color=input("What is favorite color? ");
phone=int(input("Input your phone? "));
age=2016-year_of_birth
print('\nCheck your data:\nYour name:'+name+"\nYour surname:"+surname+"\nYour age:")
print(age)
print("Your favorite color is "+color+"\nYour phone:")
print(phone)

f = open('output.txt', 'w', encoding='utf-8')
f.write(name+'\n')
f.write(surname+'\n')
f.write(str(age)+'\n')
f.write(color+'\n')
f.write(str(phone))
f.close()

print('File written successfully')
