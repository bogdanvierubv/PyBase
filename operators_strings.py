#produs = 1
import sys
from pkgutil import get_data
from subprocess import STARTUPINFO

#for i in range(5):
#   produs + produs * (i+1)

#    print(produs)

#   import nath


#    produs = natn.factorial(5):
#    print(produs)

#doime_nr = 121
#nr=doime_nr *2
#print(nr)
#triplu_nr = 3*nr
#print(triplu_nr)


#produs_numere_pare = 1
#for i in range(6):
#    if i % 2 == 0 and i != 0:
#        produs_numere_pare = produs_numere_pare *i

#print(produs_numere_pare)

#rezultat = triplu_nr + produs_numere_pare
#print(rezultat)

# // operator care afiseaza catul, fara rest

#boxes = 53
#boxes_per_palet = 10
#full_pallets = boxes // boxes_per_palet
#print(full_pallets)

# ** un alt operator, care intoarce primul termen la puterea celui de al doilea
#a=2
#b=3
#c=a**b
#print(c)

#modes = 3
#devices = 4
#
#combin= modes  ** devices
#print(combin)

#sa presupunem ca o masina poate fi pornita daca are usa inchisa si sa nu aiba butonul de urgenta apasat (folosim operatorii logici True sau False)

#door_closed = True
#emergency_stop_pressed = False
#break_pressed = True
#start_machine = door_closed and not emergency_stop_pressed and break_pressed
#print(start_machine)

#facem un test- un divice alimentat la tensiune, daca counicatia cu alte aparate este ok, testul este trecut, daca nu sunt indeplinite conditiile testul este esuat

#voltage_ok = True
#communication_ok = True

#test_failed = (not voltage_ok) or (not communication_ok)
#print (test_failed)

#value = 42

#print(value)
#print(bin(value))
#print(hex(value))

# &, | , ~ (acesteia sunt operatorii de biti- si - sau- ori)
#  001100101

#READ = 0b001
#WRITE = 0b010
#EXEC = 0b100

#user_permissions =  READ | WRITE | EXEC
#print(bin(user_permissions))


#can_write = user_permissions & WRITE
#can_write = user_permissions & EXEC
#print(bin(can_write))



#tipul de date string (pus intre "")

#print("Hello world!")

#s= "Hello world!"
#print(type(s))

#

#cum gasesc in Python codul unui caracter ASCII

# print(ord("a"))

#daca avem codul ASCII si vrem sa vedem ce carater reprezinta
# print(ord("S"))
# print(chr(83))


# CUM FORMATAM STRINGURILE
# print("Primul rand \nAl doilea rand \nAl treilea rand")

# Primul rand
# Al doilea rand
# Al treilea rand

# formatarea folosind """

# print ("""Primul rand
# Al doilea rand
# Al treilea rand  """)

# variabile unui test results

test_name = "voltageCheck"
# duration = 1.237
# # vrem sa afiseze test apoi VoltageCheck si finished in (duration) 1.23 (si afisare in doar doua zecimale)
#
# print(f"Test {test_name} finished in {duration:.2f} ")

# print (test_name.upper())
# afisarea mesajului cu litere mici
#print (test_name.lower())

# exercitiu- presupunem ca avem o comanda

# command = "StaRt"
#
# if command == "start":
#     print ("Starting system")
#
# if command.lower() == "start":
#     print ("Starting system")


# word = "Python"
#
# print(word[0])
# print(word[3])
#
# print(word[-1])

# text = "programming"
#
# print(text[0:6])
# print(text[:4])
#
# print(text[4:])

# pentru afisarea lungimii caracterelor
# message = "Hello Python"
# print(len(message))

#  concatenarea unui mesaj
# a= "Hello"
# b= "World"
#
# print (a +" "+ b)


# avem un mesaj de eroare care se defineste..

# raw = "   ERROR_CODE_12 "
# print(raw)
# # strip - curata spatiile din mesaj
# clean_string = raw.strip()
# print(clean_string)



# metoda replace-

# log = "Voltage=12,5V"
# #  float 12.5 <- 12.5
# print(log)
# #  folosim metoda replace
# log = log.replace( ",", ".")
# print(log)

# selectarea fisierelor cu extensia log
# sdsdsd.txt
# sdsd.exe
#  file.log

filename = "report_2025.log"

# if filename.endswith(".log"):
#     print ("Log file detected")

# if filename.startswith("report"):
#     print ("Report file detected")


# find - cauta un cuvant intr-un text si intraorce indexul lui, daca nu gaseste intoarce -1
# message = "CAN timeout detected"
#
# index = message.find("timeout")
# print(index)
#
# index = message.find("exit")
# print(index)

# cautarea intr-un sir de caractere prin in sau find
# in vs find
# Timeout_flag = False
#
# if "timeout" in message:
#     timeout_flag = True
#     print("timeout found!")


# metoda split(), imparte un text

# data = "12.5, 3.7, OK"
# print(data)
# values = data.split(",")
# print(values)

# join este operatia inversa a split-ului
# my_string = [ "Ana ", "are ", "mere ", "!"]
# print(my_string)
# final_string = "".join(my_string)
# print(final_string)

# parts = ["C", "logs", "2026", "run_01.txt"]
# path ="/".join(parts)
# print(path)


#  Password Generator
#  avem nevoie de a genera aleator un sir de caractere
# import random
#
# s= "Ana are mere!"
# s_random = random.sample(s,3)
# print(s_random)

# facem un generator de parola
# lower = "abcdefghijklmnoprstuvwxyz"
# upper = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
# numbers = "0123456789"
# symbols = "!@#$%^&*()?"
#
# all_string = lower + upper + numbers + symbols
# # print(all_string)
#
# lenght = 16
# import random
# password = "".join(random.sample(all_string, lenght))
# print(password)


#  exercitiu- avem nevoie de un input de la utilizator. Cu imput preluam date de la utilizator.
# Function Input
# a=""
# while a !="STOP":
#     a = input("Add data: ")
#     print(a)
#
# print("The user stopped entering the data!")

# Liste

# my_list = [70, 5, -7, 50, -7, 20.5, True, "Ana are mere", 4+7j]
# print(my_list)
#
# print(my_list[0])
# print(my_list[-1])

# print(len(my_list))

# sliced_list = my_list[:6]
# print(sliced_list)

# print(my_list[-3])


# cu input vom crea o baza de date

db=[]
print(db)

get_data= ""

while get_data != "Stop":
    get_data = input("Add data: ")
    if get_data !="Stop": db.append(get_data)

print (db)


