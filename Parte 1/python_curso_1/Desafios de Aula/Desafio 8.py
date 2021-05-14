# Escreva um programa que leia um valor em metros e mostre o valor em centimetros e milimetros:
m = float(input('Insira a medida: '))
cm = m*100
mm = m*1000
print('{} metros é igual a:\n {} cm\n {} mm'.format(m, cm, mm))
