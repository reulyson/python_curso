# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
al1 = input('aluno 1: ')
al2 = input('aluno 2: ')
al3 = input('aluno 3: ')
al4 = input('aluno 4: ')
lista = [al4,al3,al2,al1]
escolhido = random.choice(lista)
print('o aluno escolhido foi: {}'.format(escolhido))

