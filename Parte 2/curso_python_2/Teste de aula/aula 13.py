#for é um laço com variável de controle

#exemplo1
'''
for c in range(6, 0, -1): # contagem considera um numero a menos no final #para fazer a contagem de tras para frente no final se adiciona -1
    print(c)
print('Fim')
'''
#exemplo2
'''
n = int(input('Digite um numero: '))
for c in range(0, n + 1): #faz uma contagem ate o numero escrito. pois a variavel n esta somando +1.
    print(c)
print('Fim')
'''
#exemplo3
'''
i = int(input('Inicio: ')) #determina o inico da contagem
f = int(input('Fim: ')) #o fim da contagem
p = int(input('Passo: ')) #quantas casas serão puladas na contagem
for c in range(i, f + 1, p): #determinando o funcionamento
    print(c)
print('Fim')
'''
#exemplo4
'''
for c in range(0, 3): #determinha quantos numeros serão digitados
    n = int(input('Digite um numero: '))
print('Fim')
'''
#exemplo5
s = 0
for c in range(0, 3): #determina quantos numeros serão digitados
    n = int(input('Digite um numero: '))
    s += n #e soma os numeros escritos
print('Somatorio dos numeros é: {}'.format(s))
