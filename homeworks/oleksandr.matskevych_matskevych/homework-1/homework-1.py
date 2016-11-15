
file1= open ('hello.txt','r')
data=file1.read()
print(data)
file1.close()

name=input("Hello, what is you name?")
live=input("We do you live?")
hobby=input('Talk about your hobby?')

answer=("Hello guy,your name is %s,you live in %s, your hobby is %s " % (name, live, hobby))
print('OK, check data')
print (answer)


file2= open ('hobby.txt','w')
data1=file2.write(answer)
file2.close()

