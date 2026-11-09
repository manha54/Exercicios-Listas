vetor1 = []
vetor2 = []
comuns = []

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º valor do primeiro vetor: "))
    vetor1.append(numero)

for i in range(12):
    numero = int(input(f"Digite o {i + 1}º valor do segundo vetor: "))
    vetor2.append(numero)

for numero in vetor1:
    if numero in vetor2 and numero not in comuns:
        comuns.append(numero)

comuns.sort(reverse=True)

print("Valores comuns em ordem decrescente:", comuns)