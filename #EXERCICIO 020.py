#EXERCICIO 020
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

A1 = str(input('Escreva o nome do primeiro aluno ->'))
A2 = str(input('Escreva o nome do segundo aluno ->'))
A3 = str(input('Escreva o nome do terceiro aluno ->'))
A4 = str(input('Escreva o nome do quarto aluno ->'))

Lista = [A1, A2, A3, A4]
shuffle(Lista)
print('A ordem dos alunos sorteados é:{}'.format(Lista))

