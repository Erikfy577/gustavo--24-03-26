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