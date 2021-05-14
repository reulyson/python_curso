# Faça um programa que diga qual o maior e o menor numero dentre 3 escritos
a = int(input('1° NUMERO: '))
b = int(input('2° NUMERO: '))
c = int(input('3° NUMERO: '))
#verificando o numero menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# verificando o numero maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor numero é {}.'.format(menor))
print('O maior numero é {}'.format(maior)
      )