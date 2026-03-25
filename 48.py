#Jogo da Adivinhação v2.0: O computador pensa em um número de 0 a 10. Ojogador tenta adivinhar até acertar, mostrando quantos palpites foram necessários.
import random
computador = random.randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual é seu palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente novamente.")
        else:
            print("Menos... Tente novamente.")
print(f"Acertou com {palpites} tentativas. Parabéns!")