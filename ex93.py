frase = input("Digite uma frase: ")

vogais = 0
consoantes = 0
outros = 0

for caractere in frase:
    if caractere in "aeiouAEIOU":
        vogais += 1
    elif caractere.isalpha() and caractere.isascii():
        consoantes += 1
    else:
        outros += 1

print("Quantidade de vogais:", vogais)
print("Quantidade de consoantes:", consoantes)
print("Quantidade de outros caracteres:", outros)