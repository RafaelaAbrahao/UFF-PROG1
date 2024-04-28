tempo = float(input("Digite o tempo percorrido em segundos entre a visualização do raio e o barulho do trovão: "))
velocidade = 340
distancia_quilometros = (tempo * velocidade) / 1000

print("A distância do raio para o observador é de",distancia_quilometros,"km.")