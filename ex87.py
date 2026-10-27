print("Algoritmo de vetores")
print()

X = []
Y = []

for i in range(8):
    X.append(int(input("Digite um valor inteiro para X: ")))

for i in range(8):
    Y.append(int(input("Digite um valor inteiro para Y: ")))

for i in range(8):
    print(X[i] * Y[i])