#Fatorial: Calcule o fatorial de um número digitado (ex: 5! = 5x4x3x2x1 = 120).Fatorial: Calcule o fatorial de um número digitado (ex: 5! = 5x4x3x2x1 = 120).
n = int(input("Digite um número para calcular seu Fatorial: "))
c = n
f = 1
while c > 0:
    f *= c
    c -= 1
print(f"O fatorial de {n} é {f}.")