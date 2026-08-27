#EXERCICIO 033
"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor
"""
from time import sleep
print('---=---' *12)
print('BEM VINDO AO ANALISTA DE NÚMEROS')
print('---=---' *12)
sleep(2)
print('Me diga três números e te direi qual o maior e o menor!')
print('---=---' *12)
sleep(2)
a = int(input('Digite aqui o primeiro -> '))
b = int(input('Digite aqui o segundo -> '))
c = int(input('Digite aqui o terceiro -> '))
print('---=---' *12)
print('ANALISANDO OS NÚMEROS ...')
print('---=---' *12)
sleep(3)
if a>b and a>c:
    print('O número {} é o primeiro e maior entre os três'.format(a))
    if b>c:
        print('O número {} é o terceiro e menor entre os três'.format(c))
    else:
        print('O número {} é o segundo e menor entre os três'.format(b))
elif b>a and b>c:
    print('O número {} é o segundo e maior entre os três'.format(b))
    if a>c:
        print('O número {} é o terceiro e menor entre os três'.format(c))
    else:
        print('O número {} é o primeiro e menor entre os três'.format(a))
else:
    print("O número {} é o terceiro e maior entre os três".format(c))
    if b>a:
        print('O número {} é o primeiro e menor entre os três'.format(a))
    else: 
        print('O número {} é o segundo e menor entre os três'.format(b))