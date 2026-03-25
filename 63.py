#Vetor de Nomes: Crie uma lista vazia. Peça para o usuário digitar 5 nomes. Imprima alista no final.Vetor de Nomes: Crie uma lista vazia. Peça para o usuário digitar 5 nomes. Imprima alista no final.
nomes = []
for i in range(0, 5):
    nomes.append(input(f"Digite o {i+1}º nome: "))
print(f"Nomes cadastrados: {nomes}")