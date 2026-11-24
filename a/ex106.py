print("algoritmo que solicite para o usuário: data, temperatura mínima e máxima e a amplitude térmica")
print("data, temperatura mínima e máxima e a amplitude térmica")
print()

arquivo = open("banco-temperaturas-julho.txt", "r", encoding="utf-8")

data = input("Informe a data (aaaa-mm-dd): ")

menor = None
maior = None
encontrou = False

for linha in arquivo:
    dados = linha.strip().split("\t")

    data_hora = dados[0]
    temperatura = float(dados[1])

    if data_hora[:10] == data:

        encontrou = True

        if menor is None or temperatura < menor:
            menor = temperatura

        if maior is None or temperatura > maior:
            maior = temperatura

arquivo.close()

if encontrou:
    amplitude = maior - menor

    print("Temperatura mínima:", menor)
    print("Temperatura máxima:", maior)
    print("Amplitude térmica:", round(amplitude, 2))
else:
    print("Essa data não foi encontrada no arquivo.")
