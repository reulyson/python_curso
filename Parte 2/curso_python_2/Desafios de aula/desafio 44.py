#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço normal 
#– 3x ou mais no cartão: 20% de juros

preco = float(input("Digite o preço do produto: R$"))
print('''Qual a forma de pagamento?\n
- [1] À vista dinheiro/cheque (Desconto 10%)
- [2] À vista no cartão (Desconto 5%)
- [3] 2x vezes no cartão (Valor normal)
- [4] 3x ou mais no cartão (Juros 20%)''')

#verificando valor e forma de pagamento
while True:
    pagamento = str(input("Escolha uma opção: "))
    if pagamento == "1":
        desconto = preco * 10 / 100
        novo = preco - desconto
        print('''\nPagando à vista o produto sairá com 10% de desconto.\n
        Preço normal: R${:.2f}
        Valor do desconto (10%): R${:.2f}
        Total à pagar: R${:.2f}\n'''.format(preco, desconto, novo))
        break
    elif pagamento == "2":
        desconto = preco * 5 / 100
        novo = preco - desconto
        print('''\nPagando á vista no cartão o produto sairá com 5% de desconto.\n
        Preço normal: R${:.2f}
        Valor do desconto: R${:.2f}
        Total à pagar: R${:.2f}\n'''.format(preco, desconto, novo))
        break
    elif pagamento == "3":
        parcela = preco / 2
        print("\nPagando no cartão em 2x sua compra de R${:.2f} o valor das parcelas sairam a R${:.2f}\n".format(preco, parcela))
        break
    elif pagamento == "4":
        while True:
            juros = preco * 20 / 100
            novo = preco + juros
            parcela = int(input("Em quantas vezes deseja parcelar? "))
            if parcela >= 3:
                print('''\nPagando no cartão acima de 3x é adicionado um juros de 20% em cima do valor.
Valor normal: R${:.2f}
Valor do juros: R${:.2f}
Valor reajustado: R${:.2f}
Numero de parcelas: {}x
Valor das parcelas: R${:.2f}\n'''.format(preco, juros, novo, parcela, novo/parcela ))
                break
            else:
                print("\nOpção invalida.\n")
        break            
    else:
        print("\nOpção invalida.\n")