#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

for p in range(1, 6):
    peso = float(input(f"Quantos kg tem a {p}°: "))
    
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso

        if peso < menor:
                menor = peso

print("O maior peso é {:.2f}kg\nO menor peso é {:.2f}kg".format(maior, menor))
