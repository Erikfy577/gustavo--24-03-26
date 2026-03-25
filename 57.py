#Maior e Menor na Lista: Leia 5 valores, guarde em uma lista e mostre qual é o maior, omenor e as suas posições na lista.
valores = []
for i in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {i}: ")))

print(f"O maior valor foi {max(valores)} nas posições ", end="")
for i, v in enumerate(valores):
    if v == max(valores):
        print(f"{i}... ", end="")

print(f"\nO menor valor foi {min(valores)} nas posições ", end="")
for i, v in enumerate(valores):
    if v == min(valores):
        print(f"{i}... ", end="")