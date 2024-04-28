import random

resultados = []

for i in range(50):
    lancamento = random.randint(1, 6)
    resultados.append(lancamento)

ocor_face_6 = resultados.count(6)
per_face_6 = (ocor_face_6 / 50) * 100

print(f"Percentual de ocorrências da face 6: {per_face_6:.2f}%")