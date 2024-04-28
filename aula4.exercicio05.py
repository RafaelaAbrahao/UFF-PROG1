centavos = int(input("Digite o valor em centavos: "))

R1 = 0
C50 = 0
C25 = 0
C10 = 0
C5 = 0
C1 = 0
Total = 0

R1 = centavos // 100
centavos %= 100

C50 = centavos // 50
centavos %= 50

C25 = centavos // 25
centavos %= 25

C10 = centavos // 10
centavos %= 10

C5 = centavos // 5
centavos %= 5

C1 = centavos

print("Você possui",R1,"moeda(s) de 1 real,", C50 ,"moeda(s) de 50 centavos,", C25 ,"moeda(s) de 25 centavos", C10 ,"moeda(s) de 10 centavos", C5 ,"moeda(s) de 5 centavos e", C1 ,"moeda(s) de 1 centavo.")

