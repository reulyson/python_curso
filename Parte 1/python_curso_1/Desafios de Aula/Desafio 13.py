#  Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Insira seu salário: R$'))
aum = (sal*15)/100
print('Seu salário era R${:.2f}\nAgora seu salário será R${:.2f}'.format(sal, sal+aum))
