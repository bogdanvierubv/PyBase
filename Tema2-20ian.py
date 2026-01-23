from operator import add

lista = []
lista1 = []
# cerinta 1
for i in range(0, 34):
    i= i*3
    lista.append(i)

# cerinta 2
for i in range(30, 61):
    i= i*10
    lista1.append(i)
lista.extend(lista1)
# print(lista)

# cerinta 3
lista.remove(51)
lista.remove(54)
lista.remove(66)
lista.remove(600)

print(lista)

#  cerinta 4
print(len(lista))

#  cerinta 5
for i in range(len(lista)):
     print(lista[i])

# suma= sum(lista)
# print(suma)
# media = suma/len(lista)
# print(media)

#  cerinta 6
lista.sort(reverse=True)
# print(lista)

# cerinta 7
maxim=max(lista)
print(maxim)

# cerinta 8

print(lista[(len(lista)+1)//2 : len(lista)])
