soma = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n
print(f"A soma de todos os valores solicitados é {soma}")