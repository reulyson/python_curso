#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

#zerando as variáveis para realizar a contagem e a soma
soma = 0
contagem = 0

#lendos os numeros 6 vezes
for n in range(0, 6):
    num = int(input("Digite um numero: "))

    #selecionando os numeros pares e somando eles
    if num % 2 == 0: #determinando os números pares
        soma = soma + num #realizando a soma
        contagem = contagem + 1 #realizando a contegem de números selecionados
print(f"Você informou {contagem} numeros e a soma deles é {soma}")
