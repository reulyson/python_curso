# Crie um algoritimo que leia um numero que mostre o dobro, triblo e raiz quadrada:
num = int(input('Digite um número: '))
dob = num*2
tri = num*3
raiz = num**(1/2)
print('Os resultados para {} é:\n DOBRO: {}\n TRIPLO: {}\n RAIZ QUADRADA: {:.2f}'.format(num, dob, tri, raiz)) # {:.2f} limita a duas casas usando do f.
