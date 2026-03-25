#Média com Status: Média abaixo de 5.0 (Reprovado), entre 5.0 e 6.9 (Recuperação), 7.0ou superior (Aprovado).
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
media = (n1 + n2) / 2
if media < 5.0:
    print(f"Média {media:.1f}: REPROVADO")
elif 5.0 <= media <= 6.9:
    print(f"Média {media:.1f}: RECUPERAÇÃO")
else:
    print(f"Média {media:.1f}: APROVADO")