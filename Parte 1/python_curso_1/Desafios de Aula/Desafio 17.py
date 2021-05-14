# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
#forma matematica
'''co = float(input('digite o cateto oposto'))
ca = float(input('digite o catete adjacente'))
hi = (co**2+ca**2)**(1/2)
print('a hipotenusa é {:.2f}'.format(hi))'''

#importanto biblioteca math e usando a função hypot (hipotenusa)
import math
co = float(input('digite o cateto oposto: '))
ca = float(input('digite o cateto adjacente: '))
hi = math.hypot(co, ca)
print('a hipotenusa é {:.2f}'.format(hi))
