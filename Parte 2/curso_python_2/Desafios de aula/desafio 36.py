# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos deseja pagar? '))
parcela = casa / (anos*12)
minimo = (salario*30) / 100
print('Uma casa de R${:.2f} parcelada em {} anos ficará em torno de R${:.2f} por mes e seu salario de R${:.2f}'.format(casa, anos, parcela, salario))
if parcela <= minimo:
    print('Aprovado!Parabens seu emprestimo foi aprovado')
else:
    print('NEGADO! Não sera possivel fazer o emprestimo.')