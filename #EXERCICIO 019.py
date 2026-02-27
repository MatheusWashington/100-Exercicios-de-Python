# EXERCICIO 019
#  Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o do escolhido.
import random

A1 = input('Escreva aqui o nome do primeiro aluno -> ')
A2 = input('Escreva aqui o nome do segundo aluno -> ')
A3 = input('Escreva aqui o nome do terceiro aluno -> ')
A4 = input('Escreva aqui o nome do quarto aluno -> ')
lista = [A1, A2, A3, A4]
Aluno = random.choice (lista)

print('O aluno sorteado a apagar o quadro foi: {}'.format(Aluno))
