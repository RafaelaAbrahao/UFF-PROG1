matriz = [[int(input(f"Digite o número da matriz na posição ({i+1},{j+1}): ")) for j in range(3)] for i in range(3)]

maior_soma = 0
linha_maior_soma = 0

print("\nMatriz:")
for linha in matriz:
    print(linha)

for i in range(3):
    soma_linha = sum(matriz[i])
    if soma_linha > maior_soma:
        maior_soma = soma_linha
        linha_maior_soma = i

print(f"\nLinha de maior soma: {matriz[linha_maior_soma]}")
print(f"Soma da linha de maior soma: {maior_soma}")