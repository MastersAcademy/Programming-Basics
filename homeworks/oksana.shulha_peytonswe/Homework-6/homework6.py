import json

from Fiction import Fiction
book1 = Fiction("George Orwell", "1984", 1948, 267, "novel", "dystopian")
data = {"author": "George Orwell", "title": "1984", "year_of_writing": 1948,
        "number_of_pages": 267, "form": "novel", "kind": "dystopian"}
print(data)

file = open("fiction.json", "w")
json.dump(data, file, indent=4)
file.close()
