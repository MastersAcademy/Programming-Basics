# Ask user some questions and write answers to file


# Define answers storage
secret_answers = []


print("Hello, dear customer! We need some info to register you.")


name = input("What is your full name? ")
secret_answers.append("Users's name is " + name + "\n")
salary = input("What is your approximate salary(USD)? ")
secret_answers.append("Salary is " + salary + " USD" + "\n")
answer = input("What is the Answer to the Ultimate Question of Life, the Universe, and Everything? ")
secret_answers.append("Answer to the Ultimate Question of Life, the Universe, and Everything is " + answer + "\n")


print("Thank you!")


# Operations with file in the current working directory
f = open("answers.txt", "w")
f.writelines(secret_answers)
f.close()
