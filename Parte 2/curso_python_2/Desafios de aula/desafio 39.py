#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda 
#vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input("Em que ano você nasceu? "))
idade =  2021- ano
if idade < 18:
    tempo = 18 - idade
    print(f"Você ainda não está no tempo de se alistar. Ainda faltam {tempo} anos para isso.")
elif idade == 18:
    print("Você ja está com idade para se alistar")
else:
    tempo = idade - 18
    print(f"Você está atrasado, seu alistamento deveria ter ocorrido à {tempo} anos!")
