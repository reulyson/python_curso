#  Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.
nome = str(input('Digte seu nome: ')).strip()
separado = nome.split()
print('Analizando nome...')
print('Seu nome é: {}'.format(nome.title()))
print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras.'.format(separado[0].capitalize(), len(separado[0])))
