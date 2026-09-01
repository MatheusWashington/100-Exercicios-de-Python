#EXERCICIO 037

''' Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário
2 para octal
2 para hexadecimal
'''
linha ='---=---' *12
print(linha)
num = int(input('Digite aqui um número a ser convertido -> '))
print(linha)
print('Escolha a base que quer converter:')
print(linha)
print('Para binário digite [1]')
print('Para octal digite [2]')
print('Para hexadecimal digite [3]')
print(linha)
base = int(input('Digite aqui sua opção -> '))
print(linha)
if base == 1:
    print('A conversão do seu número em bináro é {}'.format(bin(num)[2:]))
    if base == 2:
        print('A conversão do seu número em octal é {}'.format(oct(num)[2:]))
        if base == 3:
            print('A conversão do seu número em hexadecimal é {}'.format(hex(num)[2:]))
else :
    print('Escolha inválida, favor escolher uma das opções indicadas.')
print(linha)