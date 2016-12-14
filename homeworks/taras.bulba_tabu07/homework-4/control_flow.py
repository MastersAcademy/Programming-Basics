# homework-4
# taras.bulba_tabu07


#ex 1
print ('что одеть')
Temp=int(input("введите значение температуры"))
pogoda=str(input("дождь-1, снег-2, ветер-3, ясно-4"))
if Temp>20 and pogoda=='дождь':
    print('можете одеть шорты с футболкои, но возьмите зонт')
elif Temp>20 and pogoda=="ясно":
    print ('одеваитесь легко на улице жарко')
elif Temp<=20 and Temp>1 and pogoda=="дождь":
    print('одеваитесь теплее и возмите зонт')
elif Temp<=0 and Temp>=-15 and pogoda=='снег':
    print ('одеваите зимние вещи и бегом на улицу, погода класс!!!')
else:
    print ('сиди дома и молись, возможно конец близок))')


#ex2
print('Добрый день')
name=input("Введите ваше имя:")
print(name.upper())
sredstva=float(input('Введите кол. Ваших средств цифрами в формате 1.0 грн или 1:'))
print(name,'Сумма Ваших средств составляет',sredstva,'грн')
tovar1=float(input('введите стоимость 1 товара:'))
tovar2=float(input('введите стоимость 2 товара:'))
pokupki=tovar1+tovar2
print('Сумма Ваших покупок составляет:', pokupki, 'грн')
itogo=sredstva-pokupki
if itogo>0:
    print('Поздравляем, у Вас достаточно средств!', 'Остаток средств:', itogo, 'грн')
else:
    print('Увы, но у Вас не достаточно средств.', 'Вам необходимо еще:', -itogo, 'грн')


#end