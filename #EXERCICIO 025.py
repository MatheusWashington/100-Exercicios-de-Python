#EXERCICIO 025
#Exercício Python 25: Crie um programa que leia o nome de uma pessoa
# e diga se ela tem “SILVA” no nome.

print('Digite aqui o seu nome completo')
nome = str(input('-> ')).strip()
print('-------------------------------------------------')
print('Olá {}'.format(nome))
print('-------------------------------------------------')
print('Estamos analisando seu nome pra ver se "Silva" aparece nele...')
print('-------------------------------------------------')
nome = nome.upper()
if 'SILVA' in nome:
    print('Sim! Aparece o nome "Silva" no seu nome completo!')
else:
    print('Conferimos e não aparece "Silva" no seu nome completo')

print('--------------------- FIM DA EXECUÇÃO ----------------------------')