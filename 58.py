#Valores Únicos: O usuário digita vários números. Adicione-os a uma lista apenas se onúmero ainda não estiver nela.
lista = []
while True:
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado! Não vou adicionar.")
    
    resp = input("Quer continuar? [S/N] ").strip().upper()
    if resp == 'N':
        break
print(f"Você digitou os valores: {sorted(lista)}")