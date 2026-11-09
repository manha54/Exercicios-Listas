X = int(input("Digite o número X: "))

vetor = []
contador = 0

for i in range(32):
    numero = int(input(f"Digite o {i + 1}º número: "))
    vetor.append(numero)

    if numero == X:
        contador += 1

print(f"O número {X} apareceu {contador} vezes.")