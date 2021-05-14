# Faça um programa que mostro o antecesor e sucessor do numeros escrito.
num = int(input('Escreva um número: '))
ant = num - 1
suc = num + 1
print('-O antecessor de {} é {}\n-O sucessor de {} é {}'. format(num, ant, num, suc))
