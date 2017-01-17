from passplain import PassPlain  # import classes we need for app
from militaryplain import MilPlain
from pilot import Pilot
from writer import *

check = 'y'  # var. for while cycle. used to know when app will be stopped
num = 0  # var. is used to create numbers for plains
print('====Hello====')
print('Lets create a plain')
while check == 'y':  # main cycle
    answ1 = input('what kind of plain will be created ? (pass/mil)')  # user select type of plain
    while answ1 != 'pass' and answ1 != 'mil':
        answ1 = input('try again.. (pass/mil)')
        if answ1 == 'pass' and answ1 == 'mil':
            break

    answ2 = input('what color of plain will you select ?')  # user select color of plain

    num += 1  # generation number of plain

    if answ1 == 'pass':  # info collected from user is used to create objects
        p = PassPlain(num, answ2)  # p is instance of PassPlain class
        print(p)
        status = p.status
    else:
        m = MilPlain(num, answ2)  # m is instance of MIlPlain class
        print(m)
        status = m.status

    Pilot(status)

    writer(num, answ1, answ2, status)  # preparing data to save in files

    check = input('One more plain ? (y/n)')
    if check == 'n':
        break

write_to_json(full)  # writing attr in JSON-file
write_to_xml(num)  # writing attr in XML-file

print('Good-bye!')
