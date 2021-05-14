# Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python.

#estrutura condicional IF so tem 2 opcões: V ou F
#a estrutura basica de condições aninhadas é de 3 blocos que contem if > elif > else
#numa estrutura com 4 ou mais blocos é montado if >  elif > elif(por cada bloco novo) > else

#condição composta (basica)
'''
nome = str(input('Qual seu nome: '))
if nome == 'Gustavo':
    print('Que nome bonito!')
else:
    print('Que nome comum!')
'''

#condição aninhada
nome = str(input('Qual seu nome: '))
if nome == 'Reulyson':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Gustavo':
    print('Seu nome é bem comum no Brasil!')
elif nome == 'Maria' or nome == 'Julia':
    print('Belo nome feminino!')
elif nome == 'Creusa':
    print('Que nome esquisito!')
else: #existe casos que o else é opcional, pois a condição pode finalizar sem ele.
    print('Que nome normal!')
print('Bom dia {}!'.format(nome))
