n = int(input("Digite um número inteiro positivo: "))

if n <= 0:
    print(f"O número informado é inválido.")
else:
    n_digitos = len(str(n))
    print(f"O número possui {n_digitos} dígitos!")