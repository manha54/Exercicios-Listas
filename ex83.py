
vetor = []

for i in range(18):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    vetor.append(numero)

print("\nNúmeros em ordem inversa:")

for numero in reversed(vetor):
    print(numero)
