# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input('Digite um numero: '))
u = num//1 %10
d = num//10 %10
c = num//100 %10
m = num//1000 %10
print('O número é: {}\nEle esta dividido:'.format(num))
print('Milhar {}'.format(m))
print('Centena {}'.format(c))
print('Dezena {}'.format(d))
print('Unidade {}'.format(u))
