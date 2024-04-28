vet = []

for i in range(20):
    valor = int(input("Digite um valor para entrar no vetor Vet: "))
    vet.append(valor)

pos = [valor for valor in vet if valor > 0]

semdup = []
for valor in pos:
    if valor not in semdup:
        semdup.append(valor)

print(f"Os valores do vetor Vet são: {vet}")
print(f"O vetor Pos com apenas os valores inteiros positivos do vetor Vet é: {pos}")
print(f"O vetor Semdup com apenas uma ocorrência de cada valor do vetor Pos é: {semdup}")



