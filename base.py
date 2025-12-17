a=3

aux = 55

a=aux

PI = 3.14
TIMEOUT_MSG_X = 500

print(a)
print (id(a))

suma_doua_numere = 0

check_flag = False
print(type(check_flag))


b=6

c=b+a
#print(c)

#0, 1, 2, 3,4, ...9
#This is for statement
#suma= 1+2+3+4+5
suma1=0
produs = 1

for i in range(5):
    suma1 = suma1  + i
    produs = produs * (i+1)
    #print(suma)
 #   print(2*i)

print(suma1)

print(produs)



#suma= n(n+1)/2
suma2 = 9*(9+1)/2
#print(suma2)

print(type(suma2))

var_flag = False

if var_flag == True:
    print ("Astazi este miercuri!")
else:
    print("Astazi este o zi de weekend!")


for i in range(20):
    if i % 2 == 1:
        print (f"Numarul {i} este par: ")