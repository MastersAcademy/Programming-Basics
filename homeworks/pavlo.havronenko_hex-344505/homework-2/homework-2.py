import os
import datetime
data_path = './DATA.csv'
user = dict()
print ("Please provide some information for statistic")
user["Name"] = input ("What is Your Name => ")
user["Location"] = input ("Where are You From => ")
cust_age = input ("How Old Are You => ")

if not cust_age.isdigit():
    cust_age = input ("Provide only numders for age, try once again => ")
user["Birth"] = str(datetime.datetime.now().year - int(cust_age))

print ("So your name %s, you from %s, and you was born in %s " %(user["Name"], user["Location"], user["Birth"]))

if os.path.exists(data_path):
    data_file = open (data_path,'a')
    data_file.write(user["Name"] + ',' + user["Location"] + ',' + user["Birth"] + '\n')
    data_file.close()
else:
    data_file = open (data_path, 'w')
    data_file.write("Name,Location,Year of Birth\n")
    data_file.write(user["Name"] + ',' + user["Location"] + ',' + user["Birth"] + '\n')
    data_file.close()

print ("Data SAVED to %s" %(data_path))



