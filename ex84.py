print("algoritmo que solicite 12 números inteiros para o usuário")
print()

vetor = []

for i in range(12):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    vetor.append(numero)

print("\nNúmeros pares:")

for numero in vetor:
    if numero % 2 == 0:
        print(numero)

print("\nNúmeros ímpares:")

for numero in vetor:
    if numero % 2 != 0:
        print(numero)
