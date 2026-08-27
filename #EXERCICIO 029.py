#EXERCICIO 029
"""Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada Km acima do limite.
"""
from time import sleep

vel = int(input("Registre a velocidade aferida -> "))
print('---=---' *12)
print('ANALISANDO...')
print('---=---' *12)
sleep(3)

if vel>80:
    multa = (vel - 80) *7
    print("Sua velocidade foi acima do permitido, você receberá uma multa de R$ {} reais".format(multa))
else:
    print("Você passou abaixo do limite de velocidade e não será penalizado.")
print('---=---' *12)