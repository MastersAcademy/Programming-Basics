import os
import datetime
data_path = './DATA.csv'

print ("Please provide some information for statistic")
cust_name = input ("What is Your Name => ")
cust_loc = input ("Where are You From => ")
cust_age = input ("How Old Are You => ")


if not cust_age.isdigit():
    cust_age = input ("Provide only numders for age, try once again => ")
print ("So your name %s, you from %s, and you %s yeas old" %(cust_name, cust_loc, cust_age))

customer_birth = datetime.datetime.now().year - int(cust_age)

if os.path.exists(data_path):
    data_file = open (data_path,'a')
    data_file.write(cust_name + ',' + cust_loc + ',' + str(customer_birth) + '\n')
    data_file.close()
else:
    data_file = open (data_path, 'w')
    data_file.write("Name,Location,Year of Birth\n")
    data_file.write(cust_name + ',' + cust_loc + ',' + str(customer_birth) + '\n')
    data_file.close()

print ("Data SAVED to %s" %(data_path))

