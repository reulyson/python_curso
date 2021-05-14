# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('A que velocidade o carro está? '))
if velocidade > 80:
    multa = (velocidade-80)*7
    print('Você ultrapassou o limite de 80Km/h. Receberá uma multa de R${:.2f} pela infração!'.format(multa))
else:
    print('Tudo Certo. Tenha uma boa viagem!')
print('Dirija com segurança')