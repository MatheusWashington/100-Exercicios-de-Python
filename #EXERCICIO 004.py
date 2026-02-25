#EXERCICIO 4
#  Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

numero = input('Escreva alguma coisa -> ')
print("tipo primitivo: {}".format(type(numero)))

print("É numérico? {}".format(numero.isnumeric()))
print("É alfanumérico? {}".format(numero.isalpha()))
print("É decimal? {}".format(numero.isdecimal()))
print("Está em caixa baixa? {}".format(numero.islower()))
print("É apenas um espaço em branco? {}".format(numero.isspace()))
print("Está em caixa alta? {}".format(numero.isupper()))