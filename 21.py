# Custo da Viagem: Cobre R$ 0.50 por km para viagens até 200km, e R$ 0.45 para viagens mais longas.
dist = float(input("Distância (km): "))
preco = dist * 0.50 if dist <= 200 else dist * 0.45
print(f"Preço da passagem: R$ {preco:.2f}")