print("Let's play a riddle game, a right answer makes 1 point, a wrong answer removes 1 point:")
count = 0
answer_1 = input("1. When you have me, you feel like sharing me. But,if you do share me, you don't have me. What I am?")
if answer_1 == "secret":
    count += 1
    print("Yes! points earned:", count)
else:
    count -= 1
    print("Wrong!:", count)

answer_2 = input("2. A mirror for the famous, informative to all. I'll show you the world, but it may be a bit small")
if answer_2 == "tv":
    count += 1
    print("Congratulations! points earned:", count)
else:
    count -= 1
    print("No, try again", count)

answer_3 = input("3. The person who makes it it has no need for it. The person who purchases it does not use it. "
                 "The person who does use it, is not aware that they are using it. What is it?")
if answer_3 == "coffin":
    count += 1
    print("That was an easy one! points earned:", count)
else:
    count -= 1
    print("Sorry, try again", count)
