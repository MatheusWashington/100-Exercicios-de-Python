# Desafio 16: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc
N = float(input('Escreva aqui um numero decimal -> '))
print('A porção inteira do numero {} é {}'.format(N, trunc(N)))