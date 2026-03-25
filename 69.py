alunos = [
    ["João", 7.5, 8.0],
    ["Maria", 9.0, 6.5],
    ["Pedro", 5.0, 7.0],
    ["Ana", 8.5, 9.5]
]

print("BOLETIM:\n")

for aluno in alunos:
    nome = aluno[0]
    nota1 = aluno[1]
    nota2 = aluno[2]
    media = (nota1 + nota2) / 2

    print(nome, "- Média:", media)