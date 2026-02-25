#EXERCICIO 10
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
C = float(input('Olá! Para saber quantos dolares pode comprar, digite aqui o quanto você tem em sua carteira -> '))
D = (C/6)
print('Com o valor de R$ {}, você pode comprar até $ {} USD'.format(C, D))
