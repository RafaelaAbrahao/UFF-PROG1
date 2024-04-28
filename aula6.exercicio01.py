massa = float(input("Informe sua massa em kg: "))
altura = float(input("Informe sua altura em metros: "))

imc = massa / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.6 <= imc <= 24.9:
    classificacao = "Saudável"
elif 25 <= imc <= 29.9:
    classificacao = "Peso em excesso"
elif 30 <= imc <= 34.9:
    classificacao = "Obesidade Grau I"
elif 35 <= imc <= 39.9:
    classificacao = "Obesidade Grau II (severa)"
elif imc >= 40:
    classificacao = "Obesidade Grau III (mórbida)"

print(f"Seu IMC é: {imc:.2f} ,e sua classificação é: {classificacao}")