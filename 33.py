#Empréstimo Bancário: Leia valor da casa, salário e anos a pagar. A prestação não podeexceder 30% do salário.
casa = float(input("Valor da casa: R$ "))
salario = float(input("Salário: R$ "))
anos = int(input("Anos para pagar: "))
prestacao = casa / (anos * 12)
limite = salario * 0.30

if prestacao <= limite:
    print(f"Empréstimo APROVADO! Parcela: R$ {prestacao:.2f}")
else:
    print(f"Empréstimo NEGADO! Parcela de R$ {prestacao:.2f} excede 30% do salário.")