#EXERCICIO 022
##Crie um programa que leia o nome completo de uma pessoa e mostre:
## O nome com todas as letras maiúsculas.
## O nome com todas as letras minúsculas.
## Quantas letras ao todo (sem considerar espaços).
## Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: "))
print('Analisando o seu nome...')
print('Seu nome em maiúsculas -> {}'.format(nome.upper()))
print('Seu nome em minúsculas -> {}'.format(nome.lower()))
print('O número de letras do seu nome é -> {}'.format(len(nome) - nome.count(' ')))
print('O número de letras do seu primeiro nome é -> {}'.format(len(nome.split()[0])))