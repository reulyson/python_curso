# Faça um programa que leia algo pelo teclado e mostre as informações sobre ele.
a = input('Digite algo: ')
print('O tipo primitivo deste valor é', type(a))
print('Só tem espaço?', a.isspace())
print('É um numero?', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanumerico?', a.isalnum())
print('Esta maiuscula?', a.isupper())
print('Esta minuscula?', a.islower())
