'''First_name=str(input('Tell me please your first name: '))
Second_name=str(input('Tell me please your second name: '))
Size_footwear=int(input('Please tell us your shoe size: '))
Age=int(input('How old are you: '))
Hobby=input('Your favorite activity: ')
Phone=input('Your favorite brand of phone: ')
Music=input('What are your favorite artists: ')'''
First_name='Vasyl'
Second_name='Shcherbatenko'
Size_footwear='45'
Age='21'
Hobby='Football'
Phone='Nokia'
Music='Curt Cobain, James Hetfield'


dict = {
    'first_name': First_name,
    'second_name': Second_name,
    'size_foot': Size_footwear,
    'age': Age,
    'hobby':Hobby,
    'phone':Phone,
    'music':Music
}

print (dict)
K=open('personal_data.txt', 'w')
K.write('Your first name: '+dict['first_name']+'\n'+'Your second name: '+dict['second_name']+'\n'+'Your size foot'+(dict['size_foot'])+'\n'+'Your age: '+(dict['age'])+'\n'+'Your Hobby: '+dict['hobby']+'\n'+'Your favorite phone: '+'\n'+'Your favorite artists: '+dict['music'])

