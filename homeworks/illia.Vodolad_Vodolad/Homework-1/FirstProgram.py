# Homework-1
# Illia Vodolad

name = input("Your name plz ")
education = input("What education do you have? ")
fingerLeft = int(input("How many fingers you have on your left hand? "))
fingerRight = int(input("How many fingers you have on your right hand? "))
fingers = fingerLeft+fingerRight

print()
print("Dear %s have education  %s, he has %i fingers on a left hand, and has %i fingers on a right hand." % (name, education, fingerLeft, fingerRight))
print("Congratulations, you have %s fingers.Take care of them." % (fingers))
print("Thank you %s for watching my little Homework_1!" % (name))
print()
print("Data stored in the file data.txt")
print()


file_0 = "Your name is %s \n" % (name)
file_1 = "Your profession %s \n" % (education)
file_2 = "left hand fingers %i \n" % (fingerLeft)
file_3 = "right hand fingers %i \n" % (fingerRight)
file_4 = "number of fingers %i \n" % (fingers)

datafile = open("data.txt", "w")
datafile.write(file_0)
datafile.write(file_1)
datafile.write(file_2)
datafile.write(file_3)
datafile.write(file_4)
datafile.close

