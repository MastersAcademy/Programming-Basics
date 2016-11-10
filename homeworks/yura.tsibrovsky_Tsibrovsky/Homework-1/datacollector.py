#! /usr/bin/env python
# -*- coding: utf-8 -*-
# data collection
print("Введите ваши данные, пожалуйста")
name_string = raw_input("Ваше имя ")
fathersname_string = raw_input("Отчество ")
surname_string = raw_input("Фамилия ")
age_integer = int(input("Ваш возраст "))
nationality_string = raw_input("Национальность ")
taxid_integer = int(input("Индивидуальный налоговый номер "))
email_string = raw_input("электронный ящик ")
city_string = raw_input("Город проживания ")
# data output
print("Давайте проверим, что вы внесли: ")
print("Вас зовут:  %s %s %s  " % (name_string, fathersname_string, surname_string))
print("Ваш возраст %i , Вы %s, живете в городе  %s   " % (age_integer, nationality_string, city_string))
print("Ваш налоговый номер  %i,  " % (taxid_integer))
print("Для связи с вами вы оставили вот такой имейл:  %s " % (email_string))
print("Отлично. Мы сохраним информацию о вас в файле data.txt ")
# data to file
file_sting_0 = "Анкетные данные. \n" 
file_sting_1 = "ФИО:  %s %s %s  \n" % (name_string, fathersname_string, surname_string)
file_sting_2 = "возраст %i , национальность %s, город проживания  %s   \n" % (age_integer, nationality_string, city_string)
file_sting_3 = "Налоговый номер:  %i,  \n" % (taxid_integer)
file_sting_4 = "email :  %s \n" % (email_string)
# file creation and writing
datafile = open("data.txt", "w")
datafile.write(file_sting_0)
datafile.write(file_sting_1)
datafile.write(file_sting_2)
datafile.write(file_sting_3)
datafile.write(file_sting_4) 
datafile.close
print("Файл data.txt готов. В нем вы можете просмотреть свои анкетные данные.")
# the end 