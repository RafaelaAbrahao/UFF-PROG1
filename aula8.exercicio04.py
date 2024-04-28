P1 = str(input("Digite a primeira palavra: "))
P2 = str(input("Digite a segunda palavra: "))

if P1 == P2[::-1] and P2 == P1[::-1]:
    print(f"As duas palavras são palíndromas mútuas!")
else:
    print(f"As duas palavras não são palíndromas mútuas.")

