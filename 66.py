#Matriz Simples: Crie uma lista de listas (matriz 3x3) e preencha com valores pelo teclado. Imprima a matriz com a formatação correta.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite o valor para [{l}, {c}]: "))

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()