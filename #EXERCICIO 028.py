#EXERCICIO 028
"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.

"""

from random import randint
from time import sleep

ran = randint(0,5)
print ("--=--" * 15)
print ("Vou pensar em um número, você consegue adivinhar qual é?")
print ("--=--" * 15)

num = int(input("Em qual número eu pensei? -> "))
print("PROCESSANDO...")
sleep(2)

while True:
    if num > 5 or num < 0:
        print("Esse número é inválido")
        num = int(input("Escreva um número de 0 a 5 -> "))
    else:
        if num == ran:
            print("Você leu a minha mente?")
            print("O número que eu escolhi foi o {} mesmo, parabéns!".format(num))
            break
        else:
            print("Você escolheu o número {}, não foi esse que pensei".format(num))
            print("Tente novamente! o número certo era o {}".format(ran))
            break