#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
#Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input("Digite uma frase: ")).strip().upper() #deixando a frase com letras maiusculas e ignorando espaços antes de dps
palavra = frase.split() #separando cada palavra em uma lista
junto = "".join(palavra) #unido as palavras separadas sem o espaço
inverso = "" #

for letra in range(len(junto)-1, -1, -1): #len(junto)-1: subitrai uma letra do junto pois ele inicia no 0, -1: inica a contagem dps do zero, -1: faz com que seja lido de tras pra frente
    inverso += junto[letra]
print(f"O inverso de {junto} é {inverso}.")
if inverso == junto:
    print("É palídromo")
else:
    print("Não é palídromo.")
