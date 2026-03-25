dias = int(input("Dias alugados: "))
km = float(input("Km rodados: "))
total = (dias * 60) + (km * 0.15)
print(f"O total a pagar pelo aluguel é R$ {total:.2f}")