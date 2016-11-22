start = input("Auto complit, press '1': \n"
              "To list, press '2': \n: ")

auto_complit = list(range(11))
# auto complit array
if start == "1":
    with open("data.txt") as file_object:
       fromFile = file_object.read()

    def auto(auto_complit):
        print("\n" + fromFile)
    auto(auto_complit)

    toFile = "data.txt"
    with open(toFile, 'w') as file_object:
       file_object.write(str(auto_complit))

# toList
elif start == "2":
    with open("data.txt") as file_object:
       fromFile = file_object.read()
    print("\n" + fromFile)

# add number
edit = input("\n Add number - 10, Delete number - 20, Sort number - 30: \n")
if edit == "10":
    num_1 = input("Add number: \n")
    auto_complit.append(int(num_1))
    print("Added: " + str(num_1))
    print("List: " + str(auto_complit))

# delete number
if edit == "20":
    with open("data.txt") as file_object:
       fromFile = file_object.read()

    delNum_1 = input("Delete number: \n")
    auto_complit.__delitem__(int(delNum_1))
    print("Delete number: " + str(delNum_1))
    print("Array: " + str(auto_complit))

if edit == "30":
    arr = [2, 3, 4, 1, 0, 20, 1]
    print("Before sort" + str(arr))
    arr.sort()
    print("After sort" + str(arr))


 toFile = "data.txt"
 with open(toFile, 'w') as file_object:
        file_object.write(str(auto_complit))
