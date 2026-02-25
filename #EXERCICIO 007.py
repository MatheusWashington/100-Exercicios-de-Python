#EXERCICIO 7
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
Aluno = (input('Olá Aluno! Digite aqui o seu nome -> '))
print('Ola {}! Para descobrir sua Média digite a seguir o valor das suas notas!'.format(Aluno))
print('-------------------------------------------------------------')
N1 = int(input('Digite aqui a primeira nota -> '))
N2 = int(input('Digite aqui a sua segunda nota -> '))
M = (N1+N2)/2
print('Sua media é ',(M))
