import math

def calc_combinacoes(n, m):
    combinacoes = math.comb(n, m)
    return combinacoes

n = int(input("Digite o número total de alunos: "))
m = int(input("Digite o número de alunos em cada grupo: "))

if 0 <= m <= n:
    resultado = calc_combinacoes(n, m)
    print(f"O número de combinações possíveis é: {resultado}")
else:
    print("Por favor, digite um valor válido para divisão de alunos.")