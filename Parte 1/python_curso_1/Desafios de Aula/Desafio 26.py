# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

let = str(input('Digite uma frase: ')).strip().upper()
print('Analisando a frase...')
print('A frase possui {} letras A'.format(let.count('A')))
print('A primeira letra A está: {}'.format(let.find('A')+1))
print('A ultima letra A está: {}'.format(let.rfind('A')+1)) # adicionar o r no find faz com que a frase seja lida apartir da direita
