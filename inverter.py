def inverter_palavras(frase):
    palavras = frase.split()
    palavras_invertidas = [palavra[::-1] for palavra in palavras]
    return ' '.join(palavras_invertidas)

frase = input("Digite uma frase: ")
print(inverter_palavras(frase))
