#Calculadora IMC: Calcule o IMC e classifique (Abaixo do peso, Peso ideal, Sobrepeso, Obesidade, Obesidade Mórbida).
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / (altura ** 2)
if imc < 18.5:
    status = "Abaixo do peso"
elif 18.5 <= imc < 25:
    status = "Peso ideal"
elif 25 <= imc < 30:
    status = "Sobrepeso"
elif 30 <= imc < 40:
    status = "Obesidade"
else:
    status = "Obesidade Mórbida"
print(f"Seu IMC é {imc:.1f}: {status}")