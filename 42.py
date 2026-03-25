#Progressão Aritmética (PA): Leia o primeiro termo e a razão de uma PA. Mostre os 10primeiros termos.
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f"{c}", end=" -> ")
print("ACABOU")