vetor = []

for i in range (10):
    n = int(input("Digite um número: "))
    vetor.append(n)

n_unicos = set(vetor)
quant_n_dif = len(n_unicos)

print(f"Existe(m) {quant_n_dif} número(s) diferente(s) armazenado(s) no vetor.")