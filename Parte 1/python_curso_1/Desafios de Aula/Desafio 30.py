# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
numero = int(input('Digite um numero: '))
resultado = numero%2
if resultado == 0:
    print('Numero {} é par!'.format(numero))
else:
    print('Numero {} é impa!'.format(numero))
