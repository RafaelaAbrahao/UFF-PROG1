matriz = [[int(input(f"Digite o número da posição ({i+1},{j+1}): ")) for j in range(3)] for i in range(3)]

n_mult = int(input("Digite o número que deseja multiplicar: "))

print("Matriz original:")
for linha in matriz:
    print(linha)

for i in range(3):
    matriz[i][i] *= n_mult

print("Matriz após a multiplicação:")
for linha in matriz:
    print(linha)