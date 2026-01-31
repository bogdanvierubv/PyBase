# student2 = {
#     "name" : "Adrian",
#     "age" : 25,
#     "weight" : 65.0,
#     "backpack" : [],
# }
from unittest import result

# student3 = {
#     "name" : "Catalin",
#     "age" : 30,
#     "weight" : 80.0,
#     "backpack": ["keys", "wallet", "camera"],
# 0: "nothing at all",
# (1, 2): "alpha and omega",
# }

# def get_backpack(student):
#     return student["backpack"]
#
# print(get_backpack(student3))
# print(get_backpack(100))- aici da eroare, functioneaza doar pe dictionare


# ------------CLASE--------------

# definirea unei clase
# pass inseamna ca este o clasa goala
#  este o abstractitate privind obiecte

# class  Dog:
#     pass
#
# var1 = Dog()
# var2 = Dog()
#
# print(var1)
# print(var2)
#
# # -----------Proprietatile Claselor------------
#
# var4 = Dog()
# # ii dam o proprietate obiectului punand . dupa var
#
# var4.name = "Spot"
# var4.owner = "Iulian"
# var4.legs = "4"
# var4.last_vaccine = 2025
#
# print(var4.name)
# # putem vedea toate proprietatile unui obiect prin __dict__
# print(var4.__dict__)
#
# var5 = Dog()
# var5.name = "Shadow"
#
# print(var5.__dict__)
# # au acelasi tata dar sunt diferiti, printeaza doar proprietatile lui var5
# print(var5.__class__)

# in javascript, java- self este denumit this
#  self este o referinta la instanta curenta, cu care lucram
# class Cat():
#     def __init__(self, name, owner, legs, last_vaccine=None):
#         self.name = name
#         self.owner = owner
#         self.legs = legs
#         self.last_vaccine = last_vaccine
# #                 acestia sunt parametrii clasei
#
# # aceiasi functie in care se definesc parametrii mai pot fi scrisi asa:
# class Cat():
#     def __init__(self, param1, param2, param3, param4=None):
#         self.name = param1
#         self.owner = param2
#         self.legs = param3
#         self.last_vaccine = param4
#
# def make_sound(self):
#     print(self.name, "Meoww!")
#
# # putem face un constructor pentru o clasa, care atribuie acei parametrii. pentru aceasta trebuie sa scriem o functie in clasa cat
#
# var6 = Cat("Missy", "Vlad", 4, 2025)
# # print(var6.__dict__)
#
# # putem face ca un parametru sa fie optional, exmeplu:
#
#
#
# var7 = Cat("KitKat", "Bogdan", 4)
# def make_sound(self):
#     print(self.name, "Meoww!")
# var7.make_sound()
# print(var7.__dict__)
#
# def take_a_bite(self, param1):
#     a_bite = param1.pop()
#     print(f"{self.name} took a bite of {a_bite}")
# # pop-sterge ultimul element din lista, apoi il returneaza in lista
#
# snacks= ["fish_snack", "meat_popsickle", "milk", "fresh_rat", "catnip"]
#
# var7.take_a_bite(snacks)


# -------exercitiu----------


# 1. Creati o functie "top_students" care extrage toti studentii cu un test_score mai mare de 90, si returneaza o lista cu acei studenti.

# 2. Creaza o functie "extract_students" care extrage toti studentii "bachelor" si "masters", intr-un dictionar si il returneaza. Dictionarul arata in urmatorul fel:

example_dict = {
    "bachelor": [{"name": "Mason Dubois", "age": 21, "test_score": 71, "role": "bachelor"}, {"name": "Ethan Singh", "age": 20, "test_score": 79, "role": "bachelor"}],
    "masters": [{"name": "Isabella Nowak", "age": 25, "test_score": 89, "role": "masters"}, {"name": "Isabella Nowak", "age": 25, "test_score": 89, "role": "masters"}]
}

# 3. Creaza o functie "student_balance" care returneaza "bachelor" daca sunt mai multi bachelor decat masters, si "masters" daca sunt mai multi masters decat bachelor.

students = [
    {"name": "Emma Thompson", "age": 21, "test_score": 88, "role": "bachelor"},
    {"name": "Liam Chen", "age": 22, "test_score": 76, "role": "bachelor"},
    {"name": "Sofia Rodriguez", "age": 24, "test_score": 92, "role": "masters"},
    {"name": "Noah Patel", "age": 20, "test_score": 65, "role": "bachelor"},
    {"name": "Ava Müller", "age": 23, "test_score": 95, "role": "masters"},
    {"name": "Lucas Kim", "age": 19, "test_score": 82, "role": "bachelor"},
    {"name": "Isabella Nowak", "age": 25, "test_score": 89, "role": "masters"},
    {"name": "Mason Dubois", "age": 21, "test_score": 71, "role": "bachelor"},
    {"name": "Olivia Rossi", "age": 22, "test_score": 94, "role": "masters"},
    {"name": "Ethan Singh", "age": 20, "test_score": 79, "role": "bachelor"},
]

def top_students(students):
    result = []
    for student in students:
        if student["test_score"] > 90:
            result.append(student["name"])
    return result

print(top_students(students))

print("Exercitiu 2:")

def extract_students(students):
   result = {
       "bachelor": [],
       "masters": []
   }
   for student in students:
       if student["role"] == "bachelor":
           result["bachelor"].append(student)
       elif student["role"] == "masters":
           result["masters"].append(student)
   return result

print(extract_students(students))

print("Exercitiu 3:")

def student_balance(students):
    bachelor = 0
    masters = 0
    for student in students:
        if student["role"] == "masters":
            bachelor += 1
        elif student["role"] == "bachelor":
            bachelor += 1
    if bachelor > masters:
        return "bachelor"
    elif masters > bachelor:
        return "masters"
    else:
        return "equal"

print(student_balance(students))
