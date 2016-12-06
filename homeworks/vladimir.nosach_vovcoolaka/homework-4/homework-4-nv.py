#request
print("Please provide us with the following information")

fullname = input("What is your full name?\n")
country = input("What is your country of residence?\n")
age = int(input("How old are You?\n"))

result = ("Your full name is %s, You are %i years old, you live in %s Thank you.\n\n" % (fullname, age, country))
print()
#if elif else

print("May i ask you some questions???\n\n")
situps = int(input("How many sit-ups you do?? \n"))
pullups = int(input("How many pull-ups you do?? \n"))
pushups = int(input("How many push-ups you do?? \n"))

s_coefficient = int(round(situps/2 + pullups*2 + pushups))
print("Your sport coefficient is %i" % (s_coefficient))
print()

if s_coefficient in range(0, 5):
    print("You are weak, work harder!!!")
elif s_coefficient in range(5, 25):
    print("You are strong, good work!!!")
elif s_coefficient > 25:
    print("You are very strong, have a rest!!!")
else:
    print("Are you sure???")
print()
#for

dict_a = {
    'Sit-Ups': situps,
    'Pull-ups': pullups,
    'Push-ups': pushups
    }
print()
print("Your sport data is:\n")
print()

for a, b in dict_a.items():
    print(a + ' -- ' + str(b))
print()

# while
s = 0
q = 0
while q <= 1000:
    s = q + s
    q = q + 1
print("sum from 1 to 1000 is:", s)
print()

#break, continue
list_1 = range(0, 20)

for i in list_1:
    if i > 3:
        continue
    print('--- %i' % i)

print()

for i in 'The End':
    if i == 'd':
        break
    print(" *%s* " %(i), end='')