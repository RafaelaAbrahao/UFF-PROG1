lista1 = [int(input("Digite um valor para lista 1: ")) for i in range(int(input("Digite a quantidade de elementos para a lista 1: ")))]
lista2 = [int(input("Digite um valor para lista 2: ")) for i in range(int(input("Digite a quantidade de elementos para a lista  2:")))]

lista3 = []

if len(lista1) <= len(lista2):
    lista_menor = lista1
    lista_maior = lista2
else:
    lista_menor = lista2
    lista_maior = lista1

for i in range(len(lista_menor)):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(f"Lista intercalada: {lista3}")