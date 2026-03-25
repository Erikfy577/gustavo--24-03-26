#Aluguel de Carros: Calcule o preço a pagar sabendo que o carro custa R$60 por dia eR$0.15 por km rodado. Peça os dias e os km.
dias = int(input("Dias alugados: "))
km = float(input("Km rodados: "))
total = (dias * 60) + (km * 0.15)
print(f"O total a pagar pelo aluguel é R$ {total:.2f}")