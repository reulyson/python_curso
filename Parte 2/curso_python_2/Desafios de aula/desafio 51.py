#Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética. No final, mostre os 10 primeiros termos dessa progressão.

p = int(input("Informe o primeiro número: "))
r = int(input("Informe a razão: "))
decimo = p + (10-1) * r #regra matematica para que se leia ate o 10° numero da contagem.
for c in range(p, decimo + r, r):
    print(c, end=" - ")
print("ACABOU!")
