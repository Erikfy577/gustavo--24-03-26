# Fatiamento de Nome: Leia o nome completo de uma pessoa e imprima apenas o primeiro nome.
nome_completo = input("Digite seu nome completo: ").strip()
nome_dividido = nome_completo.split()
print(f"Seu primeiro nome é: {nome_dividido[0]}")