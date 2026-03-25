#Radar Eletrônico: Leia a velocidade de um carro. Se ultrapassar 80km/h, calcule umamulta de R$ 5 por km acima do limite.
vel = float(input("Velocidade (km/h): "))
if vel > 80:
    multa = (vel - 80) * 5
    print(f"MULTADO! Valor da multa: R$ {multa:.2f}")