#  Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''
soma = 0
for c in range(1,501, 2):
    if c % 3 == 0:
        soma = soma + c
print('A soma dos numeros pedidos é: {}'.format(soma))
'''

soma = 0
cont = 0
for c in range(1, 101):
    if c % 3 == 0:
        #cont = cont + 1
        cont += 1
        #soma = soma + c
        soma += c
        print(c, end=' ')
print('\nA soma dos valores é {}'.format(soma))
print('A quantidade de valores é {}'.format(cont))