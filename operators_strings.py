#produs = 1

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

print (test_name.upper())
