#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

#lendo idade
nome =  str(input("Nome do atleta: "))
idade = int(input("Idade: "))

#verificando categoria
if idade <= 9:
    print(f"{nome} pertence a categoria MIRIN.")
elif idade <= 14:
    print(f"{nome} pertence a categoria INFANTIL.")
elif idade <= 19:
    print(f"{nome} pertence a categoria JÚNIOR.")
elif idade <= 25:
    print(f"{nome} pertence a categoria SÊNIOR.")
elif idade > 25:
    print(f"{nome} pertece a categiria MASTER.")
