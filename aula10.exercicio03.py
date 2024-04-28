n_elementos = int(input("Digite a quantidade de elementos para a lista: "))

vetor = [float(input("Digite um valor para a lista: ")) for _ in range(n_elementos)]

soma = sum(vetor)
media = soma / len(vetor)

diferenca_proxima = abs(vetor[0] - media)
valor_proximo = vetor[0]

for valor in vetor[1:]:
    diferenca_atual = abs(valor - media)
    if diferenca_atual < diferenca_proxima:
        diferenca_proxima = diferenca_atual
        valor_proximo = valor

print(f"\nVetor: {vetor}")
print(f"Média: {media:.1f}")
print(f"Valor mais próximo da média: {valor_proximo}")
