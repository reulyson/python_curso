#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases de conversão:
[1] Binario
[2] Octal
[3] Hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para Binario é {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é {}.'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print('Opção invalida, tente novamente.')

