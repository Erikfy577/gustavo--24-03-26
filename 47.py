#Validação de Dados: Leia o sexo de uma pessoa (M/F). Se digitar errado, peça novamente até acertar (use while).
sexo = input("Informe seu sexo [M/F]: ").strip().upper()[0]
while sexo not in "MF":
    sexo = input("Dados inválidos. Por favor, informe seu sexo [M/F]: ").strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso.")