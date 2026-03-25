#Categoria de Atleta: Classifique um atleta pela idade: até 9 (Mirim), até 14 (Infantil), até 19 (Junior), até 25 (Sênior), acima (Master).
idade = int(input("Idade do atleta: "))
if idade <= 9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("Classificação: JUNIOR")
elif idade <= 25:
    print("Classificação: SÊNIOR")
else:
    print("Classificação: MASTER")