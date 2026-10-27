print("Algoritmo que apresente uma lista com os nomes das pessoas que possuem 18 anos ou mais.")
print()

nomes = []
idades = []

for i in range(7):
    nome = input(f"Digite o nome da {i + 1}ª pessoa: ")
    idade = int(input(f"Digite a idade de {i + 1}ª pessoa: "))

    nomes.append(nome)
    idades.append(idade)

print("\nPessoas com 18 anos ou mais:")

for i in range(7):
    if idades[i] >= 18:
        print(nomes[i])
