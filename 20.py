vel = float(input("Velocidade (km/h): "))
if vel > 80:
    multa = (vel - 80) * 5
    print(f"MULTADO! Valor da multa: R$ {multa:.2f}")