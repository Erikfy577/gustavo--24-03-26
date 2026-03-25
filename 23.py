#Maior e Menor de Três: Leia três números e diga qual é o maior e qual é o menor.
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))
maior = max(a, b, c)
menor = min(a, b, c)
print(f"Maior: {maior}")
print(f"Menor: {menor}")