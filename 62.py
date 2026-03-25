#Expressões Matemáticas: Leia uma expressão com parênteses (ex: ((a+b)*c)) e validese a quantidade de parênteses abertos e fechados está correta.Expressões Matemáticas: Leia uma expressão com parênteses (ex: ((a+b)*c)) e validese a quantidade de parênteses abertos e fechados está correta.
expr = input("Digite a expressão: ")
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
print("Expressão válida!" if len(pilha) == 0 else "Expressão inválida!")