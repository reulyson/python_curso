#Crie um programa que faça o computador jogar Jokenpô com você.

#biblioteca para gerar numeros aleatorios para o computador
from random import randint

#biblioteca para pausar o enunciado de JOKENPÔ
from time import sleep
#preparando os itens que serão utilizando e fazendo a leitura das opções
item = ("Pedra", "Papel", "Tesoura")
print('''Vamos jogar Jokenpô? Escolha sua opção e vamos ver quem ganha:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
computador = randint(1, 3)
jogador = int(input("Faça sua jogada: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!!!!")
print("-="*16)
print(f"O computador jogou {item[computador]}")
print(f"O jogador jogou {item[jogador]}")
print("-="*16)
#determinando o vencedor
if computador == 1: #computador escolheu pedra
    if jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCEU")
    elif jogador == 3:
        print("COMPUTADOR VENCEU")
    else:
        print("JOGADA INVALIDA")
elif computador == 2: #computador escolheu papel
    if jogador == 1:
        print("COMPUTADOR VENCEU")
    elif jogador == 2:
        print("EMPATE")
    elif jogador == 3:
        print("JOGADOR VENCEU")
    else:
        print("JOGADA INVALIDA")
elif computador == 3: #computador escolheu tesoura
    if jogador == 1:
        print("JOGADOR VENCEU")
    elif jogador == 2:
        print("COMPUTADOR VENCEU")
    elif jogador == 3:
        print("EMPATE")
    else:
        print("JOGADA INVALIDA")
