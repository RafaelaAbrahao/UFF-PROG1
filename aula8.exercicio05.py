p1 = str(input("Digite a primeira palavra: "))
p2 = str(input("Digite a segunda palavra: "))

nova_p1 = p1.replace(" ","").lower()
nova_p2 = p2.replace(" ","").lower()

if sorted(nova_p1) == sorted(nova_p2):
    print(f"As palavras {p1} e {p2} são anagramas!")
else:
    print(f"As palavras {p1} e {p2} não são analgramas.")