frase = input("Digite uma frase: ")

nova_frase = ""

for caractere in frase:
    if caractere in "aeiouAEIOU" or (caractere.isalpha() and caractere.isascii()):
        nova_frase += caractere
    else:
        nova_frase += "-"

print("Frase modificada:", nova_frase)