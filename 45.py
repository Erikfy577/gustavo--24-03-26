#Grupo da Maioridade: Leia o ano de nascimento de 7 pessoas e diga quantas já sãodemaior.
from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pess in range(1, 8):
    nasc = int(input(f"Ano de nascimento da {pess}ª pessoa: "))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f"Ao todo tivemos {maior} pessoas maiores e {menor} menores.")