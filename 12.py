#Desconto de Loja: Leia o preço de um produto e mostre seu novo preço com 5%de desconto.
preco = float(input("Preço do produto: R$ "))
novo_preco = preco - (preco * 0.05)
print(f"Com 5% de desconto, o novo preço é R$ {novo_preco:.2f}")