frase = input("Digite uma frase: ")

frase = frase.strip()
palavras = frase.split()
n_palavras = len(palavras)

print(f"A frase contém {n_palavras} palavra(s)")