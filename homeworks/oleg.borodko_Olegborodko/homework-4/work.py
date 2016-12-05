import random

try:
    name=str(input("Please enter your name: "))
    year=float(input("Please enter your age: "))
except:
    print("You have error in your data")
else:

    data_array=[name,year]

    print("Your name is-"+data_array[0])
    print("Your age is-"+str(data_array[1]))
    print("=== *** manipulation list *** ===")

    if year < 0:
        print('I am sorry, but you not born yet')
    elif year == 0:
        print('Hey, you are a baby')
    elif year < 16:
        print('I think you study at the school')
    else:
        print('Now, it is time think about children')

    data_array.insert(0, random.choice(name))
    data_array.insert(-1, random.choice(name))
    data_array.insert(1, random.choice(name))

    for i in range(len(data_array)):
        m = random.randint(i, 10)
        data_array.append(m)

    data_array = data_array + list(range(5))

    print(data_array)

    print("=== *** manipulation set *** ===")

    data_set=set(data_array)

    print(data_set)

    data_set.add("1")
    data_set.add("[1,2]")
    data_set.add(True)
    data_set.add("1") #not added
    data_set.pop() #delete first element
    #data_set.add(0)

    for n in data_set:
        if n != 0:
            continue
        else:
            print("Set have 0")
            break

    print(data_set)

    print("=== *** manipulation hash *** ===")

    data_hash={}
    i=0
    for value in data_set:
        data_hash[str(value)]=i
        i+=1

    for key in data_hash:
        #print("%s -> %s" % (key, data_hash[key]))
        pass #don't nothing do

    #print(data_hash.values())

    your_secret_key=""
    for key in data_hash.keys():
        your_secret_key+=("%s" % (key))

    print(data_hash)

    def part_delete(hash, *args):
        for key in args:
            if key in hash.keys():
                print("Removed %s -> %s" % (key, hash[key]))
                del hash[key]
        #print(hash)

    part_delete(data_hash, '1','2','3','4','5','6','7','8','9')

    print(data_hash)

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