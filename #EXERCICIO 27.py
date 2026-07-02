#EXERCICIO 27
#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente.

print('Escreva aqui o seu nome completo')
nome = str(input('-> ')).strip()
nome = nome.split()
print('Prazer em conhecê-lo {}'.format(nome))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
