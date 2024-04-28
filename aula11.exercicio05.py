ordem = int(input("Digite a ordem da matriz (até 100): "))

matriz_original = [[int(input(f"Digite o valor para A[{i}][{j}]: ")) for j in range(ordem)] for i in range(ordem)]

matriz_transposta = [[matriz_original[j][i] for j in range(ordem)] for i in range(ordem)]

print("\nMatriz A:")
for linha in matriz_original:
    print(linha)

print("\nMatriz AT:")
for linha in matriz_transposta:
    print(linha)