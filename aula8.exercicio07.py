nome = input("Digite seu nome: ")

escadinha = ""

for i in nome:
    escadinha += i
    escadinha = escadinha.upper()
    print(escadinha)