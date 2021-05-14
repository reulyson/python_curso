# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nome = str(input('Digite o nome da Cidade: ')).split()
print('A cidade começa com o nome SANTO?: {}'.format(nome[0].strip().upper() == 'SANTO'))
