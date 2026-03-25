matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
soma_par = soma_col3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
        if c == 2:
            soma_col3 += matriz[l][c]

print(f"Soma dos pares: {soma_par}")
print(f"Soma da terceira coluna: {soma_col3}")