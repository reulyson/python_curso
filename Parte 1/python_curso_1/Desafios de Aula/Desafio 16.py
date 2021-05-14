# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math #biblioteca de matematica
num = float(input('digite um numero: '))
print ('o valor digitado  foi {} e sua parte inteira é {}'.format(num, math.trunc(num))) #trunc é um comando para retirar numeros dps da virgula

#desta forma se importa a biblioteca math e especifica que usará apenas a função tunc.
'''from math import trunc
num = float(input('digite um numero: '))
print ('o valor digitado  foi {} e sua parte inteira é {}'.format(num, trunc(num)))'''
