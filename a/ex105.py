print("Programa de que para ler e listar as informações")
print()

arquivo = open("banco-temperaturas-julho.txt", "r", encoding="utf-8")

quantidade = 0
soma = 0
menor = None
maior = None
data_menor = ""

for linha in arquivo: #1
    dados = linha.strip().split("\t")

    data_hora = dados[0]
    temperatura = float(dados[1])

    quantidade += 1
    soma += temperatura

    if menor is None or temperatura < menor:
        menor = temperatura
        data_menor = data_hora

    if maior is None or temperatura > maior:
        maior = temperatura

arquivo.close()

media = soma / quantidade #2

print("Total de linhas:", quantidade)
print("Média das temperaturas:", round(media, 2)) #2
print("Temperatura mínima:", menor)
print("Temperatura máxima:", maior)
print("Primeiro registro da temperatura mínima:", data_menor)
