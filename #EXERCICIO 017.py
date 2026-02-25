#EXERCICIO 17
#Desafio 17: Faça um programa que leia o comprimento do cateto oposto (co) e do cateto adjacente (ca) de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
print('Olá! Esse programa serve pra calcular a hipotenusa.')
Co = float(input('Digite aqui o valor do cateto oposto -> '))
Ca = float(input('Digite agora o cateto adjacente -> '))
H = hypot(Co, Ca)
print('O valor da hipotenusa é -> {:.2f}'.format(H))