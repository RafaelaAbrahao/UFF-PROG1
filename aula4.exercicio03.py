#Exercício 03

import math
x1 = float(input("Digite o valor da coordenada X no primerio ponto: "))
y1 = float(input("Digite o valor da coordenada Y no primeiro ponto: "))

x2 = float(input("Digite o valor da coordenada X no segundo ponto: "))
y2 = float(input("Digite o valor da coordenada Y no segundo ponto: "))

cateto1 = x2 - x1
cateto2 = y2 - y1

distancia = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

print("A distância entre os pontos é: ",distancia)
