def status_aluno(media):
    if media > 6:
        return "APROVADO!!"
    elif 4 <= media <= 6:
        return "Verificação Suplementar."
    else:
        return "Reprovado."

media_aluno = float(input("Digite a média do aluno: "))

status = status_aluno(media_aluno)
print(f"O status do aluno é: {status}")