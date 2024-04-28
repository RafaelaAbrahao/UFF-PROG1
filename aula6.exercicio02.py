import math

x1 = int(input("Digite a coordenada X do primeiro ponto: "))
y1 = int(input("Digite a coordenada Y do primeiro ponto: "))
x2 = int(input("Digite a coordenada X do segundo ponto: "))
y2 = int(input("Digite a coordenada Y do segundo ponto: "))
x3 = int(input("Digite a coordenada X do terceiro ponto: "))
y3 = int(input("Digite a coordenada Y do terceiro ponto: "))

lado1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
lado2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
lado3 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    if lado1 == lado2 and lado2 == lado3:
        classificacao = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        classificacao = "Isósceles"
    else:
        classificacao = "Escaleno"

    print(f"As coordenadas informadas formam um triângulo {classificacao}.")
else:
    print(f"As coordenadas informadas não formam um triângulo.")
