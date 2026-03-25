#Conversor de Moedas: Leia quantos Reais a pessoa tem e mostre quantos Dólares elapode comprar.
reais = float(input("Quantos R$ você tem? "))
cotacao = 5.00 
print(f"Você pode comprar US$ {reais / cotacao:.2f}")
