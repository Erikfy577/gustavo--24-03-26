#Pintando a Parede: Leia a largura e altura de uma parede, calcule sua área e a quantidade de tinta necessária (1 litro pinta 2m²).
larg = float(input("Largura: "))
alt = float(input("Altura: "))
area = larg * alt
tinta = area / 2
print(f"Área: {area}m². Você precisará de {tinta}L de tinta.")