#Lista Ordenada (Sem usar sort): Leia 5 números e insira-os na lista já na posição correta(crescente), sem usar a função sort().
lista = []
for i in range(0, 5):
    n = int(input("Digite um valor: "))
    if i == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(f"Os valores em ordem são: {lista}")