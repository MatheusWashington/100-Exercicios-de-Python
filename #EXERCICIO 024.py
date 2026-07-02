#EXERCICIO 024
#Exercício Python 24: Crie um programa que leia o nome de uma cidade 
# diga se ela começa ou não com o nome “SANTO”.

print('Digite aqui o nome de uma cidade em que você nasceu ou que você gosta:')
cidade = str(input('Cidade -> ')).strip()
cidade = cidade.upper()
print('Analisando a cidade ...{}...'.format(cidade))

if cidade[:5] == 'SANTO':
    print('Sim a cidade de {} tem o nome Santo no começo!'.format(cidade))
else:
        print('A cidade de {} não tem Santo no começo!'.format(cidade))
