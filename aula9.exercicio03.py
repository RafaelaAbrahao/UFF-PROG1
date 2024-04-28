vetor = []

for i in range (5):
    valor = int(input("Digite um valor: "))
    vetor.append(valor)

valor_procurado =  int(input("Digite o valor a ser procurado: "))

posicao = -1
for i in range(len(vetor)):
    if vetor[i] == valor_procurado:
        posicao = i + 1
        break

print(f"A primeria ocorrência de {valor_procurado} no vetor é na posição {posicao}. ")
