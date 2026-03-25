num = []
while True:
    num.append(int(input("Digite um valor: ")))
    resp = input("Continuar? [S/N] ")
    if resp in "Nn":
        break
print(f"Foram digitados {len(num)} elementos.")
num.sort(reverse=True)
print(f"Valores em ordem decrescente: {num}")
print("O valor 5 faz parte da lista!" if 5 in num else "O valor 5 não foi encontrado.")