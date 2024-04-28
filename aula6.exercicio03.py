numero = int(input("Digite um número de 5 dígitos: "))

if 9999 < numero < 100000:

    n1 = numero // 10000
    n2 = (numero % 10000) // 1000
    n3 = (numero % 1000) // 100
    n4 = (numero % 100) // 10
    n5 = numero % 10

    if n1 == n5 and n2 == n4:
        print(f"O número {numero} é um palíndromo.")
    else:
        print(f"O número {numero} não é um palíndromo.")

else:
    print(f"O número inserido não é válido.")