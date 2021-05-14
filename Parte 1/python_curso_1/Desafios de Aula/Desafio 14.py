# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input('Escreva a temperatura em °C: '))
f = ((9/5)*c)+32
print('{}°C é equivalente a {}°F'.format(c, f))
