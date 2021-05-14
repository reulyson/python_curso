# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um outro numero: '))
escolha = 0
while escolha != 5:
    print('''Escolha uma operação:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    escolha = int(input('Qual a opção que deseja? '))
    if escolha == 1:
        resultado = num1 + num2
        print('O resultado de {}+{}={}'.format(num1, num2,resultado))
    elif escolha == 2:
        resultado = num1 * num2
        print('O resultado de {}x{}={}'.format(num1, num2, resultado ))
    elif escolha == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O maior numero é: {}'.format(maior))
    elif escolha == 4:
        num1 = int(input('Digite um numero: '))
        num2 = int(input('Digite um outro numero: '))
    elif escolha == 5:
        print('FINALIZANDO...')
    else:
        print('Opção invalida!')
    print('-=-' * 10)
    sleep(2)
print('Programa encerrado!')
