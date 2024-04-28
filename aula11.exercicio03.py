linhas_a = int(input("Digite o número de linhas da matriz A: "))
colunas_a = int(input("Digite o número de colunas da matriz A: "))

linhas_b = int(input("Digite o número de linhas da matriz B: "))
colunas_b = int(input("Digite o número de colunas da matriz B: "))

if colunas_a != linhas_b:
    print("As matrizes não são compatíveis para multiplicação.")
else:
    matriz_a = [[int(input(f"Digite o elemento da matriz A na posição ({i+1},{j+1}): ")) for j in range(colunas_a)] for i in range(linhas_a)]

    matriz_b = [[int(input(f"Digite o elemento da matriz B na posição ({i+1},{j+1}): ")) for j in range(colunas_b)] for i in range(linhas_b)]

    matriz_resultante = [[0 for _ in range(colunas_b)] for _ in range(linhas_a)]

    for i in range(linhas_a):
        for j in range(colunas_b):
            for k in range(colunas_a):
                matriz_resultante[i][j] += matriz_a[i][k] * matriz_b[k][j]

    print("\nMatriz A:")
    for linha in matriz_a:
        print(linha)

    print("\nMatriz B:")
    for linha in matriz_b:
        print(linha)

    print("\nMatriz Resultante da Multiplicação (A * B):")
    for linha in matriz_resultante:
        print(linha)