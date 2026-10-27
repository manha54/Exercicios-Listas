print("Solicitações com 10 números")
print()

vetor = []

for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    vetor.append(numero)

soma = 0
multiplicacao = 1

for i in range(10):
    if i % 2 == 0:
        multiplicacao *= vetor[i]
    else:
        soma += vetor[i]

print("Soma dos valores nas posições ímpares:", soma)
print("Multiplicação dos valores nas posições pares:", multiplicacao)