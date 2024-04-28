frase = input("Digite uma frase: ")

frase = frase.strip()
frase_nova = ""

for i in frase:
    if i == " ":
        frase_nova += "#"
    else:
        frase_nova += i

print(f"A frase com # no lugar de esçaços é {frase_nova}")
