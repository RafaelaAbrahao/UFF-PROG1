tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

def imprimir_tabuleiro():
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(jogador):
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def verificar_empate():
    return all(tabuleiro[i][j] != ' ' for i in range(3) for j in range(3))

while not verificar_empate():
    imprimir_tabuleiro()

    linha_jogador = int(input("Digite a linha (0, 1, ou 2): "))
    coluna_jogador = int(input("Digite a coluna (0, 1, ou 2): "))
    tabuleiro[linha_jogador][coluna_jogador] = 'X'

    if verificar_vitoria('X'):
        imprimir_tabuleiro()
        print("Você ganhou!")
        break

    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                tabuleiro[i][j] = 'O'
                break

    if verificar_vitoria('O'):
        imprimir_tabuleiro()
        print("O computador ganhou!")
        break

if verificar_empate():
    imprimir_tabuleiro()
    print("O jogo terminou em empate.")