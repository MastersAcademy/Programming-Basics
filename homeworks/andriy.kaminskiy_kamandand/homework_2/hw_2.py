print('Tell us a few words about yourself, please')
name=input('What is your name?')
age=int(input('How old are you?'))
sex=input('What is your gender?')
result = {
    'your name': name,
    'your age': age,
    'your sex': sex
    }
print("Ok. Let's write down:")
print(result)
print('But we still have a bit of interest:')
weight=int(input('What is your weight?'))
height=int(input('What is your height?'))
result1 = {
    'your weight': weight,
    'your height': height
}
result['some more information'] = result1
print("Let's summarize information about you. So:")
print(result)
result="Your name is %s, your age is %i, your sex is %s, your weight is %i, your height is %i" %(name, age, sex, weight, height)
file=open('questionnaire.txt', 'w')
file.write(result)
file.close()