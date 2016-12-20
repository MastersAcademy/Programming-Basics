from MobilePhone import MobilePhone
from SensorMobilePhone import SensorMobilePhone
from ButtonMobilePhone import ButtonMobilePhone
from Caller import Caller

from faker import Factory as FakerFaktory

faker = FakerFaktory.create()


answer = 'Y'
phone_list = []
person1 = Caller(faker.first_name(), faker.last_name())

print("Hello %s" % person1)

type = input('Are your phone has buttons or sensor input? - ')
brand = input('What is your phone brand? - ')

#object's class depends on answer

if type == 'button':
    phone1 = ButtonMobilePhone(type, brand)
elif type == 'sensor':
    phone1 = SensorMobilePhone(type, brand)
else:
    print('Wrong type')


while answer == 'Y':
    print("Choose function: ")
    print("1 - Make a call ")
    print("2 - Connect to internet ")
    print("3 - Beat nuts (only for the button phones!!!) ")

    function_answer = input("What are you want? - ")

    #these methods use polymorphism. in each class these methods implemented different

    #method beat_nuts use incapsulation. it available for objects from ButtonMobilePhones, but available
    #for objects from SensorMobilePhones

    if function_answer == '1':
        print(phone1.make_call())
    elif function_answer == '2':
        print(phone1.connect_to_internet())
    elif function_answer == '3':
        print(phone1.beat_nuts())
    else:
        print("Wrong input")

    answer = str(input('Do you want to continue (Y or N)? - '))