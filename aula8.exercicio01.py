frase = input("Digite a frase: ")
palavra_antiga = input("Digite a palavra antiga: ")
palavra_nova = input("Digite a palavra nova: ")

palavras = frase.split()
palavras_substituidas = (palavra_nova if palavra == palavra_antiga else palavra for palavra in palavras)

nova_frase = " ".join(palavras_substituidas)

print(nova_frase)