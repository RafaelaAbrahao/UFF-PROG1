matriz_a = [[int(input(f"Digite o numero da matriz A na posição ({i+1},{j+1}): ")) for j in range(2)] for i in range(2)]

matriz_b = [[int(input(f"Digite o numero da matriz B na posição ({i+1},{j+1}): ")) for j in range(2)] for i in range(2)]

matriz_c = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        matriz_c[i][j] = matriz_a[i][j] + matriz_b[i][j]

print("Matriz A:")
for linha in matriz_a:
    print(linha)

print("Matriz B:")
for linha in matriz_b:
    print(linha)

print("Matriz C (soma de A e B):")
for linha in matriz_c:
    print(linha)