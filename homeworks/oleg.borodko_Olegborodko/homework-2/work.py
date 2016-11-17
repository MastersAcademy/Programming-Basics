import random

try:
    name=str(input("Please enter your name: "))
    year=float(input("Please enter your age: "))
except:
    print("You have error in your data")
else:

    data_masiv=[name,year]

    print("Your name is-"+data_masiv[0])
    print("Your age is-"+str(data_masiv[1]))
    print("=== *** manipulation list *** ===")

    data_masiv.append(list(name))
    data_masiv.insert(0, random.choice(name))

    print(data_masiv.__class__)
    print(data_masiv)
    print(len(data_masiv))
    print(data_masiv[::-1])

    del(data_masiv[-1])

    data_masiv.insert(0, random.choice(name))
    data_masiv.insert(-1, random.choice(name))
    data_masiv.insert(1, random.choice(name))

    for i in data_masiv:
        print(i)

    print("=== *** manipulation set *** ===")

    data_set=set(data_masiv)

    print(data_set)

    data_set.add("1")
    data_set.add("[1,2]")
    data_set.add(True)
    data_set.add("1") #not added
    data_set.pop()

    print(data_set)
    print("=== *** manipulation hash *** ===")

    data_hash={}
    i=0
    for value in data_set:
        data_hash[str(value)]=i
        i+=1

    for key in data_hash:
        print("%s -> %s" % (key, data_hash[key]))

    print(data_hash.values())

    your_secret_key=""
    for key in data_hash.keys():
        your_secret_key+=("%s" % (key))

    print("=== *** key *** ===")
    print("Your secret key-"+your_secret_key)

    try:
        file = open('history.txt', 'a')
        file.write("Name-"+name+"\n")
        file.write("Year-"+str(year)+"\n")
        file.write("Secret key-"+your_secret_key+"\n")
        file.write('---\n')
    except:
        print("can not write to file")
    else:
        print("thank you, your data was recorded")
    finally:
        # this works in any case
        file.close()
