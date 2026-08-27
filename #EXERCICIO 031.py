#EXERCICIO 031
"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km
e R$ 0,45 para viagens mais longas
"""
from time import sleep

print('---=---' *12)
print('OLÁ, SEJA BEM VINDO A PLATAFORMA DE ORÇAMENTO DE VIAGENS!!!')
print('---=---' *12)
km = int(input('Para calcular informe em KM a distãncia da sua viagem -> '))
print('---=---' *12)
print('ANALISANDO...')
print('---=---' *12)
sleep(2)
print('ORÇAMENTO QUASE PRONTO...')
print('---=---' *12)
sleep(2)
print('ORÇAMENTO PRONTO!')
print('---=---' *12)

if km<=200:
    valor = km * 0.50
    print('Sua viajem vai custar R$ 0,50 o quilômetro, num total de R$ {}'.format(valor))
    print('---=---' *12)
else:
    valor = km * 0.45
    print('Sua viajem vai custar R$ 0,45 o quilômetro, num total de R$ {}'.format(valor))
    print('---=---' *12)