print("Algoritmo que leia o nome de 5 alunos e suas notas")
print()

alunos = []
soma = 0

for i in range(5):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))

    alunos.append([nome, nota])
    soma += nota

media = soma / 5

print("Média das notas:", media)
print("Alunos com nota menor que 7:")

for aluno in alunos:
    if aluno[1] < 7:
        print(aluno[0])