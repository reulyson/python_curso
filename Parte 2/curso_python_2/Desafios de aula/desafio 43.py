#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

#lendo o peso e a altura
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

#gerando o imc
imc = peso / (altura*altura)
print("Seu IMC é de {:.2f}".format(imc))
#verificando o status
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc >= 18.5 and imc <= 25:
    print("Você está no peso ideal.")
elif imc > 25 and imc <= 30:
    print("Você está com sobrepeso.")
elif imc > 30 and imc <= 40:
    print("Você está com obesidade.")
else:
    print("Você está com obesidade mórbida.")
