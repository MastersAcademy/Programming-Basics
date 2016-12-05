print('Ok. We have five participants')
print('Let each of you to introduce yourself')
result2={}
count=1
while count < 6:
  name=input('What is your name?')
  result1 = {
    'participant %s'%(count): name,
    }
  result2.update(result1)
  count+=1
print('So, let us summarize')
result=sorted(result2.keys())
for participant in result:
    print("You are %s and your name is %s"%(participant, result2[participant]))
a=list(result2.values())
a1=sorted(a)
aa=set(a)
aa=list(set(a))
aa1=sorted(aa)
if a1 < aa1 or a1 > aa1:
    print('We have namesakes here!')
else:
    print('---------------------')
file=open('participants.txt', 'w')
file.write(str(a1))
file.close()