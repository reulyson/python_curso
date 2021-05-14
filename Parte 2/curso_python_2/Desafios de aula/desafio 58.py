# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
computador = random.randint(0, 10) # o numero que o computador está pensando
print('-*-'*22)
print('Vamos jogar!!! Tente adivinhar que numero estou pensando de 0 a 10: ')
print('-*-'*22)
acerto = False
tentativa = 0
while not acerto:
    jogador = int(input('Vai diz ai: '))  # o numero que o jogador escreveu
    tentativa += 1
    if jogador == computador:
        print('ISSO AI!!! Você acertou, eu também pensei no {}!'.format(computador))
        acerto = True
    else:
        if jogador < computador:
            print('Mais...')
        elif jogador > computador:
            print('Menos...')
print('Em {} tentativas. Legal'.format(tentativa))

