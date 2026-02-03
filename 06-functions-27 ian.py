# v1 = "Hello World"
#
# print(v1[0], v1[1], v1[-11])
#
# # Ce se printeaza?
#
# # 1. Eroare
# # 2. "H l o"
# # 3. Nimic
#
#
# # Exemplul 2
#
# x1 = 10
#
# def change (x1):
#     x1 = 11
#
# change(x1)
# print(x1)


print ("======Curs functii 06=======")

# Ex:
#  primim o lista de numere intregi. Separati-le in numere pare si impare, si salvatile intr-un dictionar.

# ex dictionar = {
#     "odd_numbers": [3, 5, 11, 13, 201],
#     "even_numbers": [2, 4, 8, 10, 12, 200, 340],
#     "odd_total": 233,
#     "even_total": 576
# }

def is_even(nr):
    return nr % 2 == 0

def list_total(list1):
    total = 0
    for n in list1:
        total = total + n
    return total


result = {}
odd_list = []
even_list = []


for n in list1:
        if is_even(n):
            even_list.append(n)
        else:
            odd_list.append(n)

# print(odd_list)
# print(even_list)



    result["odd_numbers"]= odd_list
    result["even_list"]= even_list
    result["odd_total"]= list_total(odd_list)
    result["even_total"]= list_total(even_list)
    return result

data_list = [0, 5, 11, 31, 40, 52, 100, 999]
var2 = process_data(data_list)
print(var2)