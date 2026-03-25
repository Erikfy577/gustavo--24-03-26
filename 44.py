#Detector de Palíndromo: Leia uma frase e diga se ela é igual lida de trás para frente.
frase = input("Digite uma frase: ").strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo.")