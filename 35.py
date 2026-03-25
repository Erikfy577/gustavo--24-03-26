#Vogal ou Consoante: Leia uma letra e diga se ela é vogal ou consoante.
letra = input("Digite uma letra: ").strip().lower()
if letra in "aeiou":
    print(f"A letra '{letra}' é uma Vogal.")
else:
    print(f"A letra '{letra}' é uma Consoante.")