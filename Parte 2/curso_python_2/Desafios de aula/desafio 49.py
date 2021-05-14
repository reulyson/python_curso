# Faça uma tabuada
num = int(input('Escreva um numero: '))
for t in range(1, 11):
    print('{} x {} = {}'.format(t, num, num * t))
