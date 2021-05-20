#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO

#leitura das notas
aluno = str(input("Digite o nome do aluno: "))
nota1 = float(input("Digite a nota do 1° bimestre: "))
nota2 = float(input("Digite a nota do 2° bimestre: "))
nota3 = float(input("Digite a nota do 3° bimestre: "))
nota4 = float(input("Digite a nota do 4° bimestre: "))
nota_total = nota1, nota2, nota3, nota4

#gerando a média
media = sum(nota_total)/4
print(f"A media do aluno {aluno} foi {media}")

#verificando a aprovação, recuperação ou reprovação do aluno
if media >= 7:
    print("O aluno foi aprovado!")
elif media >= 5 and media < 7:
    print("O aluno está de recuperação.")
elif media < 5:
    print("O aluno está reprovado.")