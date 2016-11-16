
file1= open ('hello.txt','r')
data=file1.read()
print(data)
file1.close()

dict={}
dict['name']=input("Hello, what is you name?")
dict['soname']=input("Hello, what is you soname?")
live=input("We do you live?")

dict['hobby']=input('Talk about your hobby?')
print(dict)

answer=("Hello guy,your name is %s,you soname is %s you live in %s, your hobby is %s " % (dict['name'], dict['soname'],live, dict['hobby']))
print('OK, check data')
print (answer)

list=[]
list=dict['hobby']
print(list)


file2= open ('hobby.txt','w')
data1=file2.write(answer)
file2.close()