# Tabuada v2.0: Mostre a tabuada de um número que o usuário escolher, usando for
num = int(input("Digite um número para ver sua tabuada: "))
for c in range(1, 11):
    print(f"{num} x {c:2} = {num * c}")