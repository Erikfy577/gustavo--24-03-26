sal = float(input("Salário do funcionário: R$ "))
if sal > 1250:
    novo = sal * 1.10
else:
    novo = sal * 1.15
print(f"Novo salário: R$ {novo:.2f}")