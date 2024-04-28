def somar(memoria, numero):
    return memoria + numero

def subtrair(memoria, numero):
    return memoria - numero

def multiplicar(memoria, numero):
    return memoria * numero

def dividir(memoria, numero):
    if numero != 0:
        return memoria / numero
    else:
        print("Erro: Divisão por zero.")
        return memoria

def limpar_memoria():
    return 0

def main():
    memoria = 0

    while True:
        print(f"Estado da memória: {memoria}")
        print("Opções:")
        print("(1) Somar")
        print("(2) Subtrair")
        print("(3) Multiplicar")
        print("(4) Dividir")
        print("(5) Limpar memória")
        print("(6) Sair do programa")

        opcao = int(input("Qual opção você deseja? "))

        if opcao == 6:
            print("Programa encerrado.")
            break

        numero = float(input("Digite um número: "))

        if opcao == 1:
            memoria = somar(memoria, numero)
        elif opcao == 2:
            memoria = subtrair(memoria, numero)
        elif opcao == 3:
            memoria = multiplicar(memoria, numero)
        elif opcao == 4:
            memoria = dividir(memoria, numero)
        elif opcao == 5:
            memoria = limpar_memoria()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
