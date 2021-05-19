#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda 
#vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

#importando biblioteca date para informar ano atual
from datetime import date
from typing import List

#variaveis para idade
atual = date.today().year
ano = int(input("Em qual ano você nasceu? "))
idade = atual - ano
print(f"Quem nasceu em {ano} tem {idade} em {atual}.")

#verificado a idade e ano para alistamento
if idade < 18:
    tempo = 18 - idade
    print(f"Você ainda não está no tempo de se alistar. Ainda faltam {tempo} anos para isso.")
    alist = atual + tempo
    print(f"Seu alistamento será em {alist}")
elif idade == 18:
    print("Você ja está com idade para se alistar")
else:
    tempo = idade - 18
    print(f"Você está atrasado, seu alistamento deveria ter ocorrido à {tempo} anos!")
    alist = atual - tempo
    print(f"Seu alistamento foi em {alist}")
