#Tipos de Triângulo: Baseado no ex 26, diga se o triângulo é Equilátero, Isósceles ouEscaleno.
r1 = float(input("Reta 1: "))
r2 = float(input("Reta 2: "))
r3 = float(input("Reta 3: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print("Triângulo Equilátero.")
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print("Triângulo Escaleno.")
    else:
        print("Triângulo Isósceles.")
else:
    print("Não forma um triângulo.")