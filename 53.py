#Tratando Vários Valores: Leia números até o usuário digitar 999. Mostre quantos números foram digitados e a soma entre eles (desconsiderando o 999).
num = cont = soma = 0
num = int(input("Digite um número [999 para parar]: "))
while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um número [999 para parar]: "))
print(f"Você digitou {cont} números e a soma foi {soma}.")