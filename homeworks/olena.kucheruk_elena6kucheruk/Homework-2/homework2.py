print ("Please write about your favorite books \n")

name = input("What is your name?\n  ")
age = int(input("What is your age?\n    "))
book = input("What is your favorite book?\n         ")


#results
result = ("Your name is %s, You are %i years old, your favorite book is %s. Thank you." % ( name, age, book ))
print (result)


print("Please give us with the additional information")

author = input("What is your favorite author?\n")
det = input("What is your favorite getective story\n")
novel = input("What is your favorite novel\n")

#dictionaries

dict_a = {
    'Name': name,
    'Age': age,
    'book': book
    }
dict_a['profession'] = ['books lover']

dict_b = {
    'author': author,
    'det': det,
    'novel': novel
}
dict_a['new information'] = dict_b

print(dict_a)



