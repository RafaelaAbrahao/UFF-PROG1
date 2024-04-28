data = input("Digite sua data de nascimento no formato DD/MM/AAAA: ")

dia, mes, ano = [int(i) for i in data.split("/")]

meses_extenso = {
    1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril", 5: "maio", 6: "junho", 7: "julho", 8: "agosto", 9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro" }

print(f"{dia} de {meses_extenso[mes]} de {ano}")