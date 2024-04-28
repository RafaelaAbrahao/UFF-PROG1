while True:
    n = int(input("Digite um número para saber seus divisores: "))

    while n <= 0:
       n = int(input("O número informado não é válido, digite um inteiro positivo: "))

    divisores = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisores.append(i)

    if len(divisores) == 2:
        print(f"O número {n} é primo.")
    else:
        print(f"Os divisores de {n} são: {divisores}")

    prosseguir = input("Deseja analisar outro número? Digite S ou N.")
    if prosseguir.upper() != "S":
        break


