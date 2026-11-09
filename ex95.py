vetor = []

for i in range(12):
    caractere = input(f"Digite o {i + 1}º caractere: ")
    vetor.append(caractere)

for i in range(0, 12, 2):
    auxiliar = vetor[i]
    vetor[i] = vetor[i + 1]
    vetor[i + 1] = auxiliar

print("Vetor após as trocas:", vetor)