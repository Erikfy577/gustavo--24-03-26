#Menu de Opções: Leia dois números e mostre um menu: [1] somar, [2] multiplicar, [3] maior, [4] novos números, [5] sair. O programa só fecha no 5.
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0
while opcao != 5:
    print("[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair")
    opcao = int(input(">>>> Qual é a sua opção? "))
    if opcao == 1: print(f"A soma é {n1 + n2}")
    elif opcao == 2: print(f"O produto é {n1 * n2}")
    elif opcao == 3: print(f"O maior é {max(n1, n2)}")
    elif opcao == 4:
        n1 = int(input("Novo primeiro valor: "))
        n2 = int(input("Novo segundo valor: "))