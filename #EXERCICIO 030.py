#EXERCICIO 030
"""
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""
from time import sleep
num = int(input('Escreva aqui um número e te direi se ele é par ou ímpar -> '))
print('---=---' *12)
print('AGUARDE...')
print('---=---' *12)
sleep(1)

if num%2==0:
    print('O número {} é par.'.format(num))
else:
    print('O número {} é ímpar.'.format(num))
print('---=---' *12)