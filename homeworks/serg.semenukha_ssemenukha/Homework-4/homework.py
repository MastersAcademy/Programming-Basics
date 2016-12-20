lines = []

print("Невелика анкета");
full_name = input("Ваше ім'я: ")
age = int(input("Скільки Вам років: "))

current_year = 2016
year_of_birth = current_year - age

lines.append("Ваше ім'я %s" % (full_name))
lines.append("Вам %d років" % (age))
lines.append("Ви народились у %d році" % (year_of_birth))

if age < 6:
    lines.append("Вам серйозно вдалось запустити цю програму?")
elif age < 17:
    school_name = input("В якій школі ви навчаєтесь? ")
    lines.append("Ви навчаєтесь в школі %s" % (school_name))
elif age < 22:
    hschool_name = input("В якому вузі ви навчаєтесь? ")
    lines.append("Ви навчаєтесь у вузі %s" % (hschool_name))
else:
    job = input("Вкажіть місце роботи (порожня строка, якщо не працюєте) ")
    if job == "":
        lines.append("Ви тунєядєц")
    else:
        lines.append("Ви працюєту у %s" % (job))

if age > 15:
    children = input("У вас є діти? (y/n)")
    if children == "y":
        children_names = []
        lines.append("У вас є діти")
        while True:
            children_name = input("Ім'я дитини (порожня строка, щоб завершити) ")
            if children_name == "":
                break
            else:
                children_names.append(children_name)
        lines.append("Їх імена: %s" % ", ".join(children_names))
    else:
        lines.append("У вас не має дітей")

print("--- === ||| === ---")

for line in lines:
    print(line)