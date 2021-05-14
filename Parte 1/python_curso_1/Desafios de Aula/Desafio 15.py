# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dia = int(input('Insira os dias usados: '))
km = float(input('Insira a distancia percorrida Km: '))
pagar = (60*dia)+(0.15*km)
print('Você alugou o carro por {} dias e rodou um total de {}Km.\nO valor total do aluguel é R${:.2f}'.format(dia, km, pagar))
