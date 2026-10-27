print("Algoritmo que solicite 10 números")
print()

numeros = []
contador = 0

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

x = int(input("Digite o número X: "))

for numero in numeros:
    if numero == x:
        contador += 1

print(f"O número {x} aparece {contador} vezes no vetor.")