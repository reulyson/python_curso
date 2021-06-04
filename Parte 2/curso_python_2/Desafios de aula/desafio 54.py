#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.

from datetime import date

atual = date.today().year
totalmaior = 0
totalmenor = 0

for i in range(1,8):
    nasc = int(input(f"Em que ano a {i}° nasceu?: "))
    idade = atual - nasc
    if idade < 18:
        totalmenor = totalmenor + 1
    else:
        totalmaior = totalmaior + 1
print(f"{totalmaior} pessoas são maiores de idade.\n{totalmenor} pessoas são menores de idade")