#Usar listas para armazenar as temperaturas dos 365 dias 
#é melhor do que criar variáveis separadas (dia1…dia365) 
#porque deixa o código mais curto, organizado e fácil de manter. 
#Cada dia fica em uma posição da lista (índice), permitindo acessar 
#e alterar valores de forma padronizada. Além disso, listas funcionam 
#muito bem com estruturas de repetição (for/while): o programador escreve 
#a lógica uma única vez (somar, contar, buscar maior/menor, calcular média)
#e o laço percorre todos os dias automaticamente, evitando repetição, erros
#e facilitando mudanças (por exemplo, ano bissexto ou mais cidades).

# Exemplo em Python: 365 temperaturas (uma por dia)
temperaturas = [25.0, 26.5, 24.0, 27.2]  # exemplo com poucos dias (seria 365 na prática)

soma = 0.0
maior = temperaturas[0]
menor = temperaturas[0]

for t in temperaturas:
    soma += t
    if t > maior:
        maior = t
    if t < menor:
        menor = t

media = soma / len(temperaturas)

print("Média:", media)
print("Maior:", maior)
print("Menor:", menor)