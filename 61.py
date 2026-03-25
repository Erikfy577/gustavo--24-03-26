geral = []
pares = []
impares = []
while True:
    n = int(input("Digite um número: "))
    geral.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    if input("Continuar? [S/N] ") in "Nn":
        break
print(f"Lista completa: {geral}\nPares: {pares}\nÍmpares: {impares}")