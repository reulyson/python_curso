# Faça um programa que leia o ano e diga se ele é bisexto
ano = int(input('Digite o ano: '))
if ano % 4 == 0 and ano % 100 ==0 or ano % 400 == 0:
    print('O ano {} é BISEXTO.'.format(ano))
else:
    print('O ano {} não é BISEXTO.'.format(ano))
