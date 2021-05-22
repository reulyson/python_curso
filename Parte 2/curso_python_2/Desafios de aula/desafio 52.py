#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("Digite um número: "))
total = 0
for c in range(1, num+1):

    #selecionando somente os números que são divisiveis com os numeros da contagem
    if num % c == 0:
        print("\033[32m", end=" ") #cor amarela
        total = total + 1
    else:
        print("\33[31m", end= " ") #cor vermelha
    print(c, end=" ")
print(f"\n\33[mO número {num} foi divisivel {total} vezes.")

#um numero só considerado primo quando ele é divisivel por 1 e por ele mesmo.
if total == 2:
    print(f"O número {num} é primo!")
else:
    print(f"O número {num} não é primo!")