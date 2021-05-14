#  Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Escreva seu nome: ')).title().strip().split()
print('Analisando nome...')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1])) # usando o len para analisar as posiçoes e colocando -1 para sempre ser a ultima
