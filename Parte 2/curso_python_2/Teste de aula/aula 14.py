'''
i = int(input('Inicio: '))
f = int(input('Final: '))
while i < f+1:
    print(i)
    i += 1
print('Fim!')
'''
'''
n = 1
while n != 0:
    n = int(input('Escreva um numero: '))
print('Fim!')
'''
'''
r = 'S'
while r == 'S':
    n = int(input('Escreva um numero: '))
    r = str(input('Deseja continuar? [S/N]').upper())
print('Fim!')
'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Escreva um numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} numeros pares e {} numeros impares.'.format(par, impar))
