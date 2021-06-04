#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do 
# grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaid = 0
mediaid = 0
maiorid = 0
nomevelho = ""
totalf = 0

for p in range(1, 5):
    print("------{}°PESSOA------".format(p))
    nome = str(input("Qual seu nome: ")).strip().capitalize()
    sexo = str(input("Qual seu sexo M ou F: ")).strip().capitalize()
    idade = int(input("Quantos anos você tem: "))

#realizando a soma da idade do grupo
    somaid = somaid + idade

#verificando quem é o homem mais velho
    if p == 1 and sexo == "M":
        maiorid = idade
        nomevelho = nome
    if idade > maiorid and sexo == "M":
        maiorid = idade
        nomevelho = nome

#verificando quantas mulheres com menos de 20 anos tem no grupo
    if p == 1 and sexo == "F":
        totalf = totalf
    if sexo == "F" and idade < 20:
        totalf = totalf + 1

#realizando a media da idade do grupo
mediaid = somaid / p
print("A média de idade do grupo é de {:.0f} anos.".format(mediaid))
print("O homem mais velho tem {} anos e se chama {}.".format(maiorid, nomevelho))
print("O numero de mulheres com menos de 20 anos é de {}.".format(totalf))

    
   