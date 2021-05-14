# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Digite o preço do produto: R$'))
descot = int(input('Digite o desconto: '))
final = (preço*descot)/100
print('O preço do produto é de R${}\nCom {}% de desconto você economizará R${:.2f} \nVocê pagará R${:.2f} '.format(preço, descot, final, preço-final))
