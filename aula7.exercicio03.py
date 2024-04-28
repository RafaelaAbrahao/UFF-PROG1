n = int(input("Digite um número: "))

primeiro = 0
penultimo = 1
contador = 3
print(" {} - {} ".format(primeiro, penultimo), end="")

while contador <= n:
    ultimo = primeiro + penultimo
    print(" - {}".format(ultimo), end="")
    primeiro = penultimo
    penultimo = ultimo
    contador = contador + 1
