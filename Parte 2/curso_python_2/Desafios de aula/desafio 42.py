# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

#lendo as medidas
r1 = float(input("informe o valor da 1° linha: "))
r2 = float(input("informe o valor da 2° linha: "))
r3 = float(input("informe o valor da 3° linha: "))

#determinando o tipo de triangulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos podem formar um triangulo : ", end='')
    if r1 == r2 and r2 == r3:
        print("EQUILÁTERO")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("ISÓSCELES")
    else:
        print("ESCALENO")
else:
    print("Os segmentos não podem formar um triangulo.")