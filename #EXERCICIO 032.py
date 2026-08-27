#EXERCICIO 032
"""
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
"""
from datetime import date
print('---=---' *12)
print('BEM VINDO A CALCULADORA DE ANO BISSEXTO!!!')
print('---=---' *12)
ano = int(input('Digite aqui um ano e te direi se é bissexto ou não -> '))
print('---=---' *12)
if ano%4 == 0:
    print('O ano de {} foi sim bissexto!'.format(ano))
else:
    print('O ano de {} não foi bissexto!'.format(ano))
print('---=---' *12)
