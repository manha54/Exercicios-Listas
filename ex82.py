print("algoritmo que solicite 11 valores para o usuário")
print()
vetor = []

for i in range(11):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    vetor.append(valor)

print("\nValores digitados:")

for valor in vetor:
    print(valor)
    print("----------------")
