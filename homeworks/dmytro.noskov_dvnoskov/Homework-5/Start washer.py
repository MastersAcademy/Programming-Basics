print('Welcome to get started you need to select modes')
A=input(str('Select the type of washing machine manual(1) or automatic(2)'))
if A == '1':
    pass
else: t = input(str('select spin speed 100-1000'))
r='auto'


B = input('enter the water temperature hot(1) or cold(2)')
if B == '1': q='Hot'
else : q='Cold'
e = input('specify the weight of the laundry')


w='150vat'
m ='manual'
if A=='2' :
    from washer_auto import washer_auto
    print('start')
    wash = washer_auto(q,w,e,r,t)  #wash = washer_auto('hot', '150vat', '5', 'auto', '1000')
    wash.power_work()
    wash.run_1()
else:
    from washer_manual import washer_manual
    print('start')
    wash = washer_manual(q,w,e,m) #wash = washer_manual('hot', '150vat', '5', 'manual')
    wash.power_work()
    wash.run_1()
