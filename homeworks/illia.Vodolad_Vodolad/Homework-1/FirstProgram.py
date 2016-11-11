# Homework 1
# Illia Vodolad

name = input("Your name plz ")
hand = input("What education do you have? ")
fingerLeft = int(input("How many fingers you have on your left hand? "))
fingerRight = int(input("How many fingers you have on your right hand? "))
fingers = fingerLeft+fingerRight

print("Dear %s have education  %s, he has %i fingers on a left hand and has %i fingers on a right hand." % (name, hand, fingerLeft, fingerRight))
print("Congratulations, you have %s fingers.Take care of them." % (fingers))
print("Thank you %s for watching my little Homework_1!" % (name))
