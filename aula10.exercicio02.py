import random

lancamentos = [random.randint(1, 6) for i in range(100)]

resultados = [lancamentos.count(i) for i in range(1, 7)]

print(f"O resultados dos lançamentos é: {lancamentos}")
print(f"A contagem de cada valor obtido: {resultados}")
