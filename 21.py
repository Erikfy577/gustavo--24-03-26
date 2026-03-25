dist = float(input("Distância (km): "))
preco = dist * 0.50 if dist <= 200 else dist * 0.45
print(f"Preço da passagem: R$ {preco:.2f}")