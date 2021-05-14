# Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dolares ela pode comprar (considere US$1,00=R$3,27)
real = float(input('Quantos reais você tem? R$'))
dolar = real/5.39
print('Com R${} você pode comprar US${:.2f}.'.format(real, dolar))

