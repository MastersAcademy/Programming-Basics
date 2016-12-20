name = input("What is your name? ")
surname = input("What is your surname? ")
age = int(input("How old are you? "))
city = input("Where do you live? ")
university = input("Where do you study? ")

personal_information = {
    'name': name,
    'surname': surname,
    'age': age,
    'city': city,
    'university': university
}
if (name=='Sashka') & (surname=='Datsenko') & (age==19):
    print("It`s me", personal_information)
else:
    print("It`s your information", personal_information)