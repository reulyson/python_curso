# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
import time
n = random.randint(0, 5) # o numero que o computador está pensando
print('-*-'*22)
print('Vamos jogar!!! Tente adivinhar que numero estou pensando de 0 a 5: ')
print('-*-'*22)
nn = int(input('Vai diz ai: ')) # o numero que o jogador escreveu
print('Será se é {}...'.format(nn))
time.sleep(3) # com a biblioteca time eu uso comando sleep para gerar uma espera em sec
if nn==n:
    print('ISSO AI!!! Você acertou, eu também pensei no {}!'.format(n))
else:
    print('NAÃÃÃÃÃO!!! Eu tava pensando no {}. Quem sabe na próxima!'.format(n))
