# Palpites da Mega-Sena: Pergunte quantos jogos o usuário quer gerar. Crie uma lista
# contendo N listas de 6 números aleatórios (de 1 a 60), sem repetição dentro do mesmojogo.
import random
import time
jogos = int(input("Quantos jogos você quer gerar? "))
lista_jogos = []
for j in range(0, jogos):
    temp = []
    while len(temp) < 6:
        n = random.randint(1, 60)
        if n not in temp:
            temp.append(n)
    temp.sort()
    lista_jogos.append(temp[:])
    print(f"Jogo {j+1}: {temp}")
    time.sleep(0.5)