matriz = []
for i in range(6):
    linha = [float(input(f"Digite um número para M[{i}][{j}]: ")) for j in range(3)]
    matriz.append(linha)

maior_elemento = float('-inf')
menor_elemento = float('inf')
maior_posicao = None
menor_posicao = None

for i in range(6):
    for j in range(3):
        if matriz[i][j] > maior_elemento:
            maior_elemento = matriz[i][j]
            maior_posicao = (i, j)
        if matriz[i][j] < menor_elemento:
            menor_elemento = matriz[i][j]
            menor_posicao = (i, j)

print("\nMatriz:")
for linha in matriz:
    print(linha)

print(f" O maior elemento, {maior_elemento}, está na posição: {maior_posicao}")
print(f"O menor elemento, {menor_elemento}, está na posição: {menor_posicao}")