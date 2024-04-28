import math

def calcular_area_perimetro_circunferencia(raio):
    area = math.pi * raio**2
    perimetro = 2 * math.pi * raio
    return area, perimetro

def calcular_area_perimetro_triangulo(lado1, lado2, lado3):
    semiperimetro = (lado1 + lado2 + lado3) / 2
    area = math.sqrt(semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3))
    perimetro = lado1 + lado2 + lado3
    return area, perimetro

def calcular_area_perimetro_retangulo(lado1, lado2):
    area = lado1 * lado2
    perimetro = 2 * (lado1 + lado2)
    return area, perimetro

def main():
    print("Escolha o tipo de figura que deseja saber o perímetro:")
    print("1) Circunferência")
    print("2) Triângulo")
    print("3) Retângulo")

    tipo_figura = int(input("Digite o número correspondente ao tipo de figura: "))

    if tipo_figura == 1:
        raio = float(input("Digite o raio da circunferência: "))
        area, perimetro = calcular_area_perimetro_circunferencia(raio)
    elif tipo_figura == 2:
        lado1 = float(input("Digite o tamanho do primeiro lado do triângulo: "))
        lado2 = float(input("Digite o tamanho do segundo lado do triângulo: "))
        lado3 = float(input("Digite o tamanho do terceiro lado do triângulo: "))
        area, perimetro = calcular_area_perimetro_triangulo(lado1, lado2, lado3)
    elif tipo_figura == 3:
        lado1 = float(input("Digite o tamanho do primeiro lado do retângulo: "))
        lado2 = float(input("Digite o tamanho do segundo lado do retângulo: "))
        area, perimetro = calcular_area_perimetro_retangulo(lado1, lado2)
    else:
        print("Opção inválida. Programa encerrado.")
        return

    print(f"A área da figura é: {area}")
    print(f"O perímetro da figura é: {perimetro}")

if __name__ == "__main__":
    main()