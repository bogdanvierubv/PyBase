# print("Hello")
#
# # Variabilele- ele ruleaza in memoria RAM
# l = "Hello"
# print (l)
# print("Hello")

#  variabile de tip lista = [0, 1, 2, 3]

# Tuplu: (este o variabila care nu se schimba); el se trece intre paranteze; aceste liste de date nu e pot modifica
# coordonate_punct1 = (3,5)
# coordonate_punct2 = (0,10)

# persoana = ("Adrian", 32, "Tutore", True, 300, 185, 70)
# # fiecare variabila ii corespunde cate un index    0       1     2       3      4   5    6
# #
# # print(coordonate_punct1)
# # print(coordonate_punct2)
# # print(persoana)
# # print(persoana[3])
#
# persoana1 = ["Adrian", 32, "Tutore", True, 300, 185, 70]
# persoana1[3] = "Student"
# print(persoana1[3])
# #  CTRL + SPACE - ne afiseaza ce cod putem scrie in python
#
# sir = "ASDF"

# tuplu2 = ("Tudor", (30, "Cluj", "Tamplar", ("Universitate", "Europa", ("Sursa Divina", ("Pur Existenta")))))
#
# print(tuplu2[1][3][2][1])
#  END TUPLES

#  SETS - data structure - sunt o grupare de elemente unice, seturile nu au o ordine, si nu au index, putem adauga operatii intr-un set
# {3, 4, 100, 200, 5, 9, 0}

# var2 = {3, 4, 10, 0}
# print(var2)
# var2.add(100)
# print(var2)
#
# var2.remove(10)
# print(var2)

# complexiatate
# o(n)

# sa zicem ca avem o lista de persoane
# persoane = ["Tudor", "Maria", "Vlad", "Adrian", "Flavia", "Vlad", "Marius"]
# print(persoane)

# comanda set afiseaza neordonat si nu afiseaza elementele ce se repeta
# var4 = set(persoane)
# print(var4)

# if -verifica valoarea de adevar, -in este un operator de comnarare
# aceste doua coduri sunt analizate diferit in cazul listelor si in cazul set-urilor
# - in lista se uitra de 7 ori -persoane-. Asa se defineste complexitatea unui cod care este O(n) -> liniar
# if "Marius" in persoane:
#     print("Marius este printre noi.")
# else:
#     print("Marius nu este printre noi.")

# compexitatea cautarii intr-un set se face intr-un singur pas
# Complexitatea este o(1) -> Constant
# if "Marius" in var4:
#     print("Marius este printre noi.")
# else:
#     print("Marius nu este printre noi.")

# print("==========End=========")

# Lists + Strings

# stim ca un string este o lista de caractere
str1 = "LOG: Hello this is Vlad the Impaler."
str2 = "My story is way overblown."
str3 = ')(*&^%$#$##@%^^&!)#%@%^%$#'

list3 = ["adrian", "client", "studenti"]
list4 = [str1, str2, str3]
# print(list4)

# task: split all the strings in our them using the ";" character.
#  example: "LOG: Hello this is Vlad Impaler." -> ["LOG", "Hello this is Vlad Impaler"]

# print(list4[0].split(":"))

# daca vrem sa trecem prin toate elementele dintr-o lista folosim for

#cu range generam un numar de elemente
# print(list(range(1000000)))
# functia len ne afiseaza lungimea listei
# print(list(range(len(list4))))

for i in range(len(list4)):
     # print(i)
     print(list4[i])
     list4[i] = list4[i].split(":")
     print(list4[i])


    # print("=========")

    # list5= [10, 20,30]
    # list5[1]= 100
    # print(list5)