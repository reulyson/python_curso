
#  O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
al1 = input('aluno: ')
al2 = input('aluno: ')
al3 = input('aluno: ')
al4 = input('aluno: ')
lista = [al1, al2, al3, al4]
ordem = random.shuffle(lista)  #shuffle é para misturar
print('a ordem será: ')
print(lista)

