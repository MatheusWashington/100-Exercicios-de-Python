#EXERCICIO 9
# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
i=int()
N = int(input('Escreva aqui um numero para ver sua tabuada! -> '))

for i in range (11):
    Resultado = (N*i)
    print('{}X{}={}'.format(N, i, Resultado)) 


