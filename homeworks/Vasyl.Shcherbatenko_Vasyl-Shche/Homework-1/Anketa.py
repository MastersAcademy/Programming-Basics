#var
First_name=str(input('Tell me please your first name: '))
Second_name=str(input('Tell me please your second name: '))
Size_footwear=input('Please tell us your shoe size: ')
Age=input('How old are you: ')
Hobby=input('Your favorite activity: ')
Phone=input('Your favorite brand of phone: ')
Music=input('What are your favorite artists: ')

#Working with files and output to the screen
f=open('questionnaire.txt','w')
result='First name: %s \nSecond name: %s \nSize footwear: %s \nAge: %s \nHobby: %s \nFavorite Phone: %s \nFavorite artists: %s'\
       %(First_name,Second_name,Size_footwear,Age,Hobby,Phone,Music)
print(result)
f.write(result)
f.close()