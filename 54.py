# Maior e Menor v2.0: Leia vários números. Pergunte se o usuário quer continuar. Aofinal, mostre a média, o maior e o menor Maior e Menor v2.0: Leia vários números. Pergunte se o usuário quer continuar. Aofinal, mostre a média, o maior e o menor
resp = "S"
soma = quant = media = maior = menor = 0
while resp in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior: maior = num
        if num < menor: menor = num
    resp = input("Quer continuar? [S/N] ").strip().upper()[0]
media = soma / quant
print(f"Média: {media}, Maior: {maior}, Menor: {menor}")