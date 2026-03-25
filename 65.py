#Busca em Vetor: Crie uma lista de 10 números aleatórios. Peça um número ao usuárioe diga se ele existe na lista.Busca em Vetor: Crie uma lista de 10 números aleatórios. Peça um número ao usuárioe diga se ele existe na lista.
import random
lista = [random.randint(1, 50) for _ in range(10)]
busca = int(input("Qual número deseja buscar (1 a 50)? "))
if busca in lista:
    print(f"O número {busca} existe na lista (Posição {lista.index(busca)}).")
else:
    print(f"O número {busca} não foi encontrado.")