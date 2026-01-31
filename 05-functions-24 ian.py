import copy
#
var1 = "hello"

def change_variable(param1):
    param1= "this is not a hello."

# #
# print(var1)
var1= "cat"
#
change_variable(var1)
# #  cand pasam o variabila unei functii face pass by value
# print(var1)
#
var2 = [30,100]
def change_variable_list(param2):
    param2.append(99)

#     stergerea elementelor din lista
#     param2.clear()

print(var2)
change_variable_list(var2)
# # # pass by reference
print(var2)
#
#
# # max si suma nr dintr-o lista
#
# lista2 =[40, 90, 100, 10, 4, 1]
#
# def get_total(param1):
#     total= 0
#     for nr in param1:
#         total= total + nr
#     return total
#
# print(get_total(lista2))
#
# def get_max(param1):
#     max= param1[0]
#     for nr in param1:
#     if nr max:
#         max = nr
#
# # ora 10:38 de reluat
# print(pet_max(lista2))


# print("========Dictionar=========")
# un dictionar este definit prin acolade
student = {
    "name" : "Adrian",
    "age" : 32,
    "weight" : 75,
    "backpack" : ["keys", "wallet", "camera", "phone"],
    0: "nothing at all",
    (1, 2): "alpha and omega"
}


# print(student["name"])
# print(student["backpack"][2])

# for k in student.keys():
#     print(k)
#
# for key, value in student.items():
#     print(key, "---", value)
#
# print(student)
# student["age"] =33
# print(student)
# student["address"]= "Brasov"
# print(student)

# print(student["hhh"])- daca generam o eroare, arunca exceptie si opreste programul

# daca vrem sa primtam o cheie putem folosi functia get

student["hhh"] = "assassin"
print(student.get("hhh", "default value"))

# pop sterge o valoare din dictionar

# student.pop("backpack")
#  comanda clear sterge tot dictionarul
# strudent.clear()

# if "address" in student:
#     print("Avem adresa pentru acest student!")
# else:
#     print("Studentul acesta nu are adresa!")
#
# print(student)
#
# student_doi = student.copy()
# # daca creem o functie de egalitate
# student_doi["restante"] = 3
# print("student original:")
# print(student)
# print("studentul doi cu restante:")
# print(student_doi)


# print("=======Shallow Copy Drawbaks========")
#
# student_doi["backpack"].append("casti")
# print(student_doi)
# print(student)
# #  reluare ora 11:27
#
# student_trei = copy.deepcopy(student)
# student_trei["backpack"].append("casti")
# print(student_trei)
# print("student original")
# print(student)


# creaza o functie care aduna toate numerele din dictionar

# dict2={
#     "name" : "Omega",
#     "dimensions" : 6,
#     "size" : 13,
#     "count" : -1,
#     "axis": "y",
#     "trees": "all"
# }
#
# def add_all_numbers(param1):
#     total = 0
#     for key in dict2.keys():
#         # print(dict2[key])
#         valoare = dict2[key]
#         if isinstance(valoare, int):
#             total = total + valoare
#     return total
#
# print(add_all_numbers(dict2))
#
# # check if var4 is integer
# var4 = 30.4
# print(isinstance(var4, float))
#
# # check if var4 is integer
# print(isinstance(var4,(int, float)))
#
#
# print("=====Odd/Even numbers====")

# 5 / 2 -> 2, rest 1
# operator binar % - ce returneaza 1(inseamna ca numarul este impar) sau 0
# print(5 % 2)

# def is_even(nr):
#     return nr % 2 == 0

# is_even(11)
# lista3 = [5, 10, 4, 30, 25, 7]

 # adunam toate numerele pare

# def add_all_evens(param1):
#     total = 0
#     for nr in param1:
#         if is_even(nr):
#             total = total + nr
#     return total
#
# rezultat = add_all_evens(lista3)
# print(rezultat)