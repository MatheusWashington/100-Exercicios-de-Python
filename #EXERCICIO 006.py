#EXERCICIO 6
# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada:
from math import sqrt, ceil

N = int(input('Escreva um numero -> '))
R=sqrt(N)
print('O dobro do numero {}, é {}, O seu triplo é {} e sua raiz quadrada é {})'.format(N, N*2, N*3, ceil(R)))