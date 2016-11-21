# Ask user some questions and write answers to file


# Define answers storage
answers = {}


# Questions and answers about user
print("Hello, dear customer! We need some info to register you.")
answers['full_name'] = input("What is your full name? ")
answers['salary'] = input("What is your approximate salary(USD)? ")
answers['answer'] = input("What is the Answer to the Ultimate Question of Life, the Universe, and Everything? ")


# Printing
print("Your name is %s, your approximate salary is %s, "
      "and the Answer to the Ultimate Question of Life, the Universe, "
      "and Everything is %s." % (answers['full_name'], answers['salary'], answers['answer']))
print("Thank you! Have a nice day!")

# Operations with file in the current working directory
f = open("answers.txt", "w")
f.write(" === Information about user === \n")

for k, v in answers.items():
    f.write(k + ': ' + v + '\n')

f.write(" === End of file === ")
f.close()
