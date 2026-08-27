#EXERCICIO 034
"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento

Para salários superiores a R$ 1.250,00, calcule um aumento de 10%

Para os inferiores ou iguais, o aumento é de R$ 15%.
"""
print('---=---' *12)
print('OLÁ FUNCIONÁRIO! VOCÊ GANHOU UM AUMENTO! VAMOS CALCULAR QUANTO JUNTOS?')
print('---=---' *12)
nome = str(input("Digite primeiro o seu nome -> "))
print('---=---' *12)
salario = float(input("Olá {}! Digite agora o seu salário -> ".format(nome)))
print('---=---' *12)
if salario>1250:
    aumento = salario*0.10
    salario = aumento + salario
    print('{}, o aumento do seu salario é de R$ {}, o novo valor total do seu salario é de R$ {}'.format(nome, aumento, salario))
else:
    salario<=1250
    aumento = salario*0.15
    salario = aumento + salario
    print('{}, o aumento do seu salario é de R$ {}, o novo valor total do seu salario é de R$ {}'.format(nome, aumento, salario))
print('---=---' *12)