#EXERCICIO 018
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
ang = float(input('Digite aqui o valor de um ângunlo ->'))

seno = sin(radians(ang))
co = cos(radians(ang))
tang = tan(radians(ang))

print('O ângulo de {} graus tem o seno de {:.2f}'.format(ang, seno))
print('O ângulo de {} graus tem o cosseno de {:.2f}'.format(ang, co))
print('O ângulo de {} graus tem a tangente de {:.2f}'.format(ang, tang))