#EXERCICIO 12
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

P=float(input("Olá! Digite aqui o preço do produto ->"))
print("Esse produto está em promoção")
D=P*0.95
print('De {} por {}'.format (P, D))