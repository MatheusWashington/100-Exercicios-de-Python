#EXERCICIO 36
'''
Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos
anos ele vai pagar

Calcule o valor da prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado
'''
print('---=---' *12)
print('BEM VINDO AO SIMULADOR DE FINANCIAMENTO!')
print('---=---' *12)
print('Preciso coletar alguns dados seus para simular!')
print('---=---' *12)
valor  = float(input('Digite aqui o valor da casa -> '))
print('---=---' *12)
salario = float(input('Digite agora o seu salario -> '))
print('---=---' *12)
vezes = int(input('Por fim, em quantas vezes você quer parcelar? -> '))
print('---=---' *12)
print('---=---' *12)
parcelas = valor/vezes
if parcelas < salario*0.30:
    print('PARABÉNS, SEU FINANCIAMENTO ESTÁ APROVADO!!!')
    print('O valor da sua parcela é de R$ {:.2f}, em {} vezes'.format(parcelas, vezes))
else:
    print('Infelizmente, seu financiamento NÃO foi aprovado!')
    print('Sua parcela ficaria R$ {:.2f} em {} vezes e excederia o limite permitido.'.format(parcelas, vezes))