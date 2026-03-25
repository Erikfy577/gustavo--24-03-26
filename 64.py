alunos = []
notas = []
for i in range(0, 4):
    alunos.append(input(f"Nome do aluno {i+1}: "))
    notas.append(float(input(f"Nota do aluno {i+1}: ")))

media_turma = sum(notas) / len(notas)
print(f"\nMédia da turma: {media_turma:.1f}")
print("Alunos acima da média:")
for i in range(0, len(alunos)):
    if notas[i] > media_turma:
        print(f"-> {alunos[i]}: {notas[i]}")