# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''import math
an = float(input('digite o angulo'))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('o angulo {} possui SENO {}, CONSENO {} , TANGETE {}'.format(an, sen, cos, tan))'''

# De forma direta
from math import radians, sin, cos, tan
an = float(input('digite o angulo'))
sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print('o angulo {} possui SENO {}, CONSENO {} , TANGETE {}'.format(an, sen, cos, tan))