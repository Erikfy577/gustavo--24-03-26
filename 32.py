import random
itens = ("Pedra", "Papel", "Tesoura")
computador = random.randint(0, 2)
print("0 - Pedra | 1 - Papel | 2 - Tesoura")
jogador = int(input("Sua jogada: "))

print(f"Computador jogou {itens[computador]}")
if computador == jogador:
    print("EMPATE!")
elif (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
    print("VOCÊ VENCEU!")
else:
    print("COMPUTADOR VENCEU!")