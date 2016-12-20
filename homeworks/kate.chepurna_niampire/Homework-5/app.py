from Product import Product
from Apple import Apple
from RedApple import RedApple
from GreenApple import GreenApple


print("Hello. You can pay apple in out, please please make a selection, press needs key")

answer = input("Enter 1 - red apples or 2 - green apples: ")

if answer == "1":
    red_apples = RedApple('redapple', '', '', '', 'true')
    print(red_apples._RedApple__getPrice())

elif answer == "2":
    green = GreenApple('green', '', '', '', 'true')
    print(green._GreenApple__getPrice())


