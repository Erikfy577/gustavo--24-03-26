preco = float(input("Preço do produto: R$ "))
print("1 - À vista (Dinheiro/Cheque)\n2 - À vista (Cartão)\n3 - 2x no Cartão\n4 - 3x ou mais no Cartão")
opcao = int(input("Opção de pagamento: "))

if opcao == 1:
    total = preco * 0.90
elif opcao == 2:
    total = preco * 0.95
elif opcao == 3:
    total = preco
elif opcao == 4:
    total = preco * 1.20
else:
    total = preco
    print("Opção inválida!")
print(f"O valor final será R$ {total:.2f}")