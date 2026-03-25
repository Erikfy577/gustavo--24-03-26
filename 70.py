#Sistema de Cadastro Escolar: Permita que o usuário pesquise o aluno pelo nome novetor do exercício 69 e visualize as notas individuais dele. O programa para quandopesquisar por "fim".Sistema de Cadastro Escolar: Permita que o usuário pesquise o aluno pelo nome novetor do exercício 69 e visualize as notas individuais dele. O programa para quandopesquisar por "fim".
alunos = [
    ["João", 7.5, 8.0],
    ["Maria", 9.0, 6.5],
    ["Pedro", 5.0, 7.0],
    ["Ana", 8.5, 9.5]
]

while True:
    nome_busca = input("Digite o nome do aluno (ou 'fim' para sair): ")

    if nome_busca.lower() == "fim":
        break

    encontrado = False

    for aluno in alunos:
        if aluno[0].lower() == nome_busca.lower():
            print("Aluno:", aluno[0])
            print("Nota 1:", aluno[1])
            print("Nota 2:", aluno[2])
            encontrado = True

    if not encontrado:
        print("Aluno não encontrado.")

    print()