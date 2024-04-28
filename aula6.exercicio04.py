numero = int(input("Digite um número inteiro entre 0 e 9999: "))

centena = { 1: "cento", 2: "duzentos", 3: "trezentos", 4: "quatrocentos", 5: "quinhentos", 6: "seiscentos", 7: "setecentos", 8: "oitocentos", 9: "novecentos" }
dezena = { 10: "dez", 11: "onze", 12: "doze", 13: "treze", 14: "catorze", 15: "quinze", 16: "dezesseis", 17: "dezessete", 18: "dezoito", 19: "dezenove", 2: "vinte", 3: "trinta", 4: "quarenta", 5: "cinquenta", 6: "sessenta", 7: "setenta", 8: "oitenta", 9: "noventa" }
unidade = { 0: "zero", 1: "um", 2: "dois", 3: "três", 4: "quatro", 5: "cinco", 6: "seis", 7: "sete", 8: "oito", 9: "nove" }
extenso = ""

if 0 <= numero >= 9999:

        milhar = numero // 1000
        centena = (numero % 1000) // 100
        dezena = (numero % 100) // 10
        unidade = numero % 10

        if milhar > 0:
                extenso = unidade + "mil"

        if centena > 0:
            if centena == 1 and dezena == 0 and unidade == 0:
                    extenso += "cem"
            else:
                extenso += centena



print(extenso)




#else:
    #print(f"O número inserido é inválido.")