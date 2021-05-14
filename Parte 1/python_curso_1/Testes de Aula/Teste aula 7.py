# Operações aritmeticas.
n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))
n3 = n1+n2
n4 = n1*n2
n5 = n1/n2
n6 = n1//n2
n7 = n1**n2
print('-a soma vale {}\n-a multiplicação vale {}\n-a divisão vale {:.2f}'.format(n3, n4, n5))# {:.numerof} delimita quantos numeros serao mostrado no resultado real.
print('-a divisão inteira é {}\n-a potência é {}'.format(n6, n7))
