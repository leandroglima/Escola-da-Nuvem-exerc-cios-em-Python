# Exercicio 14 - Registro de notas e cálculo da média da turma

print("=== Cálculo da Média da Turma ===")

quantidade_alunos = int(input("Digite o número de alunos: "))
soma_notas = 0

for i in range(quantidade_alunos):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    soma_notas += nota

media_turma = soma_notas / quantidade_alunos
print(f"A média da turma é: {media_turma:.2f}")
