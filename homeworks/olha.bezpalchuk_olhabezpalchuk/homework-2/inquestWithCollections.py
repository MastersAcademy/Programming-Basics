print("Hello!")

answer = 'n'
data = {}
while answer != 'y':
    data['name'] = input("What is your name?")
    data['age'] = int(input("How old are you?"))
    data['phone'] = input("Tell me your phone number?")
    data['email'] = input("Input your email address: ")
    data['place'] = input("Where do you live?")
    print("Confirm your data:")
    for key, value in data.items():
        print(key + ': ' + str(value))
    answer = input("Is it right? (y/n)")

print("Good! Have fun and remember: we know your name and where you live.")

f = open('output.txt', 'w')
for key, value in data.items():
    f.write(key + ': ' + str(value) + '\n')
f.close()
